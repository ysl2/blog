# [windows] Localhost configs

`~/.config/alacritty/alacritty.localhost.toml`

```toml
[window]
opacity = 0.7
startup_mode = 'Maximized'

[font]
size = 13

[terminal]
shell = { program = 'pwsh', args = ['-NoLogo -WorkingDirectory ~'] }
```
