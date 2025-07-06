# Create user and specify home path

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
