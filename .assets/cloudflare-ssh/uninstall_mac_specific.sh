#!/usr/bin/env bash
set -euo pipefail

ETC_DIR="/etc/cloudflared"
PLIST="/Library/LaunchDaemons/com.cloudflare.cloudflared.plist"

# Stop and remove the launchd service
sudo launchctl bootout system "$PLIST" 2>/dev/null || true
sudo rm -f "$PLIST"
sudo pkill -x cloudflared 2>/dev/null || true

# Remove system config and logs
sudo rm -rf "$ETC_DIR"
sudo rm -f /Library/Logs/com.cloudflare.cloudflared*.log 2>/dev/null || true
