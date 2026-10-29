# 计算任务

已有脚本可用原生 Slurm，也可以让[Pilot](pilot.md)协助。先认准站点和计算账户。

## 任务记在哪个账户

简单解释：“默认身份”决定登录后的起始目录和默认账户。任务实际记到哪个账户，Slurm按以下优先级顺序决定：①你手动通过--account指定的账户；②作业工作目录；③门户网站上设置的默认身份。例如个人home目录通常记个人，组织下的个人目录、共享文件夹目录记组织，项目目录则记对应项目。

课题与独立项目的资金、预算见[团队协作](collaboration.md)。需要核对脚本、环境变量、目录或排队任务时，读[工具使用](tools.md)。

## 从准备到结果

1. 查当前站点的模板、软件、分区、QOS、资源上限和价格；按显存、通信与规模选资源，NVLink 不等于自动合并显存。
2. 用 `sbatch` 批处理或 `srun` 交互计算。登录节点做准备；真实计算按用户授权的账户、规模和费用执行。
3. 按回执查排队原因、日志、退出状态和结果。`squeue` 看当前任务，`sacct` 看历史；有 CLI 时用其结构化结果。

Job Array、修改排队任务、取消和节点监控见[任务手册](https://vcnn7siwx4yx.feishu.cn/wiki/ZmkawnhNZicpxAkuwh4cNSWGnpc)。关闭网页或 SSH 不会自动取消后台批任务；需要停止时取消对应任务并读回。

原文：[5 分钟上手](https://vcnn7siwx4yx.feishu.cn/wiki/HrR6wu98kiiAvpk6LW6cIXnanRg)、[资源规则](https://vcnn7siwx4yx.feishu.cn/wiki/JEdOwsjbdirwA3kTDW0cBwQWnVe)。
