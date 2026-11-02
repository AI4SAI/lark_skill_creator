# SAI硬件资源

## GPU计算节点

- GPU 分区用于科学计算、分子模拟以及 AI for Science 训练和推理；可用规模取决于当前资源、账号权限和排队情况。
- 基于创新的硬件架构优化以及从硬件到软件的协同优化，实现高效的超大规模跨尺度高精度分子模拟和面向AI for Science的大规模训练和推理
- SAI 针对硬件和应用做了协同调优。选卡时重点比较自己的代表算例：相同输入、软件版本与精度下，哪种配置完成得快、花费低。

> **历史记录（2026 年 7 月中旬）：**当时已上线 1664 块 GPU，其中包含 268 块改进型 V100-SXM2-32GB、1360 块改进型 V100-SXM2-16GB、20 块改进型 A100-SXM2-32GB、8 块改进型 A100-SXM4-40GB 和 8 块改进型 A100-SXM4-80GB。
>
> 当时提出的“2026 年下半年约 5000 块 GPU”是建设规划，不能作为已上线数量。
>
> 下表保留硬件规格与建设记录。**规格、已上线数量、实时空闲是三回事**；提交前用 `sinfo` 查看当前分区和节点状态，空闲也不代表当前账号一定可申请。

<table>
<thead>
<tr>
<th><p><strong>分区</strong></p></th>
<th><p><strong>GPU数量</strong></p></th>
<th><p><strong>每节点</strong><br />
<strong>GPU配置</strong></p></th>
<th><p><strong>每节点CPU配置</strong></p></th>
<th><p><strong>每节点</strong><br />
<strong>内存配置</strong></p></th>
<th><p><strong>节点间</strong><br />
<strong>互联配置</strong></p></th>
<th><p><strong>节点内</strong><br />
<strong>互联配置</strong></p></th>
<th><p><strong>上线状态</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>4V100</strong><br />
<span>SlimPOD</span><br />
<span>144超节点</span></p></td>
<td><p>144 + 12</p></td>
<td><p>4*<span>改进型</span>V100-SXM2-32GB</p></td>
<td><p>AMD Ryzen <span>9950X3D</span> 16C32T 5.75GHz <span>260W OC</span></p></td>
<td><p>96GB <span>DDR5-6400</span><br />
<span>时序优化</span></p></td>
<td><p><span>2*100G</span> IB + 25G RoCE</p></td>
<td><p><span>NVLink 300GBps</span></p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p><strong>4V100PX</strong></p></td>
<td><p>16</p></td>
<td><p>4*<span>改进型</span>V100-SXM2-16GB</p></td>
<td><p>AMD Ryzen <span>9950X3D</span> 16C32T 5.75GHz <span>260W OC</span></p></td>
<td><p>96GB <span>DDR5-6400</span><br />
<span>时序优化</span></p></td>
<td><p><span>2*100G</span> IB + 25G RoCE</p></td>
<td><p><span>PCIe 4.0</span> x16</p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p><strong>16V100</strong><br />
<span>UltraPOD</span><br />
<span>1344超节点</span></p></td>
<td><p>1344</p></td>
<td><p>16*<span>改进型</span>V100-SXM2-16GB</p></td>
<td><p>AMD Threadripper Pro <span>5995WX</span> 64C128T 4.5GHz 280W</p></td>
<td><p>256GB DDR4-3200</p></td>
<td><p><span>9*100G</span> IB + 25G RoCE</p></td>
<td><p><span>NVLink 300GBps</span></p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p><strong>8V100V0</strong></p></td>
<td><p>112</p></td>
<td><p>8*<span>改进型</span>V100-SXM2-32GB</p></td>
<td><p>2*Intel Xeon Gold 6146 12C24T 4.2GHz 165W</p></td>
<td><p>384GB DDR4-2666</p></td>
<td><p><span>4*100G</span> IB + 25G RoCE</p></td>
<td><p><span>NVLink 300GBps</span></p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p><strong>4A100PX</strong></p></td>
<td><p>64（含规划）</p></td>
<td><p>4*<span>改进型</span>A100-SXM2-32GB</p></td>
<td><p>AMD Ryzen <span>9950X3D2</span> 16C32T 5.65GHz <span>270W OC</span></p></td>
<td><p>96GB <span>DDR5-6400</span><br />
<span>时序优化</span></p></td>
<td><p><span>2*100G</span> IB + 25G RoCE</p></td>
<td><p><span>PCIe 4.0</span> x16</p></td>
<td><p>✅</p>
<p>已上线20GPU</p></td>
</tr>
<tr>
<td><p><strong>8A100M40</strong></p></td>
<td><p>8</p></td>
<td><p>8*<span>改进型</span>A100-SXM4-40GB</p></td>
<td><p>2*AMD Threadripper Pro <span>5975WX</span> 32C64T 4.5GHz 280W</p></td>
<td><p>512GB DDR4-3200</p></td>
<td><p><span>18*100G</span> IB / RoCE</p></td>
<td><p><span>NVLink 600GBps with NVSwitch</span></p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p><strong>8A100M80</strong></p></td>
<td><p>8</p></td>
<td><p>8*<span>改进型</span>A100-SXM4-80GB</p></td>
<td><p>2*AMD Threadripper Pro <span>5975WX</span> 32C64T 4.5GHz 280W</p></td>
<td><p><span>2048GB</span> DDR4-3200</p></td>
<td><p><span>18*100G</span> IB + 25G RoCE</p></td>
<td><p><span>NVLink 600GBps with NVSwitch</span></p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
</tbody>
</table>

