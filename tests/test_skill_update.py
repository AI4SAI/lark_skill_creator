import hashlib
import io
import json
import os
import signal
import stat
import subprocess
import sys
import tempfile
import types
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import skill_update
from skill_package import check, install, pack, runtime, seal, snapshot
from skill_update import UpdateError, current, install_user, update


class SkillUpdateTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "source/sai-user-guide"
        (self.source / "references/handbook").mkdir(parents=True)
        self.store = self.root / "store"
        self.home = self.root / "home"
        self.home.mkdir()
        self.calls = []
        self.publish("1.0.0", "First published manual")

    def publish(self, version, content):
        (self.source / "SKILL.md").write_text(
            '---\nname: sai-user-guide\ndescription: Fixture.\nmetadata:\n  version: "'
            + version + '"\n---\n\n[Manual](references/handbook/manual.md)\n')
        (self.source / "references/handbook/manual.md").write_text(content)
        (self.source / "references/manifest.json").write_text(json.dumps({
            "fetched_at": "2026-11-02T00:00:00Z", "documents": [{
                "doc_id": "manual", "title": "Manual", "url": "https://example.org/manual",
                "revision": 1, "file": "handbook/manual.md", "status": "fetched",
                "sharing": "anyone_readable", "sha256": hashlib.sha256(content.encode()).hexdigest(),
            }]}))
        self.publish_source(version)

    def publish_source(self, version):
        seal(self.source)
        output = self.root / ("pack-" + str(len(list(self.root.glob("pack-*")))))
        receipt = pack(self.source, output)
        self.content = Path(receipt["archive"]).read_bytes()
        self.version = version
        self.digest = receipt["sha256"]

    def fetch(self, url, limit, deadline):
        self.calls.append(url)
        if url.endswith("/releases/latest"):
            return ("https://github.com/AI4SAI/lark_skill_creator/releases/tag/sai-user-guide-v" + self.version).encode()
        if url.endswith(".sha256"):
            return (self.digest + "  sai-user-guide.zip\n").encode()
        return self.content

    def refresh(self):
        return update(self.store, require_index=True, fetch=self.fetch)

    def installed(self):
        return current(self.store, require_index=True)

    def assert_old(self, before, version="1.0.0"):
        self.assertEqual(self.installed()["version"], version)
        self.assertEqual(snapshot(Path(self.installed()["path"])), before)
        self.assertEqual(json.loads((self.store / "status.json").read_text())["state"], "failed")

    def test_install_current_and_update_keep_fixed_readable_versions(self):
        first = self.refresh()
        old = Path(first["path"])
        before = snapshot(old)
        self.assertTrue(first["updated"])
        self.assertFalse(self.refresh()["updated"])
        self.assertEqual(sum(url.endswith(".zip") for url in self.calls), 1)
        self.publish("1.1.0", "New published manual")
        second = self.refresh()
        self.assertEqual(second["previous"], "1.0.0")
        self.assertEqual(snapshot(old), before)
        self.assertEqual(os.readlink(self.store / "current"), "versions/1.1.0")
        self.assertIn("New published", (Path(second["path"]) / "references/handbook/manual.md").read_text())
        for item in (self.store / "versions/1.1.0").rglob("*"):
            self.assertTrue(item.stat().st_mode & (stat.S_IXOTH if item.is_dir() else stat.S_IROTH))

    def test_transport_and_corrupt_archive_leave_previous(self):
        before = snapshot(Path(self.refresh()["path"]))
        with self.assertRaises(UpdateError):
            update(self.store, fetch=lambda *args: (_ for _ in ()).throw(UpdateError("DOWNLOAD_FAILED", "offline")))
        self.assert_old(before)
        self.publish("1.1.0", "New manual")
        self.content += b"corruption"
        with self.assertRaisesRegex(UpdateError, "校验失败"):
            self.refresh()
        self.assert_old(before)

    def test_same_version_change_and_downgrade_are_refused(self):
        before = snapshot(Path(self.refresh()["path"]))
        self.publish("1.0.0", "Changed in place")
        with self.assertRaises(UpdateError) as error:
            self.refresh()
        self.assertEqual(error.exception.code, "VERSION_CONFLICT")
        self.assert_old(before)
        self.publish("0.9.0", "Older")
        with self.assertRaises(UpdateError) as error:
            self.refresh()
        self.assertEqual(error.exception.code, "OLDER_RELEASE")
        self.assert_old(before)

    def test_resealed_managed_content_is_not_trusted(self):
        first = self.refresh()
        source = Path(first["path"])
        (source / "references/handbook/manual.md").write_text("Local edit")
        seal(source)
        with self.assertRaises(UpdateError) as error:
            self.installed()
        self.assertEqual(error.exception.code, "LOCAL_MODIFIED")

    def test_required_index_rejects_missing_private_and_corrupt_documents(self):
        before = snapshot(Path(self.refresh()["path"]))
        for failure in ("missing", "private", "bad-hash", "missing-title"):
            self.publish("1.1.0", "New manual")
            path = self.source / "references/manifest.json"
            if failure == "missing":
                path.unlink()
            else:
                data = json.loads(path.read_text())
                if failure == "missing-title":
                    del data["documents"][0]["title"]
                else:
                    data["documents"][0]["sharing" if failure == "private" else "sha256"] = "invalid"
                path.write_text(json.dumps(data))
            self.publish_source("1.1.0")
            with self.assertRaises(UpdateError):
                self.refresh()
            self.assert_old(before)

    def test_archive_traversal_and_symlink_never_escape_staging(self):
        before = snapshot(Path(self.refresh()["path"]))
        for filename, mode in (("sai-user-guide/../../escaped", 0o100644), ("sai-user-guide/link", 0o120777)):
            self.publish("1.1.0", "New manual")
            stream = io.BytesIO(self.content)
            with zipfile.ZipFile(stream, "a") as bundle:
                info = zipfile.ZipInfo(filename)
                info.external_attr = mode << 16
                bundle.writestr(info, "outside")
            self.content = stream.getvalue()
            self.digest = hashlib.sha256(self.content).hexdigest()
            with self.assertRaises(UpdateError):
                self.refresh()
            self.assertFalse((self.store / "escaped").exists())
            self.assert_old(before)

    def test_atomic_readback_failure_restores_previous_pointer(self):
        before = snapshot(Path(self.refresh()["path"]))
        self.publish("1.1.0", "New manual")
        original = skill_update.current_package

        def fail_candidate(store, name="sai-user-guide", require_index=False):
            if (store / "current").is_symlink() and os.readlink(store / "current") == "versions/1.1.0":
                raise UpdateError("INVALID_PACKAGE", "readback failed")
            return original(store, name, require_index)

        with patch.object(skill_update, "current_package", fail_candidate):
            with self.assertRaises(UpdateError):
                self.refresh()
        self.assert_old(before)

    def test_concurrent_update_is_reported_without_changing_current(self):
        self.refresh()
        with skill_update._locked(self.store):
            with self.assertRaises(UpdateError) as error:
                self.refresh()
        self.assertEqual(error.exception.code, "UPDATE_BUSY")
        self.assertEqual(self.installed()["version"], "1.0.0")

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_user_copy_uses_nss_home_preserves_edits_and_previous_inodes(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        with patch.object(skill_update.pwd, "getpwuid", return_value=account), patch.dict(os.environ, {"HOME": "/not-the-user-home"}):
            plan = install_user(self.store, agent="codex", dry_run=True)
            self.assertFalse((self.home / ".agents").exists())
            installed = install_user(self.store, agent="codex")
            self.assertEqual(installed["destination"], str(self.home / ".agents/skills/sai-user-guide"))
            self.assertEqual(installed["destination"], plan["destination"])
            local = Path(installed["destination"]) / "references/handbook/manual.md"
            with local.open("a") as writer:
                self.publish("1.1.0", "Updated manual")
                self.refresh()
                result = install_user(self.store, agent="opencode")
                writer.write("Retained open handle")
                writer.flush()
                self.assertIn("Retained open handle", (Path(result["backup"]) / "sai-user-guide/references/handbook/manual.md").read_text())
            local.write_text("Personal edit")
            with self.assertRaises(UpdateError) as error:
                install_user(self.store, agent="codex")
            self.assertEqual(error.exception.code, "LOCAL_MODIFIED")
            self.assertEqual(local.read_text(), "Personal edit")
            self.assertIn(".claude/skills", install_user(self.store, agent="claude")["destination"])

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_sigterm_during_user_replacement_restores_original(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        with patch.object(skill_update.pwd, "getpwuid", return_value=account):
            result = install_user(self.store, agent="codex")
            destination = Path(result["destination"])
            before = snapshot(destination)
            self.publish("1.1.0", "New manual")
            self.refresh()
            original = Path.rename

            def interrupt(path, target):
                result = original(path, target)
                if path == destination:
                    os.kill(os.getpid(), signal.SIGTERM)
                return result

            with patch.object(Path, "rename", interrupt):
                with self.assertRaises(UpdateError):
                    install_user(self.store, agent="codex")
            self.assertEqual(snapshot(destination), before)

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_native_legacy_roots_migrate_without_duplicate_discovery(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        legacy = self.home / ".codex/skills/sai-user-guide"
        install(self.source, legacy.parent)
        old = snapshot(legacy)
        self.publish("1.1.0", "New shared version")
        self.refresh()
        with patch.object(skill_update.pwd, "getpwuid", return_value=account):
            plan = install_user(self.store, agent="codex", dry_run=True)
            self.assertEqual(plan["retire_from"], [str(legacy)])
            self.assertTrue(legacy.exists())
            with (legacy / "references/handbook/manual.md").open("a") as writer:
                result = install_user(self.store, agent="codex")
                self.assertFalse(legacy.exists())
                saved = Path(result["backup"]) / "legacy-1/sai-user-guide"
                self.assertEqual(snapshot(saved), old)
                writer.write("Late write to original")
                writer.flush()
                self.assertIn("Late write", (saved / "references/handbook/manual.md").read_text())
            # A later personal copy in the legacy root is never discarded.
            legacy.mkdir(parents=True)
            (legacy / "SKILL.md").write_text("Personal guidance")
            with self.assertRaises(UpdateError) as error:
                install_user(self.store, agent="codex")
            self.assertEqual(error.exception.details["destination"], str(legacy))
            self.assertEqual((legacy / "SKILL.md").read_text(), "Personal guidance")

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_legacy_migration_failure_restores_every_original(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        legacy = self.home / ".config/opencode/skills/sai-user-guide"
        install(self.source, legacy.parent)
        old = snapshot(legacy)
        rename = Path.rename

        def fail_publish(path, target):
            if path.name == "sai-user-guide" and path.parent.name.startswith(".skill-install-"):
                raise OSError("Publish failed")
            return rename(path, target)

        with patch.object(skill_update.pwd, "getpwuid", return_value=account), patch.object(Path, "rename", fail_publish):
            with self.assertRaises(UpdateError):
                install_user(self.store, agent="opencode")
        self.assertEqual(snapshot(legacy), old)
        self.assertFalse((self.home / ".agents/skills/sai-user-guide").exists())

    def test_root_and_unavailable_source_return_machine_codes(self):
        with patch.object(skill_update.os, "geteuid", return_value=0):
            with self.assertRaises(UpdateError) as error:
                install_user(self.store, agent="codex")
        self.assertEqual(error.exception.code, "IDENTITY_UNAVAILABLE")
        if os.geteuid() != 0:
            with self.assertRaises(UpdateError) as error:
                install_user(self.store, agent="codex")
            self.assertEqual(error.exception.code, "SOURCE_UNAVAILABLE")

    def test_standalone_cli_is_reproducible_and_reads_actual_store(self):
        self.refresh()
        one = runtime(self.root / "one.pyz")
        two = runtime(self.root / "two.pyz")
        self.assertEqual(one["sha256"], two["sha256"])
        result = subprocess.run([sys.executable, one["archive"], "current", "--store", str(self.store), "--require-index"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["version"], "1.0.0")
        result = subprocess.run([sys.executable, one["archive"], "current", "--store", str(self.root / "missing")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stderr)["code"], "SOURCE_UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
