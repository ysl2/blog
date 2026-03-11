# openclaw

## Basic install

Refer to: <https://openclaw.ai/>

## Add full access

`nvim ~/.openclaw/openclaw.json`

```json
{
  ...
  "tools": {
    "profile": "full"
  },
  ...
}
```

## Add skills

Refer to [./skill.md](./skill.md)

## Add browser support

- Online install

  <https://chromewebstore.google.com/detail/openclaw-browser-relay/nglingapjinhecnfejdcpihlpneeadjp?pli=1>

- Offline install:

  ```bash
  openclaw browser extension install
  openclaw browser extension path

  # The command above will show this path: `~/.openclaw/browser/chrome-extension`
  ```

Enable chrome's developer mode, and add the path above into chrome extensions page.

## Add web_search support

```bash
openclaw configure --section web
# Then, enter the brave search api key.
```

## Bot

<https://q.qq.com/qqbot/openclaw/login.html>

```bash
openclaw plugins install @sliverp/qqbot@latest
openclaw channels add --channel qqbot --token "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
openclaw gateway restart
```
