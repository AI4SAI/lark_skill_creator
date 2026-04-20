---
name: "sai-user-guide"
description: "This is the comprehensive user guide for SAI HPC supercomputing platform. Make sure to use this skill whenever: 1) users cannot login (password issues, IP blocked after failed attempts, MobaXterm connection problems); 2) task submission errors (QOSMinGRES, QOSMaxGRESPerUser, tasks killed after starting, GPU count not divisible by 4); 3) GPU partition selection (4V100 vs 4V100PX, which for VASP/ABACUS/CP2K/DeePMD); 4) sbatch script templates or Slurm commands (squeue/sacct/scontrol); 5) environment setup (Conda, Environment Modules, Apptainer, Perl); 6) file transfer (RaiDrive SFTP, MobaXterm, TRZSZ); 7) performance optimization (MPI mapping, CUDA-MPS, VASP tuning); 8) storage quotas (ncdu, transparent compression). Always use when users mention: supercomputer, HPC, Slurm, sbatch, GPU, V100, QOS, partition, login, file transfer, or any SAI platform questions."
---

# SAI Skill: sai-user-guide

## 概述

Complete user guide for SAI supercomputing platform covering login, GPU resource selection, Slurm task scheduling, sbatch scripts, environment management, file transfer, and performance optimization with detailed troubleshooting.

## 包含文档

- 《AI助手》 (参见 `references/FAQ.md`)
- 《登录超算》 (参见 `references/SAI用户特殊注意事项汇总.md`)
- 《GPU计算节点》 (参见 `references/SAI硬件资源.md`)
- 《✨sbatch脚本模板`/opt/sbatch_examples`》 (参见 `references/任务提交和管理.md`)
- 《Home目录配额》 (参见 `references/存储空间.md`)
- 《MACE模型设置》 (参见 `references/常见软件用法.md`)
- 《超算核心概念通用科普》 (参见 `references/快速开始.md`)
- 《通用性能调优》 (参见 `references/性能调优✨✨✨.md`)
- 《🔥 RaiDrive挂载 (强烈推荐)》 (参见 `references/数据传输.md`)
- 《用户手册》 (参见 `references/用户手册.md`)
- 《登录节点》 (参见 `references/登录超算.md`)
- 《环境管理》 (参见 `references/软件环境.md`)

## 关键词

SAI HPC, Slurm job scheduler, sbatch script, GPU computing, V100 partition, QOS resource management, RaiDrive, Environment Modules, Conda environment, Apptainer, file transfer, ncdu storage, MPI optimization

---


## AI助手

# AI助手

待补充

# 常见问题 (持续更新)

## 登录相关

### Q: 首次登录修改密码失败，提示“Old password not accepted”，如图：
  

  **A:**"Current Password"指的是初始密码，也即**初始密码要输入2次**，中间任何一步出错，都需要重新从第1步开始

  ---

  ### Q: 多次登录没有成功，之后就连不上了，这是为何？
  **A:**10分钟内多次登录失败，客户端IP地址将被临时封禁，第1次封禁10分钟，此后再出现10分钟内的多次登录失败，封禁时间为`10*e^[此前被封禁次数]`分钟

---

## 硬件资源相关

### Q: 4V100分区和4V100PX分区有什么区别？
  **A:**如SAI硬件资源所示，4V100分区为“SAI SlimPOD-144”超节点的“完全体”，相较于4V100PX分区，GPU-GPU互联升级为300GB/s NVLink Full-Mesh直连拓扑，GPU VRAM升级为32GB，且支持144卡高效并行计算单个任务。但这种升级并非在任何情况下都有正向增益：NVLink会占用额外的功耗预算，导致GPU在极端满载情况下频率更低；由于HBM堆叠层数翻倍(8-Hi)，导致时序更宽松、访存延迟更高；在占用VRAM较低的单卡任务中，这些硬件差异一般会导致1~5%的实际性能差异。具体到应用场景，4V100分区的普适度和整体性能更好，大部分任务可以“闭着眼睛用”4V100分区，以下几类特殊任务可优先考虑4V100PX分区：

a) 16GB VRAM就够用的单卡任务；

b) 对GPU-GPU通信带宽需求低，或完全无法利用NVLink，且每卡有16GB VRAM就够用的多卡任务（例如中小体系DPMD分子动力学模拟、中小体系VASP NEB计算、CP2K多卡计算、非cusolverMp后端的ABACUS多卡计算等）

---

## 提交任务相关

### Q: “error：QOSMinGRES”是什么报错？
  

  A：slurm脚本中的QOS设置有误。请看手册中[QOS小节](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-JmCPdYcTsoyDaFxuIVHc0hS9nSg)，同时注意以下提示：
  

  如调用卡数为单卡时QOS应选择`improper-gpu`、`rush-1o2gpu`或`flood-1o2gpu`：

  ---

  ### **Q:下面这些任务的排队原因是什么？**
  排队原因1：`AssocGrpGRES`
  

  当前该用户组的全局GPU配额为64，提交该任务将超过这一配额，需要等待其他任务跑完或联系管理员扩大配额。
  排队原因2：`QOSMaxGRESPerUser`
  

  QOS为`rush-4gpu`或`rush-8gpu`时，每用户在同一QOS使用的最大gpu数目前仅为8（实时数值请看：快速开始）。QOS的命名非常直白，“rush”指的是在rush的场景使用，否则不要用。

## 软件环境相关

### Q: 如何在SAI上使用Perl脚本？运行Perl脚本提示有模块未安装
  A: Perl模块可以通过CPAN安装在自己的home目录中，例如`cpan Fortran::Format`。第一次运行`cpan`会执行初始化，一直回复`yes`即可。

  cpan初始化完成后会向`~/.bashrc`写入环境，强烈建议保持`~/.bashrc`干净，将环境配置写入独立的`.env`文件，按需`source`使用，Conda同理

---

## 登录超算

# 登录超算

- 使用预置的**SSH密钥**(`~/.ssh/id_ed25519`)用于免密便捷登录（进阶用户也可以自己写SSH config文件），不推荐日常用密码登录
- Windows系统下推荐使用MobaXterm软件登录超算命令行；使用RaiDrive软件的SFTP挂载，把集群存储挂载到资源管理器，像在本地硬盘上一样操作集群上的文件
- 10分钟内多次登录失败，客户端IP地址将被临时封禁，第1次封禁10分钟，此后再出现10分钟内的多次登录失败，封禁时间为`10*e^[此前被封禁次数]`分钟
- **登录节点**：仅用于上传/下载数据、编辑文件、提交/管理任务、安装软件，禁止在登录节点运行计算任务，每个用户在一台登录节点上最多只能使用4个CPU核心和50GB内存

# 任务提交和管理

- **计算节点**：实际执行任务的“工人”，通过调度系统自动分配，所有计算必须通过调度系统提交，任务提交后可SSH连接到计算节点
- SSH连接到计算节点后可以使用`nvm`、`btop`等命令查看各种硬件的动态监控。同时在屏幕上可以看到集群系统中为用户定制的特殊命令和别名说明（在登录到登录节点时也会显示）
- 为了实现真正的“开箱即用”，SAI预置了大量sbatch脚本模板，路径为`**/opt/sbatch_examples**`，模板列表及其介绍请看手册“软件环境”板块
- 用户应按需修改sbatch脚本模板，灵活性就是脚本和命令行存在的意义
- 务必确保提交、管理任务所在的bash环境完全干净，勿载入任何conda（包括base）、module等环境
- SAI按GPU进行收费，非特殊CPU-only计算任务，必须申请GPU；对于CPU-only任务（如数据处理），可提交至CPU-MISC分区，但此分区暂时只有1个节点，每个任务最大运行时间为48小时
- **不允许**用户在提交任务时指定CPU和内存资源，系统会自动绑定分配最佳的CPU和内存资源
- 用户只需指定`--nodes`、`--ntasks`和`--gpus-per-node`，不允许指定内存相关参数（如`--mem`）和CPU核数相关参数（如`--cpus-per-task`），否则任务会在启动的瞬间被停止
- 用户默认全局GPU配额为128（Slurm账号的`GrpTRES`设置），用户组无GPU配额限制
- 如需提升全局GPU配额，请联系管理员，SAI鼓励用户运行大规模并行任务，积极响应此类需求
- 除`improper-gpu`、`rush-1o2gpu`和`flood-1o2gpu`外，使用其他GPU QOS时每节点的GPU数量必须可被4整除
- 若任务的QOS不是`improper-gpu`、`rush-1o2gpu`或`flood-1o2gpu`，同时其在每节点上调用的GPU数量无法被4整除（例如调用4个节点，每节点2个GPU），则任务会在启动的瞬间被停止
- 下面是GPU QOS表


| **QOS** | **优先级** | **每****用户组****可同时**
      **排队的job数量** | **每****用户组****可同时**
      **调用的GPU数量** | **每job可申请的GPU数量范围** | **每job最大运行时间** | **特殊说明** | **适用场景** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **improper-gpu** | 中 | 500 | **64**
      (随资源上线而增大) | 1 ~ 64 | **30 days** | GPU数量在取值范围内无特殊限制，
      但只有少量分区支持此QOS | 单个job的GPU数量为特殊值 |
| **rush-1o2gpu** | 高 | 10 | **16**
      (随资源上线而增大) | 1 ~ 2 | **24 hrs** | 每job的GPU数量必须为1或2，
      且只有少量分区支持此QOS | 小型测试，每job只需1~2个GPU，需要尽快排上队 |
| **rush-gpu**
      **(默认)** | 高 | 10 | **16**
      (随资源上线而增大) | 4 ~ 16 | **24 hrs** | 每节点的GPU数量必须可被4整除 | 小型测试，每job只需4~16个GPU，
      需要尽快排上队 |
| **huge-gpu** | 中 | 100 | **128**
      (随资源上线而增大) | 4 ~ 128 | **30 days** | 每节点的GPU数量必须可被4整除 | 大规模计算，且每job持续时间长 |
| **ultimate-gpu** | 低 | 1 | 不限 | 4 ~ ∞ | ∞ | 每用户最多同时提交1个job，
      且每节点的GPU数量必须可被4整除 | 超大规模计算，且每job持续时间长
      （例如占满整个集群运行许多天） |
| **flood-gpu** | 低 | 10000 | 不限 | 4 ~ ∞ | **12 hrs** | 每节点的GPU数量必须可被4整除 | 超大规模计算，且每job持续时间短 |
| **flood-1o2gpu** | 低 | 10000 | 不限 | 1 ~ 2 | **12 hrs** | 每job的GPU数量必须为1或2，
      且只有少量分区支持此QOS | 大量小job，每job只需1~2个GPU且持续时间短 |


- 默认消耗用户组共享卡时，在`sbatch`/`srun`等脚本/命令行中指定`--account=`<text bgcolor="light-yellow">`private-<用户名>`</text>参数则消耗用户个人私有卡时（要更改默认消耗的卡时属性，请联系管理员）
- SAI的`squeue`命令与原生Slurm有所不同，大幅优化了信息的可读性，支持指定`-p [partition] -q [qos] -A [accounts] -u [user] -t [status]`5个选项，输出信息的末尾已给出易误解的**关键字段解释**：
  1. `GPU`：每节点的GPU数量，而非GPU总数
  1. `MemPerU`：每个GPU(GPU分区)或每个CPU逻辑核(CPU分区)所分配的CPU内存，而非总内存或显存
  1. 还需注意：Job开始运行前，`Slots`字段显示的值等于用户指定的`--ntasks`参数的值，但系统会根据固定的每个GPU对应的CPU逻辑核数进行资源调度，Job开始运行后，此字段将显示实际占用的CPU逻辑核数
    - 4V100和16V100分区：每个GPU固定对应4核8线程CPU
    - 8V100V0分区：每个GPU固定对应3核6线程CPU
- 下面是`/opt/sbatch_examples`中的一个提交ABACUS作业的示例：
  ```bash
  #!/bin/bash
  #SBATCH --job-name=ABACUS
  #SBATCH --partition=4V100
  #SBATCH --nodes=1
  #SBATCH --ntasks=4          # Nodes * GPUs-per-node * Ranks-per-GPU
  #SBATCH --gpus-per-node=4   # Specify the GPUs-per-node
  #SBATCH --qos=rush-4gpu     # Depending on your needs [Priority: rush-4gpu = rush-8gpu > improper-gpu > huge-gpu]
  
  # ⚠ DO NOT modify [CUDA-MPS] and [Rank-Map] settings unless you know what you are doing.
  source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash
  
  # Below are executing commands
  nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
  module load abacus/LTSv3.10.1-sm70-auto
  mpirun -np $SLURM_NTASKS -map-by $MAP_OPT -mca coll_hcoll_enable 0 abacus
  
  # Must explicitly exit
  exit
  
  ```

# 日常使用

- **不要**将Conda等复杂环境管理工具的初始化或特定环境的加载写入`~/.bashrc`，这将会导致环境混乱，甚至影响计算结果的正确性！！！
- 大量小文件读写或频繁访问全局共享存储（分布式存储）会严重拖慢性能（甚至影响他人）。建议：合并文件、使用计算节点本地固态硬盘（`/tmp`或`$CACHE_LOCAL`）做中间计算，最后再写回全局共享存储
- 用户home目录启用了“透明压缩”功能，总体来说，平均每TB存储空间，实际可以存储超过2TB数据
- 使用`ncdu`命令，只需运行一次统计，用户即可交互式进入各级目录查看存储空间占用、查看文件/文件夹数量、设置排序方式、分别查看实际存储占用与实际文件体积
- 对于不调用MPI的任务（如单卡任务，或程序本身不支持MPI），应将`--ntasks`参数指定为1，并删去`[CUDA-MPS] and [Rank-Map]`设置（参考脚本：`gpu_generic-nompi-mutigpu.sbatch`），否则可能会导致所有线程挤在少量CPU核心上
- SAI统一安装的应用软件位于`/opt/apps`
- SAI统一安装的开发工具位于`/opt/devtools`
- 用户为组内统一安装的软件，以及其他组内共享数据，可放置到`/home/${GROUP_NAME}/share`
- SAI通过 Environment Modules 管理大部分软件，用户自行安装的软件也可通过此方式管理
- 对于不便使用 Environment Modules 管理的软件，可使用Bash语法写成`.env`脚本，通过`source`命令调用，SAI统一安装的此类软件的`.env`脚本位于`/opt/envs`
- SAI提供Apptainer容器方案，以实现高度灵活的软件环境可移植性。SAI的Apptainer可直接通过`module`命令加载，支持[Fakeroot模式2和3](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Ffakeroot.html)，禁用了SUID以确保安全性。关于Apptainer的用法请进一步阅读手册。

