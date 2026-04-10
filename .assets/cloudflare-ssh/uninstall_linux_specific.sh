#!/usr/bin/env bash
set -euo pipefail

# Stop and remove the systemd service
sudo systemctl disable --now cloudflared 2>/dev/null || true
sudo cloudflared service uninstall 2>/dev/null || true

# Remove system config and logs
sudo rm -rf /etc/cloudflared
sudo rm -rf /var/log/cloudflared 2>/dev/null || true
