---
title: Create user and specify home path
number: 98
url: https://github.com/ysl2/.dotfiles/discussions/98
createdAt: 2025-05-16T10:00:04Z
lastEditedAt: 2025-05-16T10:01:59Z
updatedAt: 2025-05-16T10:01:59Z
author: ysl2
category: common
labels: []
countZH: 0
countEN: 50
filename: 2505-Create-user-and-specify-home-path
---

```bash
sudo chmod 755 /data/workspace
sudo useradd -m -d /data/workspace/songliyu -s /bin/bash songliyu
```

- `-m`: Automatically create home dir
- `-d`: Specify home path
- `-s`: Specify default shell

```bash
sudo passwd songliyu
```

```bash
# Check permission
ls -ld /data/workspace/songliyu
# If permission not correct, fix it.
sudo chown -R songliyu:songliyu /data/workspace/songliyu
```