# 性能相关

- SAI的所有计算节点均部署了经过性能优化的[Netdata服务](https%3A%2F%2Fwww.netdata.cloud)，可以图形化地全面监控硬件（例如CPU、内存、GPU、IB网络、存储设备等）以辅助进行程序的Profiling或Debug。Netdata会保存近一个多月的历史记录，以便回溯已经跑完的任务。建议使用MobaXterm自带的的MobaSSHTunnel功能实现SSH端口转发，将登录节点作为跳板，连接计算节点的19999端口并查看Netdata服务的网页。
- SAI竭尽一切可能，确保所有预置的应用软件在开箱即用状态下，都有最完美的性能调优
- SAI预置的sbatch脚本模板已经包含了MPI Rank 映射调优，用户不需要额外设置，`/opt/sai_config/mps_mapping.d`目录包含不同分区的自动调优脚本，用户可查看以便深入理解
- **在SAI上使用CUDA-MPS功能非常简单**，用户只需照常在sbatch脚本中设置`--nodes`、`--ntasks`和`--gpus-per-node`，通过三者隐式指定每个GPU的进程数，SAI会自动判断如何启动CUDA-MPS
- `/opt/sai_config/ib_map.d`目录下包含了UCX和NCCL通信设置，对于许多应用软件来说是最优的，但仍有部分应用软件乃至具体计算case需要进一步优化，这一般会在相应应用软件的modulefile或相应计算case的sbatch脚本模板中设置
- 对于GPU加速VASP，只需关注`NSIM`和`KPAR`参数的调优，设置`KPAR`的基本原则是**使每个K点的计算所跨的GPU尽可能少**

# 硬件相关

- SAI的改进型V100-SXM2在许多典型计算用例中性能达到市面主流V100的近2倍，**与市面A100-SXM4持平**
- 所有计算节点均开启了HT/SMT (俗称“超线程”)

# 软件编译

- 自行编译软件，请勿使用NVHPC捆绑的MPI栈（HPCX），因为其和Slurm不兼容，无法正确绑定/映射CPU核心和MPI Rank

# 定制快捷命令合集

## `job`/`jm`/`sqm`/`ja`/`sqa`/`sqaa`

- SAI定制的任务状态查看命令，其中`ja`和`sqa`可查看组内用户的任务状态，`sqaa`可查看所有用户的任务状态

用法：详见任务提交和管理

## `ssj <jobid>`

- 显示特定任务的详细信息，`scontrol show job <jobid>`的简写(alias)

## `gpu`/`cpu`

- SAI定制的计算节点状态查看命令

用法：详见任务提交和管理

## `AC`

- 加载SAI预置的Conda base环境，用户需自行创建自己的环境以进一步使用

用法：详见软件环境

## `grp-access`

- 将文件或文件夹设置为当前用户组可读取，同时确保权限最小化
- 此命令的原理：查询路径中各级目录的权限，确保对各级目录添加了`x`权限，但不修改访问指定目标不涉及的文件夹或文件的权限

用法：

1. 执行`grp-access <dir/file>`，使同用户组的用户可以读取文件夹`dir`下的所有条目（文件夹或文件）
2. 执行`grp-access <dir>/*`，使用户组可以读取文件夹`dir`下的所有条目，但无法读取文件夹`dir`本身
3. 执行`grp-access <dir> -R`，使用户组可以读取文件夹`dir`下的所有子条目（递归）

## `tmp`

- 进入当前计算节点上当前用户专属的本地SSD目录`/cache_local/${GROUP_NAME}/${USER}`或`/cache_local/${HOME#/home/}`

## `gtmp`

- 进入当前用户专属的超算全域一致高速SSD缓存目录`/cache_global/${GROUP_NAME}/${USER}`或`/cache_global/${HOME#/home/}`

📌此目录在所有节点上具有数据一致性，就像Home目录，但可靠性不如Home目录

## `nvm`

- 监控job在当前计算节点所调用的GPU的详细状态，`nvidia-smi dmon -s pucvmte -o T`命令的简写(alias)

用法：详见任务提交和管理

## `nvltm`

- 监控job在当前计算节点所调用的GPU的NVLink数据吞吐情况，以便评估程序是否正在高效利用NVLink，`watch -n 0.1 nvidia-smi nvlink -gt d`命令的简写(alias)

## `gpu_hrs_list`

- 显示卡时消费和余额统计表格

## `fee`

待补充

## `dump_job_history`

- 用户自助导出GPU计算资源使用明细，用于财务核算等

用法：详见账号与充值

---

## GPU计算节点

# GPU计算节点

- 用于超大规模并行计算，支持**千卡高效并行**计算单个任务
- 基于创新的硬件架构优化以及从硬件到软件的协同优化，实现高效的超大规模跨尺度高精度分子模拟和面向AI for Science的大规模训练和推理
- SAI的每卡性能在相同型号GPU中前所未有，SAI的改进型V100-SXM2在许多典型计算用例中性能达到市面主流V100的近2倍，**与市面A100-SXM4持平**

截至2026年1月上旬，SAI已上线300块GPU，其中包含260块改进型V100-SXM2-32GB和40块改进型V100-SXM2-16GB

预计2026年上半年将上线**1600块**改进型V100-SXM2


| **分区** | **GPU数量** | **每节点**
      **GPU配置** | **每节点CPU配置** | **每节点**
      **内存配置** | **节点间**
      **互联配置** | **节点内**
      **互联配置** | **上线状态** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **4V100**
      SlimPOD
      144超节点 | 144 + 4 | 4*改进型V100-SXM2-32GB | AMD Ryzen 9950X3D 16C32T 5.75GHz 260W OC | 96GB DDR5-6400
      时序优化 | 2*100G IB + 25G RoCE | NVLink 300GBps | ✅ 
      全量上线 |
| **4V100PX** | 40 | 4*改进型V100-SXM2-16GB | AMD Ryzen 9950X3D 16C32T 5.75GHz 260W OC | 96GB DDR5-6400
      时序优化 | 2*100G IB + 25G RoCE | PCIe 4.0 x16 | ✅ 
      全量上线 |
| **16V100**
      UltraPOD
      1344超节点 | 1344 | 16*改进型V100-SXM2-16GB | AMD Threadripper Pro 5995WX 64C128T 4.5GHz 280W | 256GB DDR4-3200 | 9*100G IB + 25G RoCE | NVLink 300GBps | 预计2026H1全量上线 |
| **8V100V0** | 112 | 8*改进型V100-SXM2-32GB | 2*Intel Xeon Gold 6146 12C24T 4.2GHz 165W | 384GB DDR4-2666 | 4*100G IB + 25G RoCE | NVLink 300GBps | ✅ 
      全量上线 |
| **4A100PX** | 64 | 4*改进型A100-SXM2-32GB | AMD Ryzen 9950X3D2 16C32T 5.65GHz 260W OC | 96GB DDR5-6400
      时序优化 | 2*100G IB + 25G RoCE | PCIe 4.0 x16 | 预计2026H1上线 |
| **8A100R40** | 8 | 8*改进型A100-SXM4-40GB | 2*AMD Threadripper Pro 5975WX 32C64T 4.5GHz 280W | 512GB DDR4-3200 | 20*100G IB + 25G RoCE | NVLink 600GBps with NVSwitch | 预计2026H1上线 |
| **8A100R80** | 8 | 8*改进型A100-SXM4-80GB | 2*AMD Threadripper Pro 5975WX 32C64T 4.5GHz 280W | 1024GB DDR4-3200 | 20*100G IB + 25G RoCE | NVLink 600GBps with NVSwitch | 预计2026H1上线 |


各个分区最适用的计算任务类型如下：

1️⃣**4V100**和**4V100PX**分区针对中等规模和小规模并行计算的极致低延迟优化，最适合ABACUS任务（大/中/小体系）、VASP和QE任务（中/小体系）、CP2K任务（中/小体系）、DPA系列模型训练/微调任务（单卡或多卡）、DeePMD分子动力学模拟任务（大/中/小体系）、GPUMD-NEP分子动力学模拟任务（单节点千万原子以下）等（两分区的差异请看[FAQ](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FLleawhoLoisgSTkLuejcJ6vFnLb%23share-W0oodpFRhoqODUxJ9vnccaJ1npE)）

2️⃣**16V100**分区针对超大规模并行计算进行低延迟优化，适合4V100和4V100PX分区的任务同样适合此分区。此外，该分区最适合各种超大体系模拟，例如：万原子级VASP AIMD、数万原子级ABACUS AIMD、十万原子以上CP2K AIMD、数亿原子级DeePMD分子动力学模拟、单节点数千万原子级GPUMD-NEP分子动力学模拟任务等

3️⃣**8V100V0**分区硬件架构与NVIDIA DGX相同，针对计算吞吐量优化，最适合VASP和QE任务（大体系）、DeePMD分子动力学模拟任务（大体系）、DPA2和DPA3训练/微调任务（多卡）等

## 不同应用场景在各分区的计算效率


| **应用场景** | **应用类型** | **4V100(PX) 效率** | **16V100 效率** | **8V100V0 效率** |
| --- | --- | --- | --- | --- |
| ABACUS-LCAO | 第一性原理/量子化学 | ⚡⚡⚡⚡⚡
      (最多1万原子) | ⚡⚡⚡
      (支持数万原子) | ⚡
      (最多1万原子) |
| VASP-PBE | 第一性原理/量子化学 | ⚡⚡⚡⚡⚡
      (最多3~5k原子) | ⚡⚡⚡⚡⚡
      (支持1万原子以上) | ⚡⚡⚡⚡
      (最多2~4k原子) |
| VASP-HSE | 第一性原理/量子化学 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ |
| Quantum ESPRESSO | 第一性原理/量子化学 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡ |
| CP2K | 第一性原理/量子化学 | ⚡⚡⚡⚡
      (最多1~2万原子) | ⚡⚡⚡
      (支持10万原子以上) | ⚡
      (最多1~2万原子) |
| Gaussian16 | 第一性原理/量子化学 | ⚡⚡⚡⚡ | ⚡⚡⚡ | ⚡ |
| DeePMD DPA-1 | 多卡训练 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡ |
| DeePMD DPA-2/3 | 多卡训练 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡(易OOM) | ⚡⚡⚡⚡ |
| DeePMD-LMP ＜2000原子/卡
      (追求最长时间尺度) | MD模拟 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡ |
| DeePMD-LMP ＞1亿原子
      (追求最大空间尺度) | MD模拟 | 🚫 | ⚡⚡⚡⚡⚡ | 🚫 |
| GPUMD-NEP | MD模拟 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡ |
| LAMMPS 经典/ReaxFF | MD模拟 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡ |
| GROMACS | MD模拟 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡ |


# CPU数据处理节点 🆓 免费

SAI的CPU数据处理节点**完全免费！**

- GPU集群会产生规模庞大的分子动力学轨迹、波函数文件、DFT数据集等数据，但用于处理这些数据的算法往往只能使用CPU执行，且并行度较差，因此需要极强单线程性能、海量内存的CPU-only节点专门处理这类负载
- 鼓励广大研究人员在条件允许的情况下开发和使用支持**GPU加速的数据处理**方法
- 已有一些前沿实验室在日常科学计算中广泛应用GPU加速数据处理

在千卡GPU超节点上线后，将上线更多CPU数据处理节点，CPU不求多但求精，超高频率大核心搭配海量内存，达到300核平均频率5.5~6.0GHz、平均每核内存16GB以上


| **分区** | **CPU核数** | **CPU配置** | **主板配置** | **内存配置** | **节点间**
      **互联配置** | **上线状态** |
| --- | --- | --- | --- | --- | --- | --- |
| **CPU-MISC** | 32 | Intel Xeon w9-3575X 44C88T 4.8GHz 97.5MB 920W OC | ASUS Pro WS W790E-SAGE SE | 768GB DDR5-5600 | 2*100G RoCE | ✅ 
      全量上线 |


# CPU-only节点


| **分区** | **CPU核数** | **CPU配置** | **内存配置** | **节点本地SSD配置** | **节点间**
      **互联配置** | **上线状态** |
| --- | --- | --- | --- | --- | --- | --- |
| **DSPRHBM** | 1872 (18*104) | 2*Intel Xeon Max 9470C 52C104T 3.5GHz 105MB 350W | 128GB HBM2e 2TB/s | 1.6TB NVMe SSD
      (写满不降速, 3GB/s 220KIOPS) | 2*100G IB + 25G RoCE | 预计2026H1上线 |


# 分布式存储

📌用户home目录采用了BeeGFS分布式并行文件系统，支持严格的全局一致性，超算内文件IO通过RoCE v2实现，后端存储（OST）通过ZFS VDEV实现。当前硬件配置：

- 48x 22 TB SAS HDD，每12块组成一组 RAID Z2 VDEV
- 2x 7.68 TB PCIe Gen4 x8 NVMe SSD 作为 L2ARC（二级缓存）
- 2 TiB RAM（16x 128GB DDR4 3200MT/s RECC）作为 ARC（内存缓存）
- 2x 6.4 TB PCIe Gen4 x4 NVMe SSD 用于元数据存储（BeeGFS MDT）
- 当前硬件配置下，实测可实现8GB/s的并发顺序写入和23GB/s的并发顺序读取

📌用户home目录启用了“透明压缩”功能，存入的数据会在文件系统层面被自动压缩，用户和软件对此无感知

