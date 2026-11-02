"""Check, package and safely install a versioned, ordinary filesystem Skill."""

import argparse
import difflib
import hashlib
import json
import re
import shutil
import sys
import tempfile
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

from wiki_exporter.bundle import canonical_directory, inventory, read_manifest
from wiki_exporter.lark import ExportError


KIND = "sai-user-skill/v1"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def snapshot(root: Path) -> dict[str, str]:
    files = inventory(root)
    manifest = root / "manifest.json"
    if manifest.is_file():
        files["manifest.json"] = hashlib.sha256(manifest.read_bytes()).hexdigest()
    return files


def skill_metadata(root: Path) -> tuple[str, str]:
    """The maintained entry uses a plain name and a quoted metadata.version."""
    entry = (root / "SKILL.md").read_text(encoding="utf-8")
    header = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", entry, re.DOTALL)
    if not header:
        raise ExportError("SKILL.md 缺少 frontmatter。")
    name = re.search(r"^name: ([a-z0-9-]+)\s*$", header[1], re.MULTILINE)
    version = re.search(r'^  version: "([0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.]+)?)"\s*$', header[1], re.MULTILINE)
    if not name or not NAME.fullmatch(name[1]) or len(name[1]) > 64 or not version:
        raise ExportError("请填写普通名称和 metadata.version（带引号的版本号）。")
    if root.name != name[1]:
        raise ExportError("Skill 目录名与 name 不一致。")
    return name[1], version[1]


def check_links(root: Path) -> None:
    for page in root.rglob("*.md"):
        for target in re.findall(r"\]\(([^\s)]+)\)", page.read_text(encoding="utf-8")):
            url = urlsplit(target)
            if url.scheme in {"https", "http", "mailto"}:
                continue
            if url.scheme or url.netloc or Path(unquote(url.path)).is_absolute():
                raise ExportError(f"{page.relative_to(root)} 含不可移植的链接：{target}")
            path = (page.parent / unquote(url.path)).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                raise ExportError(f"{page.relative_to(root)} 引用缺失或越界：{target}")


