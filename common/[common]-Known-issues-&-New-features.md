# [common] Known issues & New features

- [x] 移除过时的文件，比如`~/.tmux/_`等
- [x] 重新考虑文件夹结构。比如`~/.script`和`~/.vocal/_`的统一性
- [x] alacritty, select mode, press `w` will jump to next line. hope to jump next word start.
- [ ] 大模型排行榜。chat和database两种。找到常用大模型比如dify或者lobe。并且需要找一个agent方案，实现MCP自动化
- [ ] browser tab fast switch. seek for some browser tiling management
- [ ] W325: Ignoring swapfile from Nvim process 39989
- [x] discussion export method

---

1. 所有内容全部移动到discussions
1. 合并.dotfiles和blog的内容

工具流全部换成开源，并固定长期使用。要求配置可导入导出 (方便通过git跟踪)。将这些工具记录到discussions中
比如幕布换成开源工具
TAPD、Jira的开源替代品
腾讯文档的开源替代。要求office三件套 + 可导入导出markdown

---

<https://github.com/orgs/community/discussions/3315#discussioncomment-7081810>

- <https://github.com/intel/dffml/blob/alice/scripts/dump_discussion.py>
- <https://github.com/intel/dffml/blob/main/scripts/discussion_dump_to_markdown.py>
- <https://github.com/shridhar-tl/github-2-markdown>
- <https://github.com/King-of-Infinite-Space/gh-discussions-export>
- <https://github.com/jmikedupont2/meta-meme/blob/dc61ba23d9717155a7d68505abef910bffe75ff8/examples/generator/pull_git_comments.py>
- <https://github.com/kcorkan/discussion-exporter>

<https://api.github.com/repos/owner/repo/discussions?per_page=100&page=1>
<https://api.github.com/repos/owner/repo/discussions/Discussion-ID/comments>

---

discussion工具只能导出第一个comment。因此需要转移正文

寻找一个discussion blog page的前端页面，打造成blog。参考我自己的star列表

discussion 编辑时的tab键失效问题：<https://github.com/orgs/community/discussions/127067>
