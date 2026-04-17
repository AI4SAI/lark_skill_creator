# 飞书知识库导出脚本

一键将你（或团队）的飞书 Wiki 知识库递归导出到本地，支持文档、多维表格等常见类型。

---

## 一、前置要求

| 依赖 | 版本 | 说明 |
|------|------|------|
| **Node.js + npm** | >= 18 | 用于安装 `@larksuite/cli` |
| **Python** | >= 3.9 | 用于运行导出脚本 |

检查是否已安装：

```bash
node -v
npm -v
python3 --version
```

---

## 二、安装飞书 CLI（lark-cli）

```bash
npm install -g @larksuite/cli
```

安装完成后，验证命令：

```bash
lark-cli --version
```

---

## 三、初始化应用配置

首次使用需要配置你的飞书应用（个人自用推荐创建**企业自建应用**并开启对应权限）：

```bash
lark-cli config init --new
```

执行后会输出一个授权链接，**在浏览器中打开并完成授权**，CLI 会自动保存配置。

> 💡 如果没有自己的应用，也可以使用飞书开放平台默认的开发者测试应用（按提示操作即可）。

---

## 四、用户身份登录授权

脚本默认以 `--as user` 运行，因此需要先完成用户授权：

```bash
# 推荐按最小权限授权（增量授权，多次登录可叠加）
lark-cli auth login --scope "wiki:space:retrieve"
lark-cli auth login --scope "wiki:node:retrieve"
lark-cli auth login --scope "docx:document:readonly"
lark-cli auth login --scope "bitable:base:app:readonly"
```

或者一次性按业务域授权（更省事）：

```bash
lark-cli auth login --domain wiki
lark-cli auth login --domain docx
lark-cli auth login --domain bitable
```

> ⚠️ 如果后续导出时报 `permission denied`，请根据报错提示的缺失 scope 再次执行 `auth login --scope "xxx"`。

---

## 五、运行导出脚本

### 5.1 直接指定知识空间 ID

```bash
python3 wiki_exporter.py <space_id>
```

示例：

```bash
python3 wiki_exporter.py 7629535255193210075
```

### 5.2 交互式选择（不填参数）

```bash
python3 wiki_exporter.py
```

脚本会自动列出你有权限的 Wiki 空间，输入序号即可开始导出。

---

## 六、导出结果说明

导出完成后，文件会保存在当前目录下的：

```
wiki_export/<space_id>/
```

目录结构与 Wiki 知识库的层级保持一致。例如：

```
wiki_export/7629535255193210075/
├── 部门新人入职/
│   ├── 部门新人入职.md
│   └── 新人任务看板.json
├── 工作规划/
│   ├── 工作规划.md
│   ├── OKR_回顾.md
│   └── OKR_制定.unsupported
├── 团队会议/
│   ├── 团队会议.md
│   ├── 团队周会.md
│   └── 季度会议.md
└── 前端_后端_客户端/
    ├── 前端_后端_客户端.md
    ├── 研发流程.md
    ├── 代码规范.md
    ├── 技术方案.md
    ├── 技术分享.md
    └── 需求池管理.json
```

---

## 七、支持导出的文件类型

| 知识库类型 | 导出格式 | 说明 |
|------------|----------|------|
| **docx / doc** | `.md` | 云文档内容完整导出为 Markdown |
| **bitable** | `.json` | 多维表格，含**表结构** + **全部记录**（单表上限 500 条） |
| **sheet** | 尝试 `.csv` | 电子表格尝试导出 CSV；若 CLI 版本不支持会跳过并报错 |
| **mindnote** | `.unsupported` | 思维笔记暂不支持通过 lark-cli API 导出文本，仅做占位标记 |
| **其他** | 跳过 | slides（幻灯片）、file（普通附件）等暂不处理 |

---

## 八、常见问题

### Q1：导出时报 `permission denied` 怎么办？

根据报错信息里提示的缺失 `scope`，执行对应的授权命令即可：

```bash
lark-cli auth login --scope "缺失的scope名称"
```

### Q2：电子表格（sheet）导不出 CSV？

部分 `lark-cli` 版本未内置 `sheets +export-csv` 命令。若报错可尝试：

1. 更新 CLI 到最新版：`npm update -g @larksuite/cli`
2. 或前往飞书网页版手动下载该表格

### Q3：多维表格记录超过 500 条会截断吗？

会的。当前脚本对每张表固定拉取 `--limit 500`。如果你的表格数据量很大，需要修改 `wiki_exporter.py` 中 `fetch_bitable` 函数，加入分页逻辑（通过 `offset` 多次请求）。

### Q4：可以切换成 `--as bot` 身份运行吗？

当前脚本写死了 `--as user`。如果你确实需要 bot 身份，请修改脚本中 `run_cli` 函数，把 `cmd` 里的 `"--as", "user"` 删掉或改为 `"bot"`。

> ⚠️ 注意：Bot 身份通常**无法访问用户的个人 Wiki 空间**，只能访问应用自己有权限的资源。

---

## 九、脚本位置

```
/home/pan/proj/lark_skill_creator/
├── wiki_exporter.py   # 导出脚本
└── README.md          # 本说明文档
```

祝导出愉快～✨
