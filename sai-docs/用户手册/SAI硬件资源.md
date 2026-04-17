# GPU计算节点

- 用于<text bgcolor="light-yellow">超大规模并行计算</text>，支持<text bgcolor="light-yellow">**千卡高效并行**</text><text bgcolor="light-yellow">计算单个任务</text>
- 基于创新的<text bgcolor="light-yellow">硬件架构优化</text>以及<text bgcolor="light-yellow">从硬件到软件的协同优化</text>，实现高效的<text bgcolor="light-yellow">超大规模跨尺度高精度分子模拟</text>和<text bgcolor="light-yellow">面向AI for Science的大规模训练和推理</text>
- SAI的<text bgcolor="light-yellow">每卡性能</text>在相同型号GPU中<text bgcolor="light-yellow">前所未有</text>，SAI的改进型V100-SXM2在许多典型计算用例中性能达到市面主流V100的近2倍，<text color="orange" bgcolor="light-yellow">**与市面A100-SXM4持平**</text>

<callout emoji="kissing_heart" background-color="light-orange" border-color="light-orange">

截至2026年1月上旬，SAI已上线300块GPU，其中包含260块改进型V100-SXM2-32GB和40块改进型V100-SXM2-16GB

预计2026年上半年将上线<text bgcolor="light-yellow">**1600块**</text>改进型V100-SXM2
</callout>

