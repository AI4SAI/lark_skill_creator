#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAI Docs → Skill 生成器
功能：解析飞书导出的Markdown文档，调用AIGC生成元数据和SKILL.md
"""

import os
import sys
import json
import re
import time
import glob
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm


# ======================== 配置 ========================

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
API_KEY = os.getenv("API_KEY", "")
API_MODEL = os.getenv("API_MODEL", "gpt-4o")

if not API_KEY:
    print("❌ 错误：未设置 API_KEY，请检查 .env 文件")
    sys.exit(1)

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY,
)

# 文件长度上限（字符），超过则截断
MAX_FILE_LENGTH = 120000
# LLM输出最大token数
MAX_TOKENS = 4096
# 重试次数
MAX_RETRIES = 3
# 重试间隔（秒）
RETRY_DELAY = 5
# LLM并发数（根据API rate limit调整）
CONCURRENCY = int(os.getenv("CONCURRENCY", "4"))

# ======================== 数据结构 ========================

@dataclass
class SkillMeta:
    """Skill 元数据"""
    name: str = ""
    description: str = ""
    tags: List[str] = field(default_factory=list)
    summary: str = ""

@dataclass
class SkillDoc:
    """单个Skill文档"""
    title: str = ""
    filepath: str = ""
    raw_content: str = ""
    cleaned_content: str = ""
    meta: SkillMeta = field(default_factory=SkillMeta)

@dataclass
class SkillPackage:
    """Skill包（多个文档合并）"""
    name: str = ""
    description: str = ""
    docs: List[SkillDoc] = field(default_factory=list)
    combined_content: str = ""
    final_meta: SkillMeta = field(default_factory=SkillMeta)


# ======================== 飞书Markdown清理 ========================

def clean_feishu_markdown(content: str) -> str:
    """
    清理飞书导出的Markdown中的非标准标签
    """
    if not content:
        return ""
    
    original_len = len(content)
    
    # 1. 去掉 <image token="..." .../> 标签
    content = re.sub(
        r'<image\s+token="[^"]*"(?:\s+width="\d+"|\s+height="\d+"|\s+align="[^"]*")*\s*/?>',
        '',
        content
    )
    
    # 2. 去掉 <iframe url="..." type="..."/> 标签
    content = re.sub(
        r'<iframe\s+url="[^"]*"\s+type="[^"]*"\s*/?>',
        '',
        content
    )
    
    # 3. 去掉 <callout ...>...</callout>
    content = re.sub(
        r'<callout\s+[^>]*>.*?</callout>',
        lambda m: extract_callout_text(m.group(0)),
        content,
        flags=re.DOTALL
    )
    
    # 4. 去掉 <quote-container>...</quote-container>
    content = re.sub(
        r'<quote-container>\s*(.*?)\s*</quote-container>',
        r'\1',
        content,
        flags=re.DOTALL
    )
    
    # 5. 去掉 <mention-doc token="..." type="...">...</mention-doc>
    content = re.sub(
        r'<mention-doc\s+token="[^"]*"\s+type="[^"]*">([^<]*)</mention-doc>',
        r'\1',
        content
    )
    
    # 6. 去掉 <grid>...</grid> 和 <column ...> ... </column>
    content = re.sub(r'<grid\s+[^>]*>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<column\s+[^>]*>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*</column>\s*', '\n', content, flags=re.DOTALL)
    content = re.sub(r'\s*</grid>\s*', '\n', content, flags=re.DOTALL)
    
    # 7. 处理 <text ...> ... </text>
    # 保留文本内容，去掉飞书样式标签（通配所有属性变体）
    content = re.sub(
        r'<text\b[^>]*>([^<]*)</text>',
        r'\1',
        content
    )
    
    # 8. 去掉 <view type="..."> ... </view>
    content = re.sub(
        r'<view\s+type="[^"]*">\s*(.*?)\s*</view>',
        lambda m: f"【媒体文件】{m.group(1).strip()}",
        content,
        flags=re.DOTALL
    )
    
    # 9. 处理 <source-synced ...>...</source-synced>
    content = re.sub(
        r'<source-synced\s+[^>]*>\s*(.*?)\s*</source-synced>',
        r'\1',
        content,
        flags=re.DOTALL
    )
    
    # 10. 处理 <equation>...</equation>
    content = re.sub(
        r'<equation>\s*(.*?)\s*</equation>',
        lambda m: f"`${m.group(1).strip()}$`",
        content,
        flags=re.DOTALL
    )
    
    # 11. 处理 <lark-table>...</lark-table> → 转换为Markdown表格
    content = re.sub(
        r'<lark-table\s+[^>]*>\s*(.*?)\s*</lark-table>',
        lambda m: convert_lark_table(m.group(1)),
        content,
        flags=re.DOTALL
    )
    
    # 12. 去掉 <sub-page-list .../>
    content = re.sub(r'<sub-page-list\s+[^/]*/?>', '', content)
    
    # 13. 清理空白行（多个连续换行合并为2个）
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # 14. 去掉HTML注释
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    cleaned_len = len(content)
    print(f"  📝 清理: {original_len} → {cleaned_len} 字符")
    
    return content.strip()


def extract_callout_text(callout_html: str) -> str:
    """从callout标签中提取文本内容"""
    # 去掉开始标签
    text = re.sub(r'<callout\s+[^>]*>\s*', '', callout_html)
    # 去掉结束标签
    text = re.sub(r'\s*</callout>', '', text)
    return text.strip()


def convert_lark_table(table_html: str) -> str:
    """将飞书表格转换为Markdown表格"""
    # 提取所有行
    rows = re.findall(r'<lark-tr>\s*(.*?)\s*</lark-tr>', table_html, re.DOTALL)
    if not rows:
        return "\n📃 [表格内容]"
    
    md_lines = []
    for i, row in enumerate(rows):
        # 提取单元格
        cells = re.findall(r'<lark-td>(.*?)</lark-td>', row, re.DOTALL)
        # 清理单元格内容
        cleaned_cells = []
        for cell in cells:
            # 去掉飞书样式属性
            cell = re.sub(r'\{[^}]*\}', '', cell)
            # 去掉text标签
            cell = re.sub(r'<text[^>]*>([^<]*)</text>', r'\1', cell)
            # 去掉剩余HTML标签
            cell = re.sub(r'</?[^>]+>', '', cell)
            cleaned_cells.append(cell.strip())
        
        if cleaned_cells:
            md_lines.append("| " + " | ".join(cleaned_cells) + " |")
            # 在第一行后添加分隔线
            if i == 0:
                md_lines.append("| " + " | ".join(["---"] * len(cleaned_cells)) + " |")
    
    return "\n" + "\n".join(md_lines) + "\n"


# ======================== LLM 调用 ========================

def call_llm(prompt: str, system_prompt: str = "", temperature: float = 0.3) -> str:
    """调用LLM，带重试机制"""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    for attempt in range(MAX_RETRIES):
        try:
            print(f"  🤖 调用LLM (attempt {attempt + 1}/{MAX_RETRIES})...")
            response = client.chat.completions.create(
                model=API_MODEL,
                messages=messages,
                max_tokens=MAX_TOKENS,
                temperature=temperature,
            )
            content = response.choices[0].message.content.strip()
            print(f"  ✅ LLM返回 {len(content)} 字符")
            return content
        except Exception as e:
            print(f"  ⚠️ LLM调用失败: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"  ⏳ 等待 {RETRY_DELAY}秒后重试...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"  ❌ 所有重试次数已耗尽，返回空字符串")
                return ""
    return ""


# ======================== 围栏解析 ========================

def parse_meta_json(llm_output: str) -> Tuple[Dict[str, Any], bool]:
    """
    解析LLM返回的JSON，支持围栏格式。
    返回 (解析后的dict, 是否成功)。
    """
    if not llm_output:
        return ({}, False)
    
    # 尝试提取围栏中的JSON
    patterns = [
        r'```json\s*(.*?)\s*```',  # ```json ... ```
        r'```\s*(.*?)\s*```',       # ``` ... ```
    ]
    
    for pattern in patterns:
        match = re.search(pattern, llm_output, re.DOTALL)
        if match:
            json_str = match.group(1).strip()
            try:
                return (json.loads(json_str), True)
            except json.JSONDecodeError:
                continue
    
    # 尝试直接解析整个输出
    try:
        return (json.loads(llm_output), True)
    except json.JSONDecodeError:
        pass
    
    # 尝试寻找从第一个{ 开始的JSON对象
    brace_match = re.search(r'\{.*\}', llm_output, re.DOTALL)
    if brace_match:
        try:
            return (json.loads(brace_match.group(0)), True)
        except json.JSONDecodeError:
            pass
    
    return ({"raw": llm_output}, False)


def generate_single_doc_meta(doc: SkillDoc) -> SkillMeta:
    """为单个文档生成元数据"""
    content_preview = doc.cleaned_content[:8000]
    
    system_prompt = """你是一个专业的技术文档分析助手。你的任务是分析给定的技术文档内容，并以JSON格式返回关键信息。