> **分区选择先看显存，再做短任务对比：**
>
> **4V100 / 4V100PX：**可作为中小规模 ABACUS、VASP、QE、CP2K、DeePMD 和 GPUMD 任务的试跑起点；两者互联差异见[FAQ](https://vcnn7siwx4yx.feishu.cn/wiki/LleawhoLoisgSTkLuejcJ6vFnLb#TkjTdDEUZoxLFFxPAKcckdnznd6)。
>
> **16V100：**适合进一步测试多卡、大体系或多节点扩展。能运行的体系大小还取决于模型、精度、显存与软件版本。
>
> **8V100V0：**可用于对比大体系 VASP/QE、DeePMD 模拟以及 DPA2/DPA3 多卡训练的吞吐量。
>
> 这些是已有应用经验；最终按同一任务的耗时、显存和卡时选择。

### 不同应用的分区选择经验

下表保留以往调优经验。闪电数量用于粗略比较，不是标准化跑分；原子数范围取决于具体输入、模型、精度和并行配置，不是资源上限或性能承诺。

<table>
<thead>
<tr>
<th><p><strong>应用场景</strong></p></th>
<th><p><strong>应用类型</strong></p></th>
<th><p><strong>4V100(PX) 效率</strong></p></th>
<th><p><strong>16V100 效率</strong></p></th>
<th><p><strong>8V100V0 效率</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>ABACUS-LCAO</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡⚡<br />
(最多1万原子)</p></td>
<td><p>⚡⚡⚡<br />
(支持数万原子)</p></td>
<td><p>⚡<br />
(最多1万原子)</p></td>
</tr>
<tr>
<td><p>VASP-PBE</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡⚡<br />
(最多3~5k原子)</p></td>
<td><p>⚡⚡⚡⚡⚡<br />
(支持1万原子以上)</p></td>
<td><p>⚡⚡⚡⚡<br />
(最多2~4k原子)</p></td>
</tr>
<tr>
<td><p>VASP-HSE</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>Quantum ESPRESSO</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>CP2K</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡<br />
(最多1~2万原子)</p></td>
<td><p>⚡⚡⚡<br />
(支持10万原子以上)</p></td>
<td><p>⚡<br />
(最多1~2万原子)</p></td>
</tr>
<tr>
<td><p>Gaussian16</p></td>
<td><p>第一性原理/量子化学</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡</p></td>
<td><p>⚡</p></td>
</tr>
<tr>
<td><p>DeePMD DPA-1</p></td>
<td><p>多卡训练</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>DeePMD DPA-2/3</p></td>
<td><p>多卡训练</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡(易OOM)</p></td>
<td><p>⚡⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>DeePMD-LMP ＜2000原子/卡<br />
(追求最长时间尺度)</p></td>
<td><p>MD模拟</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡</p></td>
</tr>
<tr>
<td><p>DeePMD-LMP ＞1亿原子<br />
(追求最大空间尺度)</p></td>
<td><p>MD模拟</p></td>
<td><p>🚫</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>🚫</p></td>
</tr>
<tr>
<td><p>GPUMD-NEP</p></td>
<td><p>MD模拟</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>LAMMPS 经典/ReaxFF</p></td>
<td><p>MD模拟</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡</p></td>
</tr>
<tr>
<td><p>GROMACS</p></td>
<td><p>MD模拟</p></td>
<td><p>⚡⚡⚡⚡⚡</p></td>
<td><p>⚡⚡⚡⚡</p></td>
<td><p>⚡⚡</p></td>
</tr>
</tbody>
</table>

## CPU 数据处理节点

> `CPU-MISC` 用于 CPU 数据处理任务。费用以控制台该资源的当前价格为准，不能由“CPU-only”推断免费。
>
> 2026 年 10 月 13 日核对：该分区当前包含 `dpn01`，允许 `rush-cpu` QOS；下面保留其他节点的历史规格。

- GPU集群会产生规模庞大的分子动力学轨迹、波函数文件、DFT数据集等数据，但用于处理这些数据的算法往往只能使用CPU执行，且并行度较差，因此需要极强单线程性能、海量内存的CPU-only节点专门处理这类负载
- 鼓励广大研究人员在条件允许的情况下开发和使用支持**GPU加速的数据处理**方法
- 已有一些前沿实验室在日常科学计算中广泛应用GPU加速数据处理

<table>
<thead>
<tr>
<th><p><strong>分区</strong></p></th>
<th><p><strong>节点</strong></p></th>
<th><p><strong>CPU核数</strong></p></th>
<th><p><strong>CPU配置</strong></p></th>
<th><p><strong>内存配置</strong></p></th>
<th><p><strong>节点本地SSD配置</strong></p></th>
<th><p><strong>节点间</strong><br />
<strong>互联配置</strong></p></th>
<th><p><strong>上线状态</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2"><p><strong>CPU-MISC</strong></p></td>
<td><p>dpn01</p></td>
<td><p>44</p></td>
<td><p>Intel Xeon w9-3575X 44C88T 4.8GHz 97.5MB <span>920W OC</span></p></td>
<td><p>768GB <span>DDR5-5600</span></p></td>
<td><p>1.6TB NVMe SSD<br />
(写满不降速, 3GB/s 220KIOPS)</p></td>
<td><p><span>100G</span><br />
RoCE</p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
<tr>
<td><p>dpn02</p></td>
<td><p>128</p></td>
<td><p>2*AMD EPYC 7C13 64C128T 3.7GHz 256MB 240W</p></td>
<td><p>512GB DDR4-3200</p></td>
<td><p>2+1.6TB NVMe SSD<br />
(写满不降速, 3GB/s 220KIOPS)</p></td>
<td><p>25G<br />
RoCE</p></td>
<td><p>历史记录</p>
<p>当前不在 CPU-MISC<br />
（2026-10-13 核对）</p></td>
</tr>
</tbody>
</table>

## CPU-only节点

<table>
<thead>
<tr>
<th><p><strong>分区</strong></p></th>
<th><p><strong>CPU核数</strong></p></th>
<th><p><strong>CPU配置</strong></p></th>
<th><p><strong>内存配置</strong></p></th>
<th><p><strong>节点本地SSD配置</strong></p></th>
<th><p><strong>节点间</strong><br />
<strong>互联配置</strong></p></th>
<th><p><strong>上线状态</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>DSPRHBM</strong></p></td>
<td><p>1872 (18*104)</p></td>
<td><p>2*Intel Xeon Max 9470C 52C52T 3.5GHz 105MB 350W</p></td>
<td><p>128GB HBM2e 2TB/s</p></td>
<td><p>1.6TB NVMe SSD<br />
(写满不降速, 3GB/s 220KIOPS)</p></td>
<td><p><span>2*100G</span> IB + 25G RoCE</p></td>
<td><p>✅</p>
<p>全量上线</p></td>
</tr>
</tbody>
</table>

## 分布式存储

工作目录采用 Lustre 并行文件系统。2026 年 10 月 13 日核对，`/home` 和 `/org` 均挂载在 Lustre 上。下面保留原有存储硬件记录，不能据此推算用户当前可用容量：

- 72x 22 TB SAS HDD，每12块组成一组 RAID Z2 VDEV
- 2x 7.68 TB PCIe Gen4 x8 NVMe SSD 作为 L2ARC（二级缓存）
- 1 TiB RAM（16x 64GB DDR4 2933MT/s RECC）作为 ARC（内存缓存）
- 2x 6.4 TB PCIe Gen4 x4 NVMe SSD 用于元数据存储（Lustre MDT）
- 原测试记录的并发顺序吞吐为写入 11 GB/s、读取 56 GB/s，表示多个客户端共同读写的总量。单个任务的速度还受访问模式和并发负载影响。

工作目录的透明压缩在文件系统层面处理，应用无需改变读写方式。以下是原有数据样本的压缩比记录，实际效果随数据类型变化：

- 文本格式的分子动力学轨迹压缩率为 2~2.5x
- 主流DFT软件的波函数文件、电荷密度文件等数据的压缩率为 2~5x
- 生物信息学数据压缩率为 2.5~3.5x
- **压缩节省的是后端物理空间，不会自动把用户 quota 翻倍。**配额、已用量和可写空间以当前存储查询为准；不要用压缩比推算账号还能写入多少数据。

可用 `ncdu` 查找大文件；按 `a` 切换文件逻辑大小与文件系统报告的占用。它适合整理目录，但不能代替配额查询，也不一定反映 ZFS 后端压缩后的物理占用。

📌也可以使用 Lustre 原生 `lfs` 命令查看存储 quota 信息

## 💡FAQ

#### Q: 4V100分区和4V100PX分区有什么区别？

> **A：**一般先选 `4V100`，它的单卡显存更大，GPU 间也有 NVLink，适用范围更广。若 16 GB 显存够用，又主要跑单卡或通信较少的任务，再考虑 `4V100PX`；规格见[SAI硬件资源](index.md)。
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
