# [mac] Home

## 网络设置与配置恢复

- 手机在mihomo party的github release页面下载dmg，发送到mac上安装。导入节点信息
- `xcode-select --install`
- 手动添加ssh的github 443端口配置
- 创建ssh keypair并添加到github
- git clone dotfiles和dotlinks -b mac，并执行恢复动作

## 依赖安装

```
/bin/bash -c "$(curl -fsSL https://ghfast.top/https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 包列表

```text
❯ brew list --installed-on-request
atuin
bash
borders
chafa
docker-compose
fastfetch
fzf
gnu-sed
go
htop
lazygit
lf
ncdu
neovim
node
pngpaste
reattach-to-user-namespace
redshift
ripgrep
rustup
sketchybar
starship
switchaudio-osx
tmux
trzsz-go
uv
wget
zathura
zathura-pdf-mupdf
zathura-pdf-poppler
```

```text
❯ brew list --casks
aerospace			cursorcerer			jiggler				parallels			scroll-reverser
alt-tab				docker				keycastr			quickrecorder			snipaste
baidunetdisk			font-fira-code-nerd-font	obsidian			raycast
```

### 特殊依赖安装

```
brew install rustup
rustup-init
```

### Cleanup

```bash
brew cleanup --prune=all -s --dry-run
brew cleanup --prune=all -s
```

## 全局配置

```
defaults write -g NSAutomaticWindowAnimationsEnabled -bool false
defaults write -g NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write -g ApplePressAndHoldEnabled -bool false
```

## System settings

![](assets/[mac]-Home/2025-07-09-09-07-43.png)

![](assets/[mac]-Home/2025-07-09-13-49-23.png)

![](assets/[mac]-Home/2025-07-09-13-50-14.png)

![](assets/[mac]-Home/2025-07-09-13-51-02.png)

![](assets/[mac]-Home/2025-07-09-13-52-18.png)

![](assets/[mac]-Home/2025-07-09-13-52-53.png)

![](assets/[mac]-Home/2025-07-09-13-53-44.png)

![](assets/[mac]-Home/2025-07-09-13-54-24.png)

![](assets/[mac]-Home/2025-07-09-13-55-08.png)

## Other settings

![](assets/[mac]-Home/2025-07-09-22-51-58.png)

![](assets/[mac]-Home/2025-07-09-22-53-49.png)

---

![](assets/[mac]-Home/2025-07-09-22-55-03.png)

![](assets/[mac]-Home/2025-07-09-22-56-24.png)

---

![](assets/[mac]-Home/2025-07-09-22-57-44.png)

![](assets/[mac]-Home/2025-07-09-22-58-51.png)

![](assets/[mac]-Home/2025-07-09-23-00-03.png)

---

![](assets/[mac]-Home/2025-07-09-23-01-21.png)

---

![](assets/[mac]-Home/2025-07-09-23-02-26.png)

---

![](assets/[mac]-Home/2025-07-09-23-03-22.png)

![](assets/[mac]-Home/2025-07-09-23-04-07.png)

---

![](assets/[mac]-Home/2025-07-09-23-05-39.png)

---

![](assets/[mac]-Home/2025-07-09-23-06-37.png)

![](assets/[mac]-Home/2025-07-09-23-07-27.png)