你必须严格遵循以下格式，不要添加任何解释性文字，只返回JSON。"""

    prompt = f"""请分析以下技术文档，以严格的JSON格式返回以下字段：

### 文档标题: {doc.title}
### 文档路径: {doc.filepath}

### 文档内容（前8000字符）:
```
{content_preview}
```

### 请返回以下JSON格式（严格遵循）：
```json
{{
    "title": "文档标题（如果标题不明确或为空，请根据内容生成一个合适的标题）",
    "summary": "用一段话总结这个文档的核心内容（不超过150字）",
    "key_topics": [从文档中提取的3-7个关键主题/关键词],
    "target_audience": "这个文档适合哪类用户阅读（如新用户/有经验用户/管理员等）",
    "complexity": "难度等级：beginner、intermediate 或 advanced"
}}
```

重要约束：
1. 必须返回JSON，不要有其他任何文字
2. 不要在JSON中使用Markdown格式
3. summary必须是简洁且信息量密集的
"""
    
    # 带JSON解析重试的LLM调用
    for attempt in range(MAX_RETRIES):
        response = call_llm(prompt, system_prompt, temperature=0.3)
        data, success = parse_meta_json(response)
        if success:
            return SkillMeta(
                name=doc.title,
                description=data.get("summary", ""),
                tags=data.get("key_topics", []),
                summary=data.get("summary", "")
            )
        print(f"  ⚠️ JSON解析失败，重试 ({attempt + 1}/{MAX_RETRIES})...")
        # 第二次之后加强提示让LLM修复JSON
        if attempt == 0:
            prompt += "\n\n上次返回的内容不是标准JSON格式，请严格按照上面的要求，仅返回纯小字母组成的标准JSON，不要有Markdown代码块标记。"
    
    print(f"  ❌ 多次解析失败，使用空元数据")
    return SkillMeta(name=doc.title, description="", tags=[], summary="")


def generate_skill_package_meta(skill_pkg: SkillPackage) -> SkillMeta:
    """为Skill包生成统一的元数据"""
    # 合并所有文档的内容摘要
    doc_summaries = []
    all_tags = []
    for doc in skill_pkg.docs:
        doc_summaries.append(f"- 《{doc.title}》: {doc.meta.summary}")
        all_tags.extend(doc.meta.tags)
    
    summaries_text = "\n".join(doc_summaries)
    combined_preview = skill_pkg.combined_content[:6000]
    
    system_prompt = """你是一个专业的技术文档SKILL设计师。你的任务是根据给定的一组技术文档，设计一个完整的Skill元数据。
Skill的description是最重要的部分，它是Claude决定是否调用这个Skill的PRIMARY TRIGGERING MECHANISM。
当前Claude有"undertrigger"倾向——即使Skill有用也可能不调用。为了对抗这一点，description必须写得"pushy"（主动推荐），明确列举各种触发场景，让Claude一看到相关需求就立即调用。
你必须严格遵循以下格式，不要添加任何解释性文字，只返回JSON。"""

    prompt = f"""请根据以下文档组的内容，设计一个完整的Skill元数据，以严格的JSON格式返回。

**Skill已固定的名称为：{skill_pkg.name}**（不要更改）

## 文档列表:
{summaries_text}

## 合并内容摘要（前6000字符）:
```
{combined_preview}
```

## 请返回以下JSON格式（严格遵循）：
```json
{{
    "description": "description是Claude决定是否调用此Skill的核心触发机制，必须写得非常pushy（主动推荐）。要求：1）首先一句话概括Skill的核心功能；2）然后用'Make sure to use this skill whenever...'的句式，列举5-8个具体的触发场景——覆盖用户可能提问的各种方式，包括明确的、模糊的、甚至不直接提及关键词的（比如用户说'我任务跑不了'、'怎么登不进去'、'怎么传文件'等口语化表达）；3）场景要具体到真实用户的语言风格（带具体软件名、命令名、报错信息等），不要写抽象的概括；4）语气要坚定主动，使用'always'、'whenever'、'even if'等词确保Claude不会错过。长度控制在300-500字符之间。",
    "tags": [从所有文档中整合的关键词列表，去重后的5-10个],
    "summary": "用一段简短的话（100字以内）概括这个Skill的核心价值",
    "covered_topics": [这个Skill覆盖的所有核心主题，每个主题一句话],
    "trigger_examples": [列举5-8个真实用户可能说的话作为触发示例，每个示例一句话]
}}
```

重要约束：
1. 必须返回JSON，不要有其他任何文字
2. 不要返回skill_name字段，固定使用: {skill_pkg.name}
3. description 是最重要的触发机制，一定要写得pushy、主动推荐、覆盖尽可能多的触发场景
4. 不要在JSON中使用Markdown格式
5. trigger_examples 字段帮助验证description是否覆盖了足够多样的触发场景
"""
    
    # 带JSON解析重试的LLM调用
    for attempt in range(MAX_RETRIES):
        response = call_llm(prompt, system_prompt, temperature=0.3)
        data, success = parse_meta_json(response)
        if success:
            return SkillMeta(
                name=skill_pkg.name,
                description=data.get("description", ""),
                tags=data.get("tags", []),
                summary=data.get("summary", "")
            )
        print(f"  ⚠️ JSON解析失败，重试 ({attempt + 1}/{MAX_RETRIES})...")
        # 第二次之后加强提示让LLM修复JSON
        if attempt == 0:
            prompt += "\n\n上次返回的内容不是标准JSON格式，请严格按照上面的要求，仅返回纯小字母组成的标准JSON，不要有Markdown代码块标记。"
    
    print(f"  ❌ 多次解析失败，使用空元数据")
    return SkillMeta(name=skill_pkg.name, description=skill_pkg.description, tags=[], summary="")


# ======================== 文件处理 ========================

def read_md_files(directory: str) -> List[SkillDoc]:
    """读取目录下所有md文件（递归）"""
    docs = []
    base_path = Path(directory)
    all_md_files = list(base_path.rglob("*.md"))
    
    for md_file in tqdm(sorted(all_md_files), desc="📚 读取文件", unit="文件"):
        rel_path = md_file.relative_to(base_path)
        # 跳过太短或太简单的文件
        content = md_file.read_text(encoding='utf-8')
        if len(content.strip()) < 50:
            continue
            
        # 获取标题（第一个# 开头的行）
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else rel_path.stem
        
        # 截断过长内容
        if len(content) > MAX_FILE_LENGTH:
            content = content[:MAX_FILE_LENGTH] + "\n\n... (内容已截断)"
        
        doc = SkillDoc(
            title=title,
            filepath=str(rel_path),
            raw_content=content,
            cleaned_content=""
        )
        docs.append(doc)
    
    return docs


def group_docs_into_skills(docs: List[SkillDoc]) -> List[SkillPackage]:
    """将文档按目录结构分组为多个Skill"""
    packages: Dict[str, SkillPackage] = {}
    
    for doc in docs:
        # 根据文件路径确定所属Skill
        path_parts = Path(doc.filepath).parts
        
        if len(path_parts) == 1:
            # 根目录文件 → sai-overview
            skill_name = "sai-overview"
            skill_desc = "SAI超级计算机平台概览信息"
        else:
            # 子目录 → 以目录名称命名
            folder_name = path_parts[0]
            skill_name = f"sai-{folder_name.lower().replace('用户手册', 'user-guide').replace('账号与充值', 'account').replace('用户', 'user')}"
            skill_desc = f"SAI {folder_name} 相关文档"
        
        if skill_name not in packages:
            packages[skill_name] = SkillPackage(
                name=skill_name,
                description=skill_desc,
                docs=[]
            )
        
        packages[skill_name].docs.append(doc)
    
    return list(packages.values())


# ======================== YAML转义 ========================

def yaml_escape(value: str) -> str:
    """
    将字符串安全转义为YAML值。
    如果包含冒号、换行符或其他YAML特殊字符，用双引号包裹并转义内部字符。
    """
    value = value.strip()
    # 检查是否需要引号包裹（冒号、换行、引号等）
    if not value:
        return '""'
    # 替换双引号为转义形式
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    # 如果包含换行符，转换为空格
    escaped = escaped.replace('\n', ' ').replace('\r', ' ')
    # 永远使用双引号包裹以确保安全
    return f'"{escaped}"'


# ======================== SKILL.md 生成 ========================

def generate_skill_md(skill_pkg: SkillPackage) -> str:
    """生成SKILL.md文件内容"""
    meta = skill_pkg.final_meta
    
    # 构建文档内容索引（指向平铺后的 references/ 路径）
    toc_lines = []
    for doc in skill_pkg.docs:
        ref_name = Path(doc.filepath).name
        toc_lines.append(f"- 《{doc.title}》 (参见 `references/{ref_name}`)")
    
    # 合并所有文档内容
    all_content = []
    for doc in skill_pkg.docs:
        all_content.append(f"\n## {doc.title}\n\n{doc.cleaned_content}\n")
    
    combined_docs = "\n---\n".join(all_content)
    
    # 生成SKILL.md
    skill_md = f"""---
