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