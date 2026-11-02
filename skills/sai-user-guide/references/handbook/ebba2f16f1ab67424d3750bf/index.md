# 自建超算vs租用SAI

### 课题组内自建超算的每卡时成本计算公式

<span class="math">$`C_{卡时}=\frac{C_{总建}+t_{折旧}\times\left(C_{月人}+C_{月电}\right)}{720\times t_{折旧}\times N_\text{GPU}\times p_{用}\times f_{效}},`$</span>

<span class="math">$`C_{月电} = \begin{cases} P_{峰} \times C_{月托}, & (\text{IDC托管模式}) \\ 720 \times C_{度电} \times (P_{空} + p_{用} \times (P_{典} - P_{空})). & (\text{电费直付模式}) \end{cases}`$</span>

<table>
<thead>
<tr>
<th colspan="2"><p><strong>变量定义</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>卡</mi><mi>时</mi></mrow></msub><annotation encoding="application/x-tex">C_{卡时}</annotation></semantics></math></span></p></td>
<td><p>每卡时核算成本</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>总</mi><mi>建</mi></mrow></msub><annotation encoding="application/x-tex">C_{总建}</annotation></semantics></math></span></p></td>
<td><p>集群（+机房）总建设成本（一次性）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>月</mi><mi>人</mi></mrow></msub><annotation encoding="application/x-tex">C_{月人}</annotation></semantics></math></span></p></td>
<td><p>每月人员成本</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>月</mi><mi>电</mi></mrow></msub><annotation encoding="application/x-tex">C_{月电}</annotation></semantics></math></span></p></td>
<td><p>每月电力成本（分为[IDC托管]和[电费直付]两种模式）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>月</mi><mi>托</mi></mrow></msub><annotation encoding="application/x-tex">C_{月托}</annotation></semantics></math></span></p></td>
<td><p>每月每kW托管成本（[IDC托管]模式，单位：元/kW·月）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>C</mi><mrow><mi>度</mi><mi>电</mi></mrow></msub><annotation encoding="application/x-tex">C_{度电}</annotation></semantics></math></span></p></td>
<td><p>每kWh电费成本（[电费直付]模式，单位：元/kWh）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>P</mi><mi>峰</mi></msub><annotation encoding="application/x-tex">P_{峰}</annotation></semantics></math></span></p></td>
<td><p>超算满载峰值功率（[IDC托管]模式，单位：kW）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>P</mi><mi>空</mi></msub><annotation encoding="application/x-tex">P_{空}</annotation></semantics></math></span></p></td>
<td><p>超算空载典型功率，考虑机房PUE（[电费直付]模式，单位：kW）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>P</mi><mi>典</mi></msub><annotation encoding="application/x-tex">P_{典}</annotation></semantics></math></span></p></td>
<td><p>超算满载典型功率，考虑机房PUE和应用负载特性（[电费直付]模式，单位：kW）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>p</mi><mi>用</mi></msub><annotation encoding="application/x-tex">p_{用}</annotation></semantics></math></span></p></td>
<td><p>超算在折旧周期内综合使用率</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>t</mi><mrow><mi>折</mi><mi>旧</mi></mrow></msub><annotation encoding="application/x-tex">t_{折旧}</annotation></semantics></math></span></p></td>
<td><p>超算折旧周期（单位：月）</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>N</mi><mtext mathvariant="normal">GPU</mtext></msub><annotation encoding="application/x-tex">N_\text{GPU}</annotation></semantics></math></span></p></td>
<td><p>超算计算节点GPU总数</p></td>
</tr>
<tr>
<td><p><span class="math"><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>f</mi><mi>效</mi></msub><annotation encoding="application/x-tex">f_{效}</annotation></semantics></math></span></p></td>
<td><p>自建超算相较于SAI基线的效率因子（由于自建超算优化不到位）</p></td>
</tr>
</tbody>
</table>

### 🌰举例

