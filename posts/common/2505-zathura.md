---
title: zathura
number: 95
url: https://github.com/ysl2/.dotfiles/discussions/95
createdAt: 2025-05-06T04:44:02Z
lastEditedAt: 2025-05-06T05:07:20Z
updatedAt: 2025-05-15T13:14:38Z
author: ysl2
category: common
labels: []
countZH: 0
countEN: 60
filename: 2505-zathura
---

## Installation

### Mac

> Ref: https://github.com/homebrew-zathura/homebrew-zathura

```bash
brew tap homebrew-zathura/zathura
brew install zathura --with-synctex
brew install zathura-pdf-mupdf zathura-pdf-poppler
d=$(brew --prefix zathura)/lib/zathura ; mkdir -p $d ; for n in cb djvu pdf-mupdf pdf-poppler ps ; do p=$(brew --prefix zathura-$n)/lib$n.dylib ; [[ -f $p ]] && ln -s $p $d ; done
```