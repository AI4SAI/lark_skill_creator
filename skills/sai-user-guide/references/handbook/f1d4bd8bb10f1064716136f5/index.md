# 软件环境

## 环境管理

### Environment-Modules

`module` 用来查看和加载 SAI 预装软件，简写是 `ml`。把版本写进作业脚本，下次复现就不用猜当时加载了什么。

下面的“软件名/版本”需替换为 `module avail` 中实际存在的条目。

``` bash
module avail                 # 查看可用软件与版本
module show 软件名/版本       # 查看该模块的环境设置
module load 软件名/版本       # 加载所需版本
module list                  # 确认已加载的模块
module unload 软件名/版本     # 用完后卸载
module purge                 # 卸载所有已加载模块
```

`module purge` 只处理 Modules 管理的环境；已激活的 Conda 环境需另行 `conda deactivate`。

### Conda

单机用户熟悉的环境管理方案，主要用于与Python有关的环境管理

> **不要在** **`~/.bashrc`** **里自动加载计算环境！** Conda 的库一旦盖过 MPI、CUDA，报错往往很难追。把环境写进作业脚本，或放在独立的 `.env` 文件里按需 `source`。
>
> SAI 预装 Anaconda3 可通过 `AC` 加载。使用 `conda create -n 环境名 python=版本号` 创建自己的环境，再用 `conda activate 环境名` 激活。
>
> 个人安装的 Conda 可将加载步骤放入自己的 `.env` 脚本，使用时再 `source`。

