# 数据传输

## rclone挂载

rclone 可把 SFTP 等远程存储挂载为本地目录。首次配置先运行 `rclone config`，选择 SFTP，并填写[登录超算](../891ee584b71ab6f7b0d6d62d/index.md)中的主机、端口、用户名和密钥。挂载功能及依赖请按所在操作系统的 rclone 文档配置。

缓存可以让重复读写更顺手。开启写回缓存时，要等上传队列完成再提交计算或退出客户端。

GUI开发中：https://github.com/Stardust0831/ssh-mountmate

## 🔥 RaiDrive挂载 (强烈推荐)

对于Windows用户，推荐用RaiDrive的SFTP挂载，把集群存储挂载到资源管理器，像在本地硬盘上一样操作集群上的文件。

挂载后效果展示：

![图片展示了Windows系统中使用RaiDrive挂载集群存储后的效果。画面中，左侧资源管理器显示了多个磁盘，其中“sauser01 (X:)”和“testuser01 (Z: )”被黄色框突出显示，表明这两个磁盘是通过RaiDrive挂载的集群存储。右侧“此电脑”窗口中，同样显示了“sauser01 (X: )”和“testuser01 (Z: )”磁盘，且在“sauser01 (X: )”窗口中，还呈现了其内部文件夹及文件列表。该图片直观呈现了文档中推荐的RaiDrive挂载方式在Windows系统下的实际应用效果。](assets/47cbbe447a654d4d0be880c279fd5a8327adaf8e8e106146e29067c39d6ce538.jpeg)

可以从该链接下载RaiDrive：https://www.raidrive.com/zh-hans/download

![图片展示的是RaiDrive官网页面，用于下载安装包。页面上方有RaiDrive的标志及导航栏。中间部分以“就像一个USB驱动器”为标题，介绍RaiDrive的功能。下方有“下载RaiDrive”按钮，旁边有黄色箭头指向，提示单击此处下载安装包。页面还列出了不同操作系统版本的RaiDrive Mount GUI和RaiDrive GUI的下载链接，如Windows 11、Windows 7 SP2等。该图片与文档中推荐Windows用户使用RaiDrive的SFTP挂载功能相呼应，提供下载安装包的指引。](assets/685874b7370805dacc35a1e64ff4fb93d650d7db5d11ac167841ce0e20e86b94.jpeg)![图片展示了RaiDrive挂载操作的登录步骤。左侧是RaiDrive安装后的登录界面，提示安装后打开程序，双击处打开浏览器进行登录，下方有“登录”按钮。右侧是浏览器登录界面，可使用Google、Apple、Microsoft、GitHub、Facebook、Naver等账号登录，下方有“新注册”按钮。该图片与文档中推荐Windows用户使用RaiDrive的SFTP挂载集群存储，以及挂载后效果展示的内容相关，直观呈现了登录操作流程。](assets/1716d7d1c5c23c1f5539dddfae736cf4c8db315bb3829ecd06249faad424529c.jpeg)

新建挂载时选择 NAS → SFTP，填写[登录信息](../891ee584b71ab6f7b0d6d62d/index.md)，目录填自己在集群上的实际路径。下图是控件位置示意，其中地址和目录需要替换：

![图片展示了RaiDrive挂载时的控件位置示意。画面中，有多个控件和文字说明。上方有“单击此处添加一个新的挂载”等操作指引，如选择NAS、SFTP等。下方有“新虚拟驱动器”区域，可选择服务类型、协议、虚拟驱动器名称等。还有“虚拟驱动器”区域，可设置挂载在本地的盘符和名称，以及输入SAL的域名和端口等信息。该图与文档中新建挂载时选择NAS→SFTP的操作步骤说明相呼应，直观呈现了操作控件位置。](assets/78b3092ab9c377a9e93283ef58c0f8a3821163d8c2090cb0a0a4f50ce5631ea9.jpeg)

缓存默认占用本机磁盘。C 盘空间紧张时，可在设置中换到其他磁盘；传输大文件前留足空间。

![图片展示了RaiDrive的设置界面，其中“临时目录”默认为“RaiDriveCache”，并有黄色箭头指向该路径。界面还显示了磁盘、语言、检查更新、代理等设置选项。该图片与文档中介绍RaiDrive挂载时的文件缓存路径相关，说明RaiDrive会将上传和下载文件缓存在临时目录，该路径默认在C盘，可手动改到其他盘，且这一路径不局限于固态硬盘，使用机械硬盘通常也不会有明显效率损失。](assets/4647045bce37f5c4dd55e59413a69bdd414f4c5b626412a1858db4f1d966fe09.jpeg)

