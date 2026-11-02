"""Release delivery for local Skill consumers; no daemon or model calls."""

import fcntl
import hashlib
import json
import os
import pwd
import re
import shutil
import signal
import select
import stat
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from skill_package import NAME, check, install, snapshot
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


def _current(store, require_index=False):
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
def reading(store):
    """Native shared lock, held only while a consumer reads a fixed version."""
    store = canonical_directory(Path(store))
    try:
        descriptor = os.open(store / ".update.lock", os.O_RDONLY | os.O_NOFOLLOW)
    except OSError as error:
        raise UpdateError("SOURCE_UNAVAILABLE", "平台指引暂时不可用。") from error
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_SH | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise UpdateError("UPDATE_BUSY", "更新正在进行，请稍后重试。") from error
        yield
    finally:
        os.close(descriptor)


def current(store, require_index=False):
    with reading(store):
        return _current(store, require_index)


def current_hold(store, require_index=False):
    """One short native-provider load; EOF/newline releases the shared lock."""
    import sys
    with reading(store):
        print(json.dumps(_current(store, require_index), ensure_ascii=False), flush=True)
        if select.select([sys.stdin], [], [], 60)[0]:
            sys.stdin.readline(1)
        else:
            raise UpdateError("READ_TIMEOUT", "本次读取超时，请重试。")


def prune_versions(store, version, previous):
    """Called under the update lock, after successful activation and readback."""
    try:
        roots = sorted((store / "versions").iterdir(), key=lambda path: path.name)
    except OSError:
        return {"removed_versions": [], "retained_versions": [{"path": str(store / "versions"), "reason": "unavailable"}]}
    keep = {version}
    if previous and previous != version:
        keep.add(previous)
    else:
        older = [path.name for path in roots if VERSION.fullmatch(path.name)
                 and tuple(map(int, path.name.split("."))) < tuple(map(int, version.split(".")))]
        if older:
            keep.add(max(older, key=lambda item: tuple(map(int, item.split(".")))))
    removed, retained = [], []
    for root in roots:
        if root.name in keep:
            continue
        try:
            if not VERSION.fullmatch(root.name) or root.is_symlink() or not root.is_dir():
                raise ValueError("unmanaged")
            if {path.name for path in root.iterdir()} != {"sai-user-guide", "release.json"}:
                raise ValueError("unmanaged")
            manifest = check(root / "sai-user-guide")
            receipt = json.loads((root / "release.json").read_text(encoding="utf-8"))
            if (manifest["version"] != root.name or receipt.get("version") != root.name
                    or receipt.get("name") != "sai-user-guide"
                    or receipt.get("manifest_sha256") != hashlib.sha256((root / "sai-user-guide/manifest.json").read_bytes()).hexdigest()):
                raise ValueError("modified")
            shutil.rmtree(root)
            removed.append(root.name)
        except (OSError, ValueError, ExportError, KeyError, TypeError, AttributeError):
            retained.append({"path": str(root), "reason": "modified_or_unmanaged"})
    return {"removed_versions": removed, "retained_versions": retained}


def _open_backup_files(root):
    """Preserve observed open editor handles on this host, including aliases."""
    files = {(path.stat().st_dev, path.stat().st_ino) for path in root.rglob("*") if path.is_file()}
    try:
        processes = list(Path("/proc").iterdir())
    except OSError:
        return True
    for process in processes:
        if not process.name.isdecimal():
            continue
        try:
            if process.stat().st_uid != os.geteuid():
                continue
            descriptors = list((process / "fd").iterdir())
            for descriptor in descriptors:
                try:
                    info = descriptor.stat()
                    if (info.st_dev, info.st_ino) in files:
                        return True
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            continue
        except PermissionError:
            # Other namespaces/hosts may hide process descriptors. Only
            # observed handles establish a hold; content is checked again after
            # rename below, without widening process or home permissions.
            continue
    return False


