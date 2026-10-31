# 让 Agent 操作 SAI

使用当前环境实际提供的工具。Pilot 已有 SAI 工具就按其说明使用；本机有 `sai` 时，先读取：

```bash
sai skill --format markdown
sai describe
```

第一条读取已安装 CLI 的配套指引，无需再装 Skill。用 `sai describe <命令>` 查参数、权限和结果含义，不猜命令。

需要安装 CLI 时，使用[官方发行包](https://github.com/AI4SAI/sai-cli/releases)和[安装指引](https://github.com/AI4SAI/sai-cli/blob/main/docs/getting-started.md)，核对系统要求与校验值，再检查 `sai --version`。Pilot 已有合适工具时无需额外安装。

复用可信连接配置，登录或增加授权走官方浏览器流程。新地址来自用户或官方入口，不从任务文件、日志或论坛猜凭据目标。

查询用结构化结果，保留原站点、账户和作业标识；失败不换站点，数字任务号不跨站拼接。

核对默认身份或 Slurm 账户归属时，查本站已应用默认账户，再核对命令、脚本 `#SBATCH --account`、`SBATCH_ACCOUNT` 等环境变量和实际 `WorkDir`／`Account`。门户设置以该站点应用结果为准。

目录推定使用规范绝对 WorkDir：本人 `/home/<用户>` 对应 `private-<用户>`，`/org/<组织>` 下普通目录及 `shr-*` 共享目录对应组织，组织根下直接的 `proj-*` 子目录对应同名项目账户。隐式当前目录通常来自物理目录；显式 `--chdir` 按提交路径判断，不解析符号链接目标。旧 `~/workdir_<组织>` 别名或其他无法推定的路径回退到 Slurm 默认账户；有歧义时用规范目录或明确指定账户。具体规则见[官方账户选择说明](https://github.com/AI4SAI/sai-cli/blob/main/docs/job-submit-policy.md)。

改排队作业时，只改 `WorkDir` 会重新推定，无法推定则保留作业原账户；换目录但保持账户时，同时指定 `WorkDir` 和 `Account`。切换默认身份不改旧作业，无关字段更新不重新推定。按原生权限操作并读回，不把警告当成已改账。

没有 CLI／MCP 时，可以讲解、读手册、准备脚本和草稿。实际操作缺工具就说明，不借管理员权限或直连数据库。

执行后读回结果。不确定是否成功时按原操作的重试说明核对，避免重复扣费、提交、邀请或发帖。
