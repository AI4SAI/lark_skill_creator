#!/usr/bin/env python3
"""
飞书知识库导出脚本
使用 lark-cli 递归遍历 wiki 空间，将文档、表格等内容拉取到本地。
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote


def run_cli(args: list[str]) -> dict:
    """执行 lark-cli 命令并解析 JSON 输出。"""
    cmd = ["lark-cli"] + args + ["--as", "user"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{stderr}")
    # lark-cli 有时会先输出 warning 到 stderr，stdout 才是 JSON
    stdout = result.stdout.strip()
    if not stdout:
        raise RuntimeError(f"Empty output from: {' '.join(cmd)}")
    try:
        return json.loads(stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON output from {' '.join(cmd)}: {e}\nOutput:\n{stdout[:500]}")


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符。"""
    name = name.strip().replace(" ", "_")
    return re.sub(r'[\\/:*?"<>|]', "_", name)


def list_wiki_nodes(space_id: str, parent_node_token: str = "") -> list[dict]:
    """获取知识空间子节点列表。"""
    params = json.dumps({"space_id": space_id, "page_size": 50, "parent_node_token": parent_node_token})
    resp = run_cli(["wiki", "nodes", "list", "--params", params])
    return resp.get("data", {}).get("items", [])


def fetch_docx(obj_token: str, title: str, save_dir: Path) -> None:
    """拉取 docx 文档内容保存为 markdown。"""
    try:
        resp = run_cli(["docs", "+fetch", "--doc", obj_token])
        # 兼容两种返回结构: 顶层直接有 markdown 或嵌套在 data 里
        markdown = resp.get("markdown", "")
        if not markdown and "data" in resp:
            markdown = resp["data"].get("markdown", "")
        save_path = save_dir / f"{sanitize_filename(title)}.md"
        save_path.write_text(markdown, encoding="utf-8")
        print(f"  [docx] {title} -> {save_path.name} ({len(markdown)} chars)")
    except Exception as e:
        print(f"  [docx] {title} 下载失败: {e}")


def fetch_bitable(obj_token: str, title: str, save_dir: Path) -> None:
    """拉取多维表格的表结构和全部记录保存为 JSON。"""
    try:
        tables_resp = run_cli(["base", "+table-list", "--base-token", obj_token])
        tables = tables_resp.get("data", {}).get("tables", [])

        export_data = {"base_token": obj_token, "title": title, "tables": []}

        for table in tables:
            table_id = table["id"]
            table_name = table["name"]
            print(f"  [bitable] 读取表: {table_name}")

            # 获取字段列表
            try:
                fields_resp = run_cli(["base", "+field-list", "--base-token", obj_token, "--table-id", table_id])
                fields = fields_resp.get("data", {}).get("items", [])
            except Exception as e:
                print(f"    字段获取失败: {e}")
                fields = []

            # 获取记录列表
            try:
                records_resp = run_cli(["base", "+record-list", "--base-token", obj_token, "--table-id", table_id, "--limit", "500"])
                records = records_resp.get("data", {})
            except Exception as e:
                print(f"    记录获取失败: {e}")
                records = {}

            export_data["tables"].append({
                "table_id": table_id,
                "table_name": table_name,
                "fields": fields,
                "records": records,
            })

        save_path = save_dir / f"{sanitize_filename(title)}.json"
        save_path.write_text(json.dumps(export_data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  [bitable] {title} -> {save_path.name}")
    except Exception as e:
        print(f"  [bitable] {title} 下载失败: {e}")


def fetch_sheet(obj_token: str, title: str, save_dir: Path) -> None:
    """尝试拉取电子表格为 CSV（使用 sheets shortcut）。"""
    try:
        # lark-cli sheets 导出需要先读 workbook 和 sheet 信息，这里简化直接导出 csv
        # 部分 lark-cli 版本支持 sheets +export-csv，如果不支持则标记
        resp = run_cli(["sheets", "+export-csv", "--sheet", obj_token])
        content = resp.get("data", "")
        save_path = save_dir / f"{sanitize_filename(title)}.csv"
        save_path.write_text(content, encoding="utf-8")
        print(f"  [sheet] {title} -> {save_path.name}")
    except Exception as e:
        print(f"  [sheet] {title} 下载失败(可能不支持导出): {e}")


def fetch_mindnote(obj_token: str, title: str, save_dir: Path) -> None:
    """思维笔记暂不支持文本导出，仅做标记。"""
    print(f"  [mindnote] {title} -> 暂不支持 API 文本导出，跳过")
    save_path = save_dir / f"{sanitize_filename(title)}.unsupported"
    save_path.write_text("mindnote 暂不支持通过 lark-cli 导出文本内容\n", encoding="utf-8")


def fetch_node(node: dict, save_dir: Path) -> None:
    """根据节点类型分发下载逻辑。"""
    obj_type = node.get("obj_type", "unknown")
    obj_token = node.get("obj_token", "")
    title = node.get("title", "untitled")

    if not obj_token:
        print(f"  [skip] {title} 无 obj_token")
        return

    handlers = {
        "docx": fetch_docx,
        "doc": fetch_docx,
        "bitable": fetch_bitable,
        "sheet": fetch_sheet,
        "mindnote": fetch_mindnote,
    }

    handler = handlers.get(obj_type)
    if handler:
        handler(obj_token, title, save_dir)
    else:
        print(f"  [skip] {title} (类型: {obj_type}, 暂不处理)")


def traverse_and_download(space_id: str, parent_node_token: str, parent_dir: Path) -> None:
    """递归遍历 wiki 节点并下载。"""
    nodes = list_wiki_nodes(space_id, parent_node_token)
    for node in nodes:
        title = node.get("title", "untitled")
        has_child = node.get("has_child", False)
        node_type = node.get("obj_type", "folder")

        if has_child:
            # 有子节点的可能是文件夹也可能是文档（docx 也可以 has_child=false 或不）
            # 这里策略：如果是 origin/shortcut 且 obj_type 不是 docx 等常见类型，视为文件夹
            # 但通常 has_child=true 的是目录页，我们既下载它本身，也递归子目录
            child_dir = parent_dir / sanitize_filename(title)
            child_dir.mkdir(parents=True, exist_ok=True)
            # 下载当前节点本身
            fetch_node(node, child_dir)
            # 递归下载子节点
            traverse_and_download(space_id, node["node_token"], child_dir)
        else:
            # 叶子节点，直接在当前目录下载
            fetch_node(node, parent_dir)


def list_spaces() -> list[dict]:
    """列出用户有权限的知识空间。"""
    resp = run_cli(["wiki", "spaces", "list"])
    return resp.get("data", {}).get("items", [])


def main():
    if len(sys.argv) > 1:
        space_id = sys.argv[1]
    else:
        spaces = list_spaces()
        if not spaces:
            print("未找到任何知识空间，请检查授权权限。")
            sys.exit(1)
        print("发现以下知识空间：")
        for idx, sp in enumerate(spaces, 1):
            print(f"  {idx}. {sp['name']} (space_id: {sp['space_id']})")
        choice = input("请输入要导出的空间序号（或直接输入 space_id）: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if idx < 0 or idx >= len(spaces):
                print("无效序号")
                sys.exit(1)
            space_id = spaces[idx]["space_id"]
        else:
            space_id = choice

    output_dir = Path("wiki_export") / sanitize_filename(space_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n开始导出知识空间 {space_id} 到目录: {output_dir}\n")

    traverse_and_download(space_id, "", output_dir)
    print(f"\n导出完成！文件保存在: {output_dir.absolute()}")


if __name__ == "__main__":
    main()
