---
title: "[mac] Localhost configs"
number: 91
url: https://github.com/ysl2/.dotfiles/discussions/91
createdAt: 2025-05-03T06:19:41Z
lastEditedAt: 2025-05-03T12:54:48Z
updatedAt: 2025-06-15T17:15:47Z
author: ysl2
category: mac
labels: []
countZH: 0
countEN: 10
filename: 2505-[mac]-Localhost-configs
---

`~/.bashrc.localhost.post`

```bash
myquit() {
  [ -n "$TMUX" ] && exit || aerospace close
}
alias :q='myquit'
```