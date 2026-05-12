# autossh

1. Prepare two machines:

   Inner A
   - ip: 127.0.0.1
   - ssh port: 22
   - username: neiwang

   Public B
   - ip: 47.xxx.xxx.227
   - ssh port: 36000
   - username: gongwang

1. In Public B, edit `/etc/ssh/sshd_config`, change the settings below to `yes`, then restart ssh service.

   ```bash
   GatewayPorts yes
   ClientAliveInterval 15
   ClientAliveCountMax 3

   sudo systemctl reload ssh
   ```

1. In Inner A, genetate ssh key，and copy it to Public B.

   ```bash
   ssh-keygen
   ssh-copy-id gongwang@47.xxx.xxx.227
   ```

1. In Inner A, install autossh, and execute the following command to create a reverse ssh tunnel.

   ```bash
   autossh -M 46001 -o ExitOnForwardFailure=yes -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -NfR 47.xxx.xxx.227:36001:127.0.0.1:22 -p 36000 gongwang@47.xxx.xxx.227

   # Test login:
   # NOTE: There must be `neiwang`, not `gongwang`.
   ssh -p 36001 neiwang@47.xxx.xxx.227
   ```

   Port occupation table:

   | Port  | Inner A | Public B | Note                                 |
   | ----- | ------- | -------- | ------------------------------------ |
   | 46001 | Y       | Y        | Monitor port                         |
   | 36001 |         | Y        | For logging in Inner A from Public B |
   | 22    | Y       |          | Inner A's ssh port                   |
   | 36000 | Y       | Y        | Public B's ssh port                  |

1. (optional) In Inner A, set auto start after reboot:

   ```bash
   sudo vim /etc/rc.local

   # Add the above code line
   autossh -M 46001 -o ExitOnForwardFailure=yes -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -NfR 47.xxx.xxx.227:36001:127.0.0.1:22 -p 36000 gongwang@47.xxx.xxx.227
   ```

1. Kill
   - In Inner A, `ps aux | grep autossh`, kill -9 the corresponding PID.

   - In Inner A, `sudo lsof -i:46001`, kill -9 the corresponding PID.

   - In Public B, `sudo lsof -i:46001`, `sudo lsof -i:36001`, kill -9 the corresponding PIDs.

1. Batch script `~/autos.sh`

   ```bash
   #!/bin/bash
   SSH_OPTS=(
     -o ExitOnForwardFailure=yes
     -o ServerAliveInterval=15
     -o ServerAliveCountMax=3
   )

   autossh -M 47000 "${SSH_OPTS[@]}" -NfR 47.xxx.xxx.227:37000:127.0.0.1:7000 -p 36000 ubuntu@47.xxx.xxx.227
   autossh -M 48000 "${SSH_OPTS[@]}" -NfR 47.xxx.xxx.227:38000:127.0.0.1:8000 -p 36000 ubuntu@47.xxx.xxx.227
   ```
