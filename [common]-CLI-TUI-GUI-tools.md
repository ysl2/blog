# CLI TUI GUI tools

> Ref: <https://github.com/johnalanwoods/maintained-modern-unix>

| Basic Tool Name | Type (CLI/TUI/GUI) | Note                         | Installation |
| --------------- | ------------------ | ---------------------------- | ------------ |
| `nmtui`         | TUI                | Network                      |              |
| `brightnessctl` | CLI                | Brightness                   |              |
| `redshift`      | CLI                | Brightness                   |              |
| `bluetuith`     | TUI                | Bluetooth                    |              |
| `xrandr`        | CLI                | Monitor control              |              |
| `arandr`        | GUI                | Monitor control              |              |
| `termscp`       | TUI                | SFTP in terminal             |              |
| `nvtop`         | TUI                | Check GPU status in terminal |              |
| `ncdu`          | TUI                | Check disk usage             |              |
| `htop`          | TUI                | Check system status          |              |
| `feh`           | TUI                | For desktop wallpaper        |              |
| `picom`         | TUI                | Window transparent           |              |
| `flameshot`     | GUI                | Image capture                |              |
| `dunst`         | CLI                | Show notification            |              |
| `udiskie`       | GUI                | USB mount                    |              |
| `tlp`           | CLI                | Power saver                  |              |
| `lxappearance`  | GUI                | GTK theme changer            |              |

| Other Tool Name                                               | Type (CLI/TUI/GUI) | Note                                          | Installation |
| ------------------------------------------------------------- | ------------------ | --------------------------------------------- | ------------ |
| `bluetoothctl`                                                | CLI                | Bluetooth                                     |              |
| `img2pdf`                                                     | CLI                | Image to PDF, for Latex                       |              |
| `pdf2svg`                                                     | CLI                | PDF to SVG, for Typst                         |              |
| `qrcp`                                                        | CLI                | File transfer                                 |              |
| [`carbonyl`](https://github.com/fathyb/carbonyl)              | TUI                | Browser in terminal                           | By npm       |
| `surf`                                                        | GUI                | Lightweight browser                           |              |
| [`trans`](https://github.com/soimort/translate-shell)         | CLI                | Language translate                            |              |
| `shell_gpt`                                                   | CLI                | GPT in shell                                  |              |
| `frp`                                                         | CLI                | Proxy forward                                 |              |
| `bottom`                                                      | TUI                | Check system status                           |              |
| [`crlf2lf`](https://github.com/XadillaX/node-crlf2lf)         | CLI                | Change file ending                            |              |
| `zathura`                                                     | GUI                | PDF Viewer                                    |              |
| `chafa`                                                       | CLI                | Terminal image renderer                       |              |
| [`gh2md`](https://github.com/mattduck/gh2md)                  | CLI                | Export github issues                          |              |
| [`tldraw`](https://github.com/tldraw/tldraw)                  | GUI                | Whiteboard                                    |              |
| [`wechat`](https://github.com/web1n/wechat-universal-flatpak) | GUI                | Official WeChat (but with unofficial flatpak) |              |
| [`qq`](https://im.qq.com/linuxqq/index.shtml)                 | GUI                | Official QQ                                   |              |
| `gh`                                                          | CLI                | Official Github CLI                           | By brew      |
| `color-picker`                                                | GUI                | Color picker                                  | By apt       |
| `trzsz`                                                       | CLI                | lrzsz for tmux                                | By brew      |
| `mycli`                                                       | CLI                | mysql                                         | By brew      |
| `gh-dash`                                                     | TUI                | github                                        | By gh        |

## Brightness

```bash
#  Increase by 3%
brightnessctl set 3%+

# decrease by 3%
brightnessctl set 3%-
```

## redshift

```bash
# install
sudo apt install redshift
# Set to default night mode colur
redshift -P -O 4500K
# Reset
redshift -x
```

## Bluetooth: bluetoothctl

```
要使用 bluetoothctl 连接蓝牙设备，您可以按照以下步骤进行操作：

打开终端并输入 bluetoothctl 进入蓝牙控制台。

输入 power on，确保蓝牙适配器已经开启。

输入 agent on，启用默认的蓝牙代理。

输入 scan on，开始扫描周围的蓝牙设备。等待一段时间，直到您看到要连接的设备的 MAC 地址。

输入 pair <device MAC>，将 <device MAC> 替换为您要连接的设备的 MAC 地址。这将发起配对过程。

如果需要输入配对码，按照提示进行操作。配对码通常会在蓝牙设备上显示或者在设备的用户手册中提供。

输入 trust <device MAC>，将设备标记为受信任的设备，以便将来自动连接。

输入 connect <device MAC>，将 <device MAC> 替换为您要连接的设备的 MAC 地址。这将尝试建立与设备的连接。

如果连接成功，您应该会在终端中看到一条消息确认连接成功。

请注意，上述步骤中的 <device MAC> 是要连接的蓝牙设备的 MAC 地址。您可以在扫描步骤中获取它。此外，根据设备的类型和要求，可能还需要进行其他步骤。如果您遇到任何问题，请参考蓝牙设备的用户手册或官方文档，以获取更详细的指导。
```

## Convert image format

img -> pdf

```bash
pip install img2pdf

img2pdf *.jpg -o output.pdf
```

pdf -> svg

```bash
sudo apt install pdf2svg
```

## Audio: alsamixer

For headphone settings:

<img src="assets/[common]-CLI-TUI-GUI-tools/img/2025-07-13-11-44-36.png" alt="" width=100%>

Or amixer

```bash
amixer -M get Master
amixer -M set Master 0%
amixer -M set Master 5%+
```
