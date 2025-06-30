---
title: Add sudo permission for normal user
number: 96
url: https://github.com/ysl2/.dotfiles/discussions/96
createdAt: 2025-05-15T09:11:11Z
lastEditedAt: null
updatedAt: 2025-05-15T09:11:11Z
author: ysl2
category: common
labels: []
countZH: 0
countEN: 20
filename: 2505-Add-sudo-permission-for-normal-user
---

```
visudo

## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
songliyu        ALL=(ALL)       NOPASSWD:ALL
```