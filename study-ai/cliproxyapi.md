# cliproxyapi

> Ref:
> - <https://github.com/router-for-me/CLIProxyAPI>
> - <https://github.com/router-for-me/CLIProxyAPIPlus>

- Frontend: <http://127.0.0.1:8317/management.html>
- API subscription base url: <http://127.0.0.1:8317/v1>

## Download config file and set frontend page's password

```bash
# For brew, install cliproxyapi first, then, edit the default config file located below.
# Check the config file path by `cliproxyapi -h`
vim $(brew --prefix)/etc/cliproxyapi.conf

# For docker, download config file first, then install cliproxyapi.
mkdir -p ~/.cli-proxy-api/logs
wget -O ~/.cli-proxy-api/config.yaml https://ghfast.top/https://raw.githubusercontent.com/router-for-me/CLIProxyAPIPlus/refs/heads/main/config.example.yaml
vim ~/.cli-proxy-api/config.yaml
```

```yaml
remote-management:
  # Whether to allow remote (non-localhost) management access.
  # When false, only localhost can access management endpoints (a key is still required).
  allow-remote: true
  # management key. if a plaintext value is provided here, it will be hashed on startup.
  # all management requests (even from localhost) require this key.
  # leave empty to disable the management api entirely (404 for all /v0/management routes).
  secret-key: "Enter your password here."

# NOTE: Proxy url is only needed for docker install. No need for brew install.
# Proxy URL. Supports socks5/http/https protocols. Example: socks5://user:pass@192.168.1.1:1080/
# Per-entry proxy-url also supports "direct" or "none" to bypass both the global proxy-url and environment proxies explicitly.
# NOTE: Proxy url is only needed for docker install. No need for brew install.
proxy-url: "http://yourname:yourpassword@127.0.0.1:7897"
```

## Installation

### Install by brew

```bash
brew install cliproxyapi
```

Set auto start after login computer:

```bash
# Start service and register start when login
brew services start cliproxyapi

# Check service status
brew services list

# Stop service
brew services stop cliproxyapi

# Restart service
brew services restart cliproxyapi
```

### Install by docker

```bash
cd ~/Documents
git clone git@github.com:router-for-me/CLIProxyAPIPlus.git
cd CLIProxyAPIPlus
vim docker-compose.yml
```

```diff
diff --git a/docker-compose.yml b/docker-compose.yml
index ad2190c2..85ebac25 100644
--- a/docker-compose.yml
+++ b/docker-compose.yml
@@ -1,6 +1,7 @@
 services:
   cli-proxy-api:
     image: ${CLI_PROXY_IMAGE:-eceasy/cli-proxy-api:latest}
+    network_mode: host
     pull_policy: always
     build:
       context: .
@@ -14,13 +15,6 @@ services:
     #   - .env
     environment:
       DEPLOY: ${DEPLOY:-}
-    ports:
-      - "8317:8317"
-      - "8085:8085"
-      - "1455:1455"
-      - "54545:54545"
-      - "51121:51121"
-      - "11451:11451"
     volumes:
       - ${CLI_PROXY_CONFIG_PATH:-./config.yaml}:/CLIProxyAPI/config.yaml
       - ${CLI_PROXY_AUTH_PATH:-./auths}:/root/.cli-proxy-api
```

```bash
CLI_PROXY_CONFIG_PATH="$HOME/.cli-proxy-api/config.yaml" CLI_PROXY_AUTH_PATH="$HOME/.cli-proxy-api" CLI_PROXY_LOG_PATH="$HOME/.cli-proxy-api/logs" docker compose up -d
```
