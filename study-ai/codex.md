# codex

## Enable all permissions

`~/.codex/config.toml`

```toml
approval_policy = "never"
sandbox_mode = "danger-full-access"
```

## Enable 1m context

```toml
model_context_window = 1000000
model_auto_compact_token_limit = 900000
```
