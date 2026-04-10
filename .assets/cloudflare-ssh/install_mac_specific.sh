#!/usr/bin/env bash
set -euo pipefail

CF_DIR="$HOME/.cloudflared"
ENV_FILE="$CF_DIR/install.env"
ETC_DIR="/etc/cloudflared"
PLIST="/Library/LaunchDaemons/com.cloudflare.cloudflared.plist"
LOG="/Library/Logs/com.cloudflare.cloudflared.log"

# Run the common install script first
test -f "$ENV_FILE"
source "$ENV_FILE"

CF_BIN="$(command -v cloudflared)"

# Stop the old service
sudo launchctl bootout system "$PLIST" 2>/dev/null || true
sudo rm -f "$PLIST"
sudo pkill -x cloudflared 2>/dev/null || true

# Copy config into the system directory
sudo mkdir -p "$ETC_DIR"
sudo cp "$CF_DIR/config.yml" "$ETC_DIR/config.yml"
sudo cp "$CF_DIR/$UUID.json" "$ETC_DIR/$UUID.json"
sudo chown -R root:wheel "$ETC_DIR"
sudo chmod 644 "$ETC_DIR/config.yml"
sudo chmod 600 "$ETC_DIR/$UUID.json"

# Minimal workaround: let launchd run the official tunnel run command directly
sudo tee "$PLIST" >/dev/null <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cloudflare.cloudflared</string>
  <key>ProgramArguments</key>
  <array>
    <string>$CF_BIN</string>
    <string>tunnel</string>
    <string>--config</string>
    <string>$ETC_DIR/config.yml</string>
    <string>run</string>
    <string>$UUID</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$LOG</string>
  <key>StandardErrorPath</key>
  <string>$LOG</string>
</dict>
</plist>
EOF

sudo chown root:wheel "$PLIST"
sudo chmod 644 "$PLIST"

# Start the service
sudo launchctl bootstrap system "$PLIST"
sudo launchctl kickstart -k system/com.cloudflare.cloudflared

# Verify
sleep 8
cloudflared tunnel info "$UUID"
sudo tail -n 50 "$LOG" || true
