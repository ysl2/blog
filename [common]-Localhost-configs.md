# [common] Localhost configs

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
feh --bg-fill ~/Pictures/wallpapers/2560x1440.svg
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