<lark-table rows="8" cols="8" header-row="true" header-column="true" column-widths="108,80,100,138,94,100,100,100">

  <lark-tr>
    <lark-td>
      **分区** {align="center"}
    </lark-td>
    <lark-td>
      **GPU数量** {align="center"}
    </lark-td>
    <lark-td>
      **每节点**
      **GPU配置** {align="center"}
    </lark-td>
    <lark-td>
      **每节点CPU配置** {align="center"}
    </lark-td>
    <lark-td>
      **每节点**
      **内存配置** {align="center"}
    </lark-td>
    <lark-td>
      **节点间**
      **互联配置** {align="center"}
    </lark-td>
    <lark-td>
      **节点内**
      **互联配置** {align="center"}
    </lark-td>
    <lark-td>
      **上线状态** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **4V100**
      <text color="gray">SlimPOD</text>
      <text color="gray">144超节点</text> {align="center"}
    </lark-td>
    <lark-td>
      144 + 4 {align="center"}
    </lark-td>
    <lark-td>
      4*<text bgcolor="light-yellow">改进型</text>V100-SXM2-32GB {align="center"}
    </lark-td>
    <lark-td>
      AMD Ryzen <text bgcolor="light-yellow">9950X3D</text> 16C32T 5.75GHz <text bgcolor="light-yellow">260W OC</text> {align="center"}
    </lark-td>
    <lark-td>
      96GB <text bgcolor="light-yellow">DDR5-6400</text>
      <text bgcolor="light-yellow">时序优化</text> {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">2*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">NVLink 300GBps</text> {align="center"}
    </lark-td>
    <lark-td>
      ✅ {align="center"}
      全量上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **4V100PX** {align="center"}
    </lark-td>
    <lark-td>
      40 {align="center"}
    </lark-td>
    <lark-td>
      4*<text bgcolor="light-yellow">改进型</text>V100-SXM2-16GB {align="center"}
    </lark-td>
    <lark-td>
      AMD Ryzen <text bgcolor="light-yellow">9950X3D</text> 16C32T 5.75GHz <text bgcolor="light-yellow">260W OC</text> {align="center"}
    </lark-td>
    <lark-td>
      96GB <text bgcolor="light-yellow">DDR5-6400</text>
      <text bgcolor="light-yellow">时序优化</text> {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">2*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">PCIe 4.0</text> x16 {align="center"}
    </lark-td>
    <lark-td>
      ✅ {align="center"}
      全量上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **16V100**
      <text color="gray">UltraPOD</text>
      <text color="gray">1344超节点</text> {align="center"}
    </lark-td>
    <lark-td>
      1344 {align="center"}
    </lark-td>
    <lark-td>
      16*<text bgcolor="light-yellow">改进型</text>V100-SXM2-16GB {align="center"}
    </lark-td>
    <lark-td>
      AMD Threadripper Pro <text bgcolor="light-yellow">5995WX</text> 64C128T 4.5GHz 280W {align="center"}
    </lark-td>
    <lark-td>
      256GB DDR4-3200 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">9*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">NVLink 300GBps</text> {align="center"}
    </lark-td>
    <lark-td>
      预计<text bgcolor="light-green">2026H1</text>全量上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **8V100V0** {align="center"}
    </lark-td>
    <lark-td>
      112 {align="center"}
    </lark-td>
    <lark-td>
      8*<text bgcolor="light-yellow">改进型</text>V100-SXM2-32GB {align="center"}
    </lark-td>
    <lark-td>
      2*Intel Xeon Gold 6146 12C24T 4.2GHz 165W {align="center"}
    </lark-td>
    <lark-td>
      384GB DDR4-2666 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">4*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">NVLink 300GBps</text> {align="center"}
    </lark-td>
    <lark-td>
      ✅ {align="center"}
      全量上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **4A100PX** {align="center"}
    </lark-td>
    <lark-td>
      64 {align="center"}
    </lark-td>
    <lark-td>
      4*<text bgcolor="light-yellow">改进型</text>A100-SXM2-32GB {align="center"}
    </lark-td>
    <lark-td>
      AMD Ryzen <text bgcolor="light-yellow">9950X3D2</text> 16C32T 5.65GHz <text bgcolor="light-yellow">260W OC</text> {align="center"}
    </lark-td>
    <lark-td>
      96GB <text bgcolor="light-yellow">DDR5-6400</text>
      <text bgcolor="light-yellow">时序优化</text> {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">2*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">PCIe 4.0</text> x16 {align="center"}
    </lark-td>
    <lark-td>
      预计<text bgcolor="light-green">2026H1</text>上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **8A100R40** {align="center"}
    </lark-td>
    <lark-td>
      8 {align="center"}
    </lark-td>
    <lark-td>
      8*<text bgcolor="light-yellow">改进型</text>A100-SXM4-40GB {align="center"}
    </lark-td>
    <lark-td>
      2*AMD Threadripper Pro <text bgcolor="light-yellow">5975WX</text> 32C64T 4.5GHz 280W {align="center"}
    </lark-td>
    <lark-td>
      512GB DDR4-3200 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">20*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">NVLink 600GBps with NVSwitch</text> {align="center"}
    </lark-td>
    <lark-td>
      预计<text bgcolor="light-green">2026H1</text>上线 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **8A100R80** {align="center"}
    </lark-td>
    <lark-td>
      8 {align="center"}
    </lark-td>
    <lark-td>
      8*<text bgcolor="light-yellow">改进型</text>A100-SXM4-80GB {align="center"}
    </lark-td>
    <lark-td>
      2*AMD Threadripper Pro <text bgcolor="light-yellow">5975WX</text> 32C64T 4.5GHz 280W {align="center"}
    </lark-td>
    <lark-td>
      1024GB DDR4-3200 {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">20*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">NVLink 600GBps with NVSwitch</text> {align="center"}
    </lark-td>
    <lark-td>
      预计<text bgcolor="light-green">2026H1</text>上线 {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>

<callout emoji="💡" background-color="light-orange" border-color="light-orange">

各个分区最适用的计算任务类型如下：

1️⃣**4V100**和**4V100PX**分区针对中等规模和小规模并行计算的<text color="orange" bgcolor="light-yellow">极致低延迟</text>优化，<text bgcolor="light-yellow">最适合</text>ABACUS任务（大/中/小体系）、VASP和QE任务（中/小体系）、CP2K任务（中/小体系）、DPA系列模型训练/微调任务（单卡或多卡）、DeePMD分子动力学模拟任务（大/中/小体系）、GPUMD-NEP分子动力学模拟任务（单节点千万原子以下）等（两分区的差异请看[FAQ](https%3A%2F%2Fvcnn7siwx4yx.feishu.cn%2Fwiki%2FLleawhoLoisgSTkLuejcJ6vFnLb%23share-W0oodpFRhoqODUxJ9vnccaJ1npE)）

2️⃣**16V100**分区针对<text color="orange" bgcolor="light-yellow">超大规模并行计算</text>进行低延迟优化，适合4V100和4V100PX分区的任务同样适合此分区。此外，该分区<text bgcolor="light-yellow">最适合</text>各种<text bgcolor="light-yellow">超大体系模拟</text>，例如：万原子级VASP AIMD、数万原子级ABACUS AIMD、十万原子以上CP2K AIMD、数亿原子级DeePMD分子动力学模拟、单节点数千万原子级GPUMD-NEP分子动力学模拟任务等

3️⃣**8V100V0**分区硬件架构与NVIDIA DGX相同，针对计算吞吐量优化，<text bgcolor="light-yellow">最适合</text>VASP和QE任务（大体系）、DeePMD分子动力学模拟任务（大体系）、DPA2和DPA3训练/微调任务（多卡）等
</callout>

## 不同应用场景在各分区的计算效率

<lark-table rows="14" cols="5" header-row="true" header-column="true" column-widths="232,103,159,159,159">

  <lark-tr>
    <lark-td>
      **应用场景**
    </lark-td>
    <lark-td>
      **应用类型** {align="center"}
    </lark-td>
    <lark-td>
      **4V100(PX) 效率** {align="center"}
    </lark-td>
    <lark-td>
      **16V100 效率** {align="center"}
    </lark-td>
    <lark-td>
      **8V100V0 效率** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      ABACUS-LCAO
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡
      (最多1万原子) {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡
      (支持数万原子) {align="center"}
    </lark-td>
    <lark-td>
      ⚡
      (最多1万原子) {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      VASP-PBE
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡
      (最多3~5k原子) {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡
      (支持1万原子以上) {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡
      (最多2~4k原子) {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      VASP-HSE
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Quantum ESPRESSO
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      CP2K
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡
      (最多1~2万原子) {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡
      (支持10万原子以上) {align="center"}
    </lark-td>
    <lark-td>
      ⚡
      (最多1~2万原子) {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      Gaussian16
    </lark-td>
    <lark-td>
      第一性原理/量子化学 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      DeePMD DPA-1
    </lark-td>
    <lark-td>
      多卡训练 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      DeePMD DPA-2/3
    </lark-td>
    <lark-td>
      多卡训练 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡(易OOM) {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      DeePMD-LMP ＜2000原子/卡
      (追求最长时间尺度)
    </lark-td>
    <lark-td>
      MD模拟 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      DeePMD-LMP ＞1亿原子
      (追求最大空间尺度)
    </lark-td>
    <lark-td>
      MD模拟 {align="center"}
    </lark-td>
    <lark-td>
      🚫 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      🚫 {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      GPUMD-NEP
    </lark-td>
    <lark-td>
      MD模拟 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      LAMMPS 经典/ReaxFF
    </lark-td>
    <lark-td>
      MD模拟 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      GROMACS
    </lark-td>
    <lark-td>
      MD模拟 {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡⚡⚡ {align="center"}
    </lark-td>
    <lark-td>
      ⚡⚡ {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>

# CPU数据处理节点 🆓 免费

<callout emoji="kissing_heart" background-color="light-orange" border-color="light-orange">

SAI的CPU数据处理节点<text color="red" bgcolor="light-green">**完全免费！**</text>
</callout>

- GPU集群会产生规模庞大的分子动力学轨迹、波函数文件、DFT数据集等数据，但用于处理这些数据的算法往往只能使用CPU执行，且并行度较差，因此需要<text bgcolor="light-yellow">极强单线程性能</text>、海量内存的CPU-only节点专门处理这类负载
- 鼓励广大研究人员在条件允许的情况下开发和使用支持**GPU加速的数据处理**方法
- 已有一些前沿实验室在日常科学计算中广泛应用GPU加速数据处理

<callout emoji="kissing_heart" background-color="light-orange" border-color="light-orange">

在千卡GPU超节点上线后，将上线更多CPU数据处理节点，CPU不求多但求精，超高频率大核心搭配海量内存，达到300核平均频率5.5~6.0GHz、平均每核内存16GB以上
</callout>

<lark-table rows="2" cols="7" header-row="true" header-column="true" column-widths="100,80,175,145,102,102,102">

  <lark-tr>
    <lark-td>
      **分区** {align="center"}
    </lark-td>
    <lark-td>
      **CPU核数** {align="center"}
    </lark-td>
    <lark-td>
      **CPU配置** {align="center"}
    </lark-td>
    <lark-td>
      **主板配置** {align="center"}
    </lark-td>
    <lark-td>
      **内存配置** {align="center"}
    </lark-td>
    <lark-td>
      **节点间**
      **互联配置** {align="center"}
    </lark-td>
    <lark-td>
      **上线状态** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **CPU-MISC** {align="center"}
    </lark-td>
    <lark-td>
      32 {align="center"}
    </lark-td>
    <lark-td>
      Intel Xeon w9-3575X 44C88T 4.8GHz 97.5MB <text bgcolor="light-yellow">920W OC</text> {align="center"}
    </lark-td>
    <lark-td>
      ASUS Pro WS W790E-SAGE SE {align="center"}
    </lark-td>
    <lark-td>
      768GB <text bgcolor="light-yellow">DDR5-5600</text> {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">2*100G</text> RoCE {align="center"}
    </lark-td>
    <lark-td>
      ✅ {align="center"}
      全量上线 {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>

# CPU-only节点

<lark-table rows="2" cols="7" header-row="true" header-column="true" column-widths="100,80,175,96,151,102,102">

  <lark-tr>
    <lark-td>
      **分区** {align="center"}
    </lark-td>
    <lark-td>
      **CPU核数** {align="center"}
    </lark-td>
    <lark-td>
      **CPU配置** {align="center"}
    </lark-td>
    <lark-td>
      **内存配置** {align="center"}
    </lark-td>
    <lark-td>
      **节点本地SSD配置** {align="center"}
    </lark-td>
    <lark-td>
      **节点间**
      **互联配置** {align="center"}
    </lark-td>
    <lark-td>
      **上线状态** {align="center"}
    </lark-td>
  </lark-tr>
  <lark-tr>
    <lark-td>
      **DSPRHBM** {align="center"}
    </lark-td>
    <lark-td>
      1872 (18*104) {align="center"}
    </lark-td>
    <lark-td>
      2*Intel Xeon Max 9470C 52C104T 3.5GHz 105MB 350W {align="center"}
    </lark-td>
    <lark-td>
      128GB HBM2e 2TB/s {align="center"}
    </lark-td>
    <lark-td>
      1.6TB NVMe SSD
      (写满不降速, 3GB/s 220KIOPS) {align="center"}
    </lark-td>
    <lark-td>
      <text bgcolor="light-yellow">2*100G</text> IB + 25G RoCE {align="center"}
    </lark-td>
    <lark-td>
      预计<text bgcolor="light-green">2026H1</text>上线 {align="center"}
    </lark-td>
  </lark-tr>
</lark-table>

# 分布式存储

📌用户home目录采用了BeeGFS分布式并行文件系统，支持严格的全局一致性，超算内文件IO通过RoCE v2实现，后端存储（OST）通过ZFS VDEV实现。当前硬件配置：

- 48x 22 TB SAS HDD，每12块组成一组 RAID Z2 VDEV
- 2x 7.68 TB PCIe Gen4 x8 NVMe SSD 作为 L2ARC（二级缓存）
- 2 TiB RAM（16x 128GB DDR4 3200MT/s RECC）作为 ARC（内存缓存）
- 2x 6.4 TB PCIe Gen4 x4 NVMe SSD 用于元数据存储（BeeGFS MDT）
- 当前硬件配置下，<text bgcolor="light-yellow">实测</text>可实现8GB/s的并发顺序写入和23GB/s的并发顺序读取

📌用户home目录启用了“<text bgcolor="light-yellow">透明压缩</text>”功能，存入的数据会在文件系统层面被自动压缩，用户和软件对此无感知

- 文本格式的分子动力学轨迹压缩率为2~2.5x
- 主流DFT软件的波函数文件、电荷密度文件等数据的压缩率为2~5x
- 生物信息学数据压缩率为2.5~3.5x
- 总体来说，平均<text bgcolor="light-yellow">每1TB</text>存储空间，实际可以存储<text bgcolor="light-yellow">超过2TB</text>数据（<text color="orange" bgcolor="light-yellow">**1TB > 2TB**</text>）

📌推荐使用`ncdu`命令交互式查看文件/目录的体积和存储占用，通过键盘“a”键切换<text bgcolor="light-yellow">实际存储占用</text>和<text bgcolor="light-yellow">实际文件体积</text>

# 💡FAQ

<reference-synced source-block-id="LXq3dX9yVsB9xSbvwAccosAlnRe" source-document-id="Y0sddTeCxouM8wxyQTMcM86Jnlh">

  ### Q: 4V100分区和4V100PX分区有什么区别？
  <quote-container>
  **A:**如<mention-doc token="LleawhoLoisgSTkLuejcJ6vFnLb" type="wiki">SAI硬件资源</mention-doc>所示，4V100分区为“SAI SlimPOD-144”超节点的“完全体”，相较于4V100PX分区，GPU-GPU互联升级为300GB/s NVLink Full-Mesh直连拓扑，GPU VRAM升级为32GB，且支持144卡高效并行计算单个任务。但这种升级并非在任何情况下都有正向增益：NVLink会占用额外的功耗预算，导致GPU在极端满载情况下频率更低；由于HBM堆叠层数翻倍(8-Hi)，导致时序更宽松、访存延迟更高；在占用VRAM较低的单卡任务中，这些硬件差异一般会导致1~5%的实际性能差异。具体到应用场景，4V100分区的普适度和整体性能更好，大部分任务可以“闭着眼睛用”4V100分区，以下几类特殊任务可优先考虑4V100PX分区：

a) 16GB VRAM就够用的单卡任务；

b) 对GPU-GPU通信带宽需求低，或完全无法利用NVLink，且每卡有16GB VRAM就够用的多卡任务（例如中小体系DPMD分子动力学模拟、中小体系VASP NEB计算、CP2K多卡计算、非cusolverMp后端的ABACUS多卡计算等）
  </quote-container>

</reference-synced>
