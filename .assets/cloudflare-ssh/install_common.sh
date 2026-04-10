#!/usr/bin/env bash
set -euo pipefail

HOSTNAME="myssh.example.com"
TUNNEL_NAME="${HOSTNAME%%.*}"
CF_DIR="$HOME/.cloudflared"
ENV_FILE="$CF_DIR/install.env"

# Local SSH must already be available
nc -z 127.0.0.1 22 >/dev/null

# Log in to Cloudflare
cloudflared tunnel login

# Delete the existing tunnel with the same name if it already exists
OLD_UUID="$(cloudflared tunnel list 2>/dev/null | awk -v name="$TUNNEL_NAME" '$2==name {print $1; exit}')"
if [ -n "${OLD_UUID:-}" ]; then
    cloudflared tunnel delete -f "$OLD_UUID" || true
fi

# Create a new tunnel
OUT="$(cloudflared tunnel create "$TUNNEL_NAME" 2>&1)"
echo "$OUT"
UUID="$(echo "$OUT" | sed -n 's/.* with id \([0-9a-f-]\{36\}\).*/\1/p' | tail -n1)"

# Write the tunnel config
mkdir -p "$CF_DIR"
cat >"$CF_DIR/config.yml" <<EOF
tunnel: $UUID
credentials-file: $CF_DIR/$UUID.json

ingress:
  - hostname: $HOSTNAME
    service: ssh://127.0.0.1:22
  - service: http_status:404
EOF

# Create the DNS route
cloudflared tunnel route dns "$TUNNEL_NAME" "$HOSTNAME"

# Save shared variables for the platform-specific install step
cat >"$ENV_FILE" <<EOF
HOSTNAME="$HOSTNAME"
TUNNEL_NAME="$TUNNEL_NAME"
CF_DIR="$CF_DIR"
UUID="$UUID"
EOF

echo "Tunnel name: $TUNNEL_NAME"
echo "Tunnel UUID: $UUID"
