#!/usr/bin/env bash
set -euo pipefail

CF_DIR="$HOME/.cloudflared"
ENV_FILE="$CF_DIR/install.env"
ETC_DIR="/etc/cloudflared"

# Run the common install script first
test -f "$ENV_FILE"
source "$ENV_FILE"

# Stop and remove the existing systemd service if present
sudo systemctl disable --now cloudflared 2>/dev/null || true
sudo cloudflared service uninstall 2>/dev/null || true

# Copy config into the system directory
sudo mkdir -p "$ETC_DIR"
sudo cp "$CF_DIR/config.yml" "$ETC_DIR/config.yml"
sudo cp "$CF_DIR/$UUID.json" "$ETC_DIR/$UUID.json"
sudo chown root:root "$ETC_DIR/config.yml" "$ETC_DIR/$UUID.json"
sudo chmod 644 "$ETC_DIR/config.yml"
sudo chmod 600 "$ETC_DIR/$UUID.json"

# Install and start the systemd service
sudo cloudflared --config "$ETC_DIR/config.yml" service install
sudo systemctl enable --now cloudflared

# Verify
sleep 5
cloudflared tunnel info "$UUID"
sudo systemctl status cloudflared --no-pager
