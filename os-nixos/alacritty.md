# alacritty

## Build from source

```bash
LIBS=$(nix-build '<nixpkgs>' -A wayland -A libxkbcommon -A libglvnd -A fontconfig.lib -A freetype --no-out-link)
RPATH=$(echo "$LIBS" | sed 's/$/\/lib/' | tr '\n' ':')
patchelf --set-rpath "$RPATH" alacritty
./alacritty
```
