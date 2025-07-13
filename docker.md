# docker

## Installation and settings

### Install

- By brew:

  ```bash
  brew install --cask docker
  ```

- By apt:

  ```bash
  sudo apt install -y docker.io
  ```

- By [colima](https://github.com/abiosoft/colima) (brew):

  ```bash
  brew install colima
  colima start
  ```

### Uninstall

- By brew:

  ```bash
  # Ref: https://github.com/docker/for-mac/issues/7046#issuecomment-2579215790
  brew uninstall --cask docker --force --verbose --debug
  brew uninstall --formula docker --force --verbose --debug
  ```

### Add user into docker group

```bash
sudo usermod -aG docker "$USER"
logout  # and login again
```

### Install docker-compose

- By brew:

  ```bash
  brew install docker-compose
  ```

  Compose is a docker plugin. For docker to find the plugin, add `cliPluginsExtraDirs` to `~/.docker/config.json`:

  ```json
  {
    "cliPluginsExtraDirs": ["$HOMEBREW_PREFIX/lib/docker/cli-plugins"]
  }
  ```

- By source:

  ```bash
  # Ref: https://stackoverflow.com/a/79052312

  DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
  mkdir -p $DOCKER_CONFIG/cli-plugins
  curl -SL "https://ghfast.top/https://github.com/docker/compose/releases/download/v2.33.0/docker-compose-$(uname -s)-$(uname -m)" -o $DOCKER_CONFIG/cli-plugins/docker-compose

  chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

  # test the installation with:
  docker compose version

  # expected output is: Docker Compose version v2.29.6
  ```

### Chinese mirror

> 注：阿里云镜像我试过了，不可用。换成daocloud地址：`"registry-mirrors": ["https://docker.m.daocloud.io"]`

[阿里云加速器(点击管理控制台 -> 登录账号(淘宝账号) -> 左侧镜像工具 -> 镜像加速器 -> 复制加速器地址)](https://cr.console.aliyun.com/cn-hangzhou/instances)

```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": ["自己的阿里云镜像链接"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Check the host's IP in docker containers

```bash
ip route | awk '/default/ { print $3 }'
```

## Clean docker resources

```bash
docker system prune -a --volumes
```

WARNING! This will remove:

- all stopped containers
- all networks not used by at least one container
- all anonymous volumes not used by at least one container
- all images without at least one container associated to them
- all build cache
