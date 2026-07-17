# colima

> Ref: <https://github.com/carljmosca/colima/blob/main/docs/FAQ.md>

## Installation

```bash
brew install colima docker
colima start

# NOTE: if `colima start` failed, run this:
# brew unlink docker-completion
# brew link docker

# Start colima in background and enable it to start on login:
brew services start colima  # Or: `colima start --background`
```

## Basic usage

- Global settings

  ```bash
  # Edit the global settings
  vim ~/.colima/_templates/default.yaml

  # Stop current colima instance
  colima stop

  # Remove the current settings
  rm -rf ~/.colima/default

  # Start colima with the new global settings,
  # this will re-create the default settings in `~/.config/colima/default`.
  colima start
  ```

- Local settings

  ```bash
  colima stop
  vim ~/.colima/default/colima.yaml
  colima start
  ```

## Configuration

### Set Chinese mirror

> Ref: https://github.com/carljmosca/colima/blob/main/docs/FAQ.md

```diff
- docker: {}
+ docker:
+   registry-mirrors:
+     - https://my.dockerhub.mirror.something
+     - https://my.quayio.mirror.something
```

### Mount settings on macOS (necessary)

> Ref: <https://github.com/abiosoft/colima/issues/83#issuecomment-2646053621>

```diff
@@ -122,7 +122,7 @@
 #
 # NOTE: value cannot be changed after virtual machine is created.
 # Default: qemu
-vmType: qemu
+vmType: vz

 # Utilise rosetta for amd64 emulation (requires m1 mac and vmType `vz`)
 # Default: false
@@ -143,7 +143,7 @@
 #
 # NOTE: value cannot be changed after virtual machine is created.
 # Default: virtiofs (for vz), sshfs (for qemu)
-mountType: sshfs
+mountType: virtiofs

 # Propagate inotify file events to the VM.
 # NOTE: this is experimental.
```

### Manually write ssh config

```diff
@@ -239,7 +239,7 @@ provision: []
 # Modify ~/.ssh/config automatically to include a SSH config for the virtual machine.
 # SSH config will still be generated in $COLIMA_HOME/ssh_config regardless.
 # Default: true
-sshConfig: true
+sshConfig: false

 # The port number for the SSH server for the virtual machine.
 # When set to 0, a random available port is used.
```

Then, manually write ssh config into `~/.ssh/config`:

```sshconfig
Host *
    Include ~/.colima/ssh_config
```

## Troubleshooting

### `brew services start colima`: Bootstrap failed: 5

Usually caused by stale launchd state or Colima already running manually.

```bash
colima stop
launchctl bootout "gui/$(id -u)/homebrew.mxcl.colima" 2>/dev/null || true
brew services start colima
```