- 文本格式的分子动力学轨迹压缩率为2~2.5x
- 主流DFT软件的波函数文件、电荷密度文件等数据的压缩率为2~5x
- 生物信息学数据压缩率为2.5~3.5x
- 总体来说，平均每1TB存储空间，实际可以存储超过2TB数据（**1TB > 2TB**）

📌推荐使用`ncdu`命令交互式查看文件/目录的体积和存储占用，通过键盘“a”键切换实际存储占用和实际文件体积

# 💡FAQ

<reference-synced source-block-id="LXq3dX9yVsB9xSbvwAccosAlnRe" source-document-id="Y0sddTeCxouM8wxyQTMcM86Jnlh">

  ### Q: 4V100分区和4V100PX分区有什么区别？
  **A:**如SAI硬件资源所示，4V100分区为“SAI SlimPOD-144”超节点的“完全体”，相较于4V100PX分区，GPU-GPU互联升级为300GB/s NVLink Full-Mesh直连拓扑，GPU VRAM升级为32GB，且支持144卡高效并行计算单个任务。但这种升级并非在任何情况下都有正向增益：NVLink会占用额外的功耗预算，导致GPU在极端满载情况下频率更低；由于HBM堆叠层数翻倍(8-Hi)，导致时序更宽松、访存延迟更高；在占用VRAM较低的单卡任务中，这些硬件差异一般会导致1~5%的实际性能差异。具体到应用场景，4V100分区的普适度和整体性能更好，大部分任务可以“闭着眼睛用”4V100分区，以下几类特殊任务可优先考虑4V100PX分区：

a) 16GB VRAM就够用的单卡任务；

b) 对GPU-GPU通信带宽需求低，或完全无法利用NVLink，且每卡有16GB VRAM就够用的多卡任务（例如中小体系DPMD分子动力学模拟、中小体系VASP NEB计算、CP2K多卡计算、非cusolverMp后端的ABACUS多卡计算等）

</reference-synced>

---

## ✨sbatch脚本模板`/opt/sbatch_examples`

SAI的Slurm相关命令支持**TAB键**自动补全(很多主流超算不支持此功能)，这非常有用，**强烈推荐**体验

请务必确保提交、管理任务所在的bash环境完全干净，未载入任何conda环境（包括base环境）、module环境或其他额外的环境，除非你知道自己在做什么

# ✨sbatch脚本模板`/opt/sbatch_examples`

- 为了实现真正的“开箱即用”，SAI预置了大量sbatch脚本模板，路径为`**/opt/sbatch_examples**`
- 模板列表及其介绍请看软件环境
- 请勿把`/opt/sbatch_examples`目录直接复制到自己home中，建议用[软链接](https%3A%2F%2Fwww.runoob.com%2Flinux%2Flinux-comm-ln.html)，因为内容会不定时更新（命令示例：`ln -s /opt/sbatch_examples ~/exp`，这样就可以在复制模板文件时使用短得多的前缀`~/exp`）
- 用户应按需修改sbatch脚本模板，灵活性就是脚本和命令行存在的意义
- 对于不调用MPI的任务（如单卡任务，或程序本身不支持MPI），应将`--ntasks`参数指定为1，并删去`[CUDA-MPS] and [Rank-Map]`设置（参考脚本：`gpu_generic-nompi-mutigpu.sbatch`），否则可能会导致所有线程挤在少量CPU核心上

---

# 批处理提交 `sbatch`

Slurm支持利用`sbatch`命令采用批处理方式运行作业，`sbatch`命令在脚本正确传递给作业调度系统后立即退出，同时获取到一个作业号。作业等到系统中资源满足脚本中的指定后，将被调度到合适的计算节点上运行。可使用`squeue`命令查看作业号与作业状态。

脚本文件基本格式：

- 第1行以`#!/bin/``ba``sh`指定该脚本的解释器，`ba``sh`可以变为`sh`、`csh`等，在SAI中推荐使用`bash`
- 在可执行命令之前的每行`#SBATCH`前缀后跟的参数作为作业调度系统参数。 在任何非注释及空白之后的`#SBATCH`将不再作为Slurm参数处理

下面是`/opt/sbatch_examples`中的一个提交ABACUS作业的示例：
```bash
#!/bin/bash
#SBATCH --job-name=ABACUS
#SBATCH --partition=4V100
#SBATCH --nodes=1
#SBATCH --ntasks=4          # Nodes * GPUs-per-node * Ranks-per-GPU
#SBATCH --gpus-per-node=4   # Specify the GPUs-per-node
#SBATCH --qos=rush-4gpu     # Depending on your needs [Priority: rush-4gpu = rush-8gpu > improper-gpu > huge-gpu]

# ⚠ DO NOT modify [CUDA-MPS] and [Rank-Map] settings unless you know what you are doing.
source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash

# Below are executing commands
nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
module load abacus/LTSv3.10.1-sm70-auto
mpirun -np $SLURM_NTASKS -map-by $MAP_OPT -mca coll_hcoll_enable 0 abacus

# Must explicitly exit
exit

```

- `--job-name=ABACUS`指定了任务名为`ABACUS`
- `--partition=4V100`指定了使用`4V100`分区
- `--nodes=1`表示使用1个节点
- `--ntasks=4`应该设置为`Nodes` 、`GPUs-per-node` 和`Ranks-per-GPU`三者之乘积
  - **⚠**注意：此参数代表“进程数”，不代表“CPU核数”或“GPU卡数”，设置错误可能导致性能雪崩！
- `--gpus-per-node=4`指定了每个节点使用4个GPU
- `--qos=rush-4gpu`指定了[QOS](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-Ac8Ud70Oxoykn1xz86ackT8ynhf)，这将影响任务的排队优先级和可同时调用的资源总量：
  - 📌关于QOS的详细信息，请务必看快速开始
  - 如果**任务紧急**，且每个任务需调用1、2、4或8个GPU，QOS可使用`rush-1o2gpu`、`rush-4gpu`或`rush-8gpu`，这将拥有最高的优先级，但这些QOS最多**只能同时调用8个GPU**

任务提交后，可使用[`squeue`](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FZmkawnhNZicpxAkuwh4cNSWGnpc%23share-JhWNdM37FoLQaixD6YCcxAfQneg)查看任务排队与资源占用情况，可使用[`scancel`](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FZmkawnhNZicpxAkuwh4cNSWGnpc%23share-ZsecdzltforfjvxLlVkcFnBSnXb)取消特定任务，后文将介绍细节

## [Job Array](https%3A%2F%2Fslurm.schedmd.com%2Fjob_array.html)

对于同时提交大量相似任务的情况（例如上百乃至上万个DFT单点计算，每个任务只需几十~几百秒），务必使用Job Array功能，用法请查看[Slurm官方文档](https%3A%2F%2Fslurm.schedmd.com%2Fjob_array.html)

---

# 交互式提交 `srun`

资源分配与任务加载两步均通过`srun` 命令进行：当在登录shell中执行srun命令时，srun首先向系统提交作业请求并等待资源分配，然后在所分配的节点上加载作业任务。 

采用该模式，用户在该终端需等待任务结束才能继续其它操作，在作业结束前，**如果提交时的命令行终端断开****，****则任务终止**。

`srun`一般用于短时间测试性作业任务，若确实需要长时间运行`srun`，则推荐在[Tmux](https%3A%2F%2Fblog.csdn.net%2FCSSDCC%2Farticle%2Fdetails%2F121231906)中运行。

可使用`srun`命令搭配`--pty bash`后缀，进入计算节点进行交互式操作。例如，使用如下命令可以在4V100分区申请单卡，并进行交互式操作：
```bash
srun --qos improper-gpu --nodes=1 --ntasks=1 --gpus-per-node=1 --partition=4V100 --pty bash
```

可使用`srun --help`命令获得帮助信息，了解`srun`的各个参数的用途。

---

# ✨查看任务状态 `squeue`

📌简写：`job`、`jm`、`sqm`、`ja`、`sqa`、`sqaa`

`ja`和`sqa`可查看组内用户的任务状态，`sqaa`可查看所有用户的任务状态

SAI的`squeue`命令与原生Slurm有所不同，大幅优化了信息的可读性，支持指定`-p [partition] -q [qos] -A [accounts] -u [user] -t [status]`5个选项

以下是其典型输出：
```shell
job-ID  Prior  Name          User            Submit/Start at      ST  Run/Wait     Partition  QOS          Nodes  Slots  GPU  MemPerU  array_ID  Reason/Nodelist
----------------------------------------------------------------------------------------------------------------------------------------------------------------
114514  6076   VASP          testuser01      2025-10-24 10:52:25  R   10:53:56     8V100V0    huge-gpu     12     576    8    47000M   -         8v100v0n[02-13]
114515  10176  DP_MD         testuser01      2025-10-24 11:19:13  R   10:27:08     4V100      rush-8gpu    2      48     4    23000M   -         4v100pxn[01-02]
114516  6077   ABACUS        testuser01      2025-10-24 10:44:21  PD  11:02:00     4V100      huge-gpu     2      16     4    23000M   -         (Resources)
114517  6076   DP_MD         testuser01      2025-10-24 10:53:10  PD  10:52:41     8V100V0    huge-gpu     12     192    8    47000M   -         (Resources)
Note: 1. 'GPU' indicates per-Node allocation of GPUs.
      2. 'MemPerU' indicates per-GPU or per-CPU-Core allocation of Host-Memory.
```

如所有人可见，输出信息的末尾已给出易误解的**关键字段解释**：

1. `GPU`：每节点的GPU数量，而非GPU总数
1. `MemPerU`：每个GPU(GPU分区)或每个CPU逻辑核(CPU分区)所分配的CPU内存，而非总内存或显存

此外还需注意：

- Job开始运行前，`Slots`字段显示的值等于用户指定的`--ntasks`参数的值，但系统会根据固定的每个GPU对应的CPU逻辑核数进行资源调度，Job开始运行后，此字段将显示实际占用的CPU逻辑核数
  - 4V100分区：每个GPU固定对应4核8线程CPU
  - 8V100V0分区：每个GPU固定对应3核6线程CPU

其他字段解释（由用户指定的参数，可通过提交命令、Sbatch脚本或`scontrol update`指定）：

- `job-ID`：任务编号，每个任务唯一（不包括Job Array的子任务）
- `Prior`：任务优先级，在排队过程中动态变化，计算方式[在此](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-E1Ucd8FX0oojv7x02I7cPARLn9e)
- `Name`：任务名称，由用户指定
- `User`：任务所属用户名
- `Submit/Start at`：任务的提交时间（PD）或开始时间（R/CG/S）
- `ST`：任务状态（PD：排队中，R：运行中，S：暂停中，CG：即将完成）
- `Run/Wait`：已运行或等待的时间
- `Partition`：任务申请的分区（PD）或分配到的分区（R/CG/S），由用户指定，用户可指定分区列表，但最终只分配1个分区
- `QOS`：任务的QOS，由用户指定
- `Nodes`：节点数量，由用户指定
- `array_ID`：Job Array的子任务编号
- `Reason/Nodelist`：若任务状态为PD，则显示PD的原因；若任务状态为R/CG/S，则显示分配到的节点列表；用户可指定要调用的节点列表或要排除的节点列表，参考提交命令的文档

---

# 查看任务详细信息 `scontrol`/`sacct`

多用**TAB键**！

`scontrol show job`只能显示正在运行或者刚结束不久的任务信息，用法如下：
```bash
scontrol show job <任务ID>  # 或简写为 ssj <任务ID>
```

通过`sacct`查询已经结束任务的相关信息，如下所示：
```bash
# 显示已知JobID的任务的一般信息
sacct -X -j <任务ID>
# 显示开始于某个时间点之后的任务的一般信息,支持通过方向键滚动,按q退出交互界面
sacct -X -S <开始时间(默认今天0点)> | less -SN
# 寻找开始于某个时段内任务的工作目录,"%200"表示此字段最长显示200字符,支持通过方向键滚动,按q退出交互界面
sacct -X -S <开始时间(默认今天0点)> -E <结束时间(默认现在)> --format=jobid,jobname,workdir%200 | less -SN
# 显示开始于某个时段内任务的全部信息,每个字段长度50字符,支持通过方向键滚动,按q退出交互界面
sacct -X -S <开始时间(默认今天0点)> -E <结束时间(默认现在)> --format=all%50 | less -SN
# 例：查询2026-02-20下午14:30:00后所有任务的运行节点、QOS、开始结束时间、工作目录等信息，并滚动查看
sacct -X --format=jobid,jobname%15,NodeList,QOS%15,Start,End,State,AllocTRES%50,workdir%90 -S 2026-02-20T14:30:00 | less -SN
```

💡`sacct`的重点功能非常多，无法逐一列举，建议阅读[Slurm官方文档](https%3A%2F%2Fslurm.schedmd.com%2Fsacct.html)，并多用**TAB键**来补全命令

值得一提的是，[`dump_job_history`](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FLJo9wzMv7ipb5ckeKfEceDEPn4d%23share-JTMhd4g8Vo1OmFxwwIdcAKl1nCc)功能也是基于`sacct`实现的

---

# 🔥 修改job而不重新排队 [`scontrol update`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23SECTION_JOBS---SPECIFICATIONS-FOR-UPDATE-COMMAND)

多用**TAB键**！

## 修改分区
```bash
scontrol update jobid=<任务ID> partition=<新分区>
```

## 修改QOS
```bash
scontrol update jobid=<任务ID> qos=<新QOS>
```

## 修改每节点GPU数量
```bash
scontrol update jobid=<任务ID> gres=gpu:<新的每节点GPU数> numtasks=<新的GPU总数*Ranks-per-GPU> numcpus=<等于numtasks的值>
```

## 修改节点数量
```bash
scontrol update jobid=<任务ID> numnodes=<新的节点数> numtasks=<新的GPU总数*Ranks-per-GPU> numcpus=<等于numtasks的值>
```

## 修改CUDA-MPS的`Ranks-per-GPU`
```bash
scontrol update jobid=<任务ID> numtasks=<GPU总数*新的Ranks-per-GPU> numcpus=<等于numtasks的值>
```

## Tips

