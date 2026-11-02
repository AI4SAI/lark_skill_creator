# 性能调优✨✨✨

先用 SAI 的应用模板，Rank 映射和通信设置已经配在相应脚本里。想继续榨性能，再按下面的方法逐项试；固定输入和软件版本，比较耗时、显存与计算结果。

## 通用性能调优

### MPI Rank 映射

> 先用[当前 sbatch 脚本模板](https://vcnn7siwx4yx.feishu.cn/wiki/ZmkawnhNZicpxAkuwh4cNSWGnpc#AxIvdck6toE2UHxaa5bc2oTqnPf)运行；需要调整时，再检查 MPI Rank、CPU 核与 GPU 的对应关系。
>
> 分区映射脚本位于 `/opt/sai/runtime/mps_mapping.d`；旧路径 `/opt/sai_config/mps_mapping.d`目前是兼容链接。

> 下面是 Open MPI 的映射示例。不同 MPI 实现、Slurm 分配范围和节点拓扑会影响实际绑定；先查看当前任务的绑定结果。

#### 什么是 MPI Rank 映射？为什么需要它？

用 `mpirun -np 16` 启动 16 个 MPI 进程时，映射和绑定由 MPI 实现、启动参数及 Slurm 分配共同决定。默认配置可能已做绑定；需要关注的是这些进程、内存与 GPU 是否匹配当前节点拓扑。

Open MPI 的 `--map-by` 控制 Rank 如何分布在节点、NUMA 或缓存域等资源上；`--bind-to` 控制进程绑定。可用 `--report-bindings` 检查结果。它们不会单独替你完成应用内的 GPU 分配。

#### 历史示例：16V100 分区的 5995WX 节点

##### 🤔 单节点硬件拓扑结构简析

![这张图展示的是V100 X16 SuperNode的Block Diagram，对应文档中16张V100显卡的AMD Threadripper PRO 5995WX节点硬件拓扑结构示例。图中显示节点包含4个5995WX核心组成的NUMA域，各NUMA域通过对应PLX桥接芯片连接4张V100显卡；此外节点还有256GB的20GB/s速率内存，以及4个64GB DDR4内存区域，每个区域对应一个8-Core L3Cache的NUMA域，整体呈现出文档提到的“每个NUMA域连接4张GPU”的亲和性设计，用于MPI Rank映射时的硬件拓扑参考。](assets/ae6d386a529f915ebd0ef075800b1fc2c04ca344538bdb4ddc0a1f7072d26bb8.png)

> 本例使用 AMD Threadripper PRO 5995WX（64 核 / 128 线程）、8 个 L3 Cache 域、4 个 NUMA 域与 16 张 V100。例图按每个 NUMA 域连接 4 张 GPU 说明亲和性。
>
> 实际 NUMA 划分、设备编号和作业可用 CPU 以分配到的节点为准，可在作业内用 `lscpu` 和 `nvidia-smi topo -m` 检查。

##### 💪 实战命令解析：`mpirun -np 16 -map-by ppr:2:l3cache:pe=4`

`-np 16`：启动 16 个 MPI 进程（Rank 0~15）

`-map-by ppr:2:l3cache:pe=4`：

这是核心！含义是：

> `ppr:2:l3cache`：每个 L3 Cache 域放置 2 个 Rank。\
> `pe=4`：每个 Rank 使用 4 个处理单元；Open MPI 默认按核计数，启用硬件线程选项时含义会改变。

📌 翻译成**人话**：

> 在每个 L3 Cache 域（共 8 个）里放 2 个 MPI Rank，每个 Rank 独占 4 个 CPU 核心

📊 资源占用计算：

- 8 个 L3 Cache × 2 Ranks = 16 Ranks ✔️
- 每 Rank 占 4 核心 → 总共 16×4 = 64 核心 ✔️（正好用满 CPU）
- 每个 L3 Cache 域有 8 核 → 2 Ranks × 4 核 = 8 核 ✔️（完美填满）

本例让同一 Rank 的 4 个核心位于同一 L3 Cache 域。缓存容量仍由该域内的核心共享；CPU 绑定并不为 Rank 独占一半缓存。

这个例子使用 64 个物理核心。改完后加 `--report-bindings` 看一眼：每个 Rank 是否绑到了预期的核心，OpenMP 线程数是否与之配套。

##### 🔄 OpenMP 设置详解（两种模式）

如果应用支持 MPI + OpenMP 混合并行，还需让每个 Rank 的线程数与其可用 CPU 匹配。纯 MPI 应用无需照搬这些线程设置。

###### 🚫 不使用 SMT（同步多线程）

    export OMP_NUM_THREADS=4
    export OMP_PLACES=cores
    export OMP_PROC_BIND=close

每个 Rank 启动 4 个 OpenMP 线程，绑定到 4 个物理核心（`OMP_PLACES=cores`），并且线程尽量“靠近”主进程（`OMP_PROC_BIND=close`），提高缓存命中率。

###### ✅ 使用 SMT

    export OMP_NUM_THREADS=8

只有作业获配了这 4 个物理核心的全部 8 个逻辑线程，且绑定允许使用它们时，才可测试 `OMP_NUM_THREADS=8`。仅修改线程数不会自动获得额外 CPU。

> ⚠️ 注意：SMT 可能带来性能提升（如果程序访存密集、计算轻），也可能因资源竞争降低性能（计算密集型）。需实测！

##### 🎯 性能调优原则总结

> - 减少跨 NUMA 内存访问
> - 减少跨 L3 Cache 通信
> - 避免核心争抢
> - 提高缓存命中率
> - 最小化 GPU-CPU 通信延迟

##### 🧪 应用场景举例

你正在跑一个 16-GPU 的深度学习训练或分子动力学模拟，启动了16个 Rank ，每个 GPU 负责一部分数据，MPI 负责 Rank 间通信，OpenMP 负责每个 Rank 内部并行。

###### 绑定不匹配时可能出现的问题

- Rank 0 跑在 NUMA 0，但它的数据在 GPU 4（挂在 NUMA 1）→ 每次拷贝数据都要跨 NUMA！
- Rank 7 和 Rank 8 共享一个核心 → 上下文切换频繁，缓存失效
- Rank 4 的 8 个 OpenMP 线程分布在 2 个 L3 Cache 域中 → 数据频繁跨 L3 Cache 域读写，延迟开销大
- 先记录这些情况对应的实际耗时，作为调整前的基线。

###### 调整后需要核对的结果

- 按节点拓扑，将 Rank 分配到其所用 GPU 附近的 CPU 核心。
- 每个 Rank 的 OpenMP 线程限定在分配给它的核心内，避免与其他 Rank 争用同一核心。
- 检查内存放置是否与计算线程所在 NUMA 域匹配，减少远端访存。
- 检查 CPU–GPU 亲和性是否改善，并用应用耗时确认效果。

每次只改一类参数，用同一输入比较耗时和结果，才能知道是哪项调整起了作用。

------------------------------------------------------------------------

### CUDA-MPS

> 一个 Rank 喂不满 GPU 时，可以试试 MPS，让多个 Rank 的 CUDA 工作在同一块 GPU 上并发执行。下面几类任务值得试，最后用总耗时判断有没有收益。

> V100（Volta）及后续架构上的 MPS 客户端各自保留独立的 GPU 地址空间，并直接向 GPU 提交工作。机制详见 [NVIDIA MPS 架构说明](https://docs.nvidia.com/deploy/mps/architecture.html)。

> 在支持 MPS 的模板里，照常填写 `--nodes`、`--ntasks` 和 `--gpus-per-node`：总 Rank 数 ÷ 总 GPU 数，就是每卡 Rank 数，模板会处理对应的 MPS 配置。

以下是CUDA-MPS在具体应用场景中的用途：

- **CP2K：**MPS 可用来试配“平方数个 MPI Rank”，让进程数与应用的并行划分更合适。
- **QE：**多 K 点小体系值得试 MPS，配合 `-nk` 分配 K 点并行。
- **DP-LMP：**按原有调优经验，每卡显存占到约 1 GB 以上时，值得试试 MPS：更多 Rank 可能缩短邻居表构建时间。小任务常常得不偿失，MPI 通信会吃掉收益。对比日志里的 Neigh、Comm 和总耗时，就能看出瓶颈有没有转移。
- **VASP：**涉及 NCCL 通信的配置按每个 GPU 一个 MPI Rank 使用，不能直接套用每卡多个 Rank 的 MPS 配置。单卡、多 K 点小体系可在应用构建支持时测试 MPS 与 `KPAR`；先用小算例确认正确性和耗时。

------------------------------------------------------------------------

### 多卡、多节点通信调优

> 多节点任务先用当前应用模板验证正确运行，再逐步增加节点数，对比总耗时与卡时消耗。

UCX/NCCL 的站点配置位于 `/opt/sai/runtime/ib_map.d`（旧路径 `/opt/sai_config/ib_map.d`目前是兼容链接）。优先沿用应用模块与当前模板的设置；具体任务需要调整时，以实际拓扑和测量结果为依据。

------------------------------------------------------------------------

## 常见软件性能调优

### VASP

> GPU 版 VASP 优先关注 `NSIM` 和 `KPAR`。CPU 版常用的 `NPAR`/`NCORE` 设置不要直接照搬；具体支持情况以所用 VASP 构建为准。以下参数是试跑起点。

#### **`NSIM`**

- 较大体系可从 `NSIM=32` 或 `64` 开始测试，比较耗时与显存占用。
- 对于较小体系，一般用16、8或默认的4即可
- 更大的`NSIM`会占用更多的VRAM，若GPU显存不足（OOM），可酌情增加GPU数量或调小`NSIM`

#### **`KPAR`**

📌设置`KPAR`的基本原则是**使每个K点的计算所跨的GPU尽可能少**

- 在每个 GPU 使用一个 MPI Rank 的常见配置下，可先测试 GPU 数与实际 K 点数（以 `IBZKPT` 为准）的最大公因数作为 `KPAR`。这是负载均衡的起点，并非必须整除 K 点数的规则。
- GPU 数量也是可调的。例如 7 个 K 点，可试 7 张 GPU、`KPAR=7`：主站可用 `8V100V0` 分区、`improper-gpu`、1 个节点、每节点 7 张 GPU 和 7 个 MPI Rank。下面两个反例也说明，K 点分组仍要看具体体系。
- 上述只是“理想情况”，实际会有很多例外
  - 例如YZrO-88-2kp体系：原子数较少且只有2个K点，经有限测试发现固定`KPAR=2`最佳，包括只使用单块GPU时
  - 例如Ni-HAB-59kp体系：有59个K点，而59是大质数，很难申请这个数量的GPU；同时，这种K点数特别大的体系往往原子数较少，本身不适合大规模并行；另一方面，如果按照“最大公因数”原则，`KPAR`只能为1，但这显然不合适。对于这种情况，可以申请4个GPU并设置`KPAR=4`

------------------------------------------------------------------------

### LAMMPS

http://bbs.keinsci.com/thread-40313-1-1.html

固定输入、力场和步数，比较不同 MPI 进程数与 GPU 数下的总耗时。查看日志中的 Pair、Neigh 和 Comm 用时，定位计算、邻居表或通信开销；先确认结果一致。参数说明见 [LAMMPS 性能指南](https://docs.lammps.org/Speed.html)。

------------------------------------------------------------------------

### DeePMD-kit

先区分模型训练和分子动力学模拟。比较性能时保持模型、后端、数值精度与输入一致；增加 GPU 后同时检查耗时和显存占用。SAI 的具体环境用法见 [软件环境](../f1d4bd8bb10f1064716136f5/index.md)，参数解释见 [DeePMD-kit 文档](https://docs.deepmodeling.com/projects/deepmd/en/latest/)。

------------------------------------------------------------------------

## 💡FAQ
