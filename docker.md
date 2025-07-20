# docker

> Ref: <https://github.com/carljmosca/colima/blob/main/docs/FAQ.md>

## Add user into docker group

```bash
sudo usermod -aG docker "$USER"
logout  # and login again
```

## Set Chinese mirror

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