- `jobid=<任务ID>`也可用`jobid=[任务ID列表]`（格式如`[114-514,1919,810]`）或`jobname=<任务名称>`代替
- 对于运行中的任务，请权衡已经运行的“沉没成本”和预期修改后的收益；若决定修改，需先使用`scontrol `[`requeuehold`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23OPT_requeuehold)` <任务ID>`命令停止任务、重新排队并防止运行，然后执行`scontrol update ...`命令修改任务，最后执行`scontrol `[`release`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23OPT_release)` <任务ID>`命令允许任务运行

## 💪实战：同时修改以上所有参数

`job-114514`**修改前**：申请`4V100`分区的2个节点，每节点4个GPU（共8个GPU），CUDA-MPS的`Ranks-per-GPU`为4，QOS使用`rush-8gpu`

`job-114514`**修改后**：申请`16V100`分区的4个节点，每节点16个GPU（共64个GPU），CUDA-MPS的`Ranks-per-GPU`为2，QOS使用`huge-gpu`

📌**命令**（按**TAB键**可自动补全参数的名称）：
```bash
scontrol update jobid=114514 partition=16V100 numnodes=4 gres=gpu:16 numtasks=128 numcpus=128 qos=huge-gpu
# 此处虽然设置了numcpus=128,
# 但系统会根据Default-CPUs-per-GPU,
# 调度并分配256个物理核（512个逻辑核）
# 如squeue小节所述
```

## 降低任务优先级

场景：有一批QOS为`improper-gpu`的单卡任务已在队列中，每个任务运行时间很短；此后又提交了若干QOS为`improper-gpu`的单卡任务，每个任务运行时间很长。现希望晚交的长任务插队到先交的短任务之前。

操作：`scontrol update jobid=<先提交的短任务的jobid列表> nice=<降低的优先级指数(正整数)>`

原理：`nice`参数用于手动控制任务优先级，正值会降低任务的优先级，负值会增加任务的优先级（只有管理员可以指定负值），调整范围是+/-2147483645。

## `scontrol`的其他重要功能

- [`scontrol hold`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23OPT_hold)
- [`scontrol requeue`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23OPT_requeue)
- [`scontrol suspend`](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html%23OPT_suspend)
- ……

💡`scontrol`的重要功能非常多，无法逐一列举，建议阅读[Slurm官方文档](https%3A%2F%2Fslurm.schedmd.com%2Fscontrol.html)，并多用**TAB键**来补全命令

`scontrol`对于管理员来说也是非常重要的工具

---

# 取消任务 `scancel`

可使用`scancel <任务ID>`、`scancel --name=<任务名称>`等命令取消符合条件的特定任务

具体用法参见`scancel --help`或[Slurm官方文档](https%3A%2F%2Fslurm.schedmd.com%2Fscancel.html)，这对于批量取消任务很有用

💡对于Job-ID连续的一系列任务，可使用bash的`{a..b}`语法，例如取消Job-ID从114514到114520的7个任务：`scancel {114514..114520}`

---

# ✨查看计算节点空闲状态 `**gpu**`**/**`**cpu**`

🚫不推荐直接使用Slurm自带的`sinfo`命令查看计算节点信息，因为命令参数复杂、可读性较差

SAI定制了`gpu`和`cpu`两条命令，大幅优化了信息的可读性

## `gpu` [系统已升级，手册待更新]

以下是`gpu`命令的典型输出：
```shell
            =====================   ================= ================= ========================  =========================================
               Scheduled Mem(G)       Scheduled CPUs    Scheduled GPUs         Real Status           Cluster Options
            =====================   ================= ================= ========================  =========================================
NodeName    total   alloc   avail   total alloc avail total alloc avail LOAD   Mem_free  Status    Partition QOS
----------  ---------------------   ----------------- ----------------- ------------------------  -----------------------------------------
4v100n01    89.84   22.46   67.38   32    8     24    4     1     3     1.10   86.89     MIXED     4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn01  89.84   0.00    89.84   32    0     32    4     0     4     0.02   82.83     IDLE      4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn02  89.84   0.00    89.84   32    0     32    4     0     4     0.06   87.71     IDLE      4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn03  89.84   0.00    89.84   32    0     32    4     0     4     0.11   88.15     IDLE      4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn04  89.84   0.00    89.84   32    0     32    4     0     4     0.07   85.79     IDLE      4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn05  89.84   89.84   0.00    32    32    0     4     4     0     8.18   62.81     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn06  89.84   89.84   0.00    32    32    0     4     4     0     8.13   61.98     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn07  89.84   89.84   0.00    32    32    0     4     4     0     8.35   62.47     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn08  89.84   89.84   0.00    32    32    0     4     4     0     8.33   62.47     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn09  89.84   89.84   0.00    32    32    0     4     4     0     8.35   62.07     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
4v100pxn10  89.84   89.84   0.00    32    32    0     4     4     0     8.25   53.84     ALLOCATED 4V100     huge-gpu,rush-4gpu,rush-8gpu,improper-gpu
8v100v0n01  367.19  0.00    367.19  48    0     48    8     0     8     0.71   310.26    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n02  367.19  367.19  0.00    48    48    0     8     8     0     16.81  317.28    ALLOCATED 8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n03  367.19  367.19  0.00    48    48    0     8     8     0     19.60  261.42    ALLOCATED 8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n04  367.19  367.19  0.00    48    48    0     8     8     0     16.47  353.38    ALLOCATED 8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n05  367.19  183.59  183.59  48    24    24    8     4     4     10.32  341.98    MIXED     8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n06  367.19  0.00    367.19  48    0     48    8     0     8     0.46   366.86    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n07  367.19  0.00    367.19  48    0     48    8     0     8     0.42   368.00    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n08  367.19  0.00    367.19  48    0     48    8     0     8     0.24   367.20    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n09  367.19  0.00    367.19  48    0     48    8     0     8     0.22   368.66    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n10  367.19  0.00    367.19  48    0     48    8     0     8     0.34   312.64    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n11  367.19  0.00    367.19  48    0     48    8     0     8     0.12   364.48    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n12  367.19  0.00    367.19  48    0     48    8     0     8     0.40   368.15    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n13  367.19  0.00    367.19  48    0     48    8     0     8     0.14   365.85    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
8v100v0n14  367.19  0.00    367.19  48    0     48    8     0     8     0.44   313.88    IDLE      8V100V0   huge-gpu,rush-4gpu,rush-8gpu
```

用户日常使用最需要关注的信息如下：

- `Scheduled GPUs`主字段的`total`子字段：表示相应节点的GPU总数
- `Scheduled GPUs`主字段的`avail`子字段：表示相应节点当前空闲的GPU数量
- `Scheduled CPUs`主字段的`total`子字段：表示相应节点的CPU逻辑核心总数，可推算出每块GPU分配的CPU逻辑核数，以及评估如何设置`Ranks-per-GPU`，需注意所有计算节点均开启了HT/SMT (俗称“超线程”)
- `Status`字段：`IDLE`表示计算节点完全空闲，`MIXED`表示计算节点部分空闲，`ALLOCATED`表示计算节点被全部占用
- `QOS`字段：表示计算节点 (分区) 所支持的QOS，若用户设置了不正确的QOS，系统会拒绝任务的提交，或使任务永远处于排队状态 (后者存在于通过`scontrol update`设置的任务) 。为了防止资源过度碎片化，SAI只在4V100分区启用了支持非4的倍数个GPU的QOS (`improper-gpu`)

## `cpu`

以下是`cpu`命令的典型输出：
```shell
            ======================  ================= ========================  =========================================
               Scheduled Mem(G)       Scheduled CPUs         Real Status           Cluster Options
            ======================  ================= ========================  =========================================
NodeName    total   alloc   avail   total alloc avail LOAD   Mem_free  Status    Partition        QOS
----------- ----------------------  ----------------- ------------------------  -----------------------------------------
dpn01       750.00  0.00    750.00  64    0     64    0.13   748.63    IDLE      CPU-MISC         huge-cpu,rush-cpu
```

用户可根据上述`gpu`命令的解释举一反三进行理解

需注意所有CPU计算节点均开启了HT/SMT (俗称“超线程”)，而调度时以每个物理核心的2个逻辑核心作为基本单元

# 进入计算节点查看任务和硬件状态

## SSH连接

任务提交后，可通过SSH进入任务分配的计算节点，用`nvm`命令查看GPU动态监控、用`btop`命令查看各种硬件的动态监控

以下是一个SSH连接的示例：

首先提交一个计算任务，可通过`squeue`命令确认任务所在的计算节点的名字，用诸如：`ssh [计算节点名]`的命令连接到任务所在节点。本例中的计算节点是`4v100pxn09`，使用`ssh 4v100pxn09`命令连接到这一节点。


连接到计算节点后可以使用`nvm`、`btop`等命令查看各种硬件的动态监控。同时在屏幕上可以看到集群系统中为用户定制的特殊命令和别名说明（在登录到登录节点时也会显示）。


## GPU动态监控 `nvm`

`nvm`命令是`nvidia-smi dmon -s pucvmte -o T`命令的alias，用于监控job在当前计算节点所调用的GPU的详细状态，其输出信息的解释如下：


实践中往往会看到“SM活跃度”达到了80%以上，但GPU功率远未达到标准TDP/TGP (对于V100是300W) 的情况，这一般有3种原因：

1. 程序每批次“喂”给GPU的任务太少 (CUDA kernel太小)，或并行度不够，无法占满SM后端执行单元
1. 程序遇到了严重的“内存墙”，大部分时间都在进行显存的读写 (这种情况下往往会看到接近100%的显存带宽利用率)
1. 程序的GPU间通信通过GPU-Direct完成，但通信开销大，SM大部分时间都在执行通信任务。值得注意的是，这种情况下PCIe吞吐或NVLink吞吐不一定很大，因为瓶颈有可能是通信延迟

## NVLink吞吐监控 `nvltm`

`nvltm`命令是`watch -n 0.1 nvidia-smi nvlink -gt d`命令的alias，用于监控job在当前计算节点所调用的GPU的NVLink数据吞吐情况，以便评估程序是否正在高效利用NVLink

## ✨Netdata服务

SAI的所有计算节点均部署了经过性能优化的[Netdata服务](https%3A%2F%2Fwww.netdata.cloud)，可以图形化地全面监控硬件（例如CPU、内存、GPU、IB网络、存储设备等）以辅助进行程序的Profiling或Debug。

Netdata会保存近一个多月的历史记录，以便回溯已经跑完的任务。

此处使用MobaXterm自带的的MobaSSHTunnel功能实现SSH端口转发，将登录节点作为跳板，连接计算节点的19999端口并查看Netdata服务的网页。

MobaSSHTunnel可通过如下方式打开：


随后创建SSH Tunnel：


参考下图完成配置：


随后在浏览器中访问`localhost:19999/v3` 即可查看计算节点的Netdata网页。需保证此时访问的端口号与SSH Tunnel中转发到本地的端口号一致。本地端口号可按需自行修改，上述URL中的端口号也需随之修改。


---

# 💡FAQ

<reference-synced source-block-id="HjIHdJxYuszonUbafg9c6scbn9R" source-document-id="Y0sddTeCxouM8wxyQTMcM86Jnlh">

  ### Q: “error：QOSMinGRES”是什么报错？
  

  A：slurm脚本中的QOS设置有误。请看手册中[QOS小节](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-JmCPdYcTsoyDaFxuIVHc0hS9nSg)，同时注意以下提示：
  

  如调用卡数为单卡时QOS应选择`improper-gpu`、`rush-1o2gpu`或`flood-1o2gpu`：

  ---

  ### **Q:下面这些任务的排队原因是什么？**
  排队原因1：`AssocGrpGRES`
  

  当前该用户组的全局GPU配额为64，提交该任务将超过这一配额，需要等待其他任务跑完或联系管理员扩大配额。
  排队原因2：`QOSMaxGRESPerUser`
  

  QOS为`rush-4gpu`或`rush-8gpu`时，每用户在同一QOS使用的最大gpu数目前仅为8（实时数值请看：快速开始）。QOS的命名非常直白，“rush”指的是在rush的场景使用，否则不要用。

</reference-synced>

---

## Home目录配额

# Home目录配额

待补充

# 统计存储空间占用 `ncdu`

`ncdu`支持可视化、交互式地查看存储空间占用。

只需运行一次统计，用户即可交互式进入各级目录查看存储空间占用、查看文件/文件夹数量、设置排序方式、分别查看实际存储占用与实际文件体积（SAI的Home目录存储空间支持透明压缩，默认状态下看到的是实际存储占用，而实际文件体积往往比这个数值大得多，在ncdu界面中可通过键盘“a”键切换两种显示模式）

---

## MACE模型设置

## ABACUS计算实例

下面我们将参考ABACUS手册中的实例，在SAI上完成一次态密度和能带的计算。手册链接见：https://mcresearch.github.io/abacus-user-guide/abacus-dos.html

首先我们通过git命令获取官方的example文件。
```plaintext {wrap}
git clone https://gitee.com/mcresearch/abacus-user-guide.git
```


下载完成后，进入`abacus-user-guide/examples/dos_band` 文件夹，可以看到里面有 `Al` 和 `Fe` 两个文件夹。进入 `Al` 文件夹，可以看到相应的example文件，其中`STRU`是铝结构优化后的 fcc 单胞结构：


此时突然发现我刚刚`srun`在8V100V0玩太开心了，忘记回到登录节点了，连忙`exit`回到登录节点

由于做 DOS 和电子能带结构计算时，常用原胞，因此我们使用Atomkit需要做一步结构转换。首先使用Environment Modules工具加载环境：
```bash {wrap}
ml load atomkit
```


确保atomkit被激活后，使用以下命令得到原胞 `PRIMCELL.STRU`
```plaintext {wrap}
echo -e "2\n 202\n 101 STRU\n 101" | atomkit
```

这里为了方便演示，使用了命令行，表示将'2'、'202'、'101 STRU'和'101'依次传入atomkit，实际可以按照atomkit的提示依次输入

2代表进行Symmetry Analysis

