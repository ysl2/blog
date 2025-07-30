# autossh

- ssh

  ```bash
  autossh -M 37000 -NfR 47.xxx.xxx.227:38000:localhost:22 -p 36000 gongwang@47.xxx.xxx.227
  ```

- gitea

  ```bash
  autossh -M 37001 -NfR 47.xxx.xxx.227:38001:localhost:36001 -p 36000 yusongli@47.xxx.xxx.227
  autossh -M 37002 -NfR 47.xxx.xxx.227:38002:localhost:36002 -p 36000 yusongli@47.xxx.xxx.227
  autossh -M 37003 -NfR 47.xxx.xxx.227:38003:localhost:36003 -p 36000 yusongli@47.xxx.xxx.227
  ```

- lobe-chat

  ```bash
  autossh -M 37004 -NfR 47.xxx.xxx.227:38004:localhost:36004 -p 36000 yusongli@47.xxx.xxx.227
  autossh -M 37005 -NfR 47.xxx.xxx.227:38005:localhost:36005 -p 36000 yusongli@47.xxx.xxx.227
  autossh -M 37006 -NfR 47.xxx.xxx.227:38006:localhost:36006 -p 36000 yusongli@47.xxx.xxx.227
  # NOTE:
  # 36007 and 36008 are used by lobe-chat, but they are not intentionally exposed to the public.
  ```

- miniserve

  ```bash
  autossh -M 37009 -NfR 47.xxx.xxx.227:38009:localhost:36009 -p 36000 yusongli@47.xxx.xxx.227
  autossh -M 37010 -NfR 47.xxx.xxx.227:38010:localhost:36010 -p 36000 yusongli@47.xxx.xxx.227
  ```
