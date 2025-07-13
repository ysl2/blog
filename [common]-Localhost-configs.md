# [common] Localhost configs

`/home/yusongli/.dosbox/dosbox.localhost.conf`

```gitconfig
[autoexec]
mount c /home/yusongli/Documents/asm/dependencies/MASM
c:
```

---

`~/.ssh/config.localhost`

```text
Host hd202
    HostName abc.cn
    User yusongli
    Port 23332
    Identityfile ~/.ssh/yusongli_202

Host i53
    HostName 219.231.164.69
    User yusongli
    Port 2444
```

---

vim hot setting

```vimscript
set nu rnu sb spr et ts=4 sw=4
```

vim hot settings for single file

```bash
# vim: set et ts=4 sw=4:
```

---

`~/.config/neovide/.config.toml`

```toml
[font]
normal = ["FiraCode Nerd Font"]
size = 15
```

---

`~/.wezterm.localhost.lua`

```lua
return {
  window_background_opacity = 0.7
}
```

---

`~/.tmux.localhost.conf`

```bash
# NOTE: Must be absolute path here.
set-option -g default-shell "/home/yusongli/.vocal/nushell/bin/nu"
```

---

`~/.config/alacritty/alacritty.localhost.toml`

```toml
[font]
size = 15

[window]
opacity = 0.7
# opacity = 1

# [terminal]
# shell = "nu"

# NOTE: For some specific situation, e.g, MacBook Pro
# [keyboard]
# bindings = [
#     { key = '[', mods = 'Shift|Alt',  mode = '~Search',    action = 'ToggleViMode'   },
#     { key = '[', mods = 'Shift|Alt',  mode = 'Vi|~Search', action = 'ScrollToBottom' },
#     { key = '[', mods = 'Shift|Alt',  mode = 'Vi|~Search', action = 'ClearSelection' },
# ]
```

---

`~/.vocal/0/scripts/wm/autostart.localhost.sh`

```bash
#!/bin/bash

# Small and big:
# xrandr --output eDP-1 --mode 1920x1080 --pos 320x1440 --rotate normal --output HDMI-1 --primary --mode 2560x1440 --pos 0x0 --rotate normal --output DP-1 --off --output HDMI-2 --off
# Small and middle:
xrandr --output eDP-1 --mode 1920x1080 --pos 0x1024 --rotate normal --output HDMI-1 --off --output DP-1 --primary --mode 1280x1024 --pos 320x0 --rotate normal --output HDMI-2 --off
# Small and TV:
# xrandr --output eDP-1 --mode 1920x1080 --pos 0x768 --rotate normal --output HDMI-1 --primary --mode 1360x768 --pos 280x0 --rotate normal --output DP-1 --off --output HDMI-2 --off
feh --bg-fill /usr/share/desktop-base/emerald-theme/wallpaper/contents/images/2560x1440.svg
# feh --bg-fill ~/Pictures/wallpapers/2560x1440.svg
# feh --bg-fill ~/Pictures/flowers.jpg
# swaybg -i ~/Pictures/wall.png -m fill
fcitx5 &
udiskie --no-automount --no-notify --tray &
# cfw &
```

---

`~/.gitconfig.localhost`

```gitconfig
[user]
        name = xxx
        email = xxx@xxx.com
; [merge]
;         conflictstyle = zdiff3
; [url "https://ghfast.top/https://"]
;         insteadOf = "https://"
```

---

`~/.config/kitty/kitty.localhost.conf`

```yaml
background_opacity 0.7
```

---

`~/.bashrc.localhost.pre`

```bash
#!/bin/bash
MYCONDA=/home/yusongli/.vocal/miniconda3
MYTMUX=/usr/bin/tmux
```

---

`~/.bashrc.localhost.post`

```bash
#!/bin/bash

# Ref: https://www.python.org/downloads/release/python-2718/
# Setting PATH for Python 2.7
# The original version is saved in .zprofile.pysave
# PATH="${PATH}:/Library/Frameworks/Python.framework/Versions/2.7/bin"
# export PATH

export OPENAI_API_KEY

alias weterm="trzsz -d ssh ${WECOM_ID}@${JUMPSERVER_IP} -p ${JUMPSERVER_PORT}"
alias ali="trzsz -d ssh ${ALI_USER}@${ALI_HOST} -p ${ALI_PORT}"
alias psql='docker exec -it mypostgres /usr/bin/psql'

PP() {
    http_proxy=127.0.0.1:${COMPANY_PORT} https_proxy=127.0.0.1:${COMPANY_PORT} "$@"
}

# function cd {
#     builtin cd "$@"
#     command -v conda &> /dev/null && conda_env
# }
#
# function conda_env {
#     [[ $PWD/ == $HOME/Documents/TCSTest/* ]] && source venv/bin/activate
#     [[ $PWD/ == $HOME/Documents/tcs-test-image/* ]] && conda activate tcs-test-image
# }
```

---

- `~/.config/termscp/config.toml`
- `/Users/yusongli/Library/Application Support/termscp/config.toml`

```
[user_interface]
text_editor = "/opt/homebrew/bin/nvim"
default_protocol = "SFTP"
show_hidden_files = false
check_for_updates = true
prompt_on_file_replace = true
notifications = true
notification_threshold = 536870912

[remote]
ssh_config = "/Users/yusongli/.ssh/config"

[remote.ssh_keys]
"yusongli@hduiipl.cn" = "/Users/yusongli/Library/Application Support/termscp/.ssh/yusongli@hduiipl.cn.key"
```
