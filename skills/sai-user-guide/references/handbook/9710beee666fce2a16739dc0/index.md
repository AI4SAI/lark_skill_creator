# SAI用户特殊注意事项汇总

## 登录超算

- 使用自己的 SSH 密钥登录。新账号按通行证页面领取或管理密钥；保留集群的默认密钥，避免影响节点间互访。
- Windows系统下推荐使用MobaXterm软件登录超算命令行；使用RaiDrive软件的SFTP挂载，把集群存储挂载到资源管理器，像在本地硬盘上一样操作集群上的文件
- 连续登录失败时先停止重试，检查主机、端口、用户名和密钥；仍无法连接时，向支持人员提供时间及报错。
- 登录节点用于文件整理、环境准备和任务管理。正式计算通过 Slurm 分配计算节点；不要在登录节点长时间占用大量 CPU 或内存。

## 任务提交和管理

- 任务开始运行后，才可连接已分配给自己的计算节点。先用 `sai jobs local --format table` 或 `squeue` 确认节点名。
- SSH连接到计算节点后可以使用`nvdmon`、`btop`等命令查看各种硬件的动态监控。同时在屏幕上可以看到集群系统中为用户定制的特殊命令和别名说明（在登录到登录节点时也会显示）
- 为了实现真正的“开箱即用”，SAI预置了大量sbatch脚本模板，路径为**`/opt/sbatch_examples`**，模板列表及其介绍请看手册“软件环境”板块
- 用户应按需修改sbatch脚本模板，灵活性就是脚本和命令行存在的意义
- 从未加载额外计算环境的终端提交任务，在脚本内加载所需 Conda 或 module 环境。
- CPU-only 任务使用 CPU 分区，GPU 任务按需要申请 GPU。各分区的 QOS 与时限见[快速开始](../10e455cfa1c14a90040e58a5/index.md)，费用见[账号、计费与资金](../de0cae9d9928cde1be3cc6b6/index.md)。
- GPU 分区按 GPU 数配套分配 CPU 和内存，优先使用当前模板；CPU-only 分区按自身规则申请。
- GPU 模板中保持 `--nodes`、`--ntasks`、`--gpus-per-node` 相互匹配。不要照搬其他平台的 CPU/内存参数或不必要的 `--export` 设置。
- 账户额度与 QOS 限额同时生效。用 `sai account local --format table` 查自己的账户关联，QOS 的资源和时限看下面的规则入口。
- 如需提升全局GPU配额，请联系管理员，SAI鼓励用户运行大规模并行任务，积极响应此类需求
- 每节点 GPU 数应符合所选 QOS 的资源形状要求，非整节点任务尤其要检查。
- 提交或启动时若被拒绝，保留完整提示并对照当前模板；不要只改一个 QOS 名称反复尝试。
- GPU 与 CPU 的 QOS 规则集中维护在[快速开始](../10e455cfa1c14a90040e58a5/index.md)。

选择 QOS 前，运行 `scontrol show partition 分区名` 查看 `AllowQos`；完整限额见[QOS 规则表](../10e455cfa1c14a90040e58a5/index.md)。

- 提交前选好谁付费。用 `sai account local --format table` 查看可用 Slurm 账户，`--account=账户名` 可明确指定；现金、SAI Credit 和账单见[账号、计费与资金](../de0cae9d9928cde1be3cc6b6/index.md)。

- SAI的`squeue`命令与原生Slurm有所不同，大幅优化了信息的可读性，支持指定`-p [partition] -q [qos] -A [accounts] -u [user] -t [status]`5个选项，输出信息的末尾已给出易误解的**关键字段解释**：
  1.  `GPU`：每节点的GPU数量，而非GPU总数
  2.  `MemPerU`：每个GPU(GPU分区)或每个CPU逻辑核(CPU分区)所分配的CPU内存，而非总内存或显存
  3.  还需注意：Job开始运行前，`Slots`字段显示的值等于用户指定的`--ntasks`参数的值，但系统会根据固定的每个GPU对应的CPU逻辑核数进行资源调度，Job开始运行后，此字段将显示实际占用的CPU逻辑核数
      - 4V100和16V100分区：每个GPU固定对应4核8线程CPU
      - 8V100V0分区：每个GPU固定对应3核6线程CPU

