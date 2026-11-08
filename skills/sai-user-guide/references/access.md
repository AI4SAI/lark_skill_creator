# 账号与连接

从[控制台](https://www.open-sai.com/portal/)注册或登录 SAI 账号。账号资料和安全设置在账号中心管理，组织成员、站点开通和计算资格在控制台查看。已有账号继续使用原登录方式，登录故障按下文排查。

“默认身份”决定登录后的起始目录和默认账户。它是全局选择，修改后同步到已开通站点，各站生效进度分别查看。任务实际记到哪个账户，见[任务账户选择](compute.md)。

连接 SSH 前，在控制台确认站点已开通，再使用该站点显示的主机、Linux 用户名和公钥设置。忘记密码时使用登录页的找回入口。Agent 不收集密码、私钥或验证码。

Windows 用户可以按手册用 MobaXterm 连接，文件传输可以用 SFTP。MountMate 的 SAI Windows 预发布版及追加挂载入口见[数据传输](handbook/2145e4dfd26ad7d6fd4a40fc/index.md)，挂载使用已有文件权限。

本地 Codex 等客户端使用 SAI CLI 时，先读[工具使用](tools.md)。沿用用户已有的连接配置，需要登录时由用户完成官方浏览器授权。

连接失败先区分：网页账号问题、站点尚未开通、SSH 用户名或公钥不匹配、网络问题。保留原始错误和发生时间，按[登录手册](https://vcnn7siwx4yx.feishu.cn/wiki/XDK8wAeomiHdH1kFT11c6NsenYf)排查，需要支持时使用[问题反馈](handbook/c62336b8dd845c2de07d2bf9/index.md)。

原文：[账号申请](https://vcnn7siwx4yx.feishu.cn/wiki/DrcXwp6rZidHSQkoE95cGvLMnPf)、[数据传输](https://vcnn7siwx4yx.feishu.cn/wiki/YUK3w884Vibfzyk3gdZcSTkungh)。
