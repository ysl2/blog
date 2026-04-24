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

## Use latest model

> Ref: <https://linux.do/t/topic/2042554>

```toml
model_catalog_json = './models_cache.json'
```

Then, modify `~/.codex/models_cache.json` to copy an old model, paste, and modify it to newest model.

e.g, copy `gpt-5.4`, and modify the model name to `gpt-5.5`, and change the url to the latest model url.