- 下面是`/opt/sbatch_examples`中的一个提交ABACUS作业的示例：

  *sbatch脚本*

  ``` bash
  #!/bin/bash
  #SBATCH --job-name=ABACUS
  #SBATCH --partition=4V100
  #SBATCH --nodes=1
  #SBATCH --ntasks=4          # Nodes * GPUs-per-node * Ranks-per-GPU
  #SBATCH --gpus-per-node=4   # Specify the GPUs-per-node
  #SBATCH --qos=rush-gpu      # Depending on your needs [Priority: rush-* > improper-* = huge-* > flood-* = ultimate-*]

  # ⚠ DO NOT modify [CUDA-MPS] and [Rank-Map] settings unless you know what you are doing.
  source /opt/sai/runtime/mps_mapping.d/${SLURM_JOB_PARTITION}.bash

  # Below are executing commands
  nvidia-smi dmon -s pucvmte -o T > nvdmon_job-$SLURM_JOB_ID.log &
  module load abacus/LTSv3.10.1-sm70-auto
  mpirun -np $SLURM_NTASKS --map-by $MAP_OPT abacus

  # Must explicitly exit
  exit
  ```

## 日常使用

- 不要在 `~/.bashrc` 自动激活计算环境；按需加载并在任务脚本中记录版本。
- 大量小文件读写或频繁访问全局共享存储（分布式存储）会严重拖慢性能（甚至影响他人）。建议：合并文件、使用计算节点本地固态硬盘（`/tmp`或`$CACHE_LOCAL`）做中间计算，最后再写回全局共享存储
- 透明压缩可节省后端空间；自己的可写额度用 `quota` 查询。
- `ncdu -r 路径` 可以只读浏览目录，找出占空间的大文件。
- 对于不调用MPI的任务（如单卡任务，或程序本身不支持MPI），应将`--ntasks`参数指定为1，并删去`[CUDA-MPS] and [Rank-Map]`设置（参考脚本：`gpu_generic-nompi-mutigpu.sbatch`），否则可能会导致所有线程挤在少量CPU核心上
- SAI统一安装的应用软件位于`/opt/apps`
- SAI统一安装的开发工具位于`/opt/devtools`
- 组内共享软件和数据放在已经授权的共享目录或项目目录；不要按旧组名猜路径。
- SAI通过 Environment Modules 管理大部分软件，用户自行安装的软件也可通过此方式管理
- 对于不便使用 Environment Modules 管理的软件，可使用Bash语法写成`.env`脚本，通过`source`命令调用，SAI统一安装的此类软件的`.env`脚本位于`/opt/envs`
- SAI提供Apptainer容器方案，以实现高度灵活的软件环境可移植性。SAI的Apptainer可直接通过`module`命令加载，支持[Fakeroot模式2和3](https://apptainer.org/docs/user/latest/fakeroot.html)，禁用了SUID以确保安全性。关于Apptainer的用法请进一步阅读手册。

## 性能相关

- 需要图形化排查性能时，用 SSH 隧道连接任务节点的 [Netdata](https://www.netdata.cloud)。操作步骤见[任务提交和管理](../263082edffdfc401aebd0e23/index.md)；历史曲线可帮助回看任务运行时的状态。
- 先使用应用模板，再根据自己的输入、结果和耗时判断是否需要调优。
- 当前分区映射脚本位于 `/opt/sai/runtime/mps_mapping.d`。需要修改 MPI 绑定时，先检查模板及实际绑定结果。
- 在支持 MPS 的应用模板里，节点数、每节点 GPU 数和总 MPI Rank 数共同决定每卡进程数，模板会处理对应配置。不同软件怎样选择，见[性能调优](../1ff92c0337e3d406c61a8e77/index.md)。
- UCX/NCCL 站点配置位于 `/opt/sai/runtime/ib_map.d`。优先沿用应用模块和当前模板的设置。
- 对于GPU加速VASP，只需关注`NSIM`和`KPAR`参数的调优，设置`KPAR`的基本原则是**使每个K点的计算所跨的GPU尽可能少**

## 硬件相关

- 选择 GPU 时，用同一输入和软件版本比较耗时、显存与费用；单个性能案例不能代表所有任务。
- 物理核心、逻辑核心和 MPI Rank 不是同一个数量；在任务内用 `lscpu` 查看分配节点的 CPU 拓扑。

## 软件编译

- 优先使用模板配套的编译器与 MPI。更换 MPI 构建后，重新检查 Slurm 启动、CPU/GPU 绑定和跨节点通信。

## 定制快捷命令合集

### `job`/`jm`/`sqm`/`ja`/`sqa`/`sqaa`

- 日常查看任务，直接用 `job` 或 `sqm`。`ja`/`sqa` 查看当前计算账户范围；脚本或 Agent 用 `sai jobs local --format table`。

用法：详见[任务提交和管理](../263082edffdfc401aebd0e23/index.md)

### `ssj <jobid>`

- 显示特定任务的详细信息，`scontrol show job <jobid>`的简写(alias)

### `gpu`/`cpu`

- SAI定制的计算节点状态查看命令

用法：详见[任务提交和管理](../263082edffdfc401aebd0e23/index.md)

### `AC`

- 加载SAI预置的Conda base环境，用户需自行创建自己的环境以进一步使用

用法：详见[软件环境](../f1d4bd8bb10f1064716136f5/index.md)

### `grp-access`

- 将文件或文件夹设置为当前用户组可读取，同时确保权限最小化
- 此命令的原理：查询路径中各级目录的权限，确保对各级目录添加了`x`权限，但不修改访问指定目标不涉及的文件夹或文件的权限

用法：

1.  执行`grp-access <dir/file>`，使同用户组的用户可以读取文件夹`dir`下的所有条目（文件夹或文件）
2.  执行`grp-access <dir>/*`，使用户组可以读取文件夹`dir`下的所有条目，但无法读取文件夹`dir`本身
3.  执行`grp-access <dir> -R`，使用户组可以读取文件夹`dir`下的所有子条目（递归）

### `tmp`

- `tmp` 进入当前节点的本地缓存 `$CACHE_LOCAL`，适合计算中间文件。换节点不会自动带走这些文件，结果要及时写回工作目录。

### `gtmp`

- `gtmp` 指向 `$CACHE_GLOBAL`；使用前查看该站点是否提供此共享缓存。长期数据仍放在正式工作目录。

### `nvdmon`

- 监控job在当前计算节点所调用的GPU的详细状态，`nvidia-smi dmon -s pucvmte -o T`命令的简写(alias)

用法：详见[任务提交和管理](../263082edffdfc401aebd0e23/index.md)

### `nvltm`

- 监控job在当前计算节点所调用的GPU的NVLink数据吞吐情况，以便评估程序是否正在高效利用NVLink，`watch -n 0.1 nvidia-smi nvlink -gt d`命令的简写(alias)

### 查看计算账户

- `sai account local --format table` 查看当前 Unix 用户可用的 Slurm 账户；资金和最终费用请在控制台查询。

### 查看费用

现金、SAI Credit、费用明细与退款入口见[账号、计费与资金](../de0cae9d9928cde1be3cc6b6/index.md)。

### 查看历史任务

- `sacct -X -j JOB_ID` 查询历史运行记录；资金核对和账单导出使用当前控制台。

用法：详见[账号、计费与资金](../de0cae9d9928cde1be3cc6b6/index.md)
