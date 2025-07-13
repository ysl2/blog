# ssh

## add ssh host alias, and ssh-copy-id on windows

```powershell
# $HOME\.pwshrc.localhost.ps1

# NOTE: The function name must starts with a letter.
function s53 {
    ssh username@localhost -p 22
}

# You can use it in powershell by `s53`
```

```powershell
# NOTE: The double quotes.
ssh-copy-id "username@localhost -p 22"
```

## Install ssh on macOS

```bash
brew install openssh
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

Restart ssh service after modifying the ssh configuration file:

```bash
sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

## Change ssh port

```bash
sudo vim /etc/ssh/sshd_config

# Port 22
Port 2222

sudo systemctl restart sshd
```

## Remove an entry from `~/.ssh/known_hosts`

```bash
ssh-keygen -R [10.0.224.7]:36000
# Or:
ssh-keygen -R 10.0.224.7 -p 36000
```

## trzsz

> Ref: <https://github.com/trzsz/trzsz-go/releases>

1. 在本地连接堡垒机的时候：

   ```bash
   # 第一次使用时，本地先安装：
   # brew install trzsz-go

   trzsz -d ssh xxxx.xxxx
   ```

1. 中间无论经过多少次中转，都不需要trzsz

1. 到达最终目标机器的时候，用目标机器上的trz或者tsz传输文件（通过最上面的Ref链接下载rpm包，在目标机器上安装trzsz）
