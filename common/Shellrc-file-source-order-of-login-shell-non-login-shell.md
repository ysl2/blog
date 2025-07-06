# Shellrc file source order of login shell / non-login shell

## Conclusion

```bash
mv ~/.bash_login ~/.bash_login_
mv ~/.bash_profile ~/.bash_profile_
[ "$(uname)" = Darwin ] && mv ~/.profile ~/.profile_
[ "$(uname)" = Darwin ] && mv ~/.zshenv ~/.zshenv_
```

---

对于zsh，只需要一个文件`~/.zshrc`就可以，`~/.zshenv`和`~/.zprofile`有没有不影响，但是neovide的环境变量需要写到`~/.zprofile`里面。

对于bash，需要两个文件`~/.profile`和`~/.bashrc`，同时不能有`~/.bash_profile`和`~/.bash_login`（否则轮不到`~/.profile`加载）。

对于tmux，每打开一个pane都是登录shell，按照上面说的顺序加载。

对于startx，startx本身的过程不走这一套，而是走`~/.xinitrc`那些。但是startx之前，是按照上面这两个顺序加载的。

对于gdm登录i3的时候，是按照上面bash这套流程走的。因此条件和上面这个bash的一样。

TODO: gnomerc是给ubuntu用的？

---

因此`~/.profile`链接到`~/.bashrc`用来满足bash的登录shell以及gdm登录，`~/.zshrc`也链接到`~/.bashrc`用来同步zsh和bash的设置。

删掉`~/.bash_profile`和`~/.bash_login`。

在`~/.bashrc`中补充按照当前情况停止source的条件判断，用来满足开机等特殊情况。

---

> 对于zsh，只需要一个文件`~/.zshrc`就可以，`~/.zshenv`和`~/.zprofile`有没有不影响
> `~/.profile`链接到`~/.bashrc`用来满足bash的登录shell以及gdm登录

补充：对于Mac，由于不涉及通过dm登录到桌面的场景，并且默认$SHELL是zsh（tmux过程走上述zsh路径），因此不需要有`~/.profile`文件
