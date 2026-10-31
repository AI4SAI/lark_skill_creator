# 软件与性能

先从站点已有的软件、Module 和作业模板开始。SAI 的常见科研场景包括 VASP、ABACUS、CP2K、GROMACS、LAMMPS／DeePMD，以及机器学习、材料和生物计算。具体安装版本、许可证和支持的硬件，要查当前站点。

[常见软件用法](https://vcnn7siwx4yx.feishu.cn/wiki/NgQVwbVndictZqkG9UncfoItnxf)提供 ABACUS、MACE、AlphaFold3 等操作示例。其他软件先查[软件环境](https://vcnn7siwx4yx.feishu.cn/wiki/XEHTw8Y9bidBD6klGh5cuZvbnQb)和[手册目录](https://www.open-sai.com/docs/)，不要把缺少某篇教程理解成平台不支持。

需要独立环境时，按软件和站点条件选 Module、Conda 或 Apptainer。环境写在项目脚本中按需加载，避免把所有软件的初始化塞进 `.bashrc`。已有可用的专业 Skill 时，可以用于对应科研步骤，SAI 的站点、账户和调度条件仍以当前环境为准。

性能问题先保留输入规模、软件版本、脚本、资源分配和日志，再判断是 GPU 利用率、MPI 映射、线程、通信还是 I/O。使用站点已有的监控和[性能调优手册](https://vcnn7siwx4yx.feishu.cn/wiki/NVfBwF7d2ijPPykuq6ScDb3RnVi)，先做用户授权范围内的小规模验证，再讨论扩卡。调整后的速度和科学结果都要验证，不能用显卡型号代替实测。
