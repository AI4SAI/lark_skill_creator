"""Release delivery for local Skill consumers; no daemon or model calls."""

import fcntl
import hashlib
import json
import os
import pwd
import re
import shutil
import signal
import stat
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from skill_package import NAME, check, install
from wiki_exporter.bundle import canonical_directory
from wiki_exporter.lark import ExportError


REPOSITORY = "AI4SAI/lark_skill_creator"
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+")
HOSTS = {"github.com", "release-assets.githubusercontent.com",
         "objects.githubusercontent.com", "github-releases.githubusercontent.com"}
MAX_ARCHIVE = 128 * 1024 * 1024
MAX_UNPACKED = 512 * 1024 * 1024


class UpdateError(ExportError):
    def __init__(self, code, message, **details):
        super().__init__(message)
        self.code, self.details = code, details


class _ReleaseRedirect(urllib.request.HTTPRedirectHandler):
    max_redirections = 5

    def redirect_request(self, request, fp, code, message, headers, url):
        _release_url(url)
        return super().redirect_request(request, fp, code, message, headers, url)


def _release_url(url):
    from urllib.parse import urlsplit
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in HOSTS
            or parsed.username or parsed.password or parsed.port not in (None, 443)):
        raise UpdateError("INVALID_RELEASE", "发行包地址无效。")


def _fetch(url, limit, deadline):
    _release_url(url)
    request = urllib.request.Request(url, method="HEAD" if limit == 0 else "GET",
                                     headers={"User-Agent": "sai-skill-package", "Accept": "application/octet-stream"})
    try:
        with urllib.request.build_opener(_ReleaseRedirect()).open(request, timeout=20) as response:
            if limit == 0:
                return response.geturl().encode("utf-8")
            if response.headers.get("Content-Length") and int(response.headers["Content-Length"]) > limit:
                raise UpdateError("DOWNLOAD_TOO_LARGE", "发行包超过大小限制。")
            data = bytearray()
            while True:
                if time.monotonic() > deadline:
                    raise UpdateError("DOWNLOAD_FAILED", "更新超时，已有版本保留。")
                block = response.read(min(65536, limit + 1 - len(data)))
                if not block:
                    return bytes(data)
                data.extend(block)
                if len(data) > limit:
                    raise UpdateError("DOWNLOAD_TOO_LARGE", "发行包超过大小限制。")
    except (OSError, urllib.error.URLError, ValueError) as error:
        raise UpdateError("DOWNLOAD_FAILED", "无法下载正式版本，已有版本保留。") from error


def _release(repository, name, fetch, deadline):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) or not NAME.fullmatch(name):
        raise UpdateError("INVALID_RELEASE", "发行来源或 Skill 名称无效。")
    # GitHub's native latest-release redirect selects a published, non-prerelease
    # tag without requiring an API token or consuming the shared anonymous quota.
    release = fetch(f"https://github.com/{repository}/releases/latest", 0, deadline).decode("utf-8")
    prefix = f"https://github.com/{repository}/releases/tag/{name}-v"
    version = release.removeprefix(prefix)
    if not release.startswith(prefix) or not VERSION.fullmatch(version):
        raise UpdateError("INVALID_RELEASE", "没有可用的正式 Skill 版本。")
    base = f"https://github.com/{repository}/releases/download/{name}-v{version}/{name}.zip"
    result = {"name": name, "version": version, "release": release, "archive": base, "checksum": base + ".sha256"}
    checksum = fetch(result["checksum"], 4096, deadline).decode("ascii").strip()
    match = re.fullmatch(r"([0-9a-f]{64})\s+\*?" + re.escape(name) + r"\.zip", checksum)
    if not match:
        raise UpdateError("CHECKSUM_MISMATCH", "发行校验值不一致，已有版本保留。")
    return {**result, "sha256": match[1]}


