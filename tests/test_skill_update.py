import hashlib
import http.server
import io
import json
import os
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import types
import unittest
import zipfile
import urllib.request
from pathlib import Path
from unittest.mock import patch

import skill_update
from skill_package import check, install, pack, runtime, seal, snapshot
from skill_update import UpdateError, current, install_user, reading, update


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

    def mirror_fetch(self, url, limit, deadline):
        self.calls.append(url)
        if url == skill_update.OFFICIAL_MIRROR + "release.json":
            return json.dumps({"name": "sai-user-guide", "version": self.version,
                               "sha256": self.digest, "archive": f"sai-user-guide-v{self.version}.zip",
                               "release": f"https://github.com/AI4SAI/lark_skill_creator/releases/tag/sai-user-guide-v{self.version}"}).encode()
        if url == skill_update.OFFICIAL_MIRROR + f"sai-user-guide-v{self.version}.zip":
            return self.content
        raise UpdateError("DOWNLOAD_FAILED", "Primary offline")

    def test_official_mirror_is_transport_only_and_keeps_release_identity(self):
        before = self.refresh()
        self.assertEqual(before["source"], "github")
        self.assertFalse(any(url.startswith(skill_update.OFFICIAL_MIRROR) for url in self.calls))
        self.publish("1.1.0", "Mirrored release")
        deadlines = {}

        def fetch(url, limit, deadline):
            deadlines[url] = deadline
            return self.mirror_fetch(url, limit, deadline)

        result = update(self.store, require_index=True, fetch=fetch)
        self.assertEqual(result["source"], "sai")
        self.assertEqual(result["release"], "https://github.com/AI4SAI/lark_skill_creator/releases/tag/sai-user-guide-v1.1.0")
        self.assertEqual(result["sha256"], self.digest)
        self.assertGreater(deadlines[skill_update.OFFICIAL_MIRROR + "release.json"]
                           - deadlines["https://github.com/AI4SAI/lark_skill_creator/releases/latest"], 119)
        receipt = json.loads((Path(result["path"]).parent / "release.json").read_text())
        self.assertNotIn("source", receipt)
        self.assertEqual(current(self.store)["update"]["source"], "sai")

    def test_archive_transport_fallback_requires_same_selected_version(self):
        self.refresh()
        self.publish("1.1.0", "Mirrored release")

        def fetch(url, limit, deadline):
            if url.startswith(skill_update.OFFICIAL_MIRROR):
                return self.mirror_fetch(url, limit, deadline)
            if url.endswith(".zip"):
                raise UpdateError("DOWNLOAD_FAILED", "Primary ZIP offline")
            return self.fetch(url, limit, deadline)

        self.assertEqual(update(self.store, require_index=True, fetch=fetch)["source"], "sai")
        self.publish("1.2.0", "Next release")
        original = self.mirror_fetch

        def changed_mirror(url, limit, deadline):
            body = original(url, limit, deadline)
            if url.endswith("release.json"):
                metadata = json.loads(body)
                metadata["sha256"] = "0" * 64
                return json.dumps(metadata).encode()
            return body

        with patch.object(self, "mirror_fetch", changed_mirror):
            with self.assertRaises(UpdateError) as error:
                update(self.store, require_index=True, fetch=fetch)
        self.assertEqual(error.exception.code, "VERSION_CONFLICT")
        self.assertEqual(self.installed()["version"], "1.1.0")

    def test_bad_checksums_conflicts_and_downgrades_do_not_switch_sources(self):
        before = snapshot(Path(self.refresh()["path"]))
        self.publish("1.1.0", "New release")
        self.content += b"bad bytes"
        self.calls.clear()
        with self.assertRaises(UpdateError) as error:
            self.refresh()
        self.assertEqual(error.exception.code, "CHECKSUM_MISMATCH")
        self.assertFalse(any(url.startswith(skill_update.OFFICIAL_MIRROR) for url in self.calls))
        with self.assertRaises(UpdateError) as error:
            update(self.store, require_index=True, fetch=self.mirror_fetch)
        self.assertEqual(error.exception.code, "CHECKSUM_MISMATCH")
        self.assert_old(before)
        for version, code in (("1.0.0", "VERSION_CONFLICT"), ("0.9.0", "OLDER_RELEASE")):
            self.publish(version, "Different bytes")
            with self.assertRaises(UpdateError) as error:
                update(self.store, require_index=True, fetch=self.mirror_fetch)
            self.assertEqual(error.exception.code, code)
            self.assert_old(before)

    def test_invalid_primary_metadata_does_not_consult_mirror(self):
        self.refresh()
        for invalid_part in ("tag", "checksum"):
            self.calls.clear()

            def fetch(url, *args):
                if url.endswith("/releases/latest") and invalid_part == "tag":
                    self.calls.append(url)
                    return b"https://github.com/other/repo/releases/tag/sai-user-guide-v9.0.0"
                if url.endswith(".sha256") and invalid_part == "checksum":
                    self.calls.append(url)
                    return b"not a SHA-256 receipt"
                return self.fetch(url, *args)

            with self.assertRaises(UpdateError) as error:
                update(self.store, require_index=True, fetch=fetch)
            self.assertIn(error.exception.code, {"INVALID_RELEASE", "CHECKSUM_MISMATCH"})
            self.assertFalse(any(url.startswith(skill_update.OFFICIAL_MIRROR) for url in self.calls))

    def test_mirror_metadata_cannot_redirect_to_another_path_or_identity(self):
        before = snapshot(Path(self.refresh()["path"]))
        for field, value in (("archive", "../other.zip"), ("archive", "https://example.org/file.zip"),
                             ("release", "https://example.org/release"), ("name", "other-guide"),
                             ("version", "1.2.0-rc.1"), ("sha256", "bad")):
            def fetch(url, limit, deadline):
                body = self.mirror_fetch(url, limit, deadline)
                if url.endswith("release.json"):
                    metadata = json.loads(body); metadata[field] = value
                    return json.dumps(metadata).encode()
                return body
            with self.assertRaises(UpdateError) as error:
                update(self.store, require_index=True, fetch=fetch)
            self.assertEqual(error.exception.code, "INVALID_RELEASE")
            self.assert_old(before)
        for url in ("https://www.open-sai.com/docs/skills/../private.zip", "https://www.open-sai.com/other/release.json",
                    "http://www.open-sai.com/docs/skills/release.json", "https://example.org/docs/skills/release.json"):
            with self.assertRaises(UpdateError):
                skill_update._release_url(url)

    def test_actual_http_static_mirror_after_primary_http_failure(self):
        fixture = self
        requests = []
        slow_body = threading.Event()

        class Static(http.server.BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_HEAD(self):
                requests.append((self.command, self.path))
                self.send_error(503)

            def do_GET(self):
                requests.append((self.command, self.path))
                body = fixture.mirror_fetch("https://www.open-sai.com" + self.path, 0, 0)
                self.send_response(200)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                if slow_body.is_set():
                    time.sleep(0.12)
                try:
                    self.wfile.write(body)
                except (BrokenPipeError, ConnectionResetError):
                    pass

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Static)
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        native_opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

        class LoopbackTransport:
            def open(self, request, timeout):
                # Only route authority to an isolated HTTP fixture. The actual
                # request, HTTP failure, response streaming and updater execute.
                url = f"http://127.0.0.1:{server.server_port}" + skill_update.urlsplit(request.full_url).path
                return native_opener.open(urllib.request.Request(url, method=request.method), timeout=timeout)

        try:
            with patch.object(skill_update.urllib.request, "build_opener", return_value=LoopbackTransport()):
                result = update(self.store, require_index=True)
            self.assertEqual(result["source"], "sai")
            self.assertEqual(self.installed()["version"], "1.0.0")
            self.assertEqual(requests, [("HEAD", "/AI4SAI/lark_skill_creator/releases/latest"),
                                        ("GET", "/docs/skills/release.json"), ("GET", "/docs/skills/sai-user-guide-v1.0.0.zip")])
            slow_body.set()
            started = time.monotonic()
            with patch.object(skill_update.urllib.request, "build_opener", return_value=LoopbackTransport()):
                with self.assertRaises(UpdateError) as error:
                    skill_update._fetch(skill_update.OFFICIAL_MIRROR + "release.json", 4096, started + 0.04)
            self.assertEqual(error.exception.code, "DOWNLOAD_FAILED")
            self.assertLess(time.monotonic() - started, 0.3)
        finally:
            server.shutdown(); server.server_close(); thread.join(timeout=5)

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

    def test_failed_status_publication_restores_previous_and_preserves_replacement(self):
        before = snapshot(Path(self.refresh()["path"]))
        self.publish("1.1.0", "New manual")
        status = self.store / "status.json"
        outside = self.root / "preserved.txt"
        outside.write_text("KEEP")
        status.unlink()
        for replacement in ("symlink", "directory"):
            if replacement == "symlink":
                status.symlink_to(outside)
            else:
                status.mkdir()
            with self.assertRaises(UpdateError) as error:
                self.refresh()
            self.assertEqual(error.exception.code, "LOCAL_MODIFIED")
            self.assertEqual(os.readlink(self.store / "current"), "versions/1.0.0")
            self.assertEqual(snapshot(Path(self.installed()["path"])), before)
            self.assertEqual(outside.read_text(), "KEEP")
            status.unlink() if replacement == "symlink" else status.rmdir()

    def test_same_remote_version_cannot_override_or_misreport_admin_rollback(self):
        self.refresh()
        self.publish("1.1.0", "New manual")
        self.refresh()

        def fetch(url, *args):
            if url.endswith(".sha256"):
                pointer = self.store / "admin-rollback"
                pointer.symlink_to("versions/1.0.0")
                pointer.replace(self.store / "current")
            return self.fetch(url, *args)

        with self.assertRaises(UpdateError) as error:
            update(self.store, require_index=True, fetch=fetch)
        self.assertEqual(error.exception.code, "LOCAL_MODIFIED")
        self.assertEqual(os.readlink(self.store / "current"), "versions/1.0.0")
        self.assertEqual(self.installed()["version"], "1.0.0")
        self.assertEqual(json.loads((self.store / "status.json").read_text())["state"], "failed")

    def test_version_retention_keeps_current_previous_and_changed_data(self):
        self.refresh()
        self.publish("1.1.0", "Second")
        self.refresh()
        self.publish("1.2.0", "Third")
        result = self.refresh()
        self.assertEqual(result["removed_versions"], ["1.0.0"])
        self.assertEqual({path.name for path in (self.store / "versions").iterdir()}, {"1.1.0", "1.2.0"})
        (self.store / "versions/1.1.0/sai-user-guide/references/handbook/manual.md").write_text("Operator edit")
        self.publish("1.3.0", "Fourth")
        result = self.refresh()
        self.assertEqual(len(result["retained_versions"]), 1)
        self.assertEqual((self.store / "versions/1.1.0/sai-user-guide/references/handbook/manual.md").read_text(), "Operator edit")

    def test_reader_lock_prevents_switch_and_cleanup_until_read_finishes(self):
        self.refresh()
        self.publish("1.1.0", "Second")
        self.refresh()
        self.publish("1.2.0", "Third")
        with reading(self.store):
            with self.assertRaises(UpdateError) as error:
                self.refresh()
            self.assertEqual(error.exception.code, "UPDATE_BUSY")
            self.assertTrue((self.store / "versions/1.0.0").exists())
        self.assertEqual(self.refresh()["removed_versions"], ["1.0.0"])

    def test_cold_consumer_reads_old_version_while_writer_downloads(self):
        self.refresh()
        self.publish("1.1.0", "Second")
        tool = runtime(self.root / "cold-reader.pyz")
        observations = []

        def fetch(url, *args):
            if url.endswith(".zip"):
                process = subprocess.run([sys.executable, tool["archive"], "current", "--store", str(self.store), "--require-index"],
                                         capture_output=True, text=True, timeout=5)
                self.assertEqual(process.returncode, 0, process.stderr)
                observations.append(json.loads(process.stdout)["version"])
            return self.fetch(url, *args)

        result = update(self.store, require_index=True, fetch=fetch)
        self.assertEqual(observations, ["1.0.0"])
        self.assertEqual(result["version"], "1.1.0")

    def test_native_current_hold_releases_on_stdin_ack(self):
        self.refresh()
        tool = runtime(self.root / "hold.pyz")
        child = subprocess.Popen([sys.executable, tool["archive"], "current", "--store", str(self.store), "--require-index", "--hold"],
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            receipt = json.loads(child.stdout.readline())
            self.assertEqual(receipt["version"], "1.0.0")
            with self.assertRaises(UpdateError) as error:
                self.refresh()
            self.assertEqual(error.exception.code, "UPDATE_BUSY")
            child.stdin.write("\n")
            child.stdin.flush()
            self.assertEqual(child.wait(timeout=5), 0)
        finally:
            if child.poll() is None:
                child.terminate()
                child.wait(timeout=5)
            child.stdin.close(); child.stdout.close(); child.stderr.close()
        self.assertFalse(self.refresh()["updated"])

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

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_user_backup_retention_keeps_previous_and_open_or_changed_originals(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        with patch.object(skill_update.pwd, "getpwuid", return_value=account):
            installed = install_user(self.store, agent="codex")
            original = Path(installed["destination"]) / "references/handbook/manual.md"
            with original.open("a") as editor:
                self.publish("1.1.0", "Second")
                self.refresh()
                first = install_user(self.store, agent="codex")
                self.publish("1.2.0", "Third")
                self.refresh()
                second = install_user(self.store, agent="codex")
                self.assertIn(first["backup"], [row["path"] for row in second["retained_backups"]])
                self.assertTrue(Path(first["backup"]).exists())
            repeated = install_user(self.store, agent="codex")
            self.assertIn(first["backup"], repeated["removed_backups"])
            self.assertTrue(Path(second["backup"]).exists())
            (Path(second["backup"]) / "sai-user-guide/references/handbook/manual.md").write_text("Personal retained edit")
            self.publish("1.3.0", "Fourth")
            self.refresh()
            third = install_user(self.store, agent="codex")
            self.assertIn(second["backup"], [row["path"] for row in third["retained_backups"]])
            self.assertEqual((Path(second["backup"]) / "sai-user-guide/references/handbook/manual.md").read_text(), "Personal retained edit")
            reopened = install_user(self.store, agent="codex", dry_run=True)
            self.assertIn(second["backup"], [row["path"] for row in reopened["retained_backups"]])

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_self_sealed_personal_package_is_preserved_by_install_provenance(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        with patch.object(skill_update.pwd, "getpwuid", return_value=account):
            result = install_user(self.store, agent="codex")
            target = Path(result["destination"])
            (target / "references/handbook/manual.md").write_text("Unique personally sealed text")
            seal(target)
            self.publish("1.1.0", "Second")
            self.refresh()
            with self.assertRaises(UpdateError) as error:
                install_user(self.store, agent="codex")
            self.assertEqual(error.exception.code, "LOCAL_MODIFIED")
            self.assertEqual((target / "references/handbook/manual.md").read_text(), "Unique personally sealed text")

    @unittest.skipIf(os.geteuid() == 0, "User install intentionally refuses root")
    def test_backup_retention_is_per_native_destination(self):
        self.refresh()
        account = types.SimpleNamespace(pw_dir=str(self.home))
        with patch.object(skill_update.pwd, "getpwuid", return_value=account):
            install_user(self.store, agent="codex")
            self.publish("1.1.0", "Second"); self.refresh()
            install_user(self.store, agent="claude")
            self.publish("1.2.0", "Third"); self.refresh()
            codex_backup = install_user(self.store, agent="opencode")["backup"]
            self.publish("1.3.0", "Fourth"); self.refresh()
            claude_backup = install_user(self.store, agent="claude")["backup"]
            self.assertEqual(check(Path(codex_backup) / "sai-user-guide")["version"], "1.0.0")
            self.assertEqual(check(Path(claude_backup) / "sai-user-guide")["version"], "1.1.0")
            self.publish("1.4.0", "Fifth"); self.refresh()
            result = install_user(self.store, agent="codex")
            self.assertIn(codex_backup, result["removed_backups"])
            self.assertTrue(Path(claude_backup).exists())
            self.assertEqual(check(Path(result["backup"]) / "sai-user-guide")["version"], "1.2.0")

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
