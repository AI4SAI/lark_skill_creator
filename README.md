# SAI 用户 Skill 与文档工具

普通用户安装一个 [sai-user-guide](skills/sai-user-guide/SKILL.md) 即可。它按任务连接控制台、团队协作、存储、计算、费用、Pilot 和 BBS，详细资料按需读取。完整教程仍由作者在飞书维护。

**[下载安装包](https://github.com/AI4SAI/lark_skill_creator/releases/latest/download/sai-user-guide.zip)** · [版本说明与校验值](https://github.com/AI4SAI/lark_skill_creator/releases/latest) · [官网安装指引](https://www.open-sai.com/docs/agents/)

## 同一份资料，三个入口

本仓库统一管理内容和版本。飞书是人工手册的编辑入口，内容单向导入 Git；差异审阅、版本和回退沿用 PR、tag 和 Git。Skill 的简短指引维护在这里，手册正文由导出器原样转换，构建不调用模型。

审核后的原文放在 `skills/sai-user-guide/references/handbook/`。bot 现有检索器读取 `references/`，包括原文和 Pilot、BBS 等场景参考；Pilot 和自行安装的客户端加载整个 Skill。三端使用同一个 tag／提交号；各端的索引和安装目录只是可重建副本。接入方式见[维护说明](docs/user-skill-maintenance.md)。

当前提供构建能力；生成候选、合入仓库、发布和各端实际加载分别核验。仓库里的简短 Skill 可独立使用，尚未导入的原文继续通过飞书链接阅读。

正式安装包放在 GitHub Releases，官网文档提供固定安装入口，下载带宽由 GitHub 承担。bot、Pilot 和客户端使用本地安装的版本；网络只用于安装／更新，断网时继续读取已有资料。具体发布要求见[维护说明](docs/user-skill-maintenance.md#安装包与可用性)。CI 附件只用于验证，不作为正式下载地址。

## 安装与更新

- **Codex**：让自带的 `skill-installer` 安装本仓库的 `skills/sai-user-guide`，指定你选择的 tag 或完整提交号。保留整个目录，不只复制 `SKILL.md`。
- **其他客户端**：把该目录放入客户端支持的 Skill 位置。发行 ZIP 解压后的目录结构相同，无需飞书账号、Pandoc 或本仓库的 Python 环境。
- **Pilot／DSH**：复用同一包，放入已有 Skill 目录或通过原生 `customSkillDirs`／`bundledSkillDir` 配置加载。平台托管包固定经过验证的版本，不改变用户私有 Skill 或工作台权限。

首次安装可以使用客户端原生安装器。更新前先比较版本和改动；版本及文件校验值在每包的 `manifest.json` 中。已有旧版或个人修改时，下面的可选迁移工具会保留完整备份，需要 Python 3.10+，不需要其他依赖：

```bash
python skill_package.py diff ~/.codex/skills/sai-user-guide skills/sai-user-guide
python skill_package.py install skills/sai-user-guide \
  --dest ~/.codex/skills --backup-dir ~/.local/share/sai-skill-backups --dry-run
```

核对后去掉 `--dry-run` 执行。上例是 Codex 安装目录，请按客户端实际位置调整。未改动的有版本安装可以正常升级；无清单的旧包或已修改的文件会停止更新。明确要归档这些旧内容后替换时，加 `--archive-existing`。

旧 `sai-overview` 的平台介绍已并入统一入口；迁移时可显式加 `--retire sai-overview --archive-existing`，将它完整移出发现目录并保存在同一备份中。其他 Skill 不受影响。备份须在同一文件系统、Skill 发现目录之外：直接保留旧目录，也保住编辑器仍在向原文件写入的内容。恢复时先移出新目录，再将备份中的原目录放回；不要直接覆盖新增的个人修改。

SAI CLI 已自带匹配其版本的操作指引，主 Skill 按需运行 `sai skill --format markdown` 读取。无需再默认安装 `sai-cli`；已由其他途径安装的独立 CLI Skill 不由本工具擅自删除。

## 维护与发行

普通用户入口及场景参考维护在 `skills/sai-user-guide/`，不让导出器覆盖这个入口。人工手册继续保留原文和教学材料；有明确授权的内容修订另做差异审查。来源与更新范围见 [维护说明](docs/user-skill-maintenance.md)。

```bash
python skill_package.py seal skills/sai-user-guide
python skill_package.py check skills/sai-user-guide
python skill_package.py pack skills/sai-user-guide --output dist
```

修改内容时同步更新 `SKILL.md` 的版本号，`seal` 只生成文件清单，不代表人工批准。`check` 检查内容一致性和本地引用，`pack` 生成确定性的 ZIP 与 SHA-256；同版本已有不同内容时拒绝覆盖。CI 执行真实 Pandoc 转换测试、打包及安装迁移测试，并保留待发布包；发布 tag 或 Release 是另外的明确操作。

以下是维护者使用的飞书导出流程，安装用户 Skill 不需要执行。

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
  --public-only \
  --output wiki_export/current
```

建议使用知识库完整网址，以保留引用文档的正确地址。仅传空间 ID 时，缺少完整网址的文档引用会停止导出，不猜测域名。

省略 `--page-id` 会尝试导出整个空间。当前只接受 Docx 文档；其他节点类型会报错，不会悄悄跳过。嵌入的电子表格、多维表格和思维笔记应先在飞书中整理为独立可发布的内容。

`--public-only` 核对正文及同步块源文档的公开权限，导出结束时再核对一次。它用于公共资料包；公开可读仍不等于授权重新发布，内容范围沿用本次人工审核。

分页会取完；同名文档以稳定标识区分。导出前后会核对文档版本和目录，发现编辑中的变化就停止，不替换原输出。同步块会读取其源文档的对应内容并核对版本，不要求取消飞书中的同步关系。正文不截断，短文不丢弃；标题、代码、列表和表格交给 Pandoc 转换。图片按飞书中选定的范围裁剪，由 Pillow 处理，裁剪后的 PNG 不含被隐藏的边缘。动态图的裁剪暂不支持。已导出文档之间的链接改为本地相对路径，带飞书区块锚点的链接保留原地址。

书签与嵌入网页保留为原链接，公式保留为 LaTeX，分栏按原顺序阅读。动态子页面目录链接回该页原文；离线查看全部已收录章节可用包内手册索引。

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

SAI 统一包使用已有的普通用户入口，审核记录中只选择 `sai-user-guide`；另填 `guide_url`，指向该入口在本次 Git 提交中的公开地址，例如 `https://github.com/AI4SAI/lark_skill_creator/blob/COMMIT/skills/sai-user-guide`。为候选指定新版本：

```bash
uv run python generate_skills.py \
  --source wiki_export/current --review review.json \
  --guide skills/sai-user-guide --version 0.3.0 \
  --output build/reviewed
python skill_package.py diff skills/sai-user-guide build/reviewed/skills/sai-user-guide
python skill_package.py pack build/reviewed/skills/sai-user-guide --output dist
```

`--guide` 保留已有入口和场景参考，仅更新版本、加入本地原文索引及 `references/handbook/`。该子目录由飞书导入；再次构建时完整替换候选里的旧子目录，已移除的文档不会继续被检索。构建不改来源目录。审阅后将生成的完整 Skill 纳入同一 PR，再发布同一版本供各端使用。

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
