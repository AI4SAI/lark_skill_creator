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

## 常见误解

**Q: 任务 suspend（暂停）后还会计费吗？**

会。suspend 只是暂停程序，内存等资源仍被占用，暂停期间正常计费。要结束这次计算并释放资源，请用 `scancel JOB_ID`，随后确认任务已结束。

**Q: GPU 利用率为 0，还会计费吗？**

会。计算费用按任务占用的资源和时间计算。读文件、等待通信或程序卡住时，资源仍可能被占用；请查日志和监控，及时取消不再需要的任务。

**Q: 排队、hold 和 suspend 的费用一样吗？**

普通按量任务在首次启动前排队，尚未占用计算资源，这段时间不收计算费；hold 是让未启动的任务暂缓调度。suspend 是暂停已运行的任务，仍保留资源，正常计费。预约资源、订阅等另按订单约定。

**Q: 关闭 SSH 或 Pilot 网页，任务就结束了吗？**

已提交的 sbatch 任务会继续，资源占用期间照常计费。交互式 srun 则可能随终端断开而结束，使用 tmux 时还可能继续。以任务状态为准；要结束计算，请取消对应任务。

取消后的清理、失败任务费用、检查点续算和账户更正，见[任务 FAQ](https://vcnn7siwx4yx.feishu.cn/wiki/RsCPw4eUeieHPekYMkCc7A6KnHg#HjIHdJxYuszonUbafg9c6scbn9R)。用户希望暂停来节省费用时，先说明暂停仍计费，再确认是保留任务还是结束并释放资源。
