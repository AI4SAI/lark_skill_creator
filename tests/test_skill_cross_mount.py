"""Real same-device bind mounts exercise the legacy installation boundary."""
import errno
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from skill_package import check, install, seal, snapshot
from wiki_exporter.lark import ExportError
from skill_update import prune_backups


def exercise(root, scenario):
    source = root / "source/sai-user-guide"
    source.mkdir(parents=True)
    (source / "SKILL.md").write_text('---\nname: sai-user-guide\ndescription: Mount fixture.\nmetadata:\n  version: "1.0.0"\n---\n[Use](references/use.md)\n')
    (source / "references").mkdir()
    (source / "references/use.md").write_text("Original")
    seal(source)
    legacy = root / "legacy/sai-user-guide"
    shutil.copytree(source, legacy)
    (root / "legacy/unrelated").mkdir()
    (root / "legacy/unrelated/SKILL.md").write_text("User-owned unrelated Skill")
    destination = root / "home/.agents/skills"
    backup = root / "home/.local/share/sai-skill-backups"
    backup.mkdir(parents=True)
    old = snapshot(legacy)
    old_inode = (legacy / "references/use.md").stat().st_ino
    assert legacy.stat().st_dev == backup.stat().st_dev
    try:
        legacy.rename(backup / "probe")
    except OSError as error:
        assert error.errno == errno.EXDEV
    else:
        raise AssertionError("Fixture did not create a real mount boundary")
    (source / "SKILL.md").write_text((source / "SKILL.md").read_text().replace('"1.0.0"', '"1.1.0"'))
    (source / "references/use.md").write_text("Updated")
    seal(source)
    target = destination / "sai-user-guide"

    def perform():
        return install(source, destination, backup=backup, retire_managed=(legacy,))

    if scenario in {"success", "cleanup_failure"}:
        rmtree = shutil.rmtree
        def cleanup(path, *args, **kwargs):
            if scenario == "cleanup_failure" and Path(path).name.startswith(".skill-retired-"):
                raise PermissionError("Fixture cleanup denied")
            return rmtree(path, *args, **kwargs)
        with patch.object(shutil, "rmtree", cleanup):
            receipt = perform()
        saved = Path(receipt["backup"]) / "legacy-1/sai-user-guide"
        assert snapshot(saved) == old
        assert (saved / "references/use.md").stat().st_ino != old_inode
        assert not legacy.exists()
        assert check(target)["version"] == "1.1.0"
        assert receipt["copied_legacy"] == [str(legacy)]
        assert list((root / "legacy").rglob("SKILL.md")) == [root / "legacy/unrelated/SKILL.md"]
        if scenario == "cleanup_failure":
            retained = receipt["retained_backups"][0]["path"]
            assert Path(retained).exists()
            assert retained in [row["path"] for row in prune_backups(backup, dry_run=True)["retained_backups"]]
        else:
            assert not receipt["retained_backups"]
            assert not list((root / "legacy").glob(".skill-retired-*"))
        return {"scenario": scenario, "same_device": True, "real_exdev": True, "verified": True,
                "backup_same_bytes": True, "backup_same_inode": False, "legacy_not_discovered": True}

    rename = Path.rename
    copytree = shutil.copytree
    write_text = Path.write_text

    def failing_rename(path, to):
        if scenario == "publish_failure" and path == source:
            raise AssertionError("Source unexpectedly moved")
        if scenario == "publish_failure" and path.name == "sai-user-guide" and path.parent.name.startswith(".skill-install-"):
            raise OSError("Publication failed")
        result = rename(path, to)
        if scenario == "retire_edit" and path == legacy and Path(to).name.startswith(".skill-retired-"):
            (Path(to) / "references/use.md").write_text("Changed concurrently after in-place rename")
        if scenario == "entry_failure" and path.name == "SKILL.md" and Path(to).name == ".SKILL.md.retired":
            raise OSError("Entry retirement failed after rename")
        return result

    def changed_copy(path, to, *args, **kwargs):
        result = copytree(path, to, *args, **kwargs)
        if scenario == "copy_edit" and path == legacy:
            (legacy / "references/use.md").write_text("Changed concurrently during copy")
        return result

    def failed_receipt(path, content, *args, **kwargs):
        if scenario == "receipt_failure" and path.name == "backup.json" and "retained_originals" in content:
            raise OSError("Receipt publication failed")
        return write_text(path, content, *args, **kwargs)

    if scenario == "open_editor":
        with (legacy / "references/use.md").open("a") as editor:
            try:
                perform()
            except ExportError:
                pass
            else:
                raise AssertionError("Open original was discarded")
            editor.write("Later editor save")
            editor.flush()
        assert "Later editor save" in (legacy / "references/use.md").read_text()
    else:
        with patch.object(Path, "rename", failing_rename), patch.object(shutil, "copytree", changed_copy), patch.object(Path, "write_text", failed_receipt):
            try:
                perform()
            except (ExportError, OSError):
                pass
            else:
                raise AssertionError("Expected rollback")
        if scenario in {"copy_edit", "retire_edit"}:
            assert "Changed concurrently" in (legacy / "references/use.md").read_text()
        else:
            assert snapshot(legacy) == old
    assert (legacy / "references/use.md").stat().st_ino == old_inode
    assert not target.exists()
    assert not list((root / "legacy").glob(".skill-retired-*"))
    assert (root / "legacy/unrelated/SKILL.md").read_text() == "User-owned unrelated Skill"
    return {"scenario": scenario, "real_exdev": True, "original_inode_retained": True,
            "original_restored": True, "new_target_removed": True}


@unittest.skipUnless(shutil.which("bwrap") and sys.platform == "linux", "Linux bubblewrap required")
class CrossMountTests(unittest.TestCase):
    def test_real_bind_mount_install_and_rollback(self):
        for scenario in ("success", "publish_failure", "copy_edit", "retire_edit", "entry_failure", "open_editor", "cleanup_failure", "receipt_failure"):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory(prefix="skill-cross-mount-") as temporary:
                root = Path(temporary)
                (root / "legacy").mkdir()
                command = ["bwrap", "--ro-bind", "/", "/", "--bind", temporary, temporary,
                           "--bind", str(root / "legacy"), str(root / "legacy"), "--dev", "/dev",
                           "--", sys.executable, str(Path(__file__).resolve()), "--child", temporary, scenario]
                result = subprocess.run(command, capture_output=True, text=True, timeout=20,
                                        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1",
                                             "PYTHONPATH": str(Path(__file__).resolve().parents[1])})
                self.assertEqual(result.returncode, 0, result.stderr)
                print(result.stdout.strip())


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--child":
        print(json.dumps(exercise(Path(sys.argv[2]), sys.argv[3])))
    else:
        unittest.main()
