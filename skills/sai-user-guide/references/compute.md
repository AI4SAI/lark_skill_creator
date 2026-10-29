# 计算任务

已有脚本可用原生 Slurm，也可以让[Pilot](pilot.md)协助。先认准站点和计算账户。

## 任务记在哪个账户

新提交任务时：**显式账户 → 任务工作目录（WorkDir）推定 → 已生效的 Slurm 默认账户。** `--account`／`-A`、脚本里的 `#SBATCH` 或 `SBATCH_ACCOUNT` 等环境变量都可能提供显式账户。

假设本人叫 `alice`，组织叫 `lab`，未显式指定账户时：

| WorkDir 或其下级目录 | Slurm Account |
| --- | --- |
| `/home/alice` | `private-alice` |
| `/org/lab`、`/org/lab/alice` | `lab` |
| `/org/lab/share`、`/org/lab/shr-data` | `lab` |
| `/org/lab/proj-catalysis` | `proj-catalysis` |

默认身份选了组织，在本人 Home 提交且未指定账户，仍会用个人账户。只有组织根下直接的 `proj-*` 子目录会推定为同名项目账户。这里只决定作业归属；课题与独立项目的资金、预算规则见[团队协作](collaboration.md)。

推定看规范绝对 WorkDir，不解析符号链接；旧 `~/workdir_<组织>` 别名不能据名称推定组织。遇到路径歧义，用规范目录或显式账户；系统仍检查你是否有权使用。排错步骤见[工具使用](tools.md)，完整规则见[账户选择说明](https://github.com/AI4SAI/sai-cli/blob/main/docs/job-submit-policy.md)。

## 从准备到结果

1. 查当前站点的模板、软件、分区、QOS、资源上限和价格；按显存、通信与规模选资源，NVLink 不等于自动合并显存。
2. 用 `sbatch` 批处理或 `srun` 交互计算。登录节点做准备；真实计算按用户授权的账户、规模和费用执行。
3. 按回执查排队原因、日志、退出状态和结果。`squeue` 看当前任务，`sacct` 看历史；有 CLI 时用其结构化结果。

Job Array、修改排队任务、取消和节点监控见[任务手册](https://vcnn7siwx4yx.feishu.cn/wiki/ZmkawnhNZicpxAkuwh4cNSWGnpc)。关闭网页或 SSH 不会自动取消后台批任务；需要停止时取消对应任务并读回。

原文：[5 分钟上手](https://vcnn7siwx4yx.feishu.cn/wiki/HrR6wu98kiiAvpk6LW6cIXnanRg)、[资源规则](https://vcnn7siwx4yx.feishu.cn/wiki/JEdOwsjbdirwA3kTDW0cBwQWnVe)。