def seal(source: Path) -> dict:
    root = canonical_directory(source)
    name, version = skill_metadata(root)
    files = inventory(root)
    check_links(root)
    manifest = {"kind": KIND, "name": name, "version": version, "files": files}
    (root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def check(source: Path) -> dict:
    root = canonical_directory(source)
    try:
        manifest = read_manifest(root)
    except (AttributeError, TypeError) as error:
        raise ExportError("版本清单格式错误。") from error
    name, version = skill_metadata(root)
    if (manifest.get("kind"), manifest.get("name"), manifest.get("version")) != (KIND, name, version):
        raise ExportError("版本清单与 Skill 入口不一致。")
    check_links(root)
    return manifest


def pack(source: Path, output: Path) -> dict:
    root, output = canonical_directory(source), canonical_directory(output)
    if output.is_relative_to(root):
        raise ExportError("发行包不能写回 Skill 目录。")
    manifest = check(root)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{manifest['name']}-{manifest['version']}.zip"
    with tempfile.TemporaryDirectory(prefix=".skill-package-", dir=output.parent) as temporary:
        candidate = Path(temporary) / archive.name
        with zipfile.ZipFile(candidate, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for relative in sorted([*manifest["files"], "manifest.json"]):
                info = zipfile.ZipInfo(f"{manifest['name']}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                bundle.writestr(info, (root / relative).read_bytes())
        if check(root) != manifest:
            raise ExportError("打包时源文件发生变化。")
        content = candidate.read_bytes()
        if archive.exists():
            if archive.is_symlink() or archive.read_bytes() != content:
                raise ExportError("同版本发行包已存在且内容不同，请更新版本号。")
        else:
            with archive.open("xb") as stream:
                stream.write(content)
        digest = hashlib.sha256(content).hexdigest()
        receipt = output / (archive.name + ".sha256")
        if receipt.is_symlink():
            raise ExportError("校验文件不能是符号链接。")
        receipt.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return {"archive": str(archive), "sha256": digest, "version": manifest["version"]}


def diff(old: Path, new: Path) -> str:
    old, new = canonical_directory(old), canonical_directory(new)
    check(new)
    before, after = inventory(old), inventory(new)
    lines = []
    for name in sorted(before.keys() | after.keys()):
        if before.get(name) == after.get(name):
            continue
        action = "新增" if name not in before else "移除" if name not in after else "修改"
        lines.append(f"{action} {name}\n")
        if name in before and name in after and name.endswith(".md"):
            lines.extend(difflib.unified_diff(
                (old / name).read_text(encoding="utf-8").splitlines(keepends=True),
                (new / name).read_text(encoding="utf-8").splitlines(keepends=True),
                fromfile=f"before/{name}", tofile=f"after/{name}",
            ))
    return "".join(lines) or "内容一致。\n"


def install(source: Path, destination: Path, *, backup: Path | None = None,
            archive_existing: bool = False, retire: tuple[str, ...] = (), dry_run: bool = False,
            retire_managed: tuple[Path, ...] = (), original_receipts: dict | None = None) -> dict:
    source, destination = canonical_directory(source), canonical_directory(destination)
    manifest = check(source)
    if source.is_relative_to(destination) or destination.is_relative_to(source):
        raise ExportError("来源与安装目录不能重叠。")
    name = manifest["name"]
    if any(not NAME.fullmatch(item) or len(item) > 64 or item == name for item in retire):
        raise ExportError("停用名称无效，不能停用正在安装的 Skill。")
    target = destination / name
    managed = tuple(canonical_directory(path) for path in retire_managed)
    if any(path.name != name or path.is_relative_to(destination) or destination.is_relative_to(path)
           or path.is_relative_to(source) or source.is_relative_to(path) for path in managed):
        raise ExportError("旧安装路径无效。")
    existing = {}
    originals = {}
    unchanged = False
    for path in [target, *(destination / item for item in sorted(set(retire))), *managed]:
        if path.is_symlink():
            raise ExportError(f"{path.name} 是符号链接，请由客户端原有安装方式管理。")
        if not path.exists():
            continue
        files = snapshot(path)
        if path == target:
            try:
                previous = check(path)
            except (ExportError, OSError, ValueError):
                if not archive_existing:
                    raise ExportError("已有旧包或本地修改。先查看 diff；要保留备份后替换，显式使用 --archive-existing。")
            else:
                originals[path] = previous
                unchanged = previous == manifest
                if unchanged:
                    continue
                if previous["version"] == manifest["version"]:
                    raise ExportError("相同版本却有不同内容，请先核对来源或更新版本号。")
        elif path in managed:
            # A native discovery root may still contain an earlier managed copy.
            # Only verified packages can be retired by a one-click reinstall.
            previous = check(path)
            originals[path] = previous
            if previous["name"] != name or (previous["version"] == manifest["version"] and previous != manifest):
                raise ExportError("旧安装与当前版本冲突，请先核对内容。")
        elif not archive_existing:
            raise ExportError("停用旧 Skill 须显式使用 --archive-existing 并保留备份。")
        existing[path] = files
    if existing and backup is None:
        raise ExportError("更新或停用已有 Skill 时必须指定 --backup-dir。")
    if backup is not None:
        backup = canonical_directory(backup)
        if any(backup.is_relative_to(p) or p.is_relative_to(backup) for p in (destination, source, *managed)):
            raise ExportError("备份必须位于来源和 Skill 发现目录之外。")
    plan = {"name": name, "version": manifest["version"], "destination": str(target),
            "replace": [p.name for p in existing], "already_current": unchanged and not existing,
            "dry_run": dry_run, "retire_from": [str(path) for path in managed if path in existing]}
    if dry_run or (unchanged and not existing):
        return plan
    destination.mkdir(parents=True, exist_ok=True)
    backup_run = None
    with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=destination.parent) as temporary:
        temporary = Path(temporary)
        candidate = temporary / name
        shutil.copytree(source, candidate)
        if check(candidate) != manifest or check(source) != manifest:
            raise ExportError("复制期间来源发生变化。")
        candidate_snapshot = snapshot(candidate)
        if existing:
            backup.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup_run = backup / (stamp + "-" + uuid.uuid4().hex[:8])
            backup_run.mkdir(mode=0o700)
            if backup_run.stat().st_dev != destination.stat().st_dev:
                raise ExportError("备份须与安装目录位于同一文件系统，才能保留编辑器仍在写入的原文件。")
            packages = {}
            for path, files in existing.items():
                relative = path.name if path not in managed else ("legacy-" + str(managed.index(path) + 1) + "/" + name)
                original = originals.get(path)
                provenance = (original_receipts or {}).get(str(path))
                if not original or not provenance or provenance.get("manifest_sha256") != files.get("manifest.json") or provenance.get("version") != original["version"]:
                    provenance = None
                packages[relative] = {"managed": original is not None,
                    "manifest_sha256": files.get("manifest.json"),
                    "version": original["version"] if original else None,
                    "release": provenance}
            (backup_run / "backup.json").write_text(json.dumps({
                "kind": "sai-skill-backup/v1", "created_at": datetime.now(timezone.utc).isoformat(),
                "packages": packages,
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        moved = []
        published = False
        try:
            for path, files in existing.items():
                if snapshot(path) != files:
                    raise ExportError("已有内容发生变化，未替换。")
                # Keep the actual old inodes, including writes through already-open
                # editor handles. A pre-update copy is not a sufficient backup.
                saved = backup_run / path.name if path not in managed else backup_run / ("legacy-" + str(managed.index(path) + 1)) / name
                saved.parent.mkdir(parents=True, exist_ok=True)
                moved.append((path, saved))
                path.rename(saved)
            if not unchanged:
                if target.exists() or target.is_symlink():
                    raise ExportError("目标已被其他进程创建，未覆盖。")
                published = True
                candidate.rename(target)
            if check(target) != manifest:
                raise ExportError("安装读回不一致。")
        except BaseException:
            if published and target.exists():
                # Never delete concurrent user edits during rollback.
                if snapshot(target) != candidate_snapshot:
                    raise ExportError(f"安装后内容被修改，请从保留备份恢复：{backup_run}")
                shutil.rmtree(target)
            for path, saved in reversed(moved):
                # A signal may arrive immediately after rename returns, or the
                # rename itself may have failed before moving the original.
                if not saved.exists() and path.exists():
                    continue
                if path.exists() or path.is_symlink():
                    raise ExportError(f"恢复目标已被占用，请从保留备份恢复：{backup_run}")
                saved.rename(path)
            raise
    return {**plan, "backup": str(backup_run) if backup_run else None, "verified": True}


def main() -> int:
    parser = argparse.ArgumentParser(description="检查、打包与安装普通文件夹形式的 SAI Skill；不会发布或改客户端配置。")
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("seal", "check", "pack", "install"):
        p = commands.add_parser(command)
        p.add_argument("source", type=Path)
        if command == "pack":
            p.add_argument("--output", type=Path, required=True)
        if command == "install":
            p.add_argument("--dest", type=Path, required=True)
            p.add_argument("--backup-dir", type=Path)
            p.add_argument("--archive-existing", action="store_true")
            p.add_argument("--retire", action="append", default=[])
            p.add_argument("--dry-run", action="store_true")
    p = commands.add_parser("diff")
    p.add_argument("old", type=Path)
    p.add_argument("new", type=Path)
    p = commands.add_parser("update", help="校验正式 Release 后切换本地托管版本")
    p.add_argument("--store", type=Path, required=True)
    p.add_argument("--repository", default="AI4SAI/lark_skill_creator")
    p.add_argument("--name", default="sai-user-guide")
    p.add_argument("--require-index", action="store_true")
    p = commands.add_parser("current", help="校验并读回当前本地版本")
    p.add_argument("--store", type=Path, required=True)
    p.add_argument("--require-index", action="store_true")
    p.add_argument("--hold", action="store_true", help="读回一行 JSON，等待 stdin 确认后释放读取锁")
    p = commands.add_parser("install-user", help="以本人登录身份安装供命令行 Agent 使用的副本")
    p.add_argument("--store", type=Path, required=True)
    p.add_argument("--agent", choices=("codex", "opencode", "claude"), required=True)
    p.add_argument("--dry-run", action="store_true")
    p = commands.add_parser("runtime", help="生成仅使用 Python 标准库的安装工具")
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "diff":
            print(diff(args.old, args.new), end="")
            return 0
        if args.command == "update":
            from skill_update import update
            result = update(args.store, name=args.name, repository=args.repository,
                            require_index=args.require_index)
        elif args.command == "install-user":
            from skill_update import install_user
            result = install_user(args.store, agent=args.agent, dry_run=args.dry_run)
        elif args.command == "current":
            from skill_update import current, current_hold
            if args.hold:
                current_hold(args.store, require_index=args.require_index)
                return 0
            result = current(args.store, require_index=args.require_index)
        elif args.command == "runtime":
            result = runtime(args.output)
        elif args.command == "pack":
            result = pack(args.source, args.output)
        elif args.command == "install":
            result = install(args.source, args.dest, backup=args.backup_dir,
                             archive_existing=args.archive_existing, retire=tuple(args.retire), dry_run=args.dry_run)
        else:
            result = {"command": args.command, **(seal(args.source) if args.command == "seal" else check(args.source))}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(json.dumps({"ok": False, "state": "failed", "code": getattr(error, "code", "INVALID_PACKAGE"),
                          "error": str(error), **getattr(error, "details", {})}, ensure_ascii=False), file=sys.stderr)
        return 1


def runtime(output: Path) -> dict:
    """Deterministic stdlib-only zipapp, shared by service and user installs."""
    output = canonical_directory(output)
    root = Path(__file__).parent
    files = {name: (root / name).read_bytes() for name in
             ("skill_package.py", "skill_update.py", "wiki_exporter/__init__.py",
              "wiki_exporter/bundle.py", "wiki_exporter/lark.py")}
    files["__main__.py"] = b"from skill_package import main\nraise SystemExit(main())\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".skill-runtime-", dir=output.parent) as temporary:
        candidate = Path(temporary) / "runtime.pyz"
        with zipfile.ZipFile(candidate, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for name, content in sorted(files.items()):
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                bundle.writestr(info, content)
        candidate.chmod(0o644)
        candidate.replace(output)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {"archive": str(output), "sha256": digest}


if __name__ == "__main__":
    raise SystemExit(main())