def validate_index(root, required=False):
    path = root / "references/manifest.json"
    if not path.exists() and not required:
        return
    manifest = json.loads(path.read_text(encoding="utf-8"))
    rows = manifest["documents"]
    if not isinstance(rows, list) or not rows or not manifest.get("fetched_at"):
        raise UpdateError("INVALID_PACKAGE", "手册索引不完整。")
    ids = set()
    for row in rows:
        relative = PurePosixPath(row["file"])
        if (relative.is_absolute() or ".." in relative.parts or "\\" in str(relative)
                or not isinstance(row["doc_id"], str) or not row["doc_id"] or row["doc_id"] in ids
                or not isinstance(row.get("title"), str) or not row["title"].strip()
                or not isinstance(row.get("url"), str) or not row["url"].startswith("https://")
                or not isinstance(row.get("revision"), (str, int)) or row.get("status") != "fetched"
                or row.get("sharing") not in {"anyone_readable", "anyone_editable"}):
            raise UpdateError("INVALID_PACKAGE", "手册索引含无效文档。")
        content = (root / "references" / relative).read_bytes()
        if len(content) > 2 * 1024 * 1024 or not content.decode("utf-8").strip() or hashlib.sha256(content).hexdigest() != row["sha256"]:
            raise UpdateError("INVALID_PACKAGE", "手册正文与索引不一致。")
        ids.add(row["doc_id"])


def current_package(store, name="sai-user-guide", require_index=False):
    store = canonical_directory(store)
    current = store / "current"
    if not current.is_symlink():
        if current.exists():
            raise UpdateError("LOCAL_MODIFIED", "当前版本入口不是受管理的链接。")
        return None
    target = os.readlink(current)
    parts = PurePosixPath(target).parts
    if len(parts) != 2 or parts[0] != "versions" or not VERSION.fullmatch(parts[1]):
        raise UpdateError("LOCAL_MODIFIED", "当前版本入口已被修改。")
    root = canonical_directory(store / target / name)
    manifest = check(root)
    receipt = json.loads((root.parent / "release.json").read_text(encoding="utf-8"))
    if manifest["version"] != parts[1] or receipt["version"] != parts[1] or receipt["name"] != name:
        raise UpdateError("INVALID_PACKAGE", "当前版本清单不一致。")
    if receipt.get("manifest_sha256") != hashlib.sha256((root / "manifest.json").read_bytes()).hexdigest():
        raise UpdateError("LOCAL_MODIFIED", "当前版本清单已被修改。")
    validate_index(root, require_index)
    return {"path": str(root), "target": target, "manifest": manifest, "receipt": receipt}


def current(store, require_index=False):
    package = current_package(Path(store), require_index=require_index)
    if not package:
        raise UpdateError("SOURCE_UNAVAILABLE", "平台指引暂时不可用。")
    result = {"ok": True, "path": package["path"], "current": str(Path(store) / "current" / "sai-user-guide"),
              **{key: package["receipt"][key] for key in ("name", "version", "release", "sha256")}}
    status = Path(store) / "status.json"
    if status.is_file() and not status.is_symlink():
        try:
            attempt = json.loads(status.read_text(encoding="utf-8"))
            result["update"] = {key: attempt[key] for key in ("state", "checked_at", "code", "error") if key in attempt}
        except (OSError, ValueError, TypeError):
            result["update"] = {"state": "unknown"}
    else:
        result["update"] = {"state": "unknown"}
    return result