202代表进行Find Primitive Cell

101 STRU代表读取ABACUS的STRU文件

101代表输出格式为ABACUS

转换结束后，使用`ml purge`清空使用Environment Modules工具加载的环境变量，以满足提交任务时bash环境完全干净的需求。

首先进行SCF计算来获取电子密度，ABACUS运行依赖于`INPUT`文件、`KPT`文件和结构文件，我们复制scf计算的example文件为相应的文件名。而结构文件在`INPUT`文件中被设定为了我们上一步得到的`PRIMCELL.STRU`。该步操作的具体命令：
```plaintext
cp INPUT-scf INPUT
cp KPT-scf KPT
```


随后我们从`/opt/sbatch_examples`目录获取提交ABACUS任务所需的模板文件并复制到当前目录：
```plaintext {wrap}
cp /opt/sbatch_examples/gpu_abacus.sbatch .
```


```plaintext {wrap}
nano gpu_abacus.sbatch
```

随后，用`nano`命令修改复制过来的模板文件，修改使用卡数和QOS：


修改完成后，使用ctrl+o快捷键来保存，并ctrl+x快捷键退出。

我们使用如下命令来提交修改过后的sbatch脚本：
```plaintext {wrap}
sbatch gpu_abacus.sbatch
```


我们可以使用任务提交和管理中提到的`squeue`命令来查看排队情况，使用`gpu`命令来查看集群的GPU资源的空闲情况：


---

## MACE的训练和使用

本节介绍如何在SAI上进行MACE的训练，以及如何在LAMMPS上使用MACE进行多GPU并行的MD模拟。

**本节所有的相关输入文件均在：**`**/home/**``**public/**``**tutorial/MACE**`****大家可以在SAI上直接访问该目录

### 模型训练

我们将以(Pb,Sr)TiO`$_3$`钙钛矿固溶体为例，展示如何训练一个MACE模型。