------------------------------------------------------------------------

## SFTP/SCP

少量文件直接用 MobaXterm 的 SFTP 面板拖放，很方便；也可使用命令行 `sftp`。需要重复同步整个目录时，推荐下面的 `rsync`：

``` bash
sftp -P 12022 username@c0.sai.ai-4s.com
# 在 sftp 提示符内：
put input.dat
get result.dat
bye
```

重复同步目录时，可在本机使用 rsync；先做预览，再去掉 `--dry-run` 执行：

``` bash
rsync -av --dry-run -e "ssh -p 12022" ./inputs/ username@c0.sai.ai-4s.com:/已授权的目标目录/
```

替换用户名和目标目录。源目录末尾的 `/` 表示复制其中的内容；大量小文件可先打包，通常比逐个传输快。

![图片展示了MobaXterm的Session settings界面中SSH设置部分。界面中有多个选项卡，当前选中“Advanced SSH settings”。在“SSH-browser type”处，有“SCP (enhanced speed)”和“Try to follow SSH path in browser”两个选项，其中“SCP (enhanced speed)”被红色箭头指向。界面右下角有“OK”和“Cancel”按钮。图片与上下文的关系是，上下文提到在使用MobaXterm的SFTP面板拖放少量文件时很方便，但大量小文件打包传输更高效，此图则提示在重复同步目录时，推荐使用SCP（enhanced speed）以获得更丝滑的文件传输体验。](assets/ce53a1339a7cb3e41dab8e388b4a51fef45cb25cdfb842cf226bdd30fe92874e.png)

------------------------------------------------------------------------

## TRZSZ

SAI的登录节点已经预装了TRZSZ。

`trzsz` ( trz / tsz ) 是一款优秀的文件传输工具，和 lrzsz ( rz / sz ) 类似的、兼容 tmux 的文件传输工具。手册见https://trzsz.github.io/cn/

### TRZSZ支持的终端

- [trzsz-ssh](https://trzsz.github.io/cn/ssh) ( tssh ) – 内置支持 trzsz 的 ssh 客户端（ ⭐ 推荐 ）。
- [iTerm2](https://iterm2.com/) – 参考 [Trzsz-iTerm2 安装文档](https://trzsz.github.io/cn/iterm2)。
- [tabby](https://tabby.sh/) – 安装 [tabby-trzsz](https://github.com/trzsz/tabby-trzsz) 插件即可。
- [electerm](https://electerm.github.io/electerm/) – 升级到 `1.19.0` 以上的版本即可。
- [ttyd](https://github.com/tsl0922/ttyd) – 升级到 `1.7.3` 以上的版本，并且启动时加上 `-t enableTrzsz=true`，非 localhost 要用 `https`。
- [trzsz-go](https://trzsz.github.io/cn/go) – 只要是支持本地 shell 的终端就可以用。
- [trzsz.js](https://trzsz.github.io/cn/js) – 让运行在浏览器中的 webshell 和用 electron 开发的终端支持 `trzsz`。

### 使用指南

#### `trz` 上传文件

`trz` 命令可以不带任何参数，将上传文件到当前目录。也可以带一个目录参数，指定上传到哪个目录。

``` bash
trz .
```

#### `tsz` 下载文件

`tsz` 可以带一个或多个文件名（可使用相对路径或绝对路径，也可使用通配符），将下载指定的文件。

*登录shell*

    tsz file1 file2 file3

### 使用示例

![图片展示的是在Mac终端中执行\`trz\`命令上传文件后的界面。终端提示符显示为\`lonnywong@Mac15:/private/tmp/test\$\`，表明当前目录为\`/private/tmp/test\`。界面底部状态栏显示时间为“18:51 19-Mar-22”，终端编号为“\[0\]”，进程号为“0:bash\*”。该图片与文档中介绍\`trz\`上传文件功能的上下文对应，直观呈现了上传文件后的终端界面状态。](assets/3242758b5a5826305fd0b6c6427b1756aba6c183413aae4619ca80f9340510dc.gif)
