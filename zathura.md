# zathura

## Installation

### Mac

> Ref: <https://github.com/homebrew-zathura/homebrew-zathura>

```bash
brew tap homebrew-zathura/zathura
brew install zathura --with-synctex
brew install zathura-pdf-mupdf zathura-pdf-poppler
d=$(brew --prefix zathura)/lib/zathura ; mkdir -p $d ; for n in cb djvu pdf-mupdf pdf-poppler ps ; do p=$(brew --prefix zathura-$n)/lib$n.dylib ; [[ -f $p ]] && ln -s $p $d ; done
```

## Usage

假装单页模式：

按`a`适应屏幕，然后`J`和`K`翻页。按`d`能重置位置。
