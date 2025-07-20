# colima

## Basic usage

- Global settings

  ```bash
  # Edit the global settings
  vim ~/.config/colima/_templates/default.yaml

  # Stop current colima instance
  colima stop

  # Remove the current settings
  rm ~/.config/colima/default

  # Start colima with the new global settings,
  # this will re-create the default settings in `~/.config/colima/default`.
  colima start
  ```

- Local settings

  ```bash
  colima stop
  vim ~/.config/colima/default/colima.yaml
  colima start
  ```

## Set Chinese mirror

```diff
# Ref: https://github.com/carljmosca/colima/blob/main/docs/FAQ.md
- docker: {}
+ docker:
+   registry-mirrors:
+     - https://my.dockerhub.mirror.something
+     - https://my.quayio.mirror.something
```

## Mount settings on macOS (necessary)

> Ref: <https://github.com/abiosoft/colima/issues/83#issuecomment-2646053621>

```diff
--- /Users/songliyu/.config/colima/_templates/default.yaml	2025-07-20 21:16:46
+++ /Users/songliyu/.config/colima/default/colima.yaml	2025-07-20 21:17:27
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
