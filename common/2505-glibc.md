---
title: glibc
number: 101
url: https://github.com/ysl2/.dotfiles/discussions/101
createdAt: 2025-05-18T01:27:36Z
lastEditedAt: null
updatedAt: 2025-05-18T01:27:38Z
author: ysl2
category: common
labels: []
countZH: 0
countEN: 40
filename: 2505-glibc
---

```bash
wget http://ftp.gnu.org/gnu/glibc/glibc-2.34.tar.gz
tar -xzf glibc-2.34.tar.gz
cd glibc-2.34
mkdir build && cd build
../configure --prefix=/opt/glibc-2.34  # Specify the install path
make -j$(nproc) && sudo make install
```