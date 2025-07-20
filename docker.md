# docker

> Ref: <https://github.com/carljmosca/colima/blob/main/docs/FAQ.md>

## Add user into docker group

```bash
sudo usermod -aG docker "$USER"
logout  # and login again
```

## Set Chinese mirror

- By docker

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

- By colima

  ```bash
  # Edit the global settings
  vim ~/.config/colima/_templates/default.yaml

  # Stop current colima instance
  colima stop

  # Remove the current settings
  rm ~/.config/colima/default

  # Start colima with the new global settings,
  # this will re-create the default settings in `~/.config/colima/default`.
  colima start
  ```

  ```diff
  # Ref: https://github.com/carljmosca/colima/blob/main/docs/FAQ.md
  - docker: {}
  + docker:
  +   registry-mirrors:
  +     - https://my.dockerhub.mirror.something
  +     - https://my.quayio.mirror.something
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
