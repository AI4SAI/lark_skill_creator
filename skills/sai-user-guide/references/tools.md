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

默认身份或 Slurm 账户归属不符时，查本站已应用默认账户，再核对命令、脚本 `#SBATCH`、账户环境变量和实际 `WorkDir`／`Account`。隐式当前目录通常来自物理目录；显式 `--chdir` 按提交路径判断，不跟随符号链接，不能只看终端目录名。规则见[计算任务](compute.md)。

改排队作业时，只改 `WorkDir` 会重新推定，无法推定则保留作业原账户；换目录但保持账户时，同时指定 `WorkDir` 和 `Account`。切换默认身份不改旧作业，无关字段更新不重新推定。按原生权限操作并读回，不把警告当成已改账。

没有 CLI／MCP 时，可以讲解、读手册、准备脚本和草稿。实际操作缺工具就说明，不借管理员权限或直连数据库。

执行后读回结果。不确定是否成功时按原操作的重试说明核对，避免重复扣费、提交、邀请或发帖。
