# Research workflow software

## 文献阅读与管理

### 需求

- 文献阅读和归档
- 文献笔记+画图+插入图片
- 可丝滑导出笔记+cite到latex

### 解决方案

- 阅读：zotero提供文献归档、阅读标注功能，并且可通过webdav备份
- 笔记：obsidian本身提供完备笔记功能，备份可通过git或者webdav
- 图片：obsidian第三方drawio插件，可画图；自带图片插入功能
- 联动：obsidian对于文件提供url，可链接到zotero
- 导出：zotero第三方插件复制biblatex，然后手动粘贴到obsidian的笔记做链接

### Known issues

- obsidian只提供文件url，不提供文件夹url
- obsidian的drawio插件，左侧工具栏默认折叠，需要手动打开
- obsidian的drawio插件，图片刚创建时无预览，必须切换一下笔记才能展示预览

## 文献写作

- Latex editor：overleaf or lazyvim
- Tables：<https://www.tablesgenerator.com>
- Drawings：drawio
