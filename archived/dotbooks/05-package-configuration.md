# 常用工具配置

## fcitx

参见[这里](fcitx.md)

## fcitx5

关于快捷键已经在 dotfiles 里设置好了，只需要安装下面这些包，再在 qt 设置界面里添加中文输入法就行。

```text
fcitx5
fcitx5-chinese-addons
fcitx5-configtool
fcitx5-gtk
fcitx5-qt
```

fcitx 第一项默认键盘不能是中文，否则会出现 idea 闪退的情况

直接恢复 dotfiles 的配置。但是目前单行模式与 rime 没有配置成功。凑合着用吧

取消下面这两个快捷键：

![1](assets/05-package-configuration/2021-04-17-12-09-01.png)

参考：

-   https://blog.csdn.net/m0_47627464/article/details/113790309
-   https://www.wannaexpresso.com/2020/03/26/fcitx5/
-   [Manjaro 下配置 KDE,内容很多，主要看其中 fcitx5 的部分](https://zhuanlan.zhihu.com/p/114296129)

## neovim

设置 vimdiff 默认使用 nvim，需要安装一个包

```text
yay -S neovim-symlinks
```

## chrome

设置 chrome 的 theme 为 GTK+，在浏览器设置里有

## vscode 解决二次登录问题

> 参考[这里](https://github.com/microsoft/vscode/issues/92972#issuecomment-608572519)，注意 keyring 一定要设置为空（就是什么都不输入）
>
> 如果一不小心输了密码，后面每次登录都要输入密码
>
> 解决这个问题的方法：直接删除 keyring 然后重新上面的操作
>
> keyring 的位置：`~/.local/share/keyrings/`

1. 安装 seahorse

2. 确保`~/.local/share/keyrings/`路径存在，并且文件夹是空的。

3. 打开 seahorse，点左上角的`+`，创建一个新的`Password keyring`，命名为`Login`，然后密码什么都不填直接 continue.

4. vscode 登陆帐号

5. reboot

## ranger

1. 取消标签:

    ```text
    :tag_remove
    ```

2. 拖拽

    快捷键：\d+鼠标拽

    参考：https://github.com/ranger/ranger/wiki/Drag-and-Drop

## mysql

参见[这里](_default/mysql/mysql-linux-configuration.md)

## intellij-idea

不要安装`oracle-jdk15`，这个会导致 idea 崩溃

应该安装`openjdk-src`

```bash
sudo powerpill -S openjdk-src
```

## gnome-boxes

Server 端（manjaro）需要安装`spice-vdagent`，这个包能够调节分辨率

Guest 端（linux）需要安装下图的两个包。注意，在安装完之后，重启 windows,然后设置 share-folder，然后再次重启 windows，这次就会出现一个网络驱动器

> 这两个包我已经下载好了：https://gitee.com/ysl2/gnome-boxes-windows-guest-pack
>
> 参考：
>
> -   https://askbot.fedoraproject.org/en/question/116855/boxes-windows-10-shared-files/#:~:text=The%20Sharing%20Folder%20preferences%20are%20in%20the%20Properties,default%29.%20This%20is%20available%20in%20gnome-boxes-3.26%20and%20newer.
>
> -   https://www.spice-space.org/download.html

![1](assets/05-package-configuration/2021-05-11-17-09-48.png)

![1](assets/05-package-configuration/2021-05-11-17-16-31.png)

![1](assets/05-package-configuration/2021-05-11-16-34-51.png)

## virtualbox（不推荐，建议使用 gnome-boxes）

### virtualbox 安装

Before installing virtualbox, you should run `cat /proc/version`to check your linux kernal version, then run `sudo pacman -S virtualbox` command and choose the virtualbox veision which fits your kernal version.

```bash
# Check your Linux kernel version
cat /proc/version
# Or you can use this command: `sudo uname -r`

# Choose the correct version to install
sudo pacman -S virtualbox

# Update your linux headers. Also, you need to choose the version that suits your kernel
# 注意每次更新完内核，都检查一下下面这个包是否和当前内核版本匹配
sudo pacman -S linux-headers

# Install this (I don't know why, but this is necessary)
sudo pacman -S virtualbox-host-dkms

# Add your username to "vboxusers" user group
sudo gpasswd -a yusoli vboxusers
# check current user's all group:
groups

# Add module probe
# 如果更新了内核，需要重新执行一下下面这条命令
# 如果因为更新了内核而导致执行的时候报错，就重新做一遍配置virtualbox的过程（因为我也忘了究竟是做了哪些步骤弄好的）
# 参考：https://blog.csdn.net/a805607966/article/details/112403665
sudo modprobe vboxdrv

# Finally, install the virtualbox enhance plugin
# It provides USB suggestion. If you don't install this, the virtual machine will not be lunched.
sudo pacman -S virtualbox-ext-oracle

# Note: After installing your virtual machine, don't forget install the enhancement CD in machine settings.
```

在安装完成之后，需要关闭“自动捕获键盘”

```text
File -> Preferences -> Input -> Auto Capture Keyboard
```

如果安装增强程序失败，就手动安装：

> 参考：https://superuser.com/a/1407054

```bash
sudo mkdir -p /media/cdrom
sudo mount /dev/cdrom /media/cdrom
```

然后执行：

```bash
sudo sh /media/cdrom/VBoxLinuxAdditions.run
```

可以把上述过程写成一个开机自启服务，或者直接修改 fstab 进行挂载。

需要注意的是，最后的`sh VBoxLinuxAdditions.run`不要写在服务里，只需要写挂载的那部分就行了

### virtualbox 常用命令

> 注意：不用加后面的`--type headless`，否则会导致虚拟机只是在后台运行，而没有界面。

```bash
VBoxManage list vms

VBoxManage startvm "windows-7" --type headless

VBoxManage controlvm "windows-7" pause --type headless

VBoxManage controlvm "windows-7" resume --type headless

VBoxManage controlvm "windows-7" poweroff --type headless
```

## virtualbox 排错

1. 不能为虚拟电脑 CentOS7 打开一个新任务.Failed to construct device usb-ehci instance #0...

    > 参考：https://blog.csdn.net/qq_42993678/article/details/106885510

    设置-usb 设备-选择 usb1.0 解决 …

## 学习 Java 过程中用到的相关工具

见[vscode-with-java](../../ide/vscode-settings/_default/vscode-with-java.md)

## unzip-iconv

pacman 默认的`unzip`中不包含`-O`选项，因此如果解压的文件中包含中文，那么可能会导致乱码。因此从需要卸载`unzip`重新安装`unzip-iconv`，这个是打了补丁之后的。

用法

```bash
# 先写-O选项的话，后面的压缩包文件名补全不了，所以，先-l补全写上文件，再移动到前面加上-O选项。 列出文件没问题的话，解压就行了

# 预览一下解压后将会出现的文件树
unzip -O gbk -l xxx.zip
unzip -O gb2312 -l xxx.zip

# 直接解压
unzip -O gbk xxx.zip
unzip -O gb2312 xxx.zip
```

## zsh

1. 刷新设置

    ```text
    source ~/.zshrc
    ```

2. 设置为 vi 快捷键：

    ```bash
    set -o vi
    ```

3. 一些关键词

    ```text
    grnl-zsh-config

    zoxide — cd
    tig — git
    firenvim — browser vim
    delta — diff
    ```

## tmux

1. 默认快捷键参考： https://gist.github.com/ysl2/684909e4a0f8a73db6a91a9b4f98e5b8

1. 关于 ssh 到远程服务器

    在 tmux 的官方文档中写了，如果想对当前的活动窗口执行 tmux 操作，只需要连按两次前导键就行了。

    比如，我当前的 zsh 里面有个 tmux，前导键是`ctrl + b`，但是我现在通过 ssh 连接到虚拟机上，虚拟机的前导键也是`ctrl + b`，那么如果我只是想对虚拟机执行分屏，就连按两次`ctrl + b`就能对虚拟机的窗格分屏

1. ssh 之后发现 neovim 报错：`clipboard error: no buffer`，

    说明当前 tmux 会话曾经被远程链接过，此时剪贴板无法工作。

    解决方案：重启 tmux 的 session

1. copy-mode

    `ctrl + b + [` 开启 cpoy-mode，此时可以用 vim 快捷键进行移动

    `space` 选中文本，可以换成`y`

    `enter` 退出 copy-mode

    `ctrl + b + ]` 粘贴，可以换成`p`

1. 退出 tmux 的命令模式

    快捷键：`C-c`

1. 给当前窗口重新命名编号

    快捷键`<prefix> + .`

1. pane 的分离与合并

    分离：原有快捷键`<prefix> + !`

    合并：自定义快捷键`<prefix> + u`

    自定义内容如下：

    ```bash
    bind-key u command-prompt -I "join-pane -h -t :"
    ```

1. 刷新设置

    > 我已经把前置键从`ctrl + b`改为了`ctrl + a`

    在命令模式（按 PREFIX : ，即按下 ctrl+a,再输入一个“：”)输入

    ```text
    source-file ~/.tmux.conf
    ```

## flameshot

1. 开启划取范围截图

    ```text
    flameshot gui
    ```

2. 设置 KDE 快捷键

新建一个全局命令

在 Trigger 那里绑定快捷键，在 Action 那里绑定上面的命令

![1](assets/05-package-configuration/2021-03-01-22-35-52.png)

## deepin-screenshot 深度截图（我用的不是这个）

由于 KDE 与 Deepin 的剪切板实现机制的差异，深度截图无法复制图片到剪切板，必须安装 gpaste 来辅助：

```text
yay -S gpaste
```

## thunderbird

1. 解决 outlook 重复发邮件问题

    options -> account settings -> 取消勾选下面这个框

    ![1](assets/05-package-configuration/2021-03-03-09-07-57.png)

## Matlab

> 资源：https://www.luochenzhimu.com/archives/2540.html
>
> 下面两个方法任选：
>
> -   安装步骤 1：https://blog.csdn.net/m0_37775034/article/details/80876362
> -   安装步骤 2：https://lanseyujie.com/post/matlab-download-and-activate.html

直接用我的 github 仓库的安装脚本进行安装：https://github.com/ysl2/linux-matlab

高分辨率设置：

```text
# 在matlab的命令行中敲下面的命令：
>> s = settings;s.matlab.desktop.DisplayScaleFactor
>> s.matlab.desktop.DisplayScaleFactor.PersonalValue = 2
```

## haveged：扩大系统熵值

```text
sudo systemctl enable haveged.service
sudo systemctl start haveged.service
```

## (QQ 轻聊版 || tim) && 微信

> 这个比较稳定，但是版本很旧

```text
# qq轻聊版（无法后台挂起，一旦关闭就直接退出了）
deepin.com.qq.im.light
# tim（可以在后台挂起）
deepin.com.qq.office
# 微信
deepin.com.wechat
```

打开 deepin-wine 的配置界面，并改 dpi 为 144：

```bash
# 改QQ轻聊版的dpi
env WINEPREFIX=$HOME/.deepinwine/Deepin-QQLight deepin-wine5 winecfg
# 改tim的dpi
env WINEPREFIX=$HOME/.deepinwine/Deepin-TIM deepin-wine5 winecfg
# 改微信的dpi
env WINEPREFIX=$HOME/.deepinwine/Deepin-WeChat deepin-wine5 winecfg
```

参考：https://wiki.archlinux.org/index.php/Tencent_QQ_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

## 星火商店 tim & 微信

> 星火商店是 deepin 社区维护的软件源。类似 arch 的 AUR。星火商店的 tim 与微信版本是最新的。
>
> 但是我配置的时候，tim 出现输入方块字问题。无法解决，于是暂时放弃。以后再说

```text
# 包很大，下载速度在600mb/s左右，需要十多分钟。耐心等待
yay -S com.qq.weixin.spark com.qq.tim.spark --noconfirm
```

1. 下载完之后可能会导致方块字的情况。这是因为下载包中没有包含必要的字体。解决方法如下

    以微信为例：去网上找一个微软雅黑字体`mysh.ttf`，放到`~/.deepinwine/Spark-Wechat/drive_c/windows/Fonts`目录下

2. 调节分辨率

    ```text
    # tim
    env WINEPREFIX="$HOME/.deepinwine/Spark-Tim" deepin-wine5 winecfg
    # 微信
    env WINEPREFIX="$HOME/.deepinwine/Spark-WeChat" deepin-wine5 winecfg
    ```

3. 系统语言非中文时，中文全显示成方块

    需要在：`/opt/deepinwine/tools/run.sh`中将 WINE_CMD 那一行修改为：

    ```text
    WINE_CMD="LC_ALL=zh_CN.UTF-8 deepin-wine"
    ```

## 网易云 & qq 音乐

yay 下载：

```text
# 网易云
netease-cloud-music
# qq音乐
qqmusic-bin
```

## wps

安装这两个包：

```text
ttf-wps-fonts
wps-office-cn
```

还有一个包`wps-office-fonts`我安装了，但是 b 站视频没说这个。并且我的界面还是英文，不知道咋回事

## onedrive

pacman 搜索`onedrive-git`

1. 配置 OneDrive（初次）/同步并退出。下次可以直接同步 dotfiles

    ```text
    onedrive
    ```

2. 自动同步

    ```text
    systemctl --user enable onedrive
    systemctl --user start onedrive
    ```

3. 查看日志

    ```text
    journalctl --user-unit onedrive -f
    ```

## VNC

1. 参考这篇文章： https://blog.csdn.net/zbgjhy88/article/details/85110220

2. tigervnc，`.vnc/xstartup`改一下。重启 vnc 服务。端口 5900+后面的数字。参考 b 站视频 BV1Qf4y1D7NP

## docker

> 参考 docker 的官方文档： https://docs.docker.com/engine/install/linux-postinstall/

一个可用的镜像：manjaro-with-zsh

1. 设置 docker 开机自启

    ```bash
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    ```

2. 需要配置 docker 在非 root 环境下运行。否则 vscode 插件没法识别。

    ```bash
    # 过时：sudo gpasswd -a ${USER} docker
    # 用下面这个
    sudo usermod -aG docker $USER
    # 重新启动终端
    ```

3. 关于 containerd.service 导致关机速度慢的问题

    有两种方法可以解决

    - 修改`/usr/lib/systemd/system/containerd.service`的`KillMode`，默认是`KillMode=process`，改成`KillMode=mixed`（我选用这种方法）

    - 修改`/usr/lib/systemd/system/docker.service`，让其依赖于`containerd.service`

        ```bash
        [Unit]
        ....
        After=network.target containerd.socket containerd.service
        Requires=containerd.socket containerd.service
        ```

## 终端下的计算器

1. bc

2. python

## brew

1. 安装

    按照 dotfiles 里的安装脚本可以一键执行

    参考：https://blog.csdn.net/baidu_40973299/article/details/108560242

2. 更换国内源

    ```bash
    git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
    git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/linuxbrew-core.git
    brew update
    ```

## EasyConnect

```text
https://vpn.wh.sdu.edu.cn
```

![1](assets/05-package-configuration/image_2021-07-02-12-48-59.png)

## zotero

> 参考： https://zhuanlan.zhihu.com/p/268375930

1. 设置数据文件夹位置

    ![image_2021-07-06-18-28-47](assets/05-package-configuration/image_2021-07-06-18-28-47.png)

1. 设置坚果云

    ![image_2021-07-06-18-29-09](assets/05-package-configuration/image_2021-07-06-18-29-09.png)

1. 设置直接获取英文文献

    > 特别注意可用的 Sci-Hub 域名有“http://sci-hub.st”，“http://sci-hub.do”（检测时间2020-11-04 20:33:23）。如果没有使用任何代理，由于网络环境问题，可能会有少部分从 Sci-Hub 下载的 PDF 出现损害的情况，这时你可以考虑将上述代码中的 https 改为 http，或者更换其他可用的域名，情况可能会好转。

    ```text
    # 用这个单行的，可以直接复制进去
        {     "name":"Sci-Hub",     "method":"GET",     "url":"https://sci-hubtw.hkvisa.net/{doi}",     "mode":"html",     "selector":"#pdf",     "attribute":"src",     "automatic":true }
    ```

    ![image_2021-07-06-18-34-31](assets/05-package-configuration/image_2021-07-06-18-34-31.png)

    ![image_2021-07-06-18-34-47](assets/05-package-configuration/image_2021-07-06-18-34-47.png)

    ![image_2021-07-06-18-34-58](assets/05-package-configuration/image_2021-07-06-18-34-58.png)

1. 安装 ZotFile 插件(和其他插件)

    > 此插件的原地址（下载 RELEASE）：https://github.com/jlegewie/zotfile
    >
    > 直接从官网下的话会出问题。因此从此文章的附件文件夹中下载（附件文件夹就是此文章的图片文件夹）

    ![image_2021-07-06-18-39-57](assets/05-package-configuration/image_2021-07-06-18-39-57.png)

    ![image_2021-07-06-18-40-38](assets/05-package-configuration/image_2021-07-06-18-40-38.png)

    ![image_2021-07-06-18-40-53](assets/05-package-configuration/image_2021-07-06-18-40-53.png)

    ![image_2021-07-06-18-41-02](assets/05-package-configuration/image_2021-07-06-18-41-02.png)

1. 设置移动端 papership

    特别注意，在 papership 验证会出现验证不成功，解决方法：打开坚果云官网，登录坚果云账号，在 zotero 文件夹新建空白的 lastsync.txt 文件，务必注意的是，必须使用坚果云自带的新建文件工具来新建 lastsync.txt 文件，不能通过手动上传的方式。如下图所示

    ![image_2021-07-06-18-39-21](assets/05-package-configuration/image_2021-07-06-18-39-21.png)

    ![image_2021-07-06-18-37-50](assets/05-package-configuration/image_2021-07-06-18-37-50.png)

    密码可以直接使用 zotero 的，不要再新建了

    ![image_2021-07-06-18-38-02](assets/05-package-configuration/image_2021-07-06-18-38-02.png)

1. zotero 与 notion 联动

    - 配置 zotero 搜索引擎

        在 zotero 的数据文件夹中，编辑`locate/engines.json`文件

        把下面的代码按照 json 规则添加到文件中。位置任意，但位置最终会体现在 zotero 菜单中。注意如果加在最后，那么需要删掉逗号。

        ```json
        {
            "_name": "notion",
            "_alias": "notion",
            "_description": "Zotero和notion联动，页面ID存在Call number（引用次数）字段",
            "_icon": "https://www.notion.so/images/favicon.ico",
            "_hidden": false,
            "_urlTemplate": "https://www.notion.so/{z:callNumber}",
            "_urlParams": [],
            "_urlNamespaces": {
                "z": "http://www.zotero.org/namespaces/openSearch#",
                "": "http://a9.com/-/spec/opensearch/1.1/"
            },
            "_iconSourceURI": "https://www.notion.so/images/favicon.ico"
        },
        ```

    - 在 zotero 的 Call number 字段加入 Notion 链接。注意去掉域名，只留下后面的 ysl2 之后的部分(包括 ysl2)
    - Zotero 选中文献，搜索引擎中点击 Notion，打开网页版 Notion 笔记

## firefox

关闭`从崩溃中恢复之前的会话`功能，这个功能如果开启会导致 polybar 的 bug

在 firefox 地址栏中输入`about:config`，然后搜索：

```text
# 把下面这个选项改成false
browser.sessionstore.resume_from_crash = true
```

## 测试摄像头：cheese 或者 xawtv

```bash
# 调用cheese
cheese

# 调用指定的摄像头
cheese -d /dev/video1
```

## lightdm

> 参考：https://wiki.archlinux.org/title/LightDM#Enabling_autologin

不建议用这个，除非通过预装的方式（已经配置好）。其实如果预装的话还比较好用，就算难用也能配置免密登录。

1. 编辑 lightdm 的配置文件，取消该行的注释，并添加要自动登录的用户名

    ```text
    /etc/lightdm/lightdm.conf
    -------------------------

    autologin-user=username
    ```

2. 你必须是`autologin`组的成员来使得自己登录时不用输入密码

    ```text
    groupadd -r autologin
    gpasswd -a username autologin
    ```

## drawio

1. 避免导出 svg 的 bug

    - 右键单击绘图画布的空白区域，然后从上下文菜单中选择“全选” 。
    - 在格式面板的 Text 选项卡中，取消选中 Word Wrap 和 Formatted Text。

    ![1](assets/05-package-configuration/svg-export-remove-text-formatting.gif)

## cuda 与 cudnn

> 参考：
>
> -   https://blog.csdn.net/weixin_41278720/article/details/81255265
> -   https://github.com/ypwhs/dl-engineer-guidebook/blob/master/docs/ubuntu-environment.md

### 无 root 权限安装 cuda

cuda 9.0 对应 cudnn 7.0

cuda 9.0：https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run

cudnn：https://developer.nvidia.com/rdp/cudnn-archive

需要根据系统提示来设置环境变量：

```bash
Please make sure that
 -   PATH includes /home/yusongli/.bin/cuda-9.0/bin
 -   LD_LIBRARY_PATH includes /home/yusongli/.bin/cuda-9.0/lib64, or, add /home/yusongli/.bin/cuda-9.0/lib64 to /etc/ld.so.conf and run ldconfig as root
```

### CUDA

-   最新版：[https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)
-   CUDA 10.2：[https://developer.nvidia.com/cuda-10.2-download-archive](https://developer.nvidia.com/cuda-10.2-download-archive)
-   CUDA 10.1：[https://developer.nvidia.com/cuda-10.1-download-archive-update2](https://developer.nvidia.com/cuda-10.1-download-archive-update2)
-   CUDA 10.0：[https://developer.nvidia.com/cuda-10.0-download-archive](https://developer.nvidia.com/cuda-10.0-download-archive)
-   旧版列表：[https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)

CUDA 是英伟达显卡进行各种高性能运算必备的库，不同软件包依赖的 CUDA 版本可能不同，你需要根据你所使用的深度学习框架选择合适的 CUDA 和 cuDNN 版本。

| 版本                                                                         | Windows 10                                                                                                                                    | Linux                                                                                                                                               |
| :--------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CUDA 10.2](https://developer.nvidia.com/cuda-10.2-download-archive)         | [cuda_10.2.89_441.22_win10.exe](http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_441.22_win10.exe)   | [cuda_10.2.89_440.33.01_linux.run](http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run)   |
| [CUDA 10.1](https://developer.nvidia.com/cuda-10.1-download-archive-update2) | [cuda_10.1.243_426.00_win10.exe](http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_426.00_win10.exe) | [cuda_10.1.243_418.87.00_linux.run](http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run) |
| [CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive)         | [cuda_10.0.130_411.31_win10.exe](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10)             | [cuda_10.0.130_410.48_linux.run](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux)                   |
| [CUDA 9.2](https://developer.nvidia.com/cuda-92-download-archive)            | [cuda_9.2.148_win10.exe](https://developer.nvidia.com/compute/cuda/9.2/Prod2/local_installers2/cuda_9.2.148_win10)                            | [cuda_9.2.148_396.37_linux.run](https://developer.nvidia.com/compute/cuda/9.2/Prod2/local_installers/cuda_9.2.148_396.37_linux)                     |
| [CUDA 9.1](https://developer.nvidia.com/cuda-91-download-archive)            | [cuda_9.1.85_win10.exe](https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_9.1.85_win10)                                | [cuda_9.1.85_387.26_linux.run](https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_9.1.85_387.26_linux)                        |
| [CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive)            | [cuda_9.0.176_win10.exe](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_win10-exe)                          | [cuda_9.0.176_384.81_linux.run](https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run)                  |
|                                                                              | 以下版本较低，推荐使用上面的版本。                                                                                                            |                                                                                                                                                     |
| [CUDA 8.0 GA2](https://developer.nvidia.com/cuda-80-ga2-download-archive)    | [cuda_8.0.61_win10.exe](https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_win10-exe)                           | [cuda_8.0.61_375.26_linux.run](https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run)                   |
| [CUDA 8.0 GA1](https://developer.nvidia.com/cuda-80-download-archive)        | [cuda_8.0.44_win10.exe](https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_win10-exe)                            | [cuda_8.0.44_linux.run](https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_linux-run)                                  |
| [CUDA 7.5](https://developer.nvidia.com/cuda-75-downloads-archive)           | [cuda_7.5.18_win10.exe](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_win10.exe)                    | [cuda_7.5.18_linux.run](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run)                          |
| [CUDA 7.0](https://developer.nvidia.com/cuda-toolkit-70)                     | [cuda_7.0.28_windows.exe](http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_windows.exe)                | [cuda_7.0.28_linux.run](http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/cuda_7.0.28_linux.run)                          |
| [CUDA 6.5](https://developer.nvidia.com/cuda-toolkit-65)                     | [cuda_6.5.14_windows_general_64.exe](http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_windows_general_64.exe) | [cuda_6.5.14_linux_64.run](http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run)                           |

### **cuDNN**

cuDNN 下载需要注册，地址如下：

-   最新版：[https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)
-   旧版：[https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive)

cuDNN 是英伟达推出的专门用于深度学习加速计算的库，一般来说比使用纯 CUDA 速度要快不少。比如 Keras 里有普通的 [LSTM](https://keras.io/layers/recurrent/#lstm) 以及 [CuDNNLSTM](https://keras.io/layers/recurrent/#cudnnlstm)，速度相差最高有十倍。如果没有设计特殊的结构，cuDNN 应该是你的首选。

你需要根据你所使用的深度学习框架选择合适的 CUDA 和 cuDNN 版本。

| cuDNN | CUDA9.0                                                                                                                                               | CUDA9.2                                                                                                                                               | CUDA10.0                                                                                                                                                | CUDA10.1                                                                                                                                                |
| :---- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 7.6.1 | [cudnn-9.0-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.0-linux-x64-v7.6.1.34.tgz) \(392.82MB\) | [cudnn-9.2-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.2-linux-x64-v7.6.1.34.tgz) \(396.89MB\) | [cudnn-10.0-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.0-linux-x64-v7.6.1.34.tgz) \(460.88MB\) | [cudnn-10.1-linux-x64-v7.6.1.34.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.1-linux-x64-v7.6.1.34.tgz) \(497.63MB\) |
| 7.6.0 | [cudnn-9.0-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.0-linux-x64-v7.6.0.64.tgz) \(374.59MB\) | [cudnn-9.2-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.2-linux-x64-v7.6.0.64.tgz) \(378.84MB\) | [cudnn-10.0-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.0-linux-x64-v7.6.0.64.tgz) \(440.90MB\) | [cudnn-10.1-linux-x64-v7.6.0.64.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.1-linux-x64-v7.6.0.64.tgz) \(477.61MB\) |
| 7.5.1 | [cudnn-9.0-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.0-linux-x64-v7.5.1.10.tgz) \(357.13MB\) | [cudnn-9.2-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.2-linux-x64-v7.5.1.10.tgz) \(361.63MB\) | [cudnn-10.0-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.0-linux-x64-v7.5.1.10.tgz) \(412.76MB\) | [cudnn-10.1-linux-x64-v7.5.1.10.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.1-linux-x64-v7.5.1.10.tgz) \(449.47MB\) |
| 7.5.0 | [cudnn-9.0-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.0-linux-x64-v7.5.0.56.tgz) \(357.11MB\) | [cudnn-9.2-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.2-linux-x64-v7.5.0.56.tgz) \(361.61MB\) | [cudnn-10.0-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.0-linux-x64-v7.5.0.56.tgz) \(412.76MB\) | [cudnn-10.1-linux-x64-v7.5.0.56.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.1-linux-x64-v7.5.0.56.tgz) \(449.46MB\) |
| 7.4.2 | [cudnn-9.0-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.0-linux-x64-v7.4.2.24.tgz) \(349.00MB\) | [cudnn-9.2-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.2-linux-x64-v7.4.2.24.tgz) \(353.84MB\) | [cudnn-10.0-linux-x64-v7.4.2.24.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-10.0-linux-x64-v7.4.2.24.tgz) \(404.82MB\) | -                                                                                                                                                       |
| 7.4.1 | [cudnn-9.0-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.0-linux-x64-v7.4.1.5.tgz) \(347.17MB\)   | [cudnn-9.2-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.2-linux-x64-v7.4.1.5.tgz) \(352.02MB\)   | [cudnn-10.0-linux-x64-v7.4.1.5.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-10.0-linux-x64-v7.4.1.5.tgz) \(403.12MB\)   | -                                                                                                                                                       |
| 7.3.1 | [cudnn-9.0-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.0-linux-x64-v7.3.1.20.tgz) \(344.85MB\) | [cudnn-9.2-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.2-linux-x64-v7.3.1.20.tgz) \(351.05MB\) | [cudnn-10.0-linux-x64-v7.3.1.20.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-10.0-linux-x64-v7.3.1.20.tgz) \(400.58MB\) | -                                                                                                                                                       |
| 7.3.0 | [cudnn-9.0-linux-x64-v7.3.0.29.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-9.0-linux-x64-v7.3.0.29.tgz) \(340.43MB\) | -                                                                                                                                                     | [cudnn-10.0-linux-x64-v7.3.0.29.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-10.0-linux-x64-v7.3.0.29.tgz) \(396.06MB\) | -                                                                                                                                                       |
| 7.2.1 | [cudnn-9.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-linux-x64-v7.2.1.38.tgz) \(331.19MB\) | [cudnn-9.2-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.2-linux-x64-v7.2.1.38.tgz) \(337.08MB\) | -                                                                                                                                                       | -                                                                                                                                                       |
| 7.1.4 | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-linux-x64-v7.1.tgz) \(390.26MB\)           | [cudnn-9.2-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.2-linux-x64-v7.1.tgz) \(401.58MB\)           | -                                                                                                                                                       | -                                                                                                                                                       |

以下版本较低，推荐使用上面的版本。

| cuDNN | CUDA6.5                                                                                                                            | CUDA7.0                                                                                                                                          | CUDA7.5                                                                                                                                      | CUDA8.0                                                                                                                                               | CUDA9.0                                                                                                                                               |
| :---- | :--------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7.2.1 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | [cudnn-8.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-8.0-linux-x64-v7.2.1.38.tgz) \(189.78MB\) | [cudnn-9.0-linux-x64-v7.2.1.38.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-linux-x64-v7.2.1.38.tgz) \(331.19MB\) |
| 7.1.4 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | -                                                                                                                                                     | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-linux-x64-v7.1.tgz) \(390.26MB\)           |
| 7.1.3 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | [cudnn-8.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-8.0-linux-x64-v7.1.tgz) \(245.96MB\)           | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-9.0-linux-x64-v7.1.tgz) \(387.77MB\)           |
| 7.1.2 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | [cudnn-8.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-8.0-linux-x64-v7.1.tgz) \(246.13MB\)           | [cudnn-9.0-linux-x64-v7.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-9.0-linux-x64-v7.1.tgz) \(387.42MB\)           |
| 7.0.5 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | [cudnn-8.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-8.0-linux-x64-v7.tgz) \(267.98MB\)               | [cudnn-9.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.0-linux-x64-v7.tgz) \(332.66MB\)               |
| 7.0.4 | -                                                                                                                                  | -                                                                                                                                                | -                                                                                                                                            | [cudnn-8.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-8.0-linux-x64-v7.tgz) \(267.98MB\)               | [cudnn-9.0-linux-x64-v7.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-9.0-linux-x64-v7.tgz) \(332.67MB\)               |
| 6.0   | -                                                                                                                                  | -                                                                                                                                                | [cudnn-7.5-linux-x64-v6.0.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-7.5-linux-x64-v6.0.tgz) \(109.43MB\)    | [cudnn-8.0-linux-x64-v6.0.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-8.0-linux-x64-v6.0.tgz) \(191.82MB\)             | -                                                                                                                                                     |
| 5.1   | -                                                                                                                                  | -                                                                                                                                                | [cudnn-7.5-linux-x64-v5.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-7.5-linux-x64-v5.1.tgz) \(77.18MB\)     | [cudnn-8.0-linux-x64-v5.1.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-8.0-linux-x64-v5.1.tgz) \(98.39MB\)              | -                                                                                                                                                     |
| 5     | -                                                                                                                                  | -                                                                                                                                                | [cudnn-7.5-linux-x64-v5.0-ga.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-7.5-linux-x64-v5.0-ga.tgz) \(75.66MB\) | [cudnn-8.0-linux-x64-v5.0-ga.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-8.0-linux-x64-v5.0-ga.tgz) \(94.58MB\)          | -                                                                                                                                                     |
| 4     | -                                                                                                                                  | [cudnn-7.0-linux-x64-v4.0-prod.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v4/cudnn-7.0-linux-x64-v4.0-prod.tgz) \(81.73MB\) | -                                                                                                                                            | -                                                                                                                                                     | -                                                                                                                                                     |
| 3     | -                                                                                                                                  | [cudnn-7.0-linux-x64-v3.0-prod.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v3/cudnn-7.0-linux-x64-v3.0-prod.tgz) \(63.81MB\) | -                                                                                                                                            | -                                                                                                                                                     | -                                                                                                                                                     |
| 2     | [cudnn-6.5-linux-x64-v2.tgz](https://developer.download.nvidia.com/compute/redist/cudnn/v2/cudnn-6.5-linux-x64-v2.tgz) \(15.18MB\) | -                                                                                                                                                | -                                                                                                                                            | -                                                                                                                                                     | -                                                                                                                                                     |

下面是 Windows 10 的各个版本的安装包：

| cuDNN | CUDA9.0                                                                                                                                                     | CUDA9.2                                                                                                                                                     | CUDA10.0                                                                                                                                                      | CUDA10.1                                                                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7.6.1 | [cudnn-9.0-windows10-x64-v7.6.1.34.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.0-windows10-x64-v7.6.1.34.zip) (201.80MB) | [cudnn-9.2-windows10-x64-v7.6.1.34.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-9.2-windows10-x64-v7.6.1.34.zip) (203.54MB) | [cudnn-10.0-windows10-x64-v7.6.1.34.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.0-windows10-x64-v7.6.1.34.zip) (237.73MB) | [cudnn-10.1-windows10-x64-v7.6.1.34.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.1/cudnn-10.1-windows10-x64-v7.6.1.34.zip) (263.75MB) |
| 7.6.0 | [cudnn-9.0-windows10-x64-v7.6.0.64.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.0-windows10-x64-v7.6.0.64.zip) (192.70MB) | [cudnn-9.2-windows10-x64-v7.6.0.64.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-9.2-windows10-x64-v7.6.0.64.zip) (194.52MB) | [cudnn-10.0-windows10-x64-v7.6.0.64.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.0-windows10-x64-v7.6.0.64.zip) (227.76MB) | [cudnn-10.1-windows10-x64-v7.6.0.64.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.0/cudnn-10.1-windows10-x64-v7.6.0.64.zip) (253.77MB) |
| 7.5.1 | [cudnn-9.0-windows10-x64-v7.5.1.10.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.0-windows10-x64-v7.5.1.10.zip) (184.06MB) | [cudnn-9.2-windows10-x64-v7.5.1.10.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-9.2-windows10-x64-v7.5.1.10.zip) (185.99MB) | [cudnn-10.0-windows10-x64-v7.5.1.10.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.0-windows10-x64-v7.5.1.10.zip) (213.77MB) | [cudnn-10.1-windows10-x64-v7.5.1.10.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.1/cudnn-10.1-windows10-x64-v7.5.1.10.zip) (239.76MB) |
| 7.5.0 | [cudnn-9.0-windows10-x64-v7.5.0.56.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.0-windows10-x64-v7.5.0.56.zip) (184.05MB) | [cudnn-9.2-windows10-x64-v7.5.0.56.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-9.2-windows10-x64-v7.5.0.56.zip) (185.98MB) | [cudnn-10.0-windows10-x64-v7.5.0.56.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.0-windows10-x64-v7.5.0.56.zip) (213.78MB) | [cudnn-10.1-windows10-x64-v7.5.0.56.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.5.0/cudnn-10.1-windows10-x64-v7.5.0.56.zip) (239.75MB) |
| 7.4.2 | [cudnn-9.0-windows10-x64-v7.4.2.24.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.0-windows10-x64-v7.4.2.24.zip) (180.04MB) | [cudnn-9.2-windows10-x64-v7.4.2.24.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-9.2-windows10-x64-v7.4.2.24.zip) (182.13MB) | [cudnn-10.0-windows10-x64-v7.4.2.24.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.2/cudnn-10.0-windows10-x64-v7.4.2.24.zip) (209.84MB) | -                                                                                                                                                             |
| 7.4.1 | [cudnn-9.0-windows10-x64-v7.4.1.5.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.0-windows10-x64-v7.4.1.5.zip) (179.09MB)   | [cudnn-9.2-windows10-x64-v7.4.1.5.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-9.2-windows10-x64-v7.4.1.5.zip) (181.16MB)   | [cudnn-10.0-windows10-x64-v7.4.1.5.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.4.1/cudnn-10.0-windows10-x64-v7.4.1.5.zip) (208.93MB)   | -                                                                                                                                                             |
| 7.3.1 | [cudnn-9.0-windows10-x64-v7.3.1.20.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.0-windows10-x64-v7.3.1.20.zip) (177.85MB) | [cudnn-9.2-windows10-x64-v7.3.1.20.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-9.2-windows10-x64-v7.3.1.20.zip) (180.61MB) | [cudnn-10.0-windows10-x64-v7.3.1.20.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.1/cudnn-10.0-windows10-x64-v7.3.1.20.zip) (207.59MB) | -                                                                                                                                                             |
| 7.3.0 | [cudnn-9.0-windows10-x64-v7.3.0.29.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-9.0-windows10-x64-v7.3.0.29.zip) (176.12MB) | -                                                                                                                                                           | [cudnn-10.0-windows10-x64-v7.3.0.29.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.3.0/cudnn-10.0-windows10-x64-v7.3.0.29.zip) (205.84MB) | -                                                                                                                                                             |
| 7.2.1 | [cudnn-9.0-windows10-x64-v7.2.1.38.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-windows10-x64-v7.2.1.38.zip) (171.64MB) | [cudnn-9.2-windows10-x64-v7.2.1.38.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.2-windows10-x64-v7.2.1.38.zip) (174.26MB) | -                                                                                                                                                             | -                                                                                                                                                             |
| 7.1.4 | [cudnn-9.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-windows10-x64-v7.1.zip) (201.39MB)           | [cudnn-9.2-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.2-windows10-x64-v7.1.zip) (206.81MB)           | -                                                                                                                                                             | -                                                                                                                                                             |

| cuDNN | CUDA6.5 | CUDA7.0 | CUDA7.5                                                                                                                                            | CUDA8.0                                                                                                                                                     | CUDA9.0                                                                                                                                                     |
| ----- | ------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7.2.1 | -       | -       | -                                                                                                                                                  | [cudnn-8.0-windows10-x64-v7.2.1.38.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-8.0-windows10-x64-v7.2.1.38.zip) (100.06MB) | [cudnn-9.0-windows10-x64-v7.2.1.38.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-windows10-x64-v7.2.1.38.zip) (171.64MB) |
| 7.1.4 | -       | -       | -                                                                                                                                                  | -                                                                                                                                                           | [cudnn-9.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.4/cudnn-9.0-windows10-x64-v7.1.zip) (201.39MB)           |
| 7.1.3 | -       | -       | -                                                                                                                                                  | [cudnn-8.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-8.0-windows10-x64-v7.1.zip) (128.37MB)           | [cudnn-9.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.3/cudnn-9.0-windows10-x64-v7.1.zip) (200.17MB)           |
| 7.1.2 | -       | -       | -                                                                                                                                                  | [cudnn-8.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-8.0-windows10-x64-v7.1.zip) (128.47MB)           | [cudnn-9.0-windows10-x64-v7.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.1.2/cudnn-9.0-windows10-x64-v7.1.zip) (200.00MB)           |
| 7.0.5 | -       | -       | -                                                                                                                                                  | [cudnn-8.0-windows10-x64-v7.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-8.0-windows10-x64-v7.zip) (139.68MB)               | [cudnn-9.0-windows10-x64-v7.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.0-windows10-x64-v7.zip) (172.86MB)               |
| 7.0.4 | -       | -       | -                                                                                                                                                  | [cudnn-8.0-windows10-x64-v7.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-8.0-windows10-x64-v7.zip) (139.72MB)               | [cudnn-9.0-windows10-x64-v7.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v7.0.4/cudnn-9.0-windows10-x64-v7.zip) (172.86MB)               |
| 6.0   | -       | -       | [cudnn-7.5-windows10-x64-v6.0.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-7.5-windows10-x64-v6.0.zip) (56.01MB)     | [cudnn-8.0-windows10-x64-v6.0.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-8.0-windows10-x64-v6.0.zip) (101.57MB)             | -                                                                                                                                                           |
| 5.1   | -       | -       | [cudnn-7.5-windows10-x64-v5.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-7.5-windows10-x64-v5.1.zip) (40.15MB)     | [cudnn-8.0-windows10-x64-v5.1.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-8.0-windows10-x64-v5.1.zip) (53.95MB)              | -                                                                                                                                                           |
| 5     | -       | -       | [cudnn-7.5-windows10-x64-v5.0-ga.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-7.5-windows10-x64-v5.0-ga.zip) (39.41MB) | [cudnn-8.0-windows10-x64-v5.0-ga.zip](https://developer.download.nvidia.com/compute/redist/cudnn/v5/cudnn-8.0-windows10-x64-v5.0-ga.zip) (51.21MB)          | -                                                                                                                                                           |

## 字体

```text
# 查看当前系统安装的所有字体
fc-list
# 刷新字体缓存
fc-cache -fv
```

参考： https://wiki.archlinux.org/index.php/Fonts_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

## OCR

安装后端：

```bash
tesseract
tesseract-data-chi_sim
tesseract-data-eng
```

安装前端：

```bash
ocrfeeder
```

## 向日葵

```bash
yay -S sunloginclient
```

启动服务

```bash
sudo systemctl enable --now runsunloginclient.service
```

## tensorflow套件

1. 版本匹配关系

    https://tensorflow.google.cn/install/source?hl=en#tested_build_configurations

1. cuda
    指定目录的 上级目录 需要预先手动创建好

    ```bash
    # 非root安装示例
    sh cuda_10.2.89_440.33.01_linux.run --silent --toolkit --toolkitpath=$HOME/.bin/cuda-10.1 --defaultroot=$HOME/.bin/cuda-10.1
    # 如果这一步出现log file not open，就让服务器管理员用sudo把这个log file删掉

    # 在~/.bashrc文件里添加环境变量(加入这两句话)
    export PATH="$HOME/.bin/cuda-10.1/bin:$PATH"
    export LD_LIBRARY_PATH="$HOME/.bin/cuda-10.1/lib64"
    ```

1. cudnn

    ```bash
    # 解压tgz文件
    tar zxvf 文件名.tgz
    ```

    - 将解压出来的文件夹中的`include`子文件夹和`lib64`子文件夹里的内容，分别移动到上述第二步指定的cuda安装路径下面对应的`include`文件夹和`lib64`(或者`lib`)文件夹下面，
    - 如果之前cudnn的`include`子文件夹里面包含`so.7`结尾的文件(比如`libcudnn.so.7`)，需要将这些移动后的文件位置(对应于`$HOME/.bin/include/libcudnn.so.7`)创建软连接到`$HOME/.bin/lib64/libcudnn.so.7`
