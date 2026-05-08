# docker

## Installation

- For Linux, by brew (Not recommend for macOS. Use `by colima` below)

  ```bash
  brew install --cask docker
  ```

- For Linux, by apt

  ```bash
  sudo apt install -y docker.io
  ```

- For macOS, by [colima](https://github.com/abiosoft/colima), refer to [./colima.md#installation](./colima.md#installation)

## Uninstallation

- For Linux and macOS, by brew

  ```bash
  # Ref: https://github.com/docker/for-mac/issues/7046#issuecomment-2579215790
  brew uninstall --cask docker --force --verbose --debug
  brew uninstall --formula docker --force --verbose --debug
  ```

## Configuration

### Install docker plugins

- For Linux and macOS, by source (docker-compose):

  ```bash
  # Ref: https://stackoverflow.com/a/79052312

  # DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
  # mkdir -p $DOCKER_CONFIG/cli-plugins
  # curl -SL "https://ghfast.top/https://github.com/docker/compose/releases/download/v2.33.0/docker-compose-$(uname -s)-$(uname -m)" -o $DOCKER_CONFIG/cli-plugins/docker-compose
  # chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

  mkdir ~/.docker/cli-plugins
  curl -SL "https://github.com/docker/compose/releases/download/v5.1.3/docker-compose-linux-x86_64" -o ~/.docker/cli-plugins/docker-compose
  chmod +x ~/.docker/cli-plugins/docker-compose

  # test the installation with:
  docker compose version
  ```

- For macOS, by brew:

  ```bash
  brew install docker-compose
  brew install docker-buildx
  ```

  For docker to find plugins, add `cliPluginsExtraDirs` to `~/.docker/config.json`:

  ```json
  {
    "cliPluginsExtraDirs": ["$HOMEBREW_PREFIX/lib/docker/cli-plugins"]
  }
  ```

### For Linux, add user into docker group

```bash
sudo usermod -aG docker "$USER"

# If you want to take effect immediately:
newgrp docker
# Or, you can also:
logout  # and login again
```

### Set Chinese mirror

- For macOS, refer to [./colima.md#set-chinese-mirror](./colima.md#set-chinese-mirror)

- For Linux:

  ```bash
  sudo mkdir -p /etc/docker
  sudo tee /etc/docker/daemon.json <<-'EOF'
  {
      "registry-mirrors": ["https://docker.m.daocloud.io"]
  }
  EOF
  sudo systemctl daemon-reload
  sudo systemctl restart docker
  ```

### For linux, set proxy for docker

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo vim /etc/systemd/system/docker.service.d/http-proxy.conf
```

```toml
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7897"
Environment="HTTPS_PROXY=http://127.0.0.1:7897"
Environment="NO_PROXY=localhost,127.0.0.1"
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Usage

### Check the host's IP in docker containers

```bash
ip route | awk '/default/ { print $3 }'
```

### Clean docker resources

```bash
docker system prune -a --volumes

# NOTE: For colima on macOS, also run the following command, to get back the disk space occupied by the docker images.
colima ssh -- sudo fstrim -av
```

WARNING! This will remove:

- all stopped containers
- all networks not used by at least one container
- all anonymous volumes not used by at least one container
- all images without at least one container associated to them
- all build cache