@contextmanager
def _locked(store):
    store.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(store / ".update.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o644)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise UpdateError("UPDATE_BUSY", "更新正在进行。") from error
        yield
    finally:
        os.close(descriptor)


def _json_atomic(path, payload):
    if path.is_symlink():
        raise UpdateError("LOCAL_MODIFIED", "更新记录已被改为链接。")
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fchmod(stream.fileno(), 0o644)
            os.fsync(stream.fileno())
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def _extract(content, destination, name):
    archive = destination / "download.zip"
    archive.write_bytes(content)
    with zipfile.ZipFile(archive) as bundle:
        entries = bundle.infolist()
        if len(entries) > 10000 or sum(row.file_size for row in entries) > MAX_UNPACKED:
            raise UpdateError("INVALID_PACKAGE", "解压后的发行包超过大小限制。")
        seen = set()
        for row in entries:
            path = PurePosixPath(row.filename)
            mode = row.external_attr >> 16
            if (not path.parts or path.parts[0] != name or path.is_absolute() or ".." in path.parts
                    or "\\" in row.filename or str(path) != row.filename.rstrip("/")
                    or row.filename in seen or row.flag_bits & 1
                    or (stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR))
                    or row.file_size > 64 * 1024 * 1024):
                raise UpdateError("INVALID_PACKAGE", "发行包包含无效路径或文件。")
            seen.add(row.filename)
            target = destination / path
            if row.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(row) as source, target.open("xb") as output:
                    shutil.copyfileobj(source, output)
                target.chmod(0o644)
    archive.unlink()
    for path in destination.rglob("*"):
        if path.is_dir():
            path.chmod(0o755)


def _switch(store, version, expected):
    current = store / "current"
    actual = os.readlink(current) if current.is_symlink() else None
    if actual != expected or (current.exists() and not current.is_symlink()):
        raise UpdateError("LOCAL_MODIFIED", "更新期间当前版本入口发生变化。")
    with tempfile.TemporaryDirectory(prefix=".activate-", dir=store) as temporary:
        link = Path(temporary) / "current"
        link.symlink_to("versions/" + version)
        os.replace(link, current)


def update(store, *, name="sai-user-guide", repository=REPOSITORY, require_index=False, fetch=None):
    store = canonical_directory(Path(store))
    with _locked(store):
        previous = None
        try:
            previous = current_package(store, name, require_index)
            deadline = time.monotonic() + 180
            release = _release(repository, name, fetch or _fetch, deadline)
            version = release["version"]
            if previous and tuple(map(int, version.split("."))) < tuple(map(int, previous["manifest"]["version"].split("."))):
                raise UpdateError("OLDER_RELEASE", "正式源版本早于已安装版本，未自动降级。")
            versions = canonical_directory(store / "versions")
            versions.mkdir(mode=0o755, exist_ok=True)
            target = canonical_directory(versions / version)
            if target.exists():
                stored = json.loads((target / "release.json").read_text(encoding="utf-8"))
                manifest = check(target / name)
                validate_index(target / name, require_index)
                if (any(stored.get(key) != release[key] for key in ("name", "version", "release", "sha256"))
                        or stored.get("manifest_sha256") != hashlib.sha256((target / name / "manifest.json").read_bytes()).hexdigest()
                        or manifest["version"] != version):
                    raise UpdateError("VERSION_CONFLICT", "相同版本的发行内容发生变化。")
            else:
                with tempfile.TemporaryDirectory(prefix=".download-", dir=store) as temporary:
                    staging = Path(temporary)
                    content = (fetch or _fetch)(release["archive"], MAX_ARCHIVE, deadline)
                    if hashlib.sha256(content).hexdigest() != release["sha256"]:
                        raise UpdateError("CHECKSUM_MISMATCH", "发行包校验失败，已有版本保留。")
                    _extract(content, staging, name)
                    manifest = check(staging / name)
                    if (manifest["name"], manifest["version"]) != (name, version):
                        raise UpdateError("INVALID_PACKAGE", "发行版本与包内清单不一致。")
                    validate_index(staging / name, require_index)
                    _json_atomic(staging / "release.json", {
                        **{k: release[k] for k in ("name", "version", "release", "sha256")},
                        "manifest_sha256": hashlib.sha256((staging / name / "manifest.json").read_bytes()).hexdigest(),
                    })
                    staging.chmod(0o755)
                    staging.rename(target)
            # Detect a writer changing the active package while the download ran.
            if previous and check(Path(previous["path"])) != previous["manifest"]:
                raise UpdateError("LOCAL_MODIFIED", "更新期间当前内容发生变化。")
            changed = not previous or previous["manifest"]["version"] != version
            if changed:
                _switch(store, version, previous["target"] if previous else None)
            try:
                active = current_package(store, name, require_index)
            except BaseException:
                if changed:
                    if previous:
                        _switch(store, previous["manifest"]["version"], "versions/" + version)
                    elif os.readlink(store / "current") == "versions/" + version:
                        (store / "current").unlink()
                raise
            result = {"ok": True, "state": "updated" if changed else "current", "name": name,
                      "version": version, "path": active["path"], "current": str(store / "current" / name),
                      "previous": previous["manifest"]["version"] if previous else None,
                      "updated": changed, "sha256": release["sha256"], "release": release["release"],
                      "checked_at": datetime.now(timezone.utc).isoformat()}
            _json_atomic(store / "status.json", result)
            return result
        except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError, zipfile.BadZipFile, NotImplementedError) as error:
            result = {"ok": False, "state": "failed", "code": getattr(error, "code", "INVALID_PACKAGE"),
                      "error": str(error), "checked_at": datetime.now(timezone.utc).isoformat(),
                      "version": previous["manifest"]["version"] if previous else None}
            _json_atomic(store / "status.json", result)
            if isinstance(error, UpdateError):
                raise
            raise UpdateError("INVALID_PACKAGE", "更新未完成，已有版本保留。") from error


