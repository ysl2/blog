# cloudflare-tunnel

```bash
set -euo pipefail

TUNNEL_NAME="my-tunnel"
CONFIG="$HOME/.cloudflared/config.yml"

mkdir -p "$HOME/.cloudflared"

[ -f "$HOME/.cloudflared/cert.pem" ] || cloudflared tunnel login

# NOTE:
# Then, go to https://dash.cloudflare.com/profile/api-tokens to modify newly created api's dns zone to "all zones".

cloudflared tunnel info "$TUNNEL_NAME" >/dev/null 2>&1 || cloudflared tunnel create "$TUNNEL_NAME"

TUNNEL_ID=$(cloudflared tunnel list | awk -v name="$TUNNEL_NAME" '$2 == name {print $1; exit}')

if [ -z "$TUNNEL_ID" ]; then
  echo "Failed to get tunnel ID"
  exit 1
fi

CREDENTIALS_FILE="$HOME/.cloudflared/$TUNNEL_ID.json"

if [ ! -f "$CREDENTIALS_FILE" ]; then
  echo "Missing credentials file: $CREDENTIALS_FILE"
  echo "This usually means the tunnel already exists in Cloudflare, but this machine does not have its local json credentials."
  echo "Either copy the credentials file here, or delete/recreate this tunnel."
  exit 1
fi

cat > "$CONFIG" <<EOF
tunnel: $TUNNEL_ID
credentials-file: $CREDENTIALS_FILE

ingress:
  - hostname: example.com
    service: http://127.0.0.1:8000
  - hostname: www.example.com
    service: http://127.0.0.1:8000
  - hostname: ssh.anotherexample.com
    service: ssh://127.0.0.1:22
  - service: http_status:404
EOF

# NOTE:
# Then, you should go to https://dash.cloudflare.com/ and manually add the corresponding DNS record.
# | Zone               | Type  | Name | Target                       |
# | ------------------ | ----- | ---- | ---------------------------- |
# | example.com        | CNAME | @    | <TUNNEL_ID>.cfargotunnel.com |
# | example.com        | CNAME | www  | <TUNNEL_ID>.cfargotunnel.com |
# | anotherexample.com | CNAME | ssh  | <TUNNEL_ID>.cfargotunnel.com |

sudo cloudflared service uninstall >/dev/null 2>&1 || true
sudo rm -f /etc/cloudflared/config.yml
sudo cloudflared --config "$CONFIG" service install
sudo systemctl enable --now cloudflared
sudo systemctl status cloudflared --no-pager
```
