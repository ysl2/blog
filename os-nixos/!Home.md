# [os-nixos] Home

## Update and rollback system

### Update system

   ```bash
   cd /etc/nixos
   sudo nix flake update
   sudo nixos-rebuild switch --flake /etc/nixos#nixos
   ```

### Rollback system

If something breaks, use these commands to rollback:

1. Rollback to previous generation:
   ```bash
   sudo nixos-rebuild switch --rollback
   ```

1. List all system generations:
   ```bash
   sudo nix-env --list-generations --profile /nix/var/nix/profiles/system
   ```

1. Switch to a specific generation (replace N with generation number):
   ```bash
   sudo nixos-rebuild switch --profile /nix/var/nix/profiles/system --switch-generation N
   ```

1. Clean up old generations (after confirming everything works):
   ```bash
   sudo nix-collect-garbage -d
   ```
