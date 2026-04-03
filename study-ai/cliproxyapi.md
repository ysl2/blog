# cliproxyapi

> Ref: <https://github.com/router-for-me/CLIProxyAPI>

## Installation

```bash
brew install cliproxyapi
```

- Frontend: <http://127.0.0.1:8317/management.html>
- API subscription base url: <http://127.0.0.1:8317/v1>

## Configuration

### Set frontend page's password

```bash
# Check the config file path by `cliproxyapi -h`
vim /opt/homebrew/etc/cliproxyapi.conf
```

```yaml
remote-management:
  # management key. if a plaintext value is provided here, it will be hashed on startup.
  # all management requests (even from localhost) require this key.
  # leave empty to disable the management api entirely (404 for all /v0/management routes).
  secret-key: "Enter your password here."
```

### Set auto start after login computer

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
