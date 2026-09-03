# anylinuxfs

> Ref: <https://github.com/nohajc/anylinuxfs>

## Installation

```bash
brew tap nohajc/anylinuxfs
brew install anylinuxfs
```

## Usage

### Basic usage

1. First init (run only once)

   ```bash
   anylinuxfs init
   ```

1. Daily usage

   ```bash
   # Find device number
   # NOTE: If you encnounter network issues, run `sudo su` first, then run with environment variables.
   sudo su
   HTTP_PROXY=127.0.0.1:7892 HTTPS_PROXY=127.0.0.1:7892 anylinuxfs list
   # Find the partition, e.g, disk4s2

   # Mount disk to the mount point above
   sudo anylinuxfs mount --window false /dev/disk4s2
   # NOTE: Check the mount point (Can be found by `sudo anylinuxfs list`)
   # e.g, `/Volumes/T7_Shield`, and run below only once:
   sudo chown songliyu:staff /Volumes/T7_Shield

   # Check status
   anylinuxfs status

   # Unmount (Don't unmount when current shell location is under /Volumes/T7_Shield)
   # sudo anylinuxfs unmount /Volumes/T7_Shield
   sudo anylinuxfs unmount /dev/disk4s2
   ```

### Enhanced usage

1. Auto find device number

   ```bash
   DEV=$(sudo anylinuxfs list | awk '$2=="ext4" && $3=="T7_Shield"{print "/dev/"$NF; exit}')
   sudo anylinuxfs mount "$DEV" /Volumes/T7_Shield
   ```

## Troubleshoot

1. Another instance is already running

   ```bash
   sudo anylinuxfs stop || true
   sudo pkill -f "anylinuxfs|gvproxy|vmproxy" || true
   rm -f /tmp/anylinuxfs.sock /private/tmp/anylinuxfs.sock
   anylinuxfs init
   ```
