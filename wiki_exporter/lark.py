"""Use the maintained CLI for authentication, pagination and native exports."""

import json
import os
import subprocess
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

    def document(self, token: str, block: str | None = None) -> dict:
        args = [
            "docs",
            "+fetch",
            "--doc",
            token,
            "--doc-format",
            "xml",
            "--detail",
            "full",
        ]
        if block:
            args += [
                "--scope",
                "range",
                "--start-block-id",
                block,
                "--end-block-id",
                block,
            ]
        doc = self.call(*args).get("document")
        if not isinstance(doc, dict) or type(doc.get("revision_id")) is not int:
            raise ExportError("文档版本缺失，无法确认导出内容。")
        if not isinstance(doc.get("content"), str):
            raise ExportError("文档内容缺失。")
        return doc

    def attachment(self, token: str, destination: Path, *, kind: str = "media") -> None:
        self.call(
            "docs",
            "+media-download",
            "--token",
            token,
            "--type",
            kind,
            "--output",
            str(destination.relative_to(self.cwd)),
        )
        if not destination.is_file() or destination.is_symlink():
            raise ExportError("附件未正确保存。")
