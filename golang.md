# golang

1. Build runfile with no C dependencies, and enable debug symbols:

   ```bash
   CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -gcflags="all=-N -l" -o main main.go
   # CGO_ENABLED set to 0, to disable C dependencies
   # --gcflags="all=-N -l" to disable optimizations and inlining, enabling debugging.
   ```

1. Cross build delve without any C dependencies:

   > Ref: <https://github.com/go-delve/delve>

   ```bash
   git clone git@github.com:go-delve/delve.git
   cd delve
   CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o dlv ./cmd/dlv
   ```

1. Start debugging with delve:

   ```bash
   ./dlv exec ./main -- -other_args
   # -other_args can be any arguments your program accepts.
   ```
