---
title: "[mac] Installation"
number: 89
url: https://github.com/ysl2/.dotfiles/discussions/89
createdAt: 2025-05-02T13:24:23Z
lastEditedAt: 2025-06-27T14:38:11Z
updatedAt: 2025-06-27T14:39:58Z
author: ysl2
category: mac
labels: []
countZH: 80
countEN: 270
filename: 2505-[mac]-Installation
---

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

```
❯ brew list
==> Formulae
adwaita-icon-theme		harfbuzz			libusb				pango
aom				hicolor-icon-theme		libuv				pcre2
at-spi2-core			highway				libvmaf				pinentry
atuin				htop				libx11				pixman
borders				icu4c@77			libxau				pkgconf
brotli				imath				libxcb				poppler
c-ares				intltool			libxdmcp			python@3.13
ca-certificates			jbig2dec			libxext				readline
cairo				jpeg-turbo			libxfixes			reattach-to-user-namespace
certifi				jpeg-xl				libxi				redshift
chafa				json-c				libxrender			ripgrep
cmake				json-glib			libxtst				rustup
dbus				lazygit				little-cms2			sketchybar
desktop-file-utils		leptonica			lpeg				sphinx-doc
fastfetch			lf				luajit				sqlite
fontconfig			libarchive			luv				starship
freetype			libassuan			lz4				switchaudio-osx
fribidi				libavif				lzo				synctex
fzf				libb2				meson				tesseract
gdk-pixbuf			libdeflate			mpdecimal			tmux
gettext				libepoxy			mujs				tree-sitter
giflib				libevent			mupdf				unbound
girara				libgcrypt			ncdu				unibilium
glib				libgpg-error			ncurses				utf8proc
gmp				libidn2				neovim				uv
gnu-sed				libksba				nettle				webp
gnupg				libmagic			ninja				xorgproto
gnutls				libnghttp2			node				xz
go				libnotify			npth				zathura
gpgme				libpng				nspr				zathura-pdf-mupdf
graphite2			libpthread-stubs		nss				zathura-pdf-poppler
gsettings-desktop-schemas	librsvg				openexr				zlib
gtk+3				libtasn1			openjpeg			zstd
gtk-mac-integration		libtiff				openssl@3
gumbo-parser			libunistring			p11-kit

==> Casks
aerospace			font-fira-code-nerd-font	parallels			snipaste
alt-tab				hammerspoon			quickrecorder
baidunetdisk			jiggler				raycast
cursorcerer			keycastr			scroll-reverser
```

### 特殊依赖安装

```
brew install rustup
rustup-init
```

## 全局配置

```
defaults write -g NSAutomaticWindowAnimationsEnabled -bool false
defaults write -g NSAutomaticPeriodSubstitutionEnabled -bool false
defaults write -g ApplePressAndHoldEnabled -bool false
```

---

<img width="715" alt="image" src="https://github.com/user-attachments/assets/652ae178-ebff-4119-b171-37ce9c26f633" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/eafc4890-6112-4276-af98-e32532be35bd" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/1016303c-2ed8-4587-8f8b-2b1052855ad5" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/07968bbb-4420-4d02-840b-66ab3edafb0e" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/2d1c079d-ce82-45c9-b0e7-9120c0980595" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/a770d724-867a-4c22-b258-c6c1e4fb4160" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/283d55cb-a3dc-4f21-982d-4b61c9703e8a" />
<img width="715" alt="image" src="https://github.com/user-attachments/assets/0b175b79-7eca-4e5b-bf61-44db7d2e91bb" />
<img width="715" alt="Clipboard_Screenshot_1748329272" src="https://github.com/user-attachments/assets/bf245fe4-bbed-4f60-a914-0257fc84f276" />

---

<img width="556" alt="image" src="https://github.com/user-attachments/assets/008dc3da-0a7c-4834-ae09-9e9a82041ed6" />
<img width="556" alt="image" src="https://github.com/user-attachments/assets/8f3b89cc-339a-4dbf-8805-4a6d13719645" />

---

<img width="560" alt="image" src="https://github.com/user-attachments/assets/4376d5f9-70fb-44af-83f6-1aac064bd8dd" />
<img width="560" alt="image" src="https://github.com/user-attachments/assets/00dc7ba1-4e66-4d8c-a1a3-f7f4add57cff" />

---

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/f772bcb2-1761-41ba-b0d8-b9f7c64e9596" />
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/0877d956-8ebb-461a-918d-506872ac7917" />
<img width="1000" alt="image" src="https://github.com/user-attachments/assets/ec067083-edcd-420d-a67f-0c26daabbf91" />

---

<img width="510" alt="image" src="https://github.com/user-attachments/assets/a2521615-a342-4a96-acd6-4a488c5813e0" />

---

<img width="800" alt="image" src="https://github.com/user-attachments/assets/a1007869-9f8d-45d9-9444-3846a53a49a2" />

---

<img width="400" alt="image" src="https://github.com/user-attachments/assets/0ad51e3b-6361-40f2-9ed4-78f73613c5e4" />
<img width="400" alt="image" src="https://github.com/user-attachments/assets/4d201f5e-f22e-4e1b-8bb5-3d2d3ddfe18c" />

---

<img width="884" alt="image" src="https://github.com/user-attachments/assets/052a7f6c-977d-49b6-b0ce-e636650f5ef6" />

---

<img width="403" alt="image" src="https://github.com/user-attachments/assets/c66b4694-24fd-4891-b304-75bc01e1a096" />
<img width="350" alt="image" src="https://github.com/user-attachments/assets/2a5bc34b-90cc-475e-a653-aba8b913c8b3" />
