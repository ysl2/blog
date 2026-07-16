# zathura

## Installation

### Linux installation

```bash
sudo apt install zathura
```

### Mac installation

> Ref: <https://github.com/homebrew-zathura/homebrew-zathura>

```bash
# For zathura in vimtex
# Ref: https://github.com/zegervdv/homebrew-zathura?tab=readme-ov-file#osx_native_integration
brew tap homebrew-zathura/zathura
brew install zathura --with-synctex
# brew install zathura-pdf-poppler
# d=$(brew --prefix zathura)/lib/zathura ; mkdir -p $d ; for n in cb djvu pdf-poppler ps ; do p=$(brew --prefix zathura-$n)/lib$n.dylib ; [[ -f $p ]] && ln -s $p $d ; done
brew install zathura-pdf-poppler
mkdir -p $(brew --prefix zathura)/lib/zathura
ln -sf $(brew --prefix zathura-pdf-poppler)/libpdf-poppler.dylib $(brew --prefix zathura)/lib/zathura/libpdf-poppler.dylib
```

## Set it to fullscreen

```text
# /usr/share/applications/org.pwmt.zathura.desktop

Exec=zathura %U --mode fullscreen
```

## Set to dark theme

> Ref: <https://github.com/nordtheme/nord/issues/143>
> Ref: <https://unix.stackexchange.com/questions/575451/how-to-change-white-background-color-of-zathura>

This will not invert picture color:

```text
set recolor
set recolor-lightcolor \#222222
set recolor-keephue
set default-bg \#222230
```

## Copy to gui clipboard by default

> Ref: <https://unix.stackexchange.com/questions/339487/how-to-enable-copy-to-clipboard-with-zathura-pdf-poppler>

```text
set selection-clipboard clipboard
set selection-notification false
```

## Set index to light when in light theme

> Ref: <https://github.com/catppuccin/zathura/blob/main/src/catppuccin-latte>

```text
set index-fg               "#4C4F69"
set index-bg               "#EFF1F5"
set index-active-fg          "#4C4F69"
set index-active-bg          "#CCD0DA"
```

## Smooth scroll

> Ref: <https://www.reddit.com/r/archlinux/comments/oh0m6n/zathura_smooth_scrolling>

```text
map j feedkeys "<C-Down>"
map k feedkeys "<C-Up>"
```

## Increase font size

> Ref: <https://github.com/zegervdv/homebrew-zathura/issues/45#issuecomment-634539604>

```text
set font 'monospace normal 20'
```

## Pretend to be single page mode

Press `a` to fit the screen, then use `J` and `K` to scroll. Press `d` to reset the position.
