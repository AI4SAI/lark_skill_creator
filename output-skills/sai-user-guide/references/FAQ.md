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