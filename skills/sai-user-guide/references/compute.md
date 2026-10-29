# 计算任务

已有脚本就沿原生 Slurm 工作；希望 Agent 帮忙准备和跟进任务，可以用[Pilot](pilot.md)。两种方式都要认准实际运行站点和计算账户。

1. 先看输入、软件版本、模板和任务规模。SAI 的常用模板见站点提供的 `/opt/sbatch_examples`；以目标站点实际文件为准，保留模板中的映射和环境设置。
2. 查询可用分区、QOS、当前账户的资源上限及价格。GPU 显存、节点内连接、跨节点通信和 CPU／内存配置影响选择，不能只按卡数比较；NVLink 不等于应用自动获得一块合并显存。
3. 按当前站点规则准备脚本，用 `sbatch` 批处理或 `srun` 交互计算。只准备方案时不提交；用户已授权运行时，核对账户、规模、时长和费用条件后执行。登录节点用于准备工作，计算交给调度系统。
4. 根据真实任务回执查看排队、运行、日志、退出状态和结果。排队原因可能是资源不足，也可能是配额、QOS 或账户条件；先读原因，再决定是否调整。

可以按[任务手册](https://vcnn7siwx4yx.feishu.cn/wiki/ZmkawnhNZicpxAkuwh4cNSWGnpc)修改仍在排队的任务、使用 Job Array、取消任务或进入已分配的计算节点。`squeue` 看当前任务，`sacct` 看历史记录；有 SAI CLI 时优先读取它的结构化结果，见[工具使用](tools.md)。

结束与费用以任务和账单为准。关闭浏览器或 SSH 窗口不会自动取消后台批任务；需要停止计算时，明确取消相应任务并读回状态。

原文：[5 分钟上手](https://vcnn7siwx4yx.feishu.cn/wiki/HrR6wu98kiiAvpk6LW6cIXnanRg)、[资源规则](https://vcnn7siwx4yx.feishu.cn/wiki/JEdOwsjbdirwA3kTDW0cBwQWnVe)。
