# [mac] Localhost configs

`~/.bashrc.localhost.post`

```bash
myquit() {
  [ -n "$TMUX" ] && exit || aerospace close
}
alias :q='myquit'
```
