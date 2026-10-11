# SAI 文档与 Skill 构建工具

飞书保留为手册编辑入口。这个工具读取飞书 CLI 提供的完整文档结构，由 Pandoc 生成 Markdown，图片和附件使用飞书原生接口下载。审核通过的同一份正文用于网站和 Skill，构建时不调用模型，也不改写操作说明。

接口定义由各业务代码仓库维护。手册可以解释接口，但不另存一份接口定义。历史导出内容中的计费、开户和登录说明需要重新审核，不能直接作为现行规则发布。

## 环境

- Python 3.10 或更新版本
- 已配置用户身份的 `lark-cli`，当前验证命令版本为 1.0.62
- Pandoc 3.x；也可用 `--pandoc` 指定程序路径

```bash
uv sync
lark-cli auth status --json --verify
```

文档读取使用 `--as user`，需要知识库目录、文档正文和素材下载的只读权限。缺少权限时，按 CLI 提示恢复授权。这个工具不会编辑或删除飞书文档。

## 导出

先列出知识库目录，选择本次需要审核的文档：

```bash
uv run python -m wiki_exporter https://example.feishu.cn/wiki/space/SPACE_ID --catalog
uv run python -m wiki_exporter https://example.feishu.cn/wiki/space/SPACE_ID \
  --page-id PAGE_ID --page-id ANOTHER_PAGE_ID \
  --output wiki_export/current
```

建议使用知识库完整网址，以保留引用文档的正确地址。仅传空间 ID 时，缺少完整网址的文档引用会停止导出，不猜测域名。

省略 `--page-id` 会尝试导出整个空间。当前只接受 Docx 文档；其他节点类型会报错，不会悄悄跳过。嵌入的电子表格、多维表格和思维笔记应先在飞书中整理为独立可发布的内容。

分页会取完；同名文档以稳定标识区分。导出前后会核对文档版本和目录，发现编辑中的变化就停止，不替换原输出。同步块会读取其源文档的对应内容并核对版本，不要求取消飞书中的同步关系。正文不截断，短文不丢弃；标题、代码、列表和表格交给 Pandoc 转换。图片按飞书中选定的范围裁剪，由 Pillow 处理，裁剪后的 PNG 不含被隐藏的边缘。动态图的裁剪暂不支持。已导出文档之间的链接改为本地相对路径，带飞书区块锚点的链接保留原地址。

```text
wiki_export/current/
├── manifest.json            # 文档版本、目录、转换警告和文件校验值
├── content/<page-id>/
│   ├── index.md
│   ├── assets/              # 图片
│   └── attachments/         # 原附件，以下载方式提供
└── originals/
    ├── <page-id>/source.xml # 飞书原始结构
    └── includes/           # 同步块的源内容
```

`originals/` 供核对导出效果，不属于公开网站输入。导出目录保持仅当前用户可访问。更新生成目录时显式加 `--replace`；已有文件被手工修改时会拒绝覆盖。成功更新会删除已移除页面的旧产物，失败则保留原版本。

## 审核与构建

在飞书中修正文案，再重新导出。审核时检查流程、金额与时效、图片、附件和链接，以及是否包含不应公开的信息。有转换警告的文档不能进入发布包。

工具核对图片和画板数量。任务、OKR 等尚未支持的动态内容会产生警告，不能当作完整正文发布。

在导出目录之外保存审核记录，例如 `review.json`：

```json
{
  "content_sha256": "CONTENT_SHA256_FROM_EXPORTED_MANIFEST",
  "skills": [
    {
      "name": "example-guide",
      "title": "使用指南",
      "description": "查询该产品的登录、文件传输和任务提交说明时使用。",
      "pages": ["PAGE_ID", "ANOTHER_PAGE_ID"]
    }
  ]
}
```

`pages` 使用目录列出的稳定标识。审核后填写 `manifest.json` 中的 `content_sha256`。正文、资源或文档版本变化后需要重新审核；只有导出时间变化时可以复用原审核记录。文档引用的本地页面也必须经过审核。

```bash
uv run python generate_skills.py \
  --source wiki_export/current \
  --review review.json \
  --output build/reviewed
```

输出包含：

- `site/`：供 MkDocs 使用的原文和资源。
- `skills/<name>/SKILL.md`：简短的适用范围和文档索引。
- `skills/<name>/references/`：同一份正文及其引用的已审核页面，保留相对路径。
- `manifest.json`：来源、审核记录、导航和文件校验值。

构建不会自动上传、发布网站或安装 Skill。发布方只接收 `site/` 和清单列出的 Skill，不复制 `originals/`。网站与 Skill 的相应正文、图片和附件按字节保持一致。

## 验证

```bash
python -m unittest discover -s tests -v
```

转换测试需要实际 Pandoc，可通过 `PANDOC` 环境变量指定路径。测试使用原生文档结构，覆盖分页、上游错误、同名文档、长短正文、标题、代码、图片/附件/表格、链接、同步块及版本变化、旧文件清理和手工修改保护。它们不代替飞书真实授权下的导出验收。

## 旧输出

旧的标签清理、长文截断、模型生成正文和重复全文拼接已退役。不要把旧 `output-skills` 当作当前规则。原仓库历史中的导出内容保留用于溯源，新流程只接受带版本清单和本次审核记录的输入。

DOCX 中转已移除：飞书导出的 DOCX 会丢失标题和代码块的结构信息。请用当前版本重新导出、核对和审核；原导出文件不自动升级为新版产物。
