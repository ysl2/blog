---
title: "[common] Localhost configs"
number: 93
url: https://github.com/ysl2/.dotfiles/discussions/93
createdAt: 2025-05-04T05:54:07Z
lastEditedAt: 2025-06-27T14:41:07Z
updatedAt: 2025-06-27T14:41:32Z
author: ysl2
category: common
labels: []
countZH: 0
countEN: 220
filename: 2505-[common]-Localhost-configs
---

`~/.config/alacritty/alacritty.localhost.toml`

```toml
[font]
size = 18

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
#!/bin/sh

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

```
[user]
        name = xxx
        email = xxx@xxx.com
```