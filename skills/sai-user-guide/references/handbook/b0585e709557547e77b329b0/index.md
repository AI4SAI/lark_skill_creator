# FAQ

## 提问前先准备

> 请提供任务 ID、完整报错和相关脚本片段。当前任务用 `sai jobs local --format table` 查看，历史任务用 `sacct -X -j <任务ID>` 查看。无论向用户群还是 AI 助手求助，都不要发送密码、私钥或令牌。

## 常见问题 (持续更新)

### 登录相关

#### Q: 首次登录修改密码失败，提示“Old password not accepted”，如图：

![图片展示的是首次登录修改密码失败时的提示界面。界面上方显示登录用户为“yehuang”，下方提示“Keyboard-interactive authentication prompts from server:”，接着出现“Password:”等输入框，提示“Password expired. Change your password now.”，并要求输入“Current Password:”，还显示“Password change failed. Server message: Old password not accepted.”，最后提示“Access denied”。该图片与文档中“首次登录修改密码失败，提示‘Old password not accepted’”的问题对应，直观呈现了提示内容。](assets/179b0b90ad5445a005d5319fb8586d0ca1de02e0dbdaefec04dab3651dce650a.jpeg)

> **A：**`Current Password` 要填当前密码；首次登录且尚未修改时，就是收到的初始密码。按提示完成当前密码、新密码和确认密码的输入；若本次失败，重新连接后再试。

------------------------------------------------------------------------

#### Q: 多次登录没有成功，之后就连不上了，这是为何？

> **A：**连续认证失败可能触发临时限制。请先停止反复重试，核对[登录超算](../891ee584b71ab6f7b0d6d62d/index.md)中的地址、端口和凭据配置，稍后再试。仍无法连接时，向管理员提供时间、客户端出口 IP 和报错。

#### Q: 网页能登录，为什么 SSH 还连不上？

> **A：**网页使用 SAI 账号登录；SSH 还需要该计算站点已开通，以及正确的 Linux 用户名和站点支持的登录凭据。先到控制台查看站点状态，再核对登录信息。

#### Q: 默认身份选了组织，在个人 Home 提交任务会记到哪里？

> **A：**没有通过命令、脚本或环境变量指定账户时，个人 Home 下的任务通常记到个人账户。作业工作目录的优先级高于默认身份；提交前查看账户设置和实际工作目录。

------------------------------------------------------------------------

### 硬件资源相关

#### Q: 4V100分区和4V100PX分区有什么区别？

> **A：**一般先选 `4V100`，它的单卡显存更大，GPU 间也有 NVLink，适用范围更广。若 16 GB 显存够用，又主要跑单卡或通信较少的任务，再考虑 `4V100PX`；规格见[SAI硬件资源](../7d583b3babea8f243329f3c7/index.md)。
>
> 例如中小体系 DPMD、VASP NEB、CP2K 和部分 ABACUS 配置，不一定能充分利用更高的卡间带宽。这时用自己的代表算例比较完成时间和费用，比单看硬件规格更有用。

#### Q: 有 4 张空闲 GPU，为什么我的 4 卡任务还在排队？

> **A：**先看这 4 张卡是否在同一个符合要求的节点上，再看 CPU、内存、账户额度和 QOS。分散在不同节点的空卡，未必能满足一个单节点 4 卡任务。

#### Q: CPU-only 任务免费吗？

> **A：**按所申请资源和占用时间计费，CPU 和内存的申请量都可能影响费用。提交前查看控制台价格和资源要求。

#### Q: 4 张 32 GB 显卡有 NVLink，就能当一张 128 GB 显卡用吗？

> **A：**每张卡仍有自己的 32 GB 显存。NVLink 加快卡间通信；要利用多卡总显存，软件还需要支持相应的并行或分片方式。

#### Q: 多申请几张 GPU，一定更快、更省钱吗？

> **A：**看程序和算例的并行效率。先用同一个代表算例比较完成时间和总费用；加卡后的加速不足以抵消资源增加时，反而更贵。

------------------------------------------------------------------------

### 提交任务相关

#### Q: “error：QOSMinGRES”是什么报错？

