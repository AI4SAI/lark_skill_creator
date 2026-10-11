"""Use the maintained CLI for authentication, pagination and native exports."""

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path


class ExportError(RuntimeError):
    pass


class Lark:
    def __init__(self, cwd: Path, executable: str = "lark-cli"):
        self.cwd, self.executable = cwd.resolve(), executable

    def call(self, *args: str) -> dict:
        try:
            result = subprocess.run(
                [self.executable, *args, "--as", "user", "--format", "json"],
                cwd=self.cwd,
                capture_output=True,
                text=True,
                timeout=180,
                check=False,
                env={
                    **os.environ,
                    "LARKSUITE_CLI_NO_UPDATE_NOTIFIER": "1",
                    "LARKSUITE_CLI_NO_SKILLS_NOTIFIER": "1",
                },
            )
        except subprocess.TimeoutExpired as error:
            raise ExportError("飞书请求超时，本次输出未发布。") from error
        if result.returncode:
            # Provider diagnostics may contain private URLs or credentials.
            raise ExportError(
                f"飞书命令 {args[0]} {args[1]} 未完成，退出码 {result.returncode}。"
            )
        try:
            payload = json.loads(result.stdout)
        except (ValueError, TypeError) as error:
            raise ExportError("飞书 CLI 未返回有效 JSON。") from error
        if payload.get("ok") is not True or not isinstance(payload.get("data"), dict):
            raise ExportError("飞书 CLI 未确认请求成功。")
        return payload["data"]

    def nodes(self, space: str, parent: str = "") -> list[dict]:
        items, seen, cursor = [], set(), ""
        while True:
            args = ["wiki", "+node-list", "--space-id", space, "--page-size", "50"]
            if parent:
                args += ["--parent-node-token", parent]
            if cursor:
                args += ["--page-token", cursor]
            page = self.call(*args)
            if (
                not isinstance(page.get("nodes"), list)
                or type(page.get("has_more")) is not bool
            ):
                raise ExportError("知识库目录响应不完整。")
            items.extend(page["nodes"])
            if not page["has_more"]:
                return items
            cursor = page.get("page_token")
            if not isinstance(cursor, str) or not cursor or cursor in seen:
                raise ExportError("知识库分页没有前进。")
            seen.add(cursor)

    def document(self, token: str) -> dict:
        doc = self.call(
            "docs",
            "+fetch",
            "--doc",
            token,
            "--doc-format",
            "xml",
            "--detail",
            "full",
        ).get("document")
        if not isinstance(doc, dict) or type(doc.get("revision_id")) is not int:
            raise ExportError("文档版本缺失，无法确认导出内容。")
        if not isinstance(doc.get("content"), str):
            raise ExportError("文档内容缺失。")
        return doc

    def export_docx(self, token: str, destination: Path, revision: int) -> int:
        relative = str(destination.parent.relative_to(self.cwd))
        checkpoint_root = self.cwd / ".lark-export-tasks"
        checkpoint_root.mkdir(mode=0o700, exist_ok=True)
        if checkpoint_root.is_symlink():
            raise ExportError("导出任务目录不能是符号链接。")
        checkpoint = checkpoint_root / (
            hashlib.sha256(token.encode()).hexdigest() + ".json"
        )
        if checkpoint.exists():
            if checkpoint.is_symlink():
                raise ExportError("导出任务记录不能是符号链接。")
            result = json.loads(checkpoint.read_text())
            exported_revision = result["revision"]
        else:
            exported_revision = revision
            result = self.call(
                "drive",
                "+export",
                "--token",
                token,
                "--doc-type",
                "docx",
                "--file-extension",
                "docx",
                "--file-name",
                destination.name,
                "--output-dir",
                relative,
            )
        if destination.is_file():
            checkpoint.unlink(missing_ok=True)
            return exported_revision
        ticket = result.get("ticket")
        if not isinstance(ticket, str) or not ticket:
            raise ExportError("飞书没有返回导出文件或可继续查询的任务。")
        checkpoint.write_text(
            json.dumps({"ticket": ticket, "revision": exported_revision})
        )
        checkpoint.chmod(0o600)
        # Continue the same upstream task; never create a replacement on a poll timeout.
        for _ in range(30):
            result = self.call(
                "drive",
                "+task_result",
                "--scenario",
                "export",
                "--ticket",
                ticket,
                "--file-token",
                token,
            )
            exported = result.get("file_token")
            if exported:
                self.call(
                    "drive",
                    "+export-download",
                    "--file-token",
                    exported,
                    "--file-name",
                    destination.name,
                    "--output-dir",
                    relative,
                )
                if destination.is_file():
                    checkpoint.unlink()
                    return exported_revision
                raise ExportError("导出任务完成，但本地文件缺失。")
            if result.get("job_status") not in (0, 1, 2):
                checkpoint.unlink()
                raise ExportError("飞书导出任务失败。")
            time.sleep(2)
        raise ExportError("飞书导出仍未完成；原输出保留，再次执行将继续查询同一任务。")

    def attachment(self, token: str, destination: Path) -> None:
        self.call(
            "docs",
            "+media-download",
            "--token",
            token,
            "--type",
            "media",
            "--output",
            str(destination.relative_to(self.cwd)),
        )
        if not destination.is_file() or destination.is_symlink():
            raise ExportError("附件未正确保存。")
