# 账号与连接

从[控制台](https://www.open-sai.com/portal/)注册或登录 SAI 账号。账号资料和安全设置由账号中心管理；组织成员、站点开通和计算资格在控制台查看。已有账号先使用原登录方式，避免为一次登录故障另建账号。

**默认工作身份（默认身份）**像预设的工作台：影响新登录的初始目录、默认查看的资金范围，以及同步到站点的 Slurm 默认计算账户。保存后留意站点是否已生效；已有终端不会被强行换目录，个人 Home、已提交任务和权限不会因此改变。每次任务仍按[账户推定规则](compute.md)确定归属，默认身份并不包办所有任务。

网页登录成功不等于已经开通某个计算站点。连接 SSH 前，确认当前站点已开通，再使用该站点显示的主机、Linux 用户名和公钥设置。忘记密码走登录页的找回入口；Agent 不收集密码、私钥或验证码。

Windows 用户可以按手册用 MobaXterm 连接；文件传输可以用 SFTP。使用 MountMate 或其他挂载客户端时，沿客户端实际提供的登录、站点选择与挂载流程操作，挂载不会增加文件访问权限。

本地 Codex 等客户端使用 SAI CLI 时，先读[工具使用](tools.md)。用户已有连接配置就继续使用；需要登录时让用户完成官方浏览器授权，不借用管理员的登录态。

连接失败先区分：网页账号问题、站点尚未开通、SSH 用户名或公钥不匹配、网络问题。保留原始错误和发生时间，按[登录手册](https://vcnn7siwx4yx.feishu.cn/wiki/XDK8wAeomiHdH1kFT11c6NsenYf)排查；涉及账号恢复的私密资料走控制台工单。

原文：[账号申请](https://vcnn7siwx4yx.feishu.cn/wiki/DrcXwp6rZidHSQkoE95cGvLMnPf)、[数据传输](https://vcnn7siwx4yx.feishu.cn/wiki/YUK3w884Vibfzyk3gdZcSTkungh)。
