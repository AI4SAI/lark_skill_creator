"""Real UID, NSS, locks, filesystem and bind-mount migration; synthetic content only."""
import hashlib
import json
import os
from pathlib import Path
import pwd
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE))
from skill_package import seal, snapshot


@unittest.skipUnless(shutil.which("bwrap") and sys.platform == "linux" and os.geteuid() != 0,
                     "Linux bubblewrap and an ordinary user are required")
class NativeUnmanagedTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="unmanaged-skill-"))
        self.addCleanup(lambda: shutil.rmtree(self.root))
        self.home = self.root / "home"
        self.home.mkdir()
        self.legacy = self.home / ".codex/skills/sai-user-guide"
        self.target = self.home / ".agents/skills/sai-user-guide"
        self.store = self.root / "store"
        self.release("1.0.0")
        account = pwd.getpwuid(os.getuid())
        entries = [row for row in Path("/etc/passwd").read_text().splitlines()
                   if int(row.split(":")[2]) != os.getuid()]
        entries.append(f"{account.pw_name}:x:{os.getuid()}:{os.getgid()}:Synthetic Skill fixture:{self.home}:/bin/bash")
        self.passwd = self.root / "passwd"
        self.passwd.write_text("\n".join(entries) + "\n")

    def release(self, version):
        root = self.store / "versions" / version / "sai-user-guide"
        (root / "references").mkdir(parents=True)
        (root / "SKILL.md").write_text(f'---\nname: sai-user-guide\nmetadata:\n  version: "{version}"\n---\n[Guide](references/use.md)\n')
        body = f"Published synthetic guide {version}.\n"
        (root / "references/use.md").write_text(body)
        (root / "references/manifest.json").write_text(json.dumps({"fetched_at": "2026-01-01T00:00:00Z", "documents": [{
            "doc_id": "fixture", "title": "Fixture", "file": "use.md", "url": "https://example.org/guide",
            "revision": 1, "status": "fetched", "sharing": "anyone_readable", "sha256": hashlib.sha256(body.encode()).hexdigest()}]}))
        seal(root)
        receipt = {"name": "sai-user-guide", "version": version, "sha256": "a" * 64,
                   "manifest_sha256": hashlib.sha256((root / "manifest.json").read_bytes()).hexdigest()}
        (root.parent / "release.json").write_text(json.dumps(receipt))
        (self.store / ".update.lock").touch()
        current = self.store / "current"
        current.unlink(missing_ok=True)
        current.symlink_to("versions/" + version)

    def ordinary(self):
        (self.legacy / "resources").mkdir(parents=True)
        (self.legacy / "SKILL.md").write_bytes(b"---\nname: sai-user-guide\n---\nOriginal personal guidance.\r\n")
        (self.legacy / "resources/data.bin").write_bytes(bytes(range(256)))
        return snapshot(self.legacy)

    def command(self, *args, cross_mount=False, hold=False):
        argv = ["/usr/bin/bwrap", "--ro-bind", "/", "/", "--bind", str(self.root), str(self.root),
                "--ro-bind", str(self.passwd), "/etc/passwd", "--unshare-pid", "--proc", "/proc", "--dev", "/dev"]
        if cross_mount:
            argv.extend(["--bind", str(self.legacy.parent), str(self.legacy.parent)])
        code = "import sys;sys.path.insert(0,sys.argv.pop(1));import skill_package;"
        if hold:
            code += "held=open(sys.argv.pop(1),'rb');"
        code += "raise SystemExit(skill_package.main())"
        argv.extend(["--", "/usr/bin/python3", "-I", "-B", "-c", code, str(SOURCE)])
        if hold:
            argv.append(str(self.legacy / "SKILL.md"))
        argv.extend(["install-user", "--store", str(self.store), "--agent", "codex", *args])
        result = subprocess.run(argv, text=True, capture_output=True, timeout=20)
        self.assertIn(result.returncode, (0, 1), result.stderr)
        return json.loads(result.stdout if result.returncode == 0 else result.stderr)

    def preview(self, **kwargs):
        result = self.command("--dry-run", **kwargs)
        self.assertEqual(result["code"], "UNMANAGED_EXISTING", result)
        self.assertEqual(result["recovery"], "archive-and-install")
        self.assertRegex(result["plan_sha256"], "^[a-f0-9]{64}$")
        return result["plan_sha256"]

    def confirm(self, digest, **kwargs):
        return self.command("--archive-existing", "--expect-plan-sha256", digest, **kwargs)

    def test_unmanaged_preview_is_read_only_and_confirmation_preserves_original_bytes(self):
        before = self.ordinary()
        digest = self.preview()
        self.assertEqual(snapshot(self.legacy), before)
        self.assertFalse(self.target.exists())
        self.assertFalse((self.home / ".local").exists())
        result = self.confirm(digest)
        self.assertTrue(result["verified"], result)
        self.assertFalse(self.legacy.exists())
        backup = Path(result["backup"])
        self.assertEqual(snapshot(backup / "legacy-1/sai-user-guide"), before)
        self.assertFalse((backup / "legacy-1/sai-user-guide/manifest.json").exists())
        self.assertFalse(json.loads((backup / "backup.json").read_text())["packages"]["legacy-1/sai-user-guide"]["managed"])
        self.assertTrue(self.target.is_dir())
        self.assertTrue(self.confirm(digest)["already_current"])
        self.assertTrue(backup.exists())

    def test_actual_bind_mount_uses_original_cross_mount_transaction(self):
        before = self.ordinary()
        digest = self.preview(cross_mount=True)
        result = self.confirm(digest, cross_mount=True)
        self.assertTrue(result["verified"], result)
        self.assertEqual(result["copied_legacy"], [str(self.legacy)])
        self.assertEqual(snapshot(Path(result["backup"]) / "legacy-1/sai-user-guide"), before)
        self.assertFalse(self.legacy.exists())
        self.assertEqual(list(self.legacy.parent.glob(".skill-retired-*")), [])

    def test_changed_source_after_confirmation_is_not_replaced(self):
        self.ordinary()
        digest = self.preview()
        (self.legacy / "SKILL.md").write_text("New personal content after preview.\n")
        after = snapshot(self.legacy)
        self.assertEqual(self.confirm(digest)["code"], "PLAN_CHANGED")
        self.assertEqual(snapshot(self.legacy), after)
        self.assertFalse(self.target.exists())

    def test_changed_release_after_confirmation_is_not_installed(self):
        before = self.ordinary()
        digest = self.preview()
        self.release("1.1.0")
        self.assertEqual(self.confirm(digest)["code"], "PLAN_CHANGED")
        self.assertEqual(snapshot(self.legacy), before)
        self.assertFalse(self.target.exists())

    def test_unconfirmed_post_has_no_legacy_mutation(self):
        before = self.ordinary()
        self.assertEqual(self.command()["code"], "UNMANAGED_EXISTING")
        self.assertEqual(snapshot(self.legacy), before)
        self.assertFalse(self.target.exists())

    def test_modified_managed_copy_remains_protected(self):
        shutil.copytree(self.store / "current/sai-user-guide", self.legacy)
        (self.legacy / "SKILL.md").write_text("A changed managed package.\n")
        before = snapshot(self.legacy)
        result = self.command("--dry-run")
        self.assertEqual(result["code"], "LOCAL_MODIFIED")
        self.assertEqual(snapshot(self.legacy), before)
        self.assertNotIn("plan_sha256", result)

    def test_unmodified_managed_legacy_keeps_normal_installation(self):
        shutil.copytree(self.store / "current/sai-user-guide", self.legacy)
        result = self.command()
        self.assertTrue(result["verified"], result)
        self.assertFalse(self.legacy.exists())
        self.assertTrue(self.target.is_dir())

    def test_unmanaged_recovery_does_not_overwrite_modified_normal_target(self):
        self.ordinary()
        shutil.copytree(self.store / "current/sai-user-guide", self.target)
        (self.target / "SKILL.md").write_text("Personal modification at the normal target.\n")
        before = snapshot(self.target)
        result = self.command("--dry-run")
        self.assertEqual(result["code"], "LOCAL_MODIFIED")
        self.assertNotIn("plan_sha256", result)
        self.assertEqual(snapshot(self.target), before)

    def test_changed_normal_target_after_preview_rejects_stale_confirmation(self):
        before = self.ordinary()
        digest = self.preview()
        shutil.copytree(self.store / "current/sai-user-guide", self.target)
        self.assertEqual(self.confirm(digest)["code"], "PLAN_CHANGED")
        self.assertEqual(snapshot(self.legacy), before)

    def test_missing_manifest_with_original_receipt_is_not_unmanaged(self):
        self.ordinary()
        path = self.home / ".local/state/sai-skills/installed.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"kind": "sai-skill-install/v1", "destinations": {
            str(self.legacy): {"version": "1.0.0", "manifest_sha256": "b" * 64}}}))
        self.assertEqual(self.command("--dry-run")["code"], "LOCAL_MODIFIED")

    def test_read_permission_error_is_not_called_local_modification(self):
        self.ordinary()
        entry = self.legacy / "SKILL.md"
        entry.chmod(0)
        try:
            self.assertEqual(self.command("--dry-run")["code"], "SOURCE_UNAVAILABLE")
        finally:
            entry.chmod(0o600)

    def test_symlink_is_not_offered_unmanaged_recovery(self):
        self.ordinary()
        link = self.legacy / "resources/link"
        link.symlink_to(self.root / "outside")
        result = self.command("--dry-run")
        self.assertEqual(result["code"], "LOCAL_MODIFIED")
        self.assertNotIn("plan_sha256", result)

    def test_open_original_descriptor_blocks_cross_mount_retirement(self):
        before = self.ordinary()
        digest = self.preview(cross_mount=True)
        result = self.confirm(digest, cross_mount=True, hold=True)
        self.assertEqual(result["code"], "LOCAL_MODIFIED")
        self.assertEqual(snapshot(self.legacy), before)
        self.assertFalse(self.target.exists())


if __name__ == "__main__":
    unittest.main()
