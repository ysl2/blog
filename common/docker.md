# docker

## Run docker without sudo

```bash
sudo usermod -aG docker "$USER"
logout  # and login again
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