(该数据集来自文献：PRB 107,144102(2023); DOI: https://doi.org/10.1103/PhysRevB.107.144102)

**（任务提交）**仅需几行指令，您便可在SAI上提交一个MACE训练任务：
```bash
>> cp -r /home/public/tutorial/MACE/01-training/ . # 复制Example到当前目录
>> cd 01-training/
>> ls  # 查看文件
config.yaml              # MACE的输入文件
gpu_mace-train.sbatch    # 任务提交文件
les_config.yaml          # MCAE-LES的输入文件
test.xyz                 # 测试集
train.xyz                # 训练集
>> sbatch gpu_mace-train.sbatch # 提交任务
```

**（任务状态监控**）输入`sqm`即可查看自己已提交任务。可以发现任务正在正常运行中：


**（输出文件检查）**使用`vim`打开输出日志，即可检查MACE的输出，这里已经训练到第10个Epoch：


**（资源）**本节的重点不在详细介绍MACE如何使用。如果您想了解MACE的参数，这里推荐一些或许有用的资源：

1. https://mace-docs.readthedocs.io/en/latest/index.html  (MACE官方文档）
1. https://github.com/ACEsuit/mace （MACE官方仓库）
1. https://mp.weixin.qq.com/s/pXvkUunxyqJ7Lh4KPV7L0g（MACE环境配置）
1. https://mp.weixin.qq.com/s/A46QCdyzHD6EDvPRrgrV4g（MACE-LES代码解析）

### 模型格式转换

MACE训练结束后，会产生一个`.model`后缀的文件。这个模型无法直接被LAMMPS读取，我们需要先将其转化为可用的模型格式。

目前MACE在LAMMPS中有2个可用接口，不同接口采用的模型格式不同：

- [MACE in LAMMPS](https%3A%2F%2Fmace-docs.readthedocs.io%2Fen%2Flatest%2Fguide%2Flammps.html) （早期版本，性能较低，**不推荐**）
- [MACE in LAMMPS with ML-IAP](https%3A%2F%2Fmace-docs.readthedocs.io%2Fen%2Flatest%2Fguide%2Flammps_mliap.html)（新接口，专为GPU优化，**推荐**）

本节我们只介绍第二个接口的使用方法。

**（任务提交）**仅需几行指令，您便可在SAI上提交该任务：
```bash
>> cp -r /home/public/tutorial/MACE/02-lammps/01-make-model/ . # 复制Example到当前目录
>> cd 01-make-model
>> ls 
mace-omat-0-medium.model  # MACE-OMAT预训练模型，您可以替换为自己的模型
submit.sbatch             # 提交脚本
>> sbatch submit.sbatch   # 提交任务
```

**（结果检查）**通常情况下，任务运行几秒后就会正常结束，并产生一个新文件：`mace-omat-0-medium.model-mliap_lammps.pt`

### LAMMPS中使用MACE

本节，我们将基于上节得到的模型，在LAMMPS中进行多GPU并行的MD模拟。

**（任务提交）**仅需几行指令，您便可在SAI上提交一个MD模拟：
```bash
>> cp -r /home/public/tutorial/MACE/02-lammps/02-run-MD/ . # 复制Example到当前目录
>> cd 02-run-MD/
>> ls 
conf.lmp             # 结构文件
input.lammps         # LAMMPS的输入文件
gpu_lmp-mace.sbatch  # 提交脚本
>> sbatch gpu_lmp-mace.sbatch  # 提交任务
```

**（输入文件）**我们简要解析下LAMMPS输入文件的关键内容：

（为了简洁，下面只**列举关键内容**，完整文档请前往[官网](https%3A%2F%2Fmace-docs.readthedocs.io%2Fen%2Flatest%2Fguide%2Flammps_mliap.html%23using-mace-with-ml-iap-in-lammps)）
```plaintext
units           metal
boundary        p p p
atom_style      atomic
newton          on     # 必须打开

neighbor        2.0 bin
neigh_modify    every 1

read_data       conf.lmp

# MACE模型设置
pair_style      mliap unified ../01-make-model/mace-omat-0-medium.model-mliap_lammps.pt 0
pair_coeff      * * Sr Pb Ti O # 需要与结构文件中的原子类型对应

velocity        all create ${TEMP} 539619
fix             1 all npt temp 300 300 1 z 0 0 5
timestep        0.002000
run             1000
```

**（提交脚本）**这里是完整提交脚本，该脚本调用了4V100上4个节点，每个节点使用4张GPU，共计16张GPU。一般情况下，用户只需要修改**标红**的内容：
```bash
#!/bin/bash
#SBATCH --job-name=LMP
#SBATCH --partition=4V100
#SBATCH --nodes=4
#SBATCH --ntasks=16         # Nodes * GPUs-per-node * Ranks-per-GPU
#SBATCH --gpus-per-node=4   # Specify the GPUs-per-node
#SBATCH --qos=huge-gpu      # Depending on your needs [Priority: rush-4gpu = rush-8gpu > improper-gpu > huge-gpu]

# ⚠ DO NOT modify [CUDA-MPS] and [Rank-Map] settings unless you know what you are doing.
source /opt/sai_config/mps_mapping.d/${SLURM_JOB_PARTITION}.bash

export OMP_NUM_THREADS=2

# Below are executing commands
nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &

module purge
module load lammps/25jul2025-mace-0.3.15

mpirun -np $SLURM_NTASKS -map-by $MAP_OPT lmp -k on g $SLURM_GPUS_ON_NODE -sf kk -pk kokkos cuda/aware on neigh half comm device newton on -in input.lammps

# Must explicitly exit
exit
```

**（输出文件）**使用`vim`打开`log.lammps`即可查看输出的任务日志，这里展示最后一部分，笔者将自认为重要的部分**标红**：
```yaml
       980   176.58434     -126924.75      385.15441     -126539.6      -10024.276      225144.6       59.37          59.37          63.874488
       990   178.49146     -126927.81      389.3141      -126538.5      -9362.952       225221.08      59.37          59.37          63.896188
      1000   177.35574     -126924.33      386.83694     -126537.5      -9487.2508      225295.86      59.37          59.37          63.917403
Loop time of 94.9775 on 16 procs for 1000 steps with 16875 atoms

Performance: 1.819 ns/day（性能）, 13.191 hours/ns, 10.529 timesteps/s, 177.674 katom-step/s
99.2% CPU use with 16 MPI tasks x 1 OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 91.605     | 92.409     | 93.044     |   4.3 | 97.30
Neigh   | 0.0029915  | 0.0037048  | 0.0080641  |   1.9 |  0.00
Comm    | 1.0875     | 1.7143     | 2.5117     |  31.3 |  1.80
Output  | 0.32176    | 0.35433    | 0.39619    |   2.9 |  0.37
Modify  | 0.32575    | 0.37351    | 0.40621    |   3.1 |  0.39
Other   |            | 0.1225     |            |       |  0.13

Nlocal:        1054.69 ave        1095 max         997 min
Histogram: 2 0 1 1 1 1 3 4 2 1
Nghost:        4140.62 ave        4212 max        4042 min
Histogram: 2 2 0 1 2 1 1 0 1 6
Neighs:              0 ave           0 max           0 min
Histogram: 16 0 0 0 0 0 0 0 0 0
FullNghs:       167784 ave      173977 max      158286 min
Histogram: 2 0 1 1 1 0 3 4 2 2

Total # of neighbors = 2684538
Ave neighs/atom = 159.08373
Neighbor list builds = 7
Dangerous builds = 0
write_restart   eq.restart
System init for write_restart ...
write_data      eq.data
System init for write_data ...

Total wall time: 0:02:25 # 总耗时
```

**注：**MACE-LES模型无法在LAMMPS内运行。详情请见：https://github.com/ACEsuit/mace/issues/1283

### MD效率测试

近期马上补充

---

## AlphaFold3蛋白质结构预测

### “一梭子”用法

使用通用单卡Sbatch模板`/opt/sbatch_examples/gpu_generic-singlegpu.sbatch`

填写运行命令：
```bash
module load alphafold/3.0.1
run_alphafold3.0.1.sh <输入文件所在目录> <输出文件所在目录> <输入文件(json格式)>
```

### 省钱用法 (两步式)

#### 第一步：MSA计算 (CPU-only)

Sbatch模板：`/opt/sbatch_examples/af3_st1_msa.sbatch`
```bash
#!/bin/bash
#SBATCH --job-name=AF3-MSA
#SBATCH --partition=CPU-MISC
#SBATCH --nodes=1           # Specify the number of Node(s)
#SBATCH --ntasks=1          # Specify the number of MPI Rank(s)
#SBATCH --cpus-per-task=8   # Specify the number of CPU Core(s) of each MPI Rank
#SBATCH --qos=rush-cpu      # Depending on your needs [Priority: rush-cpu > huge-cpu]

module load alphafold/3.0.1

# 手动填写以下文件路径
AF3_INPUT_JSON='af3.json'
AF3_INPUT_DIR='.'
AF3_OUT_DIR='af3-out'
# 文件路径设置完毕

mkdir -p $AF3_OUT_DIR

apptainer exec \
        --bind $AF3_INPUT_DIR:/root/af_input \
        --bind $AF3_OUT_DIR:/root/af_output \
        --bind /cache_local/alphafold/af3_data/af3_data/:/root/public_databases \
        /opt/apps/alphafold/3.0.1/alphafold3.0.1-um-modify.sif \
python /app/alphafold/run_alphafold.py \
        --json_path=/root/af_input/$AF3_INPUT_JSON \
        --db_dir=/root/public_databases \
        --output_dir=/root/af_output/ \
        --norun_inference

```

#### 第二步：推理 (GPU加速)

Sbatch模板：`/opt/sbatch_examples/af3_st2_infer.sbatch`
```bash
#!/bin/bash
#SBATCH --job-name=AF3-Inference
#SBATCH --partition=4V100
#SBATCH --nodes=1
#SBATCH --ntasks=1          # Nodes * GPUs-per-node * Ranks-per-GPU
#SBATCH --gpus-per-node=1   # Specify the GPUs-per-node
#SBATCH --qos=improper-gpu  # Depending on your needs [Priority: rush-4gpu = rush-8gpu > improper-gpu > huge-gpu]

nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &

module load alphafold/3.0.1

# 手动填写以下文件路径
AF3_INPUT_JSON='af3_data.json'  # 此文件由上一步MSA计算输出，后缀固定为'_data.json'，前缀取决于用户在上一步输入json中设置的蛋白质名称
AF3_INPUT_DIR='af3-out/af3'     # 此路径为上一行指定的文件所在路径
AF3_OUT_DIR='af3-out'
# 文件路径设置完毕

mkdir -p $AF3_OUT_DIR

apptainer exec \
        --nv \
        --bind $AF3_INPUT_DIR:/root/af_input \
        --bind $AF3_OUT_DIR:/root/af_output \
        --bind /cache_local/alphafold/af3_data/af3_models/:/root/models \
        --bind /cache_local/alphafold/af3_data/af3_data/:/root/public_databases \
        --env XLA_FLAGS="--xla_disable_hlo_passes=custom-kernel-fusion-rewriter" \
        /opt/apps/alphafold/3.0.1/alphafold3.0.1-um-modify.sif \
python /app/alphafold/run_alphafold.py \
        --json_path=/root/af_input/$AF3_INPUT_JSON \
        --model_dir=/root/models \
        --db_dir=/root/public_databases \
        --output_dir=/root/af_output/ \
        --norun_data_pipeline \
        --jax_compilation_cache_dir=/root/af_output/ \
        --flash_attention_implementation=xla

```

#### 特殊用法：批量计算

此处展示的方法为子任务集中在单个Slurm Job内串行运行，该方法缺乏并行化，速度很慢。

在sbatch脚本中使用for循环串行运行的方法与此方法无本质区别。

进阶用户应采用[Slurm Job Array](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FZmkawnhNZicpxAkuwh4cNSWGnpc%23share-LZICdrBajolf6ExF8GEcNssznsh)，以并行运行子任务。

- 删除包含`AF3_INPUT_JSON`的行
- 在python命令中添加`--input_dir=/root/af_input`
- 按需增加CPU核数/GPU卡数并调整QOS

以下为`af3_st1_msa.sbatch`的示例，`af3_st2_infer.sbatch`使用同样方法修改，注意按需修改GPU卡数等
```bash
#!/bin/bash
#SBATCH --job-name=AF3-MSA
#SBATCH --partition=CPU-MISC
#SBATCH --nodes=1           # Specify the number of Node(s)
#SBATCH --ntasks=1          # Specify the number of MPI Rank(s)
#SBATCH --cpus-per-task=32  # Specify the number of CPU Core(s) of each MPI Rank
#SBATCH --qos=huge-cpu      # Depending on your needs [Priority: rush-cpu > huge-cpu]

module load alphafold/3.0.1

# 手动填写以下文件路径
AF3_INPUT_DIR='.'  # 此路径中应包含所有要计算的json文件
AF3_OUT_DIR='af3-out'
# 文件路径设置完毕

mkdir -p $AF3_OUT_DIR

apptainer exec \
        --bind $AF3_INPUT_DIR:/root/af_input \
        --bind $AF3_OUT_DIR:/root/af_output \
        --bind /cache_local/alphafold/af3_data/af3_data/:/root/public_databases \
        /opt/apps/alphafold/3.0.1/alphafold3.0.1-um-modify.sif \
python /app/alphafold/run_alphafold.py \
        --input_dir=/root/af_input \
        --db_dir=/root/public_databases \
        --output_dir=/root/af_output/ \
        --norun_inference

```

---

## 持续更新中，敬请期待……

---

## 超算核心概念通用科普

- 此页面仅包含SAI的部分知识，建议仔细阅读完整文档（若目录未显示，请点击页面左上角“**≡**”图标）
- 请**仔细阅读登录提示**，对于有Slurm调度集群使用基础的用户，通过登录提示即可完成计算任务提交
- SAI唯一指定用户交流群：1059719323
- 技术问题（如软件问题、科研问题等）请**不要私信询问**，发到群里可获得最专业且即时的解答

# 超算核心概念通用科普

由 Qwen3-Max 大语言模型生成，经人工修补

如果您习惯单机工作站（如一台高性能PC），超算可在此基础上通过规模化协作大幅提升计算能力。以下是关键概念的简要科普，助您快速上手：

- **计算集群**

不再是单台机器，而是由数十至数千台服务器（“节点”）组成的阵列。想象成一座“计算工厂”——任务自动分配给空闲节点，避免单点瓶颈。

- **分布式存储**

数据分散存储在多个节点（而非单一硬盘），类似“共享云盘”，但访问快得多，且更可靠（一个节点故障，数据仍可从其他节点读取）。

- **分布式并行计算**

任务被智能拆解为小块，由集群节点同时计算（例如64个节点处理512个子任务），显著加速大规模模拟。

- **GPU加速**

集群节点配备GPU（图形处理器），专为并行计算优化。相比CPU，GPU能极速处理AI训练、分子动力学等计算密集型任务（速度提升10-100倍）。

- **高性能互联**

节点间通过高速网络（如InfiniBand）连接，延迟极低（亚微秒级）、速率极高（数百Gbps），避免通信拖慢整体速度。

- **登录节点 vs 计算节点**
  - **登录节点**：仅用于上传/下载数据、编辑文件、提交/管理任务、安装软件，禁止在登录节点运行计算任务。
  - **计算节点**：实际执行任务的“工人”，通过调度系统自动分配，所有计算必须通过调度系统提交。
- **计算节点分区（Partition）**

一组计算节点的集合，分隔不同类型的计算节点以适配不同的计算需求。

- **任务（Job）**

提交计算的基本单元。

- **任务调度系统**

超算资源由多人共享，不能像单机一样“随时运行”。您需通过任务脚本或专用的交互式命令提交任务（如指定需要多少CPU/GPU、内存等），系统按队列排队调度。常见调度器：Slurm、PBS、LSF。

- **QOS（Quality of Service）**

用于控制任务的类型、优先级、资源配置等，确保任务调度符合用户需求。

- **软件环境管理**

超算通常用Environment Modules管理软件（如`module load gcc/15.2.0`），避免版本冲突。

- **I/O（输入/输出）瓶颈**

大量小文件读写或频繁访问全局共享存储（分布式存储）会严重拖慢性能（甚至影响他人）。建议：合并文件、使用计算节点本地固态硬盘（`/tmp`或`$CACHE_LOCAL`）做中间计算，最后再写回全局共享存储。

- **可扩展性与并行效率**

并非“处理器越多越快”。通信开销、负载不均等因素可能导致加速比下降。建议从小规模测试开始，逐步扩展。

- **检查点与容错**

长时间任务应定期保存中间状态（checkpoint）。若任务因超时或故障中断，可从中断处恢复，避免重跑。

---

# SAI的基本系统环境
- 操作系统：Ubuntu Server 24.04.3 LTS
- 内核：GNU/Linux 6.8.0-71-generic x86_64
- GLIBC版本：2.39
- 系统GCC版本：13.3.0
- Bash版本：5.2.21
- NVIDIA GPU驱动版本：550.163.01 (CUDA Driver 12.4)
- InfiniBand驱动(OFED)版本：24.10-3.2.5.0
- GDRCopy驱动版本：2.5.0
- Slurm版本：25.05.2 (支持TAB键自动补全)
- Environment Modules版本：5.4.0
- BeeGFS(一种开源高性能并行文件系统)版本：8.1.0

---

# SAI的开发和应用软件环境


此处仅做简介，关于软件环境的具体讲解，请看软件环境章节

- ✨Sbatch脚本模板位于`**/opt/sbatch_examples**`，模板列表及其介绍请看手册软件环境
- SAI统一安装的应用软件位于`/opt/apps`
- SAI统一安装的开发工具位于`/opt/devtools`
- ✨用户为组内统一安装的软件，以及其他组内共享数据，可放置到`/home/${GROUP_NAME}/``share`
- SAI通过 Environment Modules 管理大部分软件，用户自行安装的软件也可通过此方式管理
- 对于不便使用 Environment Modules 管理的软件，可使用Bash语法写成`.env`脚本，通过`source`命令调用，SAI统一安装的此类软件的`.env`脚本位于`/opt/envs`
- **⚠****不要**将Conda等复杂环境管理工具的初始化或特定环境的加载写入`~/.bashrc`，这将会导致环境混乱，甚至影响计算结果的正确性！！！使用快捷命令`AC`激活Conda
- ✨SAI提供**Apptainer容器**方案，以实现高度灵活的软件环境可移植性。SAI的Apptainer可直接通过`module`命令加载，支持[Fakeroot模式2和3](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Ffakeroot.html)，禁用了SUID以确保安全性。关于其用法请进一步阅读手册软件环境

---

# ✨以GPU为中心的调度

- **不允许**用户在提交任务时指定CPU和内存资源，系统会自动绑定分配最佳的CPU和内存资源
- 用户只需指定`--nodes`、`--ntasks`和`--gpus-per-node`，不允许指定内存相关参数（如`--mem`）和CPU核数相关参数（如`--cpus-per-task`），否则任务会在启动的瞬间被停止
- 用户只需关注申请多少计算节点、申请在每个节点上调用多少GPU、要在每个GPU上运行多少进程

---

# 🔥 GPU配额与QOS

## 全局GPU配额

- 登录提示信息中包含了全局GPU配额：`Your global GPU quota is ``[xxx]`
- 用户默认全局GPU配额为**128**（Slurm账户的`GrpTRES`设置），用户组无GPU配额限制
- 默认全局GPU配额随着更多计算资源的陆续上线将逐步增大
- 如需提升全局GPU配额，请联系管理员，SAI鼓励用户运行大规模并行任务，积极响应此类需求

## QOS (Quality of Service)

### GPU QOS 规则

向右滚动查看完整表格


| **QOS** | **优先级** | **每****用户组****可同时**
      **排队的job数量** | **每****用户组****可同时**
      **调用的GPU数量** | **每job可申请的GPU数量范围** | **每job最大运行时间** | **特殊说明** | **适用场景** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **improper-gpu** | 中 | 500 | **64**
      (随资源上线而增大) | 1 ~ 64 | **30 days** | GPU数量在取值范围内无特殊限制，
      但只有少量分区支持此QOS | 单个job的GPU数量为特殊值 |
| **rush-1o2gpu** | 高 | 10 | **16**
      (随资源上线而增大) | 1 ~ 2 | **24 hrs** | 每job的GPU数量必须为1或2，
      且只有少量分区支持此QOS | 小型测试，每job只需1~2个GPU，需要尽快排上队 |
| **rush-gpu**
      **(默认)** | 高 | 10 | **16**
      (随资源上线而增大) | 4 ~ 16 | **24 hrs** | 每节点的GPU数量必须可被4整除 | 小型测试，每job只需4~16个GPU，
      需要尽快排上队 |
| **huge-gpu** | 中 | 100 | **128**
      (随资源上线而增大) | 4 ~ 128 | **30 days** | 每节点的GPU数量必须可被4整除 | 大规模计算，且每job持续时间长 |
| **ultimate-gpu** | 低 | 1 | 不限 | 4 ~ ∞ | ∞ | 每用户最多同时提交1个job，
      且每节点的GPU数量必须可被4整除 | 超大规模计算，且每job持续时间长
      （例如占满整个集群运行许多天） |
| **flood-gpu** | 低 | 10000 | 不限 | 4 ~ ∞ | **4 hrs** | 每节点的GPU数量必须可被4整除 | 超大规模计算，且每job持续时间短 |
| **flood-1o2gpu** | 低 | 10000 | 不限 | 1 ~ 2 | **4 hrs** | 每job的GPU数量必须为1或2，
      且只有少量分区支持此QOS | 大量小job，每job只需1~2个GPU且持续时间短 |


- QOS前缀为`flood`和`ultimate`的任务，虽然不被QOS限制同时调用的GPU数量，但会受到[全局GPU配额](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-H10AdTcoxoHdd7xKRHYcDIBOnTh)限制
- 其余QOS的“每用户组可同时调用的GPU数量”，随着更多计算资源的陆续上线将逐步增大
- 为了防止资源过度碎片化，SAI只在`4V100`分区启用了`improper-gpu`、`rush-1o2gpu`和`flood-1o2gpu`
  - 试想：如果大量单卡、双卡乃至“大质数”卡数的任务分散在各个节点上，用户将难以运行需要多个完整节点的任务，只能望着大量空闲而无法被调用的“散碎GPU”叹气

若任务的QOS不是`improper-gpu`、`rush-1o2gpu`或`flood-1o2gpu`，同时其在每节点上调用的GPU数量无法被4整除（例如调用4个节点，每节点2个GPU），则任务会在启动的瞬间被停止

为了提升体验，未来将实现在任务提交时立即发出提示

### CPU QOS 规则


| **QOS** | **优先级** | **每****用户组****可同时**
      **排队的job数量** | **每****用户组****可同时**
      **调用的CPU逻辑核数** | **每****用户组****可同时调用的RAM** | 每job最大运行时间 |
| --- | --- | --- | --- | --- | --- |
| rush-cpu | 高 | 10 | 8 | 100 GiB | 48 hrs |
| huge-cpu | 中 | 100 | 48 | 500 GiB | 48 hrs |


SAI按GPU进行收费，非特殊CPU-only计算任务，必须申请GPU

对于CPU-only任务（如数据处理），可提交至CPU-MISC分区，但此分区暂时只有2个节点，每个任务最大运行时间为48小时

---

# Job排队优先级

SAI采用了主流且先进的Job优先级计算策略，Job的优先级根据以下因素确定：

1. 用户对Job指定的QOS - 请看[上一节内容](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FJEdOwsjbdirwA3kTDW0cBwQWnVe%23share-WzcRdekscomwrfx7TNnc44FEnIf)
1. 用户在近期消耗的计算资源量（Slurm公平共享因子）- 近期消耗越少，优先级越高
1. Job已排队等待的时间 - 等待越久，优先级越高

---

# ✨定制快捷命令合集

## `job`/`jm`/`sqm`/`ja`/`sqa`/`sqaa`

- SAI定制的任务状态查看命令，其中`ja`和`sqa`可查看组内用户的任务状态，`sqaa`可查看所有用户的任务状态

用法：详见任务提交和管理

## `ssj <jobid>`

- 显示特定任务的详细信息，`scontrol show job <jobid>`的简写(alias)

## `gpu`/`cpu`

- SAI定制的计算节点状态查看命令

用法：详见提交任务

## `AC`

- 加载SAI预置的Conda base环境，用户需自行创建自己的环境以进一步使用

用法：详见软件环境

## `grp-access`

- 将文件或文件夹设置为当前用户组可读取，同时确保权限最小化
- 此命令的原理：查询路径中各级目录的权限，确保对各级目录添加了`x`权限，但不修改访问指定目标不涉及的文件夹或文件的权限

用法：

1. 执行`grp-access <dir/file>`，使同用户组的用户可以读取文件夹`dir`下的所有条目（文件夹或文件）
2. 执行`grp-access <dir>/*`，使用户组可以读取文件夹`dir`下的所有条目，但无法读取文件夹`dir`本身
1. 执行`grp-access <dir> -R`，使用户组可以读取文件夹`dir`下的所有子条目（递归）

## `tmp`

- 进入当前计算节点上当前用户专属的本地SSD目录`/cache_local/${GROUP_NAME}/${USER}`或`/cache_local/${HOME#/home/}`

## `gtmp`

- 进入当前用户专属的超算全域一致高速SSD缓存目录`/cache_global/${GROUP_NAME}/${USER}`或`/cache_global/${HOME#/home/}`

📌此目录在所有节点上具有数据一致性，就像Home目录，但可靠性不如Home目录

## `nvm`

- 监控job在当前计算节点所调用的GPU的详细状态，`nvidia-smi dmon -s pucvmte -o T`命令的简写(alias)

用法：详见提交任务

## `nvltm`

- 监控job在当前计算节点所调用的GPU的NVLink数据吞吐情况，以便评估程序是否正在高效利用NVLink，`watch -n 0.1 nvidia-smi nvlink -gt d`命令的简写(alias)

## `gpu_hrs_list`

- 显示卡时消费和余额统计表格

## `fee`

待补充

## `dump_job_history`

- 用户自助导出GPU计算资源使用明细，用于财务核算等

用法：详见账号与充值

---

## 通用性能调优

**SAI竭尽一切可能** {align="center"}

**确保所有预置的应用软件** {align="center"}

**在开箱即用状态下** {align="center"}

**都有最完美的性能调优** {align="center"}

# 通用性能调优

## MPI Rank 映射

- SAI预置的[sbatch脚本模板](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FZmkawnhNZicpxAkuwh4cNSWGnpc%23share-X45Mdn0zPocphCx70d1chPRMnth)已经**包含了此调优**，用户**不需要额外设置**
- `/opt/sai_config/mps_mapping.d`目录包含不同分区的自动调优脚本，用户可查看以便深入理解
- 感兴趣或有计算机常识的用户请继续阅读👇

为了让语言更通俗易懂，这里使用了 Qwen3-Max 大语言模型进行润色

### 什么是 MPI Rank 映射？为什么需要它？

想象一下：你写了一个并行程序，用 `mpirun -np 16` 启动了 16 个 MPI 进程。这些进程默认会被操作系统“随便”分配到 CPU 核心上运行 —— 可能有的挤在一个 NUMA 节点里争抢内存带宽，有的跨 NUMA 访问远端内存，还有的和 GPU 不在同一个 PCIe 通道下导致通信延迟…

👉 **这就是问题所在！**

MPI 的 `-map-by` 参数就是用来**精确控制每个 MPI 进程（Rank）被绑定到哪个物理资源上**（比如绑到某个 L3 Cache 域、NUMA 节点、核心等），从而最大化数据局部性、减少通信延迟、提升整体性能。

### 最佳实践：以**16V100**分区单节点为例

#### 🤔 单节点硬件拓扑结构简析


- **CPU**: AMD Threadripper PRO 5995WX
  - 64核 / 128线程（支持 SMT）
  - 分为：
    - **8 个 L3 Cache 域**（每域 8 核）→ 缓存数据共享、通信低延迟
    - **4 个 NUMA 域**（每域 16 核）→ 内存访问本地化关键
- **GPU**: 16 张 V100
  - 每 4 张 GPU 挂在一个 NUMA 域下 → 和该 NUMA 域的 CPU 通信最快
- **内存**: 8 通道插满 → 带宽高，但必须让进程访问“本地内存”

#### 💪 实战命令解析：`mpirun -np 16 -map-by ppr:2:l3cache:pe=4`

`-np 16`：启动 16 个 MPI 进程（Rank 0~15）

`-map-by ppr:2:l3cache:pe=4`：

这是核心！含义是：

**ppr:2:l3cache** = “Per Processor Rank”，在每个 `l3cache` 单元中放置 2 个 MPI Rank

**pe=4** = 每个 Rank 绑定 4 个处理单元（Processing Elements，即 CPU 核心）

📌 翻译成**人话**：

在每个 L3 Cache 域（共 8 个）里放 2 个 MPI Rank，每个 Rank 独占 4 个 CPU 核心

📊 资源占用计算：

- 8 个 L3 Cache × 2 Ranks = 16 Ranks ✔️
- 每 Rank 占 4 核心 → 总共 16×4 = 64 核心 ✔️（正好用满 CPU）
- 每个 L3 Cache 域有 8 核 → 2 Ranks × 4 核 = 8 核 ✔️（完美填满）

✅ **结果：**每个 Rank 都独占一个 L3 Cache 域的一半资源，且不跨 Cache 域，缓存亲和性极佳！

⚠️ 注意：`-map-by`参数的“咒语”必须写完整，否则可能导致映射更加错乱，性能甚至会比默认状态更低！

#### 🔄 OpenMP 设置详解（两种模式）

你的每个 MPI Rank 内部还会启动 OpenMP 多线程 —— 所以你需要告诉 OpenMP 如何使用这些核心。

##### 🚫 不使用 SMT（同步多线程）
```plaintext
export OMP_NUM_THREADS=4
export OMP_PLACES=cores
export OMP_PROC_BIND=close
```

每个 Rank 启动 4 个 OpenMP 线程，绑定到 4 个物理核心（`OMP_PLACES=cores`），并且线程尽量“靠近”主进程（`OMP_PROC_BIND=close`），提高缓存命中率。

##### ✅ 使用 SMT
```plaintext
export OMP_NUM_THREADS=8
```

每个 Rank 启动 8 个线程，跑在 4 个物理核心的 8 个逻辑线程上。

⚠️ 注意：SMT 可能带来性能提升（如果程序访存密集、计算轻），也可能因资源竞争降低性能（计算密集型）。需实测！

#### 🎯 性能调优原则总结

- 减少跨 NUMA 内存访问
- 减少跨 L3 Cache 通信
- 避免核心争抢
- 提高缓存命中率
- 最小化 GPU-CPU 通信延迟

#### 🧪 应用场景举例

你正在跑一个 16-GPU 的深度学习训练或分子动力学模拟，启动了16个 Rank ，每个 GPU 负责一部分数据，MPI 负责 Rank 间通信，OpenMP 负责每个 Rank 内部并行。

##### ❌ 默认启动（无映射绑定）

- Rank 0 跑在 NUMA 0，但它的数据在 GPU 4（挂在 NUMA 1）→ 每次拷贝数据都要跨 NUMA！
- Rank 7 和 Rank 8 共享一个核心 → 上下文切换频繁，缓存失效
- Rank 4 的 8 个 OpenMP 线程分布在 2 个 L3 Cache 域中 → 数据频繁跨 L3 Cache 域读写，延迟开销大
- 性能可能只有最优的 50%！

##### ✅ 优化后

- Rank 0~3 在 L3 Cache 0+1（属于 NUMA 3），对应 GPU 0~3 → 数据本地化 ✔️
- 每个 Rank 独占 4 核，OpenMP 线程绑在这些核上 → 无干扰 ✔️
- 所有 Rank 的内存访问都在本地 NUMA 域 → 带宽拉满 ✔️
- GPU-CPU 通信走最近 PCIe 链路 → 延迟最低 ✔️

📈 性能提升可达 30%~200%，取决于程序对内存/通信的敏感度

---

## CUDA-MPS

CUDA-MPS 是一个让多个进程“共享同一个GPU上下文”的后台服务，在多进程并发调用同一块GPU时，能显著提升GPU利用率。

互联网上关于 CUDA-MPS 的教程往往只涉及在同一个GPU上运行多个串行任务的应用场景，但实际上，CUDA-MPS 在大规模并行场景才能发挥出真正的实力 —— 在**每个GPU运行不止1个 MPI Rank**的情况下，使这些 Rank **共享同一个GPU上下文**，多个 Rank 的 CUDA kernel 可以更紧密地交错执行，**减少GPU的流水线空泡**

Qwen3-Max 大语言模型生成的比喻：

- 直接在每个GPU上运行不止1个 MPI Rank：

一个教授（GPU）被多个学生（MPI Rank）轮流问问题，但每换一个学生，教授都要先收拾桌子、翻新笔记、重新戴眼镜 —— 虽然每个学生的问题都很短，但切换成本吃掉了大量时间

- 开启MPS后，多个Rank共享一个“虚拟上下文”：

现在教授面前摆了一张大圆桌，所有学生同时坐着，举手提问，教授按顺序/空闲就答 —— 无需收拾桌面，效率飙升！

**在SAI上使用此功能非常简单**，用户只需照常在sbatch脚本中设置`--nodes`、`--ntasks`和`--gpus-per-node`，通过三者隐式指定每个GPU的进程数，SAI会自动判断如何启动CUDA-MPS

以下是CUDA-MPS在具体应用场景中的用途：

- **CP2K：**MPS可以用来凑“平方数个MPI Rank”
- **QE：**MPS对于多K点小体系有性能增益，需配合QE的`-nk`参数
- **DP-LMP：**MPS对于每卡显存能占用到1GB以上的任务有性能增益，其原理是切分更多Rank以减少Neighbor List构建的耗时；对于每卡显存占用很小的任务，Neighbor List构建的开销不大，MPI本身的开销更显著，MPS反而会使性能降低
- **VASP：**多卡任务不能用MPS，因为VASP的多卡通信后端——NCCL——不支持在单卡上启动多个Rank，但对于多K点小体系VASP任务，可以同时开MPS和K点并行`KPAR`，用单卡跑

---

## 多卡、多节点通信调优

待补充

`/opt/sai_config/ib_map.d`目录下包含了UCX和NCCL通信设置，对于许多应用软件来说是最优的，但仍有部分应用软件乃至具体计算case需要进一步优化，这一般会在相应应用软件的modulefile或相应计算case的sbatch脚本模板中设置

---

# 常见软件性能调优

## VASP

- 在CPU-only的VASP任务中，人们往往关注`NPAR`和`NCORE`的调优，但它们在GPU加速场景没有意义
- 对于GPU加速VASP，只需关注`NSIM`和`KPAR`参数

### `**NSIM**`

- 对于较大体系，设置较大的值，推荐32或64
- 对于较小体系，一般用16、8或默认的4即可
- 更大的`NSIM`会占用更多的VRAM，若GPU显存不足（OOM），可酌情增加GPU数量或调小`NSIM`

### `**KPAR**`

📌设置`KPAR`的基本原则是**使每个K点的计算所跨的GPU尽可能少**

- 对于多K点体系，在理想情况下，应使`KPAR`的值等于所用GPU数量和实际计算的K点数量（**以**`**IBZKPT**`**为准**）的**最大公因数**
- 在满足前述条件的同时，使`KPAR`的值等于所用GPU数量最佳（记住：GPU数量也是可调的，例如对于7个K点的任务，可以配合`--qos=improper-gpu`申请7个GPU）
- 上述只是“理想情况”，实际会有很多例外
  - 例如YZrO-88-2kp体系：原子数较少且只有2个K点，经有限测试发现固定`KPAR=2`最佳，包括只使用单块GPU时
  - 例如Ni-HAB-59kp体系：有59个K点，而59是大质数，很难申请这个数量的GPU；同时，这种K点数特别大的体系往往原子数较少，本身不适合大规模并行；另一方面，如果按照“最大公因数”原则，`KPAR`只能为1，但这显然不合适。对于这种情况，可以申请4个GPU并设置`KPAR=4`

---

## LAMMPS

http://bbs.keinsci.com/thread-40313-1-1.html

待补充

---

## DeePMD-kit

待补充

---

# 💡FAQ

---

## 🔥 RaiDrive挂载 (强烈推荐)

# 🔥 RaiDrive挂载 (强烈推荐)

对于Windows用户，推荐用RaiDrive的SFTP挂载，把集群存储挂载到资源管理器，像在本地硬盘上一样操作集群上的文件。

挂载后效果展示：


可以从该链接下载RaiDrive：https://www.raidrive.com/zh-hans/download


登录后可安装此流程创建需要的挂载：


调试建议：


---

# SFTP/SCP

使用MobaXterm即可方便地完成传输，推荐使用“SCP (enhanced speed)”以获得更丝滑的文件传输体验：


---

# TRZSZ

SAI的登录节点已经预装了TRZSZ。

`trzsz` ( trz / tsz ) 是一款优秀的文件传输工具，和 lrzsz ( rz / sz ) 类似的、兼容 tmux 的文件传输工具。手册见https://trzsz.github.io/cn/

## TRZSZ支持的终端

- [trzsz-ssh](https%3A%2F%2Ftrzsz.github.io%2Fcn%2Fssh) ( tssh ) – 内置支持 trzsz 的 ssh 客户端（ ⭐ 推荐 ）。
- [iTerm2](https%3A%2F%2Fiterm2.com%2F) – 参考 [Trzsz-iTerm2 安装文档](https%3A%2F%2Ftrzsz.github.io%2Fcn%2Fiterm2)。
- [tabby](https%3A%2F%2Ftabby.sh%2F) – 安装 [tabby-trzsz](https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftabby-trzsz) 插件即可。
- [electerm](https%3A%2F%2Felecterm.github.io%2Felecterm%2F) – 升级到 `1.19.0` 以上的版本即可。
- [ttyd](https%3A%2F%2Fgithub.com%2Ftsl0922%2Fttyd) – 升级到 `1.7.3` 以上的版本，并且启动时加上 `-t enableTrzsz=true`，非 localhost 要用 `https`。
- [trzsz-go](https%3A%2F%2Ftrzsz.github.io%2Fcn%2Fgo) – 只要是支持本地 shell 的终端就可以用。
- [trzsz.js](https%3A%2F%2Ftrzsz.github.io%2Fcn%2Fjs) – 让运行在浏览器中的 webshell 和用 electron 开发的终端支持 `trzsz`。

## 使用指南

### `trz` 上传文件

`trz` 命令可以不带任何参数，将上传文件到当前目录。也可以带一个目录参数，指定上传到哪个目录。
```plaintext
trz /tmp/
```

### `tsz` 下载文件

`tsz` 可以带一个或多个文件名（可使用相对路径或绝对路径，也可使用通配符），将下载指定的文件。
```plaintext
tsz file1 file2 file3
```

## 使用示例

---

## 用户手册

部分手机浏览器无法正常显示此页目录，请点击左上角“**≡**”图标显示完整目录。

---

## 登录节点

# 登录节点

**注意**

1. 登录节点是用户访问超算的窗口，不可直接运行计算任务
1. 登录节点仅用于任务提交/管理、软件安装、文件编辑、数据上传/下载等用途
1. 每个用户在一台登录节点上最多只能使用4个CPU核心和50GB内存
1. 若要进入计算节点进行交互式操作，可在sbatch任务开始运行后通过SSH进入任务分配的计算节点，或使用`srun`命令搭配`--pty bash`后缀，或使用`salloc`命令，[提交任务](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FZmkawnhNZicpxAkuwh4cNSWGnpc%23share-BAs2davWwoyaz2x2JpjcrqpAnga)章节将详细介绍
1. SAI的登录节点和计算节点均可直接访问互联网、直接下载文件

---

# 登录信息

SSH线路1: c1.sai.ai-4s.com (中国电信300M,不易限速,首选)；

SSH线路2: c2.sai.ai-4s.com (中国移动500M)；

SSH端口: 12022

**Tips:**

1. 首次登录时按提示修改密码 (a.不要使用Xshell; b.**"Current Password"指的是初始密码**)，密码需包含大小写字母、数字和特殊符号，且大于等于16位，推荐使用强密码生成器，例如：
  - https://1password.com/zh-cn/password-generator（在线强密码生成器）
  - [https://bitwarden.com](https%3A%2F%2Fbitwarden.com)（密码管理器，有免费方案，可搭建私人专属密码库）
1. 登录后自行下载预置的**SSH密钥**(`~/.ssh/id_ed25519`)用于免密便捷登录，不推荐日常用密码登录
3. 请**仔细阅读登录提示**，对于有Slurm调度集群使用基础的用户，通过登录提示即可完成计算任务提交
1. 10分钟内多次登录失败，客户端IP地址将被临时封禁，第1次封禁10分钟，此后再出现10分钟内的多次登录失败，封禁时间为`10*e^[此前被封禁次数]`分钟
1. 日常使用中，用户可以自行使用`passwd`命令修改密码，但修改密码的间隔不能低于1小时
1. 若忘记密码，可联系用户交流群内的管理员重置

---

# 🔥 MobaXterm登录（📽️附视频）

MobaXterm是常用的远程终端工具，可在此处下载：https://mobaxterm.mobatek.net/download.html

📽️下面是MobaXterm的安装、初次登录和设置密钥的操作视频：

【媒体文件】<file token="PxwsbfKzWozyi1xn3WucYIUknAf" name="MobaXterm_login_v5.mp4"/>

下图为MobaXterm的SSH Session设置示例：


防止旁观者或恶意程序窃取你的密码，输入密码时，字符通常不会显示在屏幕上。尽管你看不到输入的字符显示，但实际上密码已经被输入，只需在密码粘贴/输入完成后按下回车键即可。

## 在MobaXterm中复制粘贴

- 使用鼠标**拖动**或**双击**选中要复制的内容，即可**自动完成**复制
- 按下 [**鼠标中键**]（即滚轮按键,首选）或 [Shift + Insert键] 即可进行粘贴。也可使用鼠标右键来粘贴，通过以下方式设置：


---

# 命令行登录（以PowerShell7为例）

此处的操作对于bash等环境也是通用的，演示时以PowerShell7为例。

PowerShell 7是跨平台版本，在windows、macOS和linux中均可使用，安装见[此链接](https%3A%2F%2Flearn.microsoft.com%2Fzh-cn%2Fpowershell%2Fscripting%2Finstall%2Finstall-powershell%3Fview%3Dpowershell-7.5)。

在命令行中输入以下命令可SSH连接至SAI，请将`username`替换为实际的用户名。
```powershell
ssh -p 12022 username@c1.sai.ai-4s.com  # 备线为c2.sai.ai-4s.com
```

windows中PowerShell打开方法如下：

- 按下 ***Win + R*** 快捷键，调出运行窗口。
- 输入`powershell`并按回车，即可打开 PowerShell5（windows自带版本，但支持命令有限）。
- 输入`pwsh`并按回车，即可打开 PowerShell7（体验明显更好，要先安装）。

输入上述命令进行SSH连接：


下面介绍如何使用SFTP下载密钥并配置Windows下的自动密钥登录：

首先使用以下命令SFTP连接至SAI，请将`username`替换为实际的用户名：
```powershell
sftp -P 12022 username@c1.sai.ai-4s.com  # 备线为c2.sai.ai-4s.com
```

您可使用以下命令将预置的SSH密钥(`~/.ssh/id_ed25519`)下载至本地的`C:\Users\[用户名]\.ssh`文件夹：
```powershell
get .ssh/id_ed25519 .ssh
```


本例中，本地电脑用户名为`admin`，故id_ed25519被下载到了本地的`C:\Users\admin\.ssh`文件夹

随后新开一个PowerShell，输入以下命令来使用`nano`来编辑.ssh文件夹中的config文件（您也可自选喜欢的文本编辑器）：
```powershell
nano .ssh\config
```

windows系统自带的PowerShell5未内置`nano`命令，可参考[此链接](https%3A%2F%2Flearn.microsoft.com%2Fzh-cn%2Fpowershell%2Fscripting%2Finstall%2Finstall-powershell-on-windows%3Fview%3Dpowershell-7.5)安装最新版本的powershell

nano并不是刚需，不需要纯命令行操作的话，可以直接用VScode这种文本编辑器来编辑用户文件夹下的.ssh子文件夹下的config文件（如没有该文件可直接创建一个，切记该文件是没有后缀的）。

在文件末尾加入以下代码，请将`username`和`用户名`根据实际情况修改：
```plaintext
Host SAI
  HostName c1.sai.ai-4s.com
  User username
  Port 12022
  IdentityFile C:\Users\用户名\.ssh\id_ed25519
```


对于`nano`，可使用Ctrl+X保存并退出。

顺利编辑后，在命令行中使用以下命令可使用密钥登录集群，无需再输入密码：
```powershell
ssh SAI
```

如果遇到诡异报错，可以加上`-v`选项来获得更详细的输出，即：
```powershell
ssh -v SAI
```

如果误操作导致集群上初始私钥被覆盖，可使用`ssh-keygen -t ed25519`命令创建新的密钥，并用`cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys`授权该密钥，下载新生成的`~/.ssh/id_ed25519`作为新的私钥即可。初始密钥能用时谨慎执行该操作，该操作本身就有密钥覆盖风险。

---

# Termius登录（For MacOS）

Windows系统也可以用Termius，但更推荐MobaXTerm。Mac也可以用终端登录方法

Termius是一款跨平台的远程终端工具，可以在其官网下载：https://termius.com/

下载好并打开应该是如下界面。笔者这里有保存的服务器，新下载的应该是啥都没有的。


点击“NEW HOST”新建服务器连接，输入SAI服务器的相关信息即可。Termius能在初次登录时捕捉到SAI的初始密码和密码重置机制，并指引您进行密码重置。

---

# Xshell登录（🚫不推荐）

**不推荐**初次登录使用Xshell，**提示****信息显示不全**

初次登录时需使用Keyboard Interactive：


随后根据屏幕上的提示，输入旧密码并设置新密码：


---

# 💡FAQ

<reference-synced source-block-id="Y7ORdw9h1sTJjtbINohcJxu4ngc" source-document-id="Y0sddTeCxouM8wxyQTMcM86Jnlh">

  ### Q: 首次登录修改密码失败，提示“Old password not accepted”，如图：
  

  **A:**"Current Password"指的是初始密码，也即**初始密码要输入2次**，中间任何一步出错，都需要重新从第1步开始

  ---

  ### Q: 多次登录没有成功，之后就连不上了，这是为何？
  **A:**10分钟内多次登录失败，客户端IP地址将被临时封禁，第1次封禁10分钟，此后再出现10分钟内的多次登录失败，封禁时间为`10*e^[此前被封禁次数]`分钟

</reference-synced>

---

## 环境管理

# 环境管理

## Environment-Modules

`module`命令可简写为`ml`

待补充

## Conda

单机用户熟悉的环境管理方案，主要用于与Python有关的环境管理

**强烈反对**将Conda等复杂环境管理工具的初始化过程写入`~/.bashrc`！！！

更反对在`~/.bashrc`加载特定环境！！！

这将会导致环境混乱，甚至影响计算结果的正确性！！！

- 对于安装在个人目录下的Conda，可通过环境脚本`xxx.env`统一管理，通过`source`命令按需载入
- 对于SAI预装的Anaconda3，执行快捷命令`AC`即可使用 (需通过`conda create -n <环境名称> python=<Python版本号>`新建自己的环境)


## `source`命令

待补充

## ✨Apptainer容器

SAI提供[Apptainer](https%3A%2F%2Fapptainer.org)容器（前身为[Singularity](https%3A%2F%2Fsylabs.io)），旨在以轻微的性能损失为代价换取高度灵活的软件环境可移植性。

SAI当前部署有1.4.4和1.2.4两个版本的Apptainer，可直接通过`module`命令加载，支持[Fakeroot模式2和3](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Ffakeroot.html)（详见Apptainer用户手册），禁用了SUID以确保安全性。

若用户不了解如何在无root权限的超算环境中安装软件，通过Apptainer使用Fakeroot是一个可尝试的选项。

用户自行安装的Apptainer无法正常使用，因为SAI通过白名单来许可程序创建用户命名空间。

🔥允许用户在SAI上构建自定义容器镜像。

以下是强烈推荐SAI的典型用户阅读的Apptainer用户手册内容：

- [快速开始](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Fquick_start.html)
- [安全性简介](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Fsecurity.html)
- [MPI与跨节点应用](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Fmpi.html)
- [GPU支持](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Fgpu.html)
- [定义文件（构建自定义容器镜像）](https%3A%2F%2Fapptainer.org%2Fdocs%2Fuser%2Flatest%2Fdefinition_files.html)

---

# 软件运行模板

## sbatch脚本模板列表


| 模板名称 | 软件 | 默认软件版本 | 并行能力 | 默认并行设置 |
| --- | --- | --- | --- | --- |
| cpu_serial-dataproc.sbatch | 通用，使用CPU节点进行数据处理 | - | 用户自定义 | 2核4线程 |
| gpu_abacus.sbatch | GPU加速ABACUS | LTS-3.10.1 | 单卡/多卡/多节点 | 1节点 * 4卡 |
| gpu_cp2k.sbatch | GPU加速CP2K | 2025.1 | 单卡/多卡/多节点 | 8节点 * 4卡 |
| gpu_qe.sbatch | GPU加速Quantum ESPRESSO | 7.3 | 单卡/多卡/多节点 | 1节点 * 4卡 |
| gpu_vasp.sbatch | GPU加速VASP | 6.4.2 | 单卡/多卡/多节点 | 4节点 * 4卡 |
| gpu_lmp.sbatch | GPU加速LAMMPS (默认Kokkos) | 29Aug2024 | 单卡/多卡/多节点 | 4节点 * 4卡 |
| gpu_lmp-dp.sbatch | GPU加速LAMMPS-DeePMD | 29Aug2024-3.0.3 | 单卡/多卡/多节点 | 4节点 * 4卡 |
| gpu_dptrain-multigpu-tf.sbatch | GPU加速DeePMD训练 (默认单精度，TensorFlow后端) | 3.1.2 | 单卡/多卡/多节点 | 1节点 * 4卡 |
| gpu_dptrain-multigpu-pt.sbatch | GPU加速DeePMD训练 (默认单精度，PyTorch后端) | 3.1.2 | 单卡/多卡/多节点 | 1节点 * 4卡 |
| gpu_dptrain-singlegpu.sbatch | GPU加速DeePMD训练 (默认单精度) | 3.1.2 | 单卡 | - |
| gpu_gmx-mpi.sbatch | GPU加速GROMACS (支持PME分解) | 2025.4 | 多卡/多节点 | 4节点 * 4卡 |
| gpu_gmx-multigpu-singlenode-tmpi.sbatch | GPU加速GROMACS (tMPI) | 2024.6 | 单卡/多卡 | 1节点 * 4卡 |
| gpu_gmx-singlegpu.sbatch | GPU加速GROMACS | 2024.6 | 单卡 | - |
| gpu_generic-nompi-mutigpu.sbatch | 通用，GPU加速，无MPI多卡并行，适用于GPUMD等软件 | - | 单卡/多卡 | 1节点 * 4卡 |
| gpu_generic-singlegpu.sbatch | 通用，GPU加速，单卡脚本 | - | 单卡 | - |
| af3_st1_msa.sbatch | AlphaFold3 MSA计算，CPU-only | 3.0.1 | 用户自定义 | 4核8线程 |
| af3_st2_infer.sbatch | AlphaFold3 序列推理，GPU加速 | 3.0.1 | 单卡 | - |


## 其他模板列表


| 模板名称 | 解释 |
| --- | --- |
| gpu_1gpu-dpgen-machine.json | 单卡DPGEN任务的`machine.json`模板，关键在于`command`和`resources`字段 |
| gpu_4gpu-dpgen-machine.json | 4卡DPGEN任务的`machine.json`模板，关键在于`command`和`resources`字段 |


---

# 软件编译和安装 (进阶用户)

## ✨SAI预置的编译环境

待补充

## MPI编译器和库的选择

若自行编译软件，请勿使用NVHPC捆绑的MPI栈（HPCX），因为其和Slurm不兼容，无法正确绑定/映射CPU核心和MPI Rank

待补充

## 安装位置及其目录结构

`/home/public` SAI公共资源，如教程文件、安装包仓库等

`/home/${GROUP_NAME}/share` 用户为组内统一安装的软件，以及其他组内共享数据

`/opt/apps` 应用软件安装位置

`/opt/devtools` 开发工具安装位置

`/opt/modules/modulefiles/apps` 应用软件的module文件位置

`/opt/modules/modulefiles/devtools` 开发工具的module文件位置

`/opt/envs` 通过Bash直接管理的软件的环境脚本（`.env`，通过`source`命令调用）

`/opt/custom` 卫星集群和姊妹集群的用户自定义软件统一安装位置（支持多集群自动同步）

---

# 💡FAQ

<reference-synced source-block-id="QagOdTbmwsOF1VbYWhDc5ekInmd" source-document-id="Y0sddTeCxouM8wxyQTMcM86Jnlh">

  ### Q: 如何在SAI上使用Perl脚本？运行Perl脚本提示有模块未安装
  A: Perl模块可以通过CPAN安装在自己的home目录中，例如`cpan Fortran::Format`。第一次运行`cpan`会执行初始化，一直回复`yes`即可。

  cpan初始化完成后会向`~/.bashrc`写入环境，强烈建议保持`~/.bashrc`干净，将环境配置写入独立的`.env`文件，按需`source`使用，Conda同理

</reference-synced>


---

*Skill 由SAI Docs Skill Generator自动生成*