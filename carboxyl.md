# carboxyl

## Installation

- macOS arm64, `~/.vocal`

  If your shell auto-adds `~/.vocal/*/bin` to `PATH`, this installs a runnable Carboxyl bundle into `~/.vocal/carboxyl/bin`.

  ```bash
  repo="$HOME/Documents/carboxyl"; [ -d "$repo/.git" ] || git clone git@github.com:carboxyl-rs/carboxyl.git "$repo"
  cd "$repo" && bash scripts/runtime-pull.sh && cargo build --target aarch64-apple-darwin --release
  dst="$HOME/.vocal/carboxyl/bin"; rm -rf "$HOME/.vocal/carboxyl" "$HOME/.vocal/carbonyl" && mkdir -p "$dst"
  cp build/pre-built/aarch64-apple-darwin/{carbonyl,icudtl.dat,libEGL.dylib,libGLESv2.dylib,v8_context_snapshot.arm64.bin} "$dst"/
  cp build/aarch64-apple-darwin/release/libcarbonyl.dylib "$dst"/ && install_name_tool -id @executable_path/libcarbonyl.dylib "$dst/libcarbonyl.dylib"
  zsh -ic 'command -v carbonyl && carbonyl --version'
  ```

  This layout intentionally keeps the full runtime bundle in `~/.vocal/carboxyl/bin`. After first run, Carboxyl will also create its cache and state directories there.
