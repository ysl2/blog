#!/usr/bin/env bash
set -euo pipefail

HOSTNAME="myssh.example.com"
TUNNEL_NAME="${HOSTNAME%%.*}"
CF_DIR="$HOME/.cloudflared"

# Run the platform-specific uninstall script first

# Delete the tunnel from Cloudflare
cloudflared tunnel delete -f "$TUNNEL_NAME" || true

# Remove local config
rm -rf "$CF_DIR"