- 某课题组购入SAI SlimPOD-144超算（改进型V100-32G），<span class="math">$`C_{总建}`$</span>= 150万元，<span class="math">$`C_{月人}`$</span>= 10000 元/月。托管于学校IDC机房，<span class="math">$`C_{月托}`$</span>= 425 元/kW·月（原型机LiuLab-HPC在校内超算机房的托管费用），<span class="math">$`P_{峰}`$</span>= 60 kW（36台计算节点1.6kW/台，主节点和交换机等设备约2.4kW），<span class="math">$`p_{用}`$</span>= 0.5（此使用率对于课题组超算来说已较高），<span class="math">$`t_{折旧}`$</span>= 36月。此外由于招聘的专职运维工程师水平不如SAI团队，若与SAI对比，需除以效率因子<span class="math">$`f_{效}`$</span>= 0.95。则每卡时核算成本\
  <span class="math">$`C_{卡时}=\frac{1500000+36\times\left(10000+60\times425\right)}{720\times36\times144\times0.5\times0.95}
  =1.5669\ (元)`$</span>
- 若此课题组不为超算配置专职运维工程师，由学生运维超算，而作为代价，此课题组超算**没有性能调优和调度优化**，若与SAI对比，需除以效率因子<span class="math">$`f_{效}`$</span>= 0.8，则每卡时核算成本\
  <span class="math">$`C_{卡时}=\frac{1500000+36\times\left(60\times425\right)}{720\times36\times144\times0.5\times0.8}
  =1.6196\ (元)`$</span>
- 若此课题组进一步白嫖学校电费/托管费，而作为代价，学生使用积极性降低，超算使用率<span class="math">$`p_{用}`$</span>= 0.4，则每卡时核算成本\
  <span class="math">$`C_{卡时}=\frac{1500000}{720\times36\times144\times0.4\times0.8}
  =1.2559\ (元)`$</span>
- 若此课题组采取自建机房方案（而非IDC托管），则考虑机房设施（机柜、空调、电缆、施工费等）在3年内的摊销成本，<span class="math">$`C_{总建}`$</span>= 180万元，<span class="math">$`C_{度电}`$</span>= 0.6 元/kWh，<span class="math">$`P_{空}`$</span>= 15 kW，<span class="math">$`P_{典}`$</span>= 55 kW，则上述3种情况的每卡时核算成本分别为\
  <span class="math">$`C_{卡时}=\frac{1800000+36\times\left(10000+720 \times0.6\times(15+0.5\times(55-15))\right)}{720\times36\times144\times0.5\times0.95}
  =1.5253\ (元)`$</span>\
  <span class="math">$`C_{卡时}=\frac{1800000+36\times720 \times0.6\times(15+0.5\times(55-15))}{720\times36\times144\times0.5\times0.8}
  =1.5702\ (元)`$</span>\
  <span class="math">$`C_{卡时}=\frac{1800000}{720\times36\times144\times0.4\times0.8}
  =1.5070\ (元)`$</span>
- 若考虑硬件故障等问题带来的额外时间浪费甚至经济支出，实际核算成本将会更高。
- 自建超算往往管理混乱（甚至往往不如友商超算平台），导致**学生科研的积极性降低**，这种损失难以计量！
- 此处充值优惠为旧报价（历史参考）：一次性充值200万元，预计优惠后每卡时价格**低于1元**。

### 📌结论

**租用SAI的性价比远高于自建超算**。

对于已有自建超算的用户，SAI支持与用户自建超算深度融合，实现算力按需调配，请看[卫星集群和姊妹集群](../ac41bc6f8d0c7984e7e26283/index.md)

### 💡 Q&A

Q：<span class="math">$`p_{用}`$</span>为什么取0.5？

A：不可高看课题组超算的使用率，即使以原型机LiuLab-HPC的使用强度，超算在组员的主观感觉上常年满载、排长队，但严格统计得到的实际使用率也只有0.61，而使用强度能达到原型机水平的实验室少之又少。\
我们需要考虑到假期、半夜等时间段，还要考虑到资源碎片化导致的“有空闲资源但排不上队”，实际上，周末和法定节假日都能接近满载的课题组集群并不存在，资源碎片化也是广泛存在的问题。\
另一方面，根据开发者对亲自运维的多个不同课题组集群的观察统计，课题组内集群使用率普遍在0.3~0.6之间。\
综上所述，<span class="math">$`p_{用}`$</span>取0.5是合理的。

Q：是否可以直接向SAI购买服务器硬件？

A：请联系我们说明采购需求，SAI的硬件规格参考[SAI硬件资源](../7d583b3babea8f243329f3c7/index.md)。需要注意的是，若单轮采购规模低于96-GPU，无法提供软件服务和集群部署服务，仅提供基本的硬件技术支持。提示：在当前（2026年）DRAM、NAND、HDD等存储设备涨价数倍乃至10倍的情况下，自建非常不划算。
