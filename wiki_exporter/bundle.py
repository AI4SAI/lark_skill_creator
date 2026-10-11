"""A complete generated tree may replace only an unchanged managed output."""

import hashlib
import json
import tempfile
from contextlib import contextmanager
from pathlib import Path

from .lark import ExportError


def canonical_directory(path: Path) -> Path:
    path = path.absolute()
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise ExportError("目录路径不能经过符号链接。")
    return path.resolve()


def inventory(root: Path) -> dict[str, str]:
    if root.is_symlink():
        raise ExportError("输出目录不能是符号链接。")
    result = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ExportError("输出中含有符号链接。")
        if path.is_file() and path.relative_to(root).as_posix() != "manifest.json":
            result[path.relative_to(root).as_posix()] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return result


def read_manifest(root: Path) -> dict:
    root = canonical_directory(root)
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("files") != inventory(root):
        raise ExportError("文件与清单不一致，已有修改不会被覆盖。")
    return manifest


def review_digest(manifest: dict) -> str:
    """An unchanged export can reuse its review despite a new export timestamp."""
    reviewed = {
        "space_id": manifest["space_id"],
        "pages": manifest["pages"],
        "content": {
            name: digest
            for name, digest in manifest["files"].items()
            if name.startswith("content/")
        },
    }
    return hashlib.sha256(
        json.dumps(
            reviewed, sort_keys=True, ensure_ascii=False, separators=(",", ":")
        ).encode()
    ).hexdigest()


@contextmanager
def build_directory(output: Path, *, replace: bool, kind: str):
    output = canonical_directory(output)
    previous = None
    if output.exists():
        if not replace:
            raise ExportError("输出目录已存在；确认要更新生成内容后使用 --replace。")
        previous = read_manifest(output)
        if previous.get("kind") != kind:
            raise ExportError("输出目录属于其他流程，不会被覆盖。")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".wiki-build-", dir=output.parent
    ) as temporary:
        staging = Path(temporary) / "result"
        staging.mkdir(mode=0o700)
        yield staging
        read_manifest(staging)
        if previous is not None:
            if read_manifest(output) != previous:
                raise ExportError("构建期间原输出发生变化，未覆盖。")
            backup = Path(temporary) / "previous"
            output.rename(backup)
            try:
                staging.rename(output)
            except OSError:
                backup.rename(output)
                raise
        else:
            if output.exists():
                raise ExportError("输出已由其他进程创建，未覆盖。")
            staging.rename(output)


def write_manifest(root: Path, fields: dict) -> None:
    manifest = {**fields, "files": inventory(root)}
    if fields["kind"] == "lark-wiki-export/v1":
        manifest["content_sha256"] = review_digest(manifest)
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
