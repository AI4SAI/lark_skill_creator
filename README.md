# SAI Skill Creator

SAI 飞书知识库 → Claude Skill 自动生成器

## 功能

解析飞书导出的 Markdown 文档，调用 AIGC 自动：
1. 清理飞书特有标签（`<lark-table>`、`<callout>`、`<image>` 等）
2. 生成 Skill 元数据（name、description、tags、summary）
3. 组织成标准的 `SKILL.md` 格式

## 快速开始

```bash
# 1. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API_KEY 等信息

# 2. 安装依赖
uv sync

# 3. 运行
uv run python generate_skills.py
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `API_BASE_URL` | OpenAI 兼容 API 地址 | `https://api.openai.com/v1` |
| `API_KEY` | API 密钥 | 必填 |
| `API_MODEL` | 模型名称 | `gpt-4o` |

## 输出结构

```
output-skills/
├── sai-overview/
│   ├── SKILL.md          # 生成的 Skill 主文件
│   ├── meta.json         # 元数据备份
│   └── references/       # 清理后的原始文档
├── sai-user-guide/
│   ├── SKILL.md
│   ├── meta.json
│   └── references/
├── sai-account/
│   ├── SKILL.md
│   ├── meta.json
│   └── references/
└── ...
```

## Skill 分组逻辑

按文件夹自动分组：
- `根目录文件` → `sai-overview`
- `用户手册/*` → `sai-user-guide`
- `账号与充值/*` → `sai-account`
