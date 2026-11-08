# 软件与性能

先从站点已有的软件、Module 和作业模板开始。SAI 的常见科研场景包括 VASP、ABACUS、CP2K、GROMACS、LAMMPS／DeePMD，以及机器学习、材料和生物计算。具体安装版本、许可证和支持的硬件，要查当前站点。

VASP、Gaussian 等受控软件的申请、续期，在控制台“商业软件授权”办理。按页面选择自助声明或材料审核，查看本站开通状态。见[软件环境](handbook/f1d4bd8bb10f1064716136f5/index.md)。

[常见软件用法](https://vcnn7siwx4yx.feishu.cn/wiki/NgQVwbVndictZqkG9UncfoItnxf)提供 ABACUS、MACE、AlphaFold3 等操作示例。其他软件的版本、环境和运行方法，可查[软件环境](https://vcnn7siwx4yx.feishu.cn/wiki/XEHTw8Y9bidBD6klGh5cuZvbnQb)和[手册目录](https://www.open-sai.com/docs/)。

需要独立环境时，按软件和站点条件选 Module、Conda 或 Apptainer。环境写在项目脚本中按需加载，避免把所有软件的初始化塞进 `.bashrc`。已有适合任务的专业 Skill 时，可用于对应科研步骤，并按当前站点的账户和调度要求执行。

性能问题先保留输入规模、软件版本、脚本、资源分配和日志，再判断是 GPU 利用率、MPI 映射、线程、通信还是 I/O。使用站点已有的监控和[性能调优手册](https://vcnn7siwx4yx.feishu.cn/wiki/NVfBwF7d2ijPPykuq6ScDb3RnVi)，先做用户授权范围内的小规模验证，再讨论扩卡。调整后检查运行速度和科学结果。
