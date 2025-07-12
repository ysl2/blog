# docker

## Run docker without sudo

```bash
sudo usermod -aG docker "$USER"
logout  # and login again
```

## Install docker on macOS

```bash
brew install --cask docker
```

## Install docker-compose by brew

```bash
brew install docker-compose
```

Compose is a docker plugin. For docker to find the plugin, add `cliPluginsExtraDirs` to `~/.docker/config.json`:

```json
{
  "cliPluginsExtraDirs": ["$HOMEBREW_PREFIX/lib/docker/cli-plugins"]
}
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

## References

- <https://github.com/abiosoft/colima>
