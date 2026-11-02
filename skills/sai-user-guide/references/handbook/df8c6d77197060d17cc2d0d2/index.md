# 5分钟上手

先按[登录超算](../891ee584b71ab6f7b0d6d62d/index.md)连接登录节点。运行 `sai account local --format table`，选好本次计算的账户，并替换下面命令中的 `ACCOUNT`。任务开始运行后计费。

### 交互式命令行玩耍

用[任务提交和管理](../263082edffdfc401aebd0e23/index.md)中的 `srun` 进入计算节点玩耍。下面申请主站 4V100 的 1 张 GPU，最长 5 分钟；排到资源后会自动打开终端。

``` bash
srun --account=ACCOUNT --partition=4V100 --qos=rush-1o2gpu --nodes=1 --ntasks=1 --gpus-per-node=1 --time=00:05:00 --pty bash
```

看到命令提示符里的主机名变了，就已经进入计算节点。运行 `nvidia-smi` 看看自己的 GPU：

下图是八卡示例，这次单卡练习只需看自己分配到的 GPU。每张卡有独立显存，NVLink 负责加速卡间通信。

![图片展示的是在计算节点上使用\`nvidia-smi\`命令查看GPU信息的结果。显示了8张Tesla V100-SXM2 - 32GB GPU的详细信息，包括GPU名称、温度、性能、电源状态、显存使用情况等。每张卡的显存使用均为32768MB，显存利用率均为0%，且所有卡的GPU利用率均为0%。该图片与上文提到的在计算节点运行\`nvidia-smi\`查看GPU信息的内容相呼应，直观呈现了GPU状态。](assets/e7f806ada6b05a89087fe91b21eb1e6de930ca4554a24141fa97be7880829439.png)

再试试 `nvidia-smi topo -m`，看看 GPU 和网卡怎样连接。下图是八卡节点的拓扑：

![图片展示的是八卡节点的GPU和网卡拓扑图，是文档中介绍在计算节点运行\`nvidia-smi topo-m\`命令后显示的内容。图中以不同颜色和符号标识了GPU、NIC、CPU等硬件连接情况，如GPU间有NVLink连接，NIC有mlx5_0 - mlx5_5等标识，还标注了X、S等连接类型。该图与上文提到的通过\`nvidia-smi topo-m\`查看GPU和网卡连接情况相呼应，直观呈现了节点硬件连接状态。](assets/4c2f6ec0d4671dd376de7ae94b29a3a0afec2c96658c25ea60f695af62dff166.png)

玩耍结束后，输入 `exit` 回到登录节点。再运行 `job`，确认这项交互任务已经结束。

------------------------------------------------------------------------

### 提交一个 GROMACS 示例

接下来用预先准备好的输入做一次 GROMACS 模拟。逐行执行下面的命令即可；`GMX-demo` 请使用一个尚不存在的目录名。先运行 10 分钟体验，达到时限后任务会停止。

``` bash
mkdir GMX-demo
cp /home/public/tutorial/GMX/* GMX-demo/
cd GMX-demo
cat gpu_gmx-singlegpu.sbatch
# 核对脚本后，将 ACCOUNT 替换为自己的 Slurm 账户名
sbatch --account=ACCOUNT --time=00:10:00 gpu_gmx-singlegpu.sbatch
sai jobs local --format table
```

记下 `sbatch` 返回的任务 ID。运行时用 `job` 看状态，结束后看 `slurm-JOB_ID.out` 和 `STMV-GMX.log`；`sacct -X -j JOB_ID -o JobID,State,ExitCode,Elapsed` 可查结束原因。想提前停下就用 `scancel JOB_ID`，关闭 SSH 窗口不会取消批处理任务。

![图片展示的是在登录节点上执行\`gpu_gmx-singlegpu.sbatch\`脚本后，\`squeue\`命令显示的任务状态及资源分配信息。其中，任务ID为11617，状态为R，运行/等待时间为0:04，节点为4v100n01，GPU数量为1，内存分配为23000M。图片与上下文的关系是，通过展示任务状态和资源分配，说明了在使用\`gpu_gmx-singlegpu.sbatch\`脚本运行任务后，如何通过\`squeue\`命令查看任务状态，以及任务在登录节点上的资源分配情况。](assets/2cf3c8cca443c1849e4b589a00522e469dd63e22c4ae0e4216fa6feaf7107783.png)![图片展示的是在Linux系统下使用\`nvidia-smi\`命令查看GPU信息的结果。显示了GPU型号为Tesla V100-SXM2-32GB，当前状态为On，风扇转速为71C，性能为P0，功耗为292W / 300W，显存使用率为99%，以及一个名为\`gmx\`的进程，其GPU内存使用量为624MiB。该图片与上文介绍的在Linux系统中使用\`nvidia-smi\`命令查看GPU信息的内容相关，直观呈现了命令执行后的结果。](assets/15f5183eb9b8efc6e301d3078f79ef82a2a7b830ff800c7c1b72726ed171388a.png)![图片展示的是一个终端界面，显示了CPU、GPU、磁盘、网络等系统信息。CPU使用率方面，C0 - C15各核心使用率在10% - 41%不等，C16 - C31使用率在0% - 12%。GPU使用率为99%。磁盘方面，/dev/sda1使用率90%，/dev/sdb1使用率90%。网络方面，10.100.0.1的下载速度为20.0 Kbps，上传速度为89.5 Kbps。该界面与文档中介绍的系统监控内容相关，展示了系统运行时的实时状态。](assets/4f1db8321a0b9c5d89e0f48fa679150b2851b48ac45c501e7c05a0cabff3fa6c.png)