def prune_backups(root, keep=None, dry_run=False):
    """Keep one rollback; retain changed, unknown, or observably open originals."""
    retained, removed, candidates = [], [], []
    if not root.exists():
        return {"retained_backups": retained, "removed_backups": removed}
    try:
        for run in root.iterdir():
            if not run.is_dir() or run.is_symlink():
                retained.append({"path": str(run), "reason": "unmanaged"})
                continue
            try:
                receipt = json.loads((run / "backup.json").read_text(encoding="utf-8"))
                if (receipt.get("kind") != "sai-skill-backup/v1" or not isinstance(receipt.get("created_at"), str)
                        or not isinstance(receipt.get("destination"), str) or not Path(receipt["destination"]).is_absolute()
                        or not receipt.get("packages")):
                    raise ValueError("unmanaged")
                expected = {"backup.json"}
                for relative, original in receipt["packages"].items():
                    path = PurePosixPath(relative)
                    provenance = original.get("release")
                    if (path.is_absolute() or ".." in path.parts or not original.get("managed")
                            or not isinstance(provenance, dict)
                            or not re.fullmatch(r"[0-9a-f]{64}", provenance.get("sha256", ""))
                            or provenance.get("manifest_sha256") != original.get("manifest_sha256")
                            or provenance.get("version") != original.get("version")):
                        raise ValueError("personal")
                    package = canonical_directory(run / relative)
                    manifest = check(package)
                    digest = hashlib.sha256((package / "manifest.json").read_bytes()).hexdigest()
                    if digest != original["manifest_sha256"] or manifest["version"] != original["version"]:
                        raise ValueError("modified")
                    expected.update(relative + "/" + filename for filename in (*manifest["files"], "manifest.json"))
                before = snapshot(run)
                if set(before) != expected:
                    raise ValueError("modified")
                candidates.append((receipt["created_at"], run, before, receipt["destination"]))
            except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError):
                retained.append({"path": str(run), "reason": "modified_or_unmanaged"})
        newest = {}
        for created_at, run, _, destination in candidates:
            if destination not in newest or (created_at, str(run)) > newest[destination]:
                newest[destination] = (created_at, str(run))
        keep_paths = {row[1] for row in newest.values()}
        if keep:
            keep_paths.add(keep)
        for _, run, before, _ in candidates:
            if str(run) in keep_paths:
                continue
            if _open_backup_files(run):
                retained.append({"path": str(run), "reason": "open_or_unobservable"})
            elif not dry_run:
                # Retire the old pathname first, then recheck the original
                # inodes. An editor that raced the first scan keeps its files.
                retired = run.with_name(".retiring-" + run.name)
                if retired.exists() or retired.is_symlink():
                    retained.append({"path": str(run), "reason": "unmanaged"})
                    continue
                run.rename(retired)
                if snapshot(retired) != before or _open_backup_files(retired):
                    if not run.exists() and not run.is_symlink():
                        retired.rename(run)
                    retained.append({"path": str(run if run.exists() else retired), "reason": "modified_or_open"})
                else:
                    shutil.rmtree(retired)
                    removed.append(str(run))
    except OSError:
        retained.append({"path": str(root), "reason": "unavailable"})
    return {"retained_backups": retained, "removed_backups": removed}


@contextmanager
def _locked(store, filename=".update.lock"):
    store.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(store / filename, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o644)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise UpdateError("UPDATE_BUSY", "更新正在进行。") from error
        yield
    finally:
        os.close(descriptor)


def _json_atomic(path, payload):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise UpdateError("LOCAL_MODIFIED", "更新记录已被修改，无法写入。")
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
    with _locked(store, ".download.lock"):
        # A slow release host must not stop a cold consumer reading the last
        # installed package. Serialize writers separately from publication.
        descriptor = os.open(store / ".update.lock", os.O_CREAT | os.O_RDONLY | os.O_NOFOLLOW, 0o644)
        os.close(descriptor)
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
            with _locked(store):
                # Detect changes made while the writer downloaded separately.
                if previous and check(Path(previous["path"])) != previous["manifest"]:
                    raise UpdateError("LOCAL_MODIFIED", "更新期间当前内容发生变化。")
                changed = not previous or previous["manifest"]["version"] != version
                if changed:
                    _switch(store, version, previous["target"] if previous else None)
                try:
                    # The unchanged-release path also checks administrator races.
                    if os.readlink(store / "current") != "versions/" + version:
                        raise UpdateError("LOCAL_MODIFIED", "检查期间当前版本入口发生变化。")
                    active = current_package(store, name, require_index)
                    if active["target"] != "versions/" + version:
                        raise UpdateError("LOCAL_MODIFIED", "读回期间当前版本入口发生变化。")
                    result = {"ok": True, "state": "updated" if changed else "current", "name": name,
                              "version": version, "path": active["path"], "current": str(store / "current" / name),
                              "previous": previous["manifest"]["version"] if previous else None,
                              "updated": changed, "sha256": release["sha256"], "release": release["release"],
                              "checked_at": datetime.now(timezone.utc).isoformat()}
                    _json_atomic(store / "status.json", result)
                except BaseException:
                    if changed:
                        if previous:
                            _switch(store, previous["manifest"]["version"], "versions/" + version)
                        elif os.readlink(store / "current") == "versions/" + version:
                            (store / "current").unlink()
                    raise
                result.update(prune_versions(store, version, previous["manifest"]["version"] if previous else None))
                return result
        except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError, zipfile.BadZipFile, NotImplementedError) as error:
            result = {"ok": False, "state": "failed", "code": getattr(error, "code", "INVALID_PACKAGE"),
                      "error": str(error), "checked_at": datetime.now(timezone.utc).isoformat(),
                      "version": previous["manifest"]["version"] if previous else None}
            try:
                _json_atomic(store / "status.json", result)
            except (ExportError, OSError):
                # A replaced or unwritable receipt must not mask the original
                # failure. The CLI and native service journal still report it.
                pass
            if isinstance(error, UpdateError):
                raise
            raise UpdateError("INVALID_PACKAGE", "更新未完成，已有版本保留。") from error


def install_user(store, *, agent, dry_run=False):
    if os.geteuid() == 0 or os.getuid() != os.geteuid():
        raise UpdateError("IDENTITY_UNAVAILABLE", "请使用本人登录账号安装。")
    with reading(store):
        return _install_user(store, agent=agent, dry_run=dry_run)


def _install_user(store, *, agent, dry_run=False):
    if agent not in {"codex", "opencode", "claude"}:
        raise UpdateError("INSTALL_FAILED", "请选择支持的命令行 Agent。")
    try:
        home = Path(pwd.getpwuid(os.geteuid()).pw_dir).resolve(strict=True)
        if not home.is_absolute() or home.stat().st_uid != os.geteuid():
            raise OSError("Home owner mismatch")
    except (OSError, KeyError) as error:
        raise UpdateError("IDENTITY_UNAVAILABLE", "无法确认当前登录账号的主目录。") from error
    destination = home / (".claude" if agent == "claude" else ".agents") / "skills"
    legacy = () if agent == "claude" else (
        home / ".codex/skills/sai-user-guide", home / ".config/opencode/skills/sai-user-guide")
    # Reject personal or symlinked copies before touching any discovery root.
    # Unchanged managed copies use the same installer transaction and backups.
    for path in legacy:
        if path.exists() or path.is_symlink():
            try:
                check(path)
            except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
                raise UpdateError("LOCAL_MODIFIED", "旧目录已有个人指引，请保留后再安装。", destination=str(path)) from error
    try:
        source = current_package(Path(store), require_index=True)
        if not source:
            raise ExportError("No installed release")
    except (ExportError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        raise UpdateError("SOURCE_UNAVAILABLE", "平台指引暂时不可用，请稍后重试。", destination=str(destination)) from error
    try:
        lock_root = canonical_directory(home / ".local/state/sai-skills")
        record_path = lock_root / "installed.json"

        def installed_receipts():
            if not record_path.exists():
                return {}
            if record_path.is_symlink():
                raise ExportError("安装回执不是普通文件。")
            record = json.loads(record_path.read_text(encoding="utf-8"))
            if record.get("kind") != "sai-skill-install/v1" or not isinstance(record.get("destinations"), dict):
                raise ExportError("安装回执已修改。")
            return record["destinations"]

        def protect_personal(receipts):
            for path in (destination / "sai-user-guide", *legacy):
                receipt = receipts.get(str(path))
                if path.exists() and receipt and receipt.get("manifest_sha256") != hashlib.sha256((path / "manifest.json").read_bytes()).hexdigest():
                    raise UpdateError("LOCAL_MODIFIED", "已有个人修改，请保留后再安装。", destination=str(path))

        if dry_run:
            receipts = installed_receipts()
            protect_personal(receipts)
            result = install(Path(source["path"]), destination,
                             backup=home / ".local/share/sai-skill-backups", dry_run=True, retire_managed=legacy,
                             original_receipts=receipts)
            result.update(prune_backups(home / ".local/share/sai-skill-backups", dry_run=True))
        else:
            # Keep independent browser requests from replacing each other's copies.
            # SIGTERM enters the existing installer's inode-preserving rollback.
            def interrupted(signum, frame):
                raise InterruptedError("Installation interrupted")
            with _locked(lock_root):
                prior_signal = signal.signal(signal.SIGTERM, interrupted)
                try:
                    receipts = installed_receipts()
                    protect_personal(receipts)
                    result = install(Path(source["path"]), destination,
                                     backup=home / ".local/share/sai-skill-backups", retire_managed=legacy,
                                     original_receipts=receipts)
                    for old in result["retire_from"]:
                        receipts.pop(old, None)
                    receipts[result["destination"]] = source["receipt"]
                    try:
                        _json_atomic(record_path, {"kind": "sai-skill-install/v1", "destinations": receipts})
                    except (ExportError, OSError) as error:
                        raise UpdateError("INSTALL_OUTCOME_UNKNOWN", "安装回执未完成，请刷新查看。", destination=result["destination"]) from error
                    result.update(prune_backups(home / ".local/share/sai-skill-backups", result.get("backup")))
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