![这张图片展示了Linux系统下\`.bashrc\`文件的部分内容，该文件位于第121至135行，其中第127行的位置标注有醒目的红色“× 错误”标识。这段代码包含了与Conda环境初始化相关的配置逻辑，通过判断命令执行结果的返回值，来加载对应路径的Conda脚本。该图片对应的是软件环境模块下的环境管理内容，涉及个人Conda配置相关的Shell脚本，直观呈现了用户在配置Conda初始化脚本时出现的错误标记。](assets/c94dd131364e6f3ec34834de3edb9e9663387d5374eaf939bd94c70369c99888.png)

下载 Python 包较慢时，可按所用镜像站的说明配置 Conda 或 pip 源；安装失败时先检查包和版本是否在该源中可用。

### `source`命令

`source` 在当前 Shell 中执行环境脚本，使其中的环境变量立即生效。只加载你信任的脚本；下例的路径需替换为实际文件。

``` bash
source /实际路径/软件.env
```

用 `bash 软件.env` 启动的子进程通常不会把环境变量传回当前 Shell。批量任务所需的 `source` 也应写进提交脚本。

### ✨Apptainer容器

SAI 提供 [Apptainer](https://apptainer.org) 容器（前身为 [Singularity](https://sylabs.io)），可将软件及依赖封装为镜像，减少环境迁移时的配置工作。GPU 和跨节点 MPI 应用仍需匹配站点驱动与通信环境。

用 `module avail apptainer` 查看当前可用版本，再加载需要的版本。[Fakeroot](https://apptainer.org/docs/user/latest/fakeroot.html) 的可用模式受站点配置限制；容器中的 root 身份不等于宿主机管理员权限。

若用户不了解如何在无root权限的超算环境中安装软件，通过Apptainer使用Fakeroot是一个可尝试的选项。

请优先加载 SAI 提供的 Apptainer。用户命名空间等能力受站点安全策略控制，自行安装其他版本后可能无法直接使用。

🔥允许用户在SAI上构建自定义容器镜像。

以下是强烈推荐SAI的典型用户阅读的Apptainer用户手册内容：

- [快速开始](https://apptainer.org/docs/user/latest/quick_start.html)
- [安全性简介](https://apptainer.org/docs/user/latest/security.html)
- [MPI与跨节点应用](https://apptainer.org/docs/user/latest/mpi.html)
- [GPU支持](https://apptainer.org/docs/user/latest/gpu.html)
- [定义文件（构建自定义容器镜像）](https://apptainer.org/docs/user/latest/definition_files.html)

------------------------------------------------------------------------

## 软件运行模板

### sbatch 脚本模板列表

模板位于 `/opt/sbatch_examples`，下表便于按软件查找。复制需要的脚本到工作目录，先改分区、节点数、GPU 数和 QOS，再提交；模块与版本直接看脚本中的 `module load`。

| 模板名称 | 软件 | 默认软件版本 | 并行能力 | 默认并行设置 |
|----|----|----|----|----|
| cpu_serial-dataproc.sbatch | 通用，使用CPU节点进行数据处理 | \- | 用户自定义 | 2核4线程 |
| gpu_abacus.sbatch | GPU加速ABACUS | LTS-3.10.1 | 单卡/多卡/多节点 | 1节点 \* 4卡 |
| gpu_cp2k.sbatch | GPU加速CP2K | 2025.1 | 单卡/多卡/多节点 | 8节点 \* 4卡 |
| gpu_qe.sbatch | GPU加速Quantum ESPRESSO | 7.3 | 单卡/多卡/多节点 | 1节点 \* 4卡 |
| gpu_vasp.sbatch | GPU加速VASP | 6.4.2 | 单卡/多卡/多节点 | 4节点 \* 4卡 |
| gpu_lmp.sbatch | GPU加速LAMMPS (默认Kokkos) | 29Aug2024 | 单卡/多卡/多节点 | 4节点 \* 4卡 |
| gpu_lmp-dp.sbatch | GPU加速LAMMPS-DeePMD | 29Aug2024-3.0.3 | 单卡/多卡/多节点 | 4节点 \* 4卡 |
| gpu_dptrain-multigpu-tf.sbatch | GPU加速DeePMD训练 (默认单精度，TensorFlow后端) | 3.1.2 | 单卡/多卡/多节点 | 1节点 \* 4卡 |
| gpu_dptrain-multigpu-pt.sbatch | GPU加速DeePMD训练 (默认单精度，PyTorch后端) | 3.1.2 | 单卡/多卡/多节点 | 1节点 \* 4卡 |
| gpu_dptrain-singlegpu.sbatch | GPU加速DeePMD训练 (默认单精度) | 3.1.2 | 单卡 | \- |
| gpu_gmx-mpi.sbatch | GPU加速GROMACS (支持PME分解) | 2025.4 | 多卡/多节点 | 4节点 \* 4卡 |
| gpu_gmx-multigpu-singlenode-tmpi.sbatch | GPU加速GROMACS (tMPI) | 2024.6 | 单卡/多卡 | 1节点 \* 4卡 |
| gpu_gmx-singlegpu.sbatch | GPU加速GROMACS | 2024.6 | 单卡 | \- |
| gpu_generic-nompi-mutigpu.sbatch | 通用，GPU加速，无MPI多卡并行，适用于GPUMD等软件 | \- | 单卡/多卡 | 1节点 \* 4卡 |
| gpu_generic-singlegpu.sbatch | 通用，GPU加速，单卡脚本 | \- | 单卡 | \- |
| af3_st1_msa.sbatch | AlphaFold3 MSA计算，CPU-only | 3.0.1 | 用户自定义 | 4核8线程 |
| af3_st2_infer.sbatch | AlphaFold3 序列推理，GPU加速 | 3.0.1 | 单卡 | \- |

### 其他模板列表

| 模板名称 | 解释 |
|----|----|
| gpu_1gpu-dpgen-machine.json | 单卡DPGEN任务的`machine.json`模板，关键在于`command`和`resources`字段 |
| gpu_4gpu-dpgen-machine.json | 4卡DPGEN任务的`machine.json`模板，关键在于`command`和`resources`字段 |

------------------------------------------------------------------------

## 软件编译和安装 (进阶用户)

### ✨SAI预置的编译环境

编译前先用 `module avail` 查看编译器、CUDA 和 MPI 模块，用 `module show 模块名/版本` 检查依赖。将选定的版本及编译选项记入构建脚本，运行时使用与构建相匹配的环境。

### MPI编译器和库的选择

> 优先沿用 SAI 模板中的 MPI 和启动方式，它们已与站点环境配套。自行更换 MPI 时，先用一个小任务检查 CPU/GPU 绑定和跨节点通信。

不要混用不同 MPI 安装中的编译器包装命令、动态库和启动器。例如，`mpicc`/`mpifort` 与 `mpirun` 应来自同一套选定的环境。更换环境后先用小任务检查结果和资源绑定，再扩大规模。

### 安装位置及其目录结构

`/home/public` SAI公共资源，如教程文件、安装包仓库等

组内软件放在组织共享目录，课题专用软件放在对应项目目录，方便同组复用。路径可从控制台查看。

`/opt/apps` 应用软件安装位置

`/opt/devtools` 开发工具安装位置

`/opt/modules/modulefiles/apps` 应用软件的module文件位置

`/opt/modules/modulefiles/devtools` 开发工具的module文件位置

`/opt/envs` 通过Bash直接管理的软件的环境脚本（`.env`，通过`source`命令调用）

`/opt/custom` 用于部分站点的自定义软件；是否部署及如何同步，由所在站点配置决定。

------------------------------------------------------------------------

## 💡FAQ

#### Q: 如何在SAI上使用Perl脚本？运行Perl脚本提示有模块未安装

> A: Perl模块可以通过CPAN安装在自己的home目录中，例如`cpan Fortran::Format`。第一次运行`cpan`会执行初始化，一直回复`yes`即可。

> cpan初始化完成后会向`~/.bashrc`写入环境，强烈建议保持`~/.bashrc`干净，将环境配置写入独立的`.env`文件，按需`source`使用，Conda同理

#### Q: 任务已经 RUNNING，为什么 GPU 还没开始算？

> **A：**程序可能正在读数据、初始化或做 CPU 计算，也可能环境有错或卡住。先看输出日志和 GPU 监控；任务开始占用资源就会计费，发现异常要及时处理。

#### Q: 把 Conda 和各种软件环境都写进 .bashrc，会更方便吗？

> **A：**容易让不同软件的库和命令互相干扰。把环境放进独立脚本，或在作业脚本里按需加载，更容易复现和排错。
