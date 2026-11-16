# SAI PILOT 专项 Q&A（持续更新）

Q: 我还是想用自己熟悉的 Codex / Claude-Code / OpenCode ...

A: 可以和往常一样直接 SSH 操作，也可以让 SAI PILOT 自主调用这些你熟悉的 Harness：点击 PILOT 页面左下角的“设置” \> “Codex 与 Claude Code”，即可设置委派功能，在 Codex 与 Claude Code 中继续使用你既有的 API Key 或账号，同时你也可以通过 SSH 或 PILOT 的网页终端结合 `codex agents` 等原生功能直接监看或指挥这些被 PILOT 委派的会话。值得一提的是，你还可以通过“设置” \> “SAI 使用指引”将 PILOT 内置的 SAI 通用 skill 安装给你自己的 Codex、Claude-Code、OpenCode 等通用 Agent。

Q: 我个人 PC / SAI 上的 Codex / Claude-Code / OpenCode ... 中已经积累了很多 Memory / Session，换到 SAI PILOT 这些宝贵的记忆又要重建一遍吗？我切换到 SAI PILOT 还能无缝接续之前的工作吗？

A: 点击 PILOT 页面左下角的“设置” \> “导入 Agent 资料”，即可导入你以前在 Codex、Claude-Code 等通用 Agent 中积累的所有 Memory、Skill 和 Session，PILOT 可无缝接续这些工作。

Q: 我有自己的 API Key，怎么用？

A: 点击 PILOT 页面左下角的“设置” \> “模型” \> “添加模型提供商”，即可添加你自己的 API Key 和相应的模型（注意设置正确的思考等级等参数），并可在对话页的模型选择器中选择你的模型，此时网页搜索和抓取等功能也将来自你自己的 Key。

Q: 既然多个主会话之间能自发通信协调，这和我只开一个主会话写好工作分派然后通过原生的子 agent 功能执行有什么区别？

A: 原生子 agent 只针对 agent-to-agent 的场景设计，人类很难介入子 agent 的工作，而主会话更便于人类直接监看和介入，多个主会话就像多个“主管”，你可以直接指挥他们，他们互相之间也能主动发现和按需沟通协调，你所需要的的工作就是“微服私访”。

Q: 我在网页上打开的终端环境，会随着网页的关闭而丢失吗？

A: 不会。网页只承载可视化渲染功能，网页关闭乃至你的电脑/手机关闭后，关闭时刻的所有环境和状态都保留在 SAI 上，正在运行的任何任务和命令都不会中断，你在网页终端上的所有操作（包括输入了一半没有执行的命令）也不会丢失，重新打开 PILOT 网页即可无缝继续操作。

Q: SAI PILOT 本质上就是 DSH（DeepSeek-Harness）吗？

A: 基本上是。但 PILOT 针对科研超算场景（特别是 SAI 场景）进行了一定程度的定制，99%以上的定制完全遵循 DSH 的插件框架边界，随着 DSH 上游的继续更新，有希望实现 100% 的插件化，因此无需担心“魔改过度”导致使用不习惯。
