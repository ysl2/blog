# [mac] Home

## 网络设置与配置恢复

- 手机在mihomo party的github release页面下载dmg，发送到mac上安装。导入节点信息
- `xcode-select --install`
- 手动添加ssh的github 443端口配置
- 创建ssh keypair并添加到github
- git clone dotfiles和dotlinks -b mac，并执行恢复动作

## 依赖安装

```bash
/bin/bash -c "$(curl -fsSL https://ghfast.top/https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 包列表

```text
❯ brew list -1 --installed-on-request
atuin
autossh
bash
borders
chafa
colima
docker
docker-buildx
docker-compose
fastfetch
fzf
gemini-cli
gnu-sed
go
htop
kind
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
❯ brew list -1 --casks
aerospace
alt-tab
baidunetdisk
chatbox
cursorcerer
font-fira-code-nerd-font
jiggler
keycastr
obsidian
parallels
quickrecorder
raycast
scroll-reverser
snipaste
```

### 特殊依赖安装

```bash
brew install rustup
rustup-init
```

### Cleanup

```bash
brew cleanup --prune=all -s --dry-run
brew cleanup --prune=all -s
```

## 全局配置

```bash
defaults write -g NSAutomaticWindowAnimationsEnabled -bool false
defaults write -g NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write -g ApplePressAndHoldEnabled -bool false
```

## System settings

<img src="assets/[mac]-Home/img/2025-07-09-09-07-43.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-49-23.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-50-14.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-51-02.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-52-18.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-52-53.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-53-44.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-54-24.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-13-55-08.png" alt="" width=100%>

## Other settings

<img src="assets/[mac]-Home/img/2025-07-09-22-51-58.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-22-53-49.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-22-55-03.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-22-56-24.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-22-57-44.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-22-58-51.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-23-00-03.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-23-01-21.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-23-02-26.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-23-03-22.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-23-04-07.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-23-05-39.png" alt="" width=100%>

---

<img src="assets/[mac]-Home/img/2025-07-09-23-06-37.png" alt="" width=100%>

<img src="assets/[mac]-Home/img/2025-07-09-23-07-27.png" alt="" width=100%>