![图片展示的是一个命令行界面，用户在登录节点上执行\`sbatch -p gpu_cp2k.sbatch\`命令。命令执行后，出现“error: QOSMinGRES”报错，提示“Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)”。该图片与文档中关于“error：QOSMinGRES”报错的解释相关，直观呈现了报错时的命令执行情况及报错信息，帮助用户理解报错原因。](assets/6859ce68fbfdf2ac72545ae8a5a3d128ffab2072efe3d169e146a30fdcc400a2.png)

> **A：**申请的 GPU 数低于所选 QOS 的最低要求。先对照脚本中的 GPU 数和 QOS，再查[快速开始的 QOS 规则](../10e455cfa1c14a90040e58a5/index.md)。以下图片是历史报错示意。
>
> ![图片展示的是一个系统提示信息，其中关键内容被红色框突出显示。提示信息指出，不满足\[GPUsPerNode=4N(N\>0)\]条件的任务，对某些QOS来说是不允许的，若要使用不正确的GPU数量，请选择专门的QOS和分区。该图片与上文“下面这些任务的排队原因是什么？”的问题相关，是对其中“排队原因1：AssocGrpGRES”中任务排队原因的说明，即因不满足GPU数量条件而被某些QOS拒绝。](assets/5febd4b4bb314d8667f32c701133ff31191d60eafb669882fc91bf8506a8d1af.png)
>
> 申请 1 或 2 卡时，可选择该分区允许的 `improper-gpu`、`rush-1o2gpu` 或 `flood-1o2gpu`。用 `scontrol show partition <分区名>` 核对 `AllowQos`；只改 QOS 名称仍需满足时限和额度要求。
>
> ![图片展示了一段Bash脚本代码，其中关键部分是用红色框突出显示的\`#SBATCH --qos=improper-gpu\`指令。该指令用于指定任务的优先级，其优先级顺序为\`rush-4gpu = rush-8gpu \> improper-gpu \> huge-gpu\`。此脚本代码与文档中关于提交任务相关的内容相关，用于说明在申请1或2卡时，可选择分区允许的\`improper-gpu\`等QoS名称，以及核对\`AllowQos\`时只改QOS名称仍需满足时限和额度要求。](assets/b630890e6ed20e097bfed8292661bcef38c0144da2ab1375ae9477978ee55c27.png)

------------------------------------------------------------------------

#### **Q:下面这些任务的排队原因是什么？**

排队原因1：`AssocGrpGRES`

![图片展示的是\`testuser01\`在\`login-01\`登录节点下的\`squeue\`命令输出结果。表格中列出了job ID、Priority、Name、User、Submit/Start at、ST、Run/Wait、Partition、QOS、Nodes、Slots、GPU、MemPerU、array_ID、Reason/Modelist等信息。其中，job ID为3142的记录显示其处于运行状态（R），Partition为AV100，QOS为improper-gpu 1，GPU数量为32，Slots为32，MemPerU为23000M，Reason/Modelist为\`AssocGrpGRES\`。该图片与上文排队原因1相关，直观呈现了因账户同时使用GPU额度达到总额度而排队的情况。](assets/0b1a671fb05bc1e282410f1d1bbba1cd5da6abd3b1b7f997421fc9e134536bab.png)

这个账户同时使用的 GPU 已经达到总额度，需等已有任务结束，或联系管理员增加额度。用 `sai account local --format table` 查看自己的账户关联；图中 64 卡是当时这个账户的额度。

排队原因2：`QOSMaxGRESPerUser`

![图片展示的是\`qqueue\`命令的输出结果，用于查看队列信息。其中，job-ID为3139、3140、3141的三条记录中，job-ID为3141的记录状态为PD，对应QOS为rush - 4gpu，节点数、槽位数、GPU数均为1，MemPerU为23000M，array_ID为空，Reason/NodeList显示为“QOSMaxGRESPerUser”。该图片与上下文关于排队原因的说明相关，直观呈现了达到每用户上限时的队列信息。](assets/9fe69c41e42c4d967146dcddb9b0a03bf5c16abccbc4fe6e2c268a55e5bc7f07.png)

你在所选 QOS 下同时使用的 GPU 达到每用户上限了。用 `job` 看正在运行的任务，再对照[快速开始](../10e455cfa1c14a90040e58a5/index.md)的 QOS 表；当前提交用表中的名称。

------------------------------------------------------------------------

#### **Q:为什么我的任务CANCELLED by 0？**

`CANCELLED by 0` 表示由 root 身份执行了取消。先看任务输出中的站点检查提示，再运行下面的命令查记录：

``` bash
sacct -X -j JOB_ID -o JobID,State%30,Reason,ExitCode
```

如果看不出原因，把任务 ID、发生时间和报错交给管理员。资源检查、系统保护和管理员操作都可能触发这种取消。

#### Q: 任务 suspend（暂停）后还会计费吗？

> **A：**会。suspend 只是暂停程序，内存等资源仍被占用，暂停期间正常计费。要结束这次计算并释放资源，请用 scancel JOB_ID，随后确认任务已结束。

#### Q: GPU 利用率为 0，还会计费吗？

> **A：**会。计算费用按任务占用的资源和时间计算。读文件、等待通信或程序卡住时，资源仍可能被占用；请查日志和监控，及时取消不再需要的任务。

#### Q: 排队、hold 和 suspend 的费用一样吗？

> **A：**普通按量任务在首次启动前排队，尚未占用计算资源，这段时间不收计算费；hold 是让未启动的任务暂缓调度。suspend 是暂停已运行的任务，仍保留资源，正常计费。预约资源、订阅等另按订单约定。

#### Q: 关闭 SSH 或 Pilot 网页，任务就结束了吗？

> **A：**已提交的 sbatch 任务会继续，资源占用期间照常计费。交互式 srun 则可能随终端断开而结束，使用 tmux 时还可能继续。以任务状态为准；要结束计算，请取消对应任务。

#### Q: 程序报错、计算失败，已经花的费用怎么算？

> **A：**已占用资源的时间仍计费。主程序退出后，脚本里的等待或后续命令还可能使任务继续占用资源。发现错误后查任务状态，及时结束无用的计算。

#### Q: scancel 执行完，就已经停止计费了吗？

> **A：**先确认任务已经结束并释放资源。取消请求发出后可能还有清理过程；如果长时间停在 COMPLETING 或仍占着节点，把任务 ID 和时间交给管理员。

#### Q: 想过几天再继续算，可以一直 suspend 吗？

> **A：**暂停期间仍正常计费。需要长期停下来时，先按软件支持的方式保存检查点，再结束任务；之后从检查点重新提交。

#### Q: 切换默认身份后，之前提交的任务也会换账户吗？

> **A：**已提交任务保留原来的账户。新任务先用命令、脚本或环境变量指定的账户，其次按工作目录推定，最后用本站已生效的默认账户；排队任务若需更正账户，应单独修改并核对。

#### Q: 余额不足，任务会自动停止吗？

> **A：**是否自动取消取决于站点规则。任务仍在运行或暂停时，资源占用继续计费。收到欠费提醒后，请及时补足资金；需要停止计算时，请取消对应任务并确认已结束。

#### Q: 通知说任务会被取消，到了时间却还在运行或暂停，怎么办？

> **A：**请保留任务编号和通知，联系管理员核查实际停止时间及费用。需要立即停止计算时，用 scancel JOB_ID 取消，并确认任务已结束。

### 软件环境相关

#### Q: 如何在SAI上使用Perl脚本？运行Perl脚本提示有模块未安装

> A: Perl模块可以通过CPAN安装在自己的home目录中，例如`cpan Fortran::Format`。第一次运行`cpan`会执行初始化，一直回复`yes`即可。

> cpan初始化完成后会向`~/.bashrc`写入环境，强烈建议保持`~/.bashrc`干净，将环境配置写入独立的`.env`文件，按需`source`使用，Conda同理

#### Q: 任务已经 RUNNING，为什么 GPU 还没开始算？

> **A：**程序可能正在读数据、初始化或做 CPU 计算，也可能环境有错或卡住。先看输出日志和 GPU 监控；任务开始占用资源就会计费，发现异常要及时处理。

#### Q: 把 Conda 和各种软件环境都写进 .bashrc，会更方便吗？

> **A：**容易让不同软件的库和命令互相干扰。把环境放进独立脚本，或在作业脚本里按需加载，更容易复现和排错。

### 费用与资金相关

- [页面上的运行中费用没变化，就说明没有继续计费吗？](https://vcnn7siwx4yx.feishu.cn/wiki/LJo9wzMv7ipb5ckeKfEceDEPn4d#doxcnrO9zkVwM7mAzDAGLS8KFGf)
- [还有 SAI Credit，为什么也会扣现金？](https://vcnn7siwx4yx.feishu.cn/wiki/LJo9wzMv7ipb5ckeKfEceDEPn4d#doxcn7TZC7w7FBVN0IO6qUKNycd)
- [组织还有钱，为什么我的任务提示余额不足？](https://vcnn7siwx4yx.feishu.cn/wiki/LJo9wzMv7ipb5ckeKfEceDEPn4d#doxcn0I9LA1uzcs3MN9zG0PS5kd)

### 存储空间相关

- [容量还没用满，为什么提示 quota exceeded？](https://vcnn7siwx4yx.feishu.cn/wiki/CYWxwrFPuin9AIk27W7c18ADnSf#doxcnKrvoIoML762hyeVNemT0Mc)
- [组织总额度还有剩余，为什么某个目录写不进去？](https://vcnn7siwx4yx.feishu.cn/wiki/CYWxwrFPuin9AIk27W7c18ADnSf#doxcnhomX2qylpQrgZ0FBLDpGwb)
- [把文件存到计算节点本地缓存，任务结束后会自动保存吗？](https://vcnn7siwx4yx.feishu.cn/wiki/CYWxwrFPuin9AIk27W7c18ADnSf#doxcndNysAVgMcfFqylGq8cuv1f)

### 团队协作相关

- [加入组织，就能访问所有项目和共享文件夹吗？](https://vcnn7siwx4yx.feishu.cn/wiki/DxGewwDXgighARk7OWHcAzLqn6f#doxcnknw4iFFRlhzhaPCagqaI8f)
- [组织资助我的 Home 扩容，组里的人就能看我的文件吗？](https://vcnn7siwx4yx.feishu.cn/wiki/DxGewwDXgighARk7OWHcAzLqn6f#doxcnWDXdn1lDLBYWpOxuKFCITg)
- [有文件编辑权限，就能用这个项目的算力吗？](https://vcnn7siwx4yx.feishu.cn/wiki/DxGewwDXgighARk7OWHcAzLqn6f#doxcnryUp3PZcjCy7pFh1CVoc5k)
- [组织升级套餐后，独立项目也会一起升级吗？](https://vcnn7siwx4yx.feishu.cn/wiki/DxGewwDXgighARk7OWHcAzLqn6f#doxcn3gJ29abXXDfT4GyNII7P3e)