def install_user(store, *, agent, dry_run=False):
    if agent not in {"codex", "opencode", "claude"}:
        raise UpdateError("INSTALL_FAILED", "请选择支持的命令行 Agent。")
    if os.geteuid() == 0 or os.getuid() != os.geteuid():
        raise UpdateError("IDENTITY_UNAVAILABLE", "请使用本人登录账号安装。")
    try:
        home = Path(pwd.getpwuid(os.geteuid()).pw_dir).resolve(strict=True)
        if not home.is_absolute() or home.stat().st_uid != os.geteuid():
            raise OSError("Home owner mismatch")
    except (OSError, KeyError) as error:
        raise UpdateError("IDENTITY_UNAVAILABLE", "无法确认当前登录账号的主目录。") from error
    destination = home / (".claude" if agent == "claude" else ".agents") / "skills"
    try:
        source = current_package(Path(store), require_index=True)
        if not source:
            raise ExportError("No installed release")
    except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        raise UpdateError("SOURCE_UNAVAILABLE", "平台指引暂时不可用，请稍后重试。", destination=str(destination)) from error
    try:
        if dry_run:
            result = install(Path(source["path"]), destination,
                             backup=home / ".local/share/sai-skill-backups", dry_run=True)
        else:
            # Keep independent browser requests from replacing each other's copies.
            # SIGTERM enters the existing installer's inode-preserving rollback.
            lock_root = canonical_directory(home / ".local/state/sai-skills")
            def interrupted(signum, frame):
                raise InterruptedError("Installation interrupted")
            with _locked(lock_root):
                prior_signal = signal.signal(signal.SIGTERM, interrupted)
                try:
                    result = install(Path(source["path"]), destination,
                                     backup=home / ".local/share/sai-skill-backups")
                finally:
                    signal.signal(signal.SIGTERM, prior_signal)
    except UpdateError:
        raise
    except ExportError as error:
        raise UpdateError("LOCAL_MODIFIED", "已有本地修改，请保留后再安装。", destination=str(destination / "sai-user-guide")) from error
    except (OSError, ValueError, KeyError) as error:
        raise UpdateError("INSTALL_FAILED", "安装未完成，请检查目录权限后重试。", destination=str(destination / "sai-user-guide")) from error
    return {"ok": True, "state": "current" if result["already_current"] else "ready" if dry_run else "installed",
            "agent": agent, **result}