name: {yaml_escape(meta.name)}
description: {yaml_escape(meta.description)}
---

# SAI Skill: {meta.name}

## 概述

{meta.summary}

## 包含文档

{chr(10).join(toc_lines)}

## 关键词

{', '.join(meta.tags)}

---

{combined_docs}

---

*Skill 由SAI Docs Skill Generator自动生成*"""
    
    return skill_md


def write_skill_to_disk(skill_pkg: SkillPackage, output_dir: str) -> str:
    """将Skill写入磁盘"""
    skill_dir = Path(output_dir) / skill_pkg.name
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    # 写入SKILL.md
    skill_md = generate_skill_md(skill_pkg)
    skill_md_path = skill_dir / "SKILL.md"
    skill_md_path.write_text(skill_md, encoding='utf-8')
    
    # 写入原始文档（平铺存储，不保留子目录层级）
    ref_dir = skill_dir / "references"
    ref_dir.mkdir(parents=True, exist_ok=True)
    for doc in skill_pkg.docs:
        doc_path = ref_dir / Path(doc.filepath).name
        doc_path.write_text(doc.cleaned_content, encoding='utf-8')
    
    # 写入meta.json
    meta_json = {
        "name": skill_pkg.final_meta.name,
        "description": skill_pkg.final_meta.description,
        "tags": skill_pkg.final_meta.tags,
        "summary": skill_pkg.final_meta.summary,
        "doc_count": len(skill_pkg.docs),
        "docs": [
            {
                "title": d.title,
                "filepath": d.filepath,
                "tags": d.meta.tags
            }
            for d in skill_pkg.docs
        ]
    }
    meta_path = skill_dir / "meta.json"
    meta_path.write_text(json.dumps(meta_json, ensure_ascii=False, indent=2), encoding='utf-8')
    
    return str(skill_dir)


# ======================== 主流程 ========================

def main():
    input_dir = "sai-docs"
    output_dir = "output-skills"
    
    print("🚀 SAI Docs → Skill 生成器")
    print(f"📁 输入目录: {input_dir}")
    print(f"📁 输出目录: {output_dir}")
    print(f"🤖 LLM模型: {API_MODEL}")
    print(f"🌐 API地址: {API_BASE_URL}")
    print("=" * 60)
    
    # 1. 读取所有Markdown文件
    print("\n📚 步骤1: 读取Markdown文件...")
    docs = read_md_files(input_dir)
    print(f"✅ 共读取 {len(docs)} 个文件")
    
    # 2. 清理飞书Markdown
    print("\n🧼 步骤2: 清理飞书Markdown标签...")
    for doc in tqdm(docs, desc="🧼 清理Markdown", unit="文件"):
        doc.cleaned_content = clean_feishu_markdown(doc.raw_content)
    
    # 3. 分组为Skill
    print("\n📦 步骤3: 分组为Skill...")
    skill_packages = group_docs_into_skills(docs)
    print(f"✅ 共 {len(skill_packages)} 个Skill包:")
    for pkg in skill_packages:
        print(f"   - {pkg.name}: {len(pkg.docs)} 个文件")
    
    # 4. 为每个文档生成元数据（并发）
    print(f"\n📋 步骤4: 为单个文档生成元数据 (并发={CONCURRENCY})...")
    all_docs = []
    for pkg in skill_packages:
        all_docs.extend(pkg.docs)
    
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        future_to_doc = {executor.submit(generate_single_doc_meta, doc): doc for doc in all_docs}
        for future in tqdm(as_completed(future_to_doc), total=len(all_docs), desc="📋 文档meta", unit="文档"):
            doc = future_to_doc[future]
            try:
                doc.meta = future.result()
            except Exception as e:
                print(f"\n  ⚠️ 文档meta失败 [{doc.filepath}]: {e}")
                doc.meta = SkillMeta(name=doc.title, description="", tags=[], summary="")
    
    # 5. 为每个Skill生成统一元数据（并发）
    print(f"\n🎨 步骤5: 为Skill生成统一元数据 (并发={CONCURRENCY})...")
    for pkg in skill_packages:
        pkg.combined_content = "\n\n".join([d.cleaned_content for d in pkg.docs])
    
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        future_to_pkg = {executor.submit(generate_skill_package_meta, pkg): pkg for pkg in skill_packages}
        for future in tqdm(as_completed(future_to_pkg), total=len(skill_packages), desc="🎨 Skill meta", unit="skill"):
            pkg = future_to_pkg[future]
            try:
                pkg.final_meta = future.result()
            except Exception as e:
                print(f"\n  ⚠️ Skill meta失败 [{pkg.name}]: {e}")
                pkg.final_meta = SkillMeta(name=pkg.name, description=pkg.description, tags=[], summary="")
    
    # 6. 写入磁盘
    print("\n💾 步骤6: 写入输出目录...")
    for pkg in tqdm(skill_packages, desc="💾 写入磁盘", unit="skill"):
        skill_path = write_skill_to_disk(pkg, output_dir)
        print(f"  ✅ 已生成: {skill_path}")
    
    # 7. 生成总结报告
    print("\n" + "=" * 60)
    print("🎉 全部完成!")
    print(f"\n📁 输出位置: {output_dir}/")
    print(f"\n📝 生成的Skills:")
    for pkg in skill_packages:
        print(f"   • {pkg.name}")
        print(f"     描述: {pkg.final_meta.description[:80]}...")
        print(f"     文件: {len(pkg.docs)} 个")
        print()


if __name__ == "__main__":
    main()
