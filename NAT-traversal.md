# NAT Traversal

## Frp

### Deploy by self-hosted

按照官网的教程来

<https://gofrp.org/zh-cn/docs/examples/ssh/>

注意公网服务器上面需要开放相应的端口

sdu_net 一旦检测到有 frp 行为，会直接封禁 ip。因此如果要用的话，需要做 tls 加密。而且就算采用了加密，也不知道能不能行，因为没法测试了，我的腾讯云的 ip 已经被封了。

可以采用外部 frp 嵌套内部 autossh 的方法。对于封禁 ip 的网段，采用 autossh 先连接到其他不封禁的网段。然后把不封禁的这台机器的对应端口用 frp 映射出去。比如 yin3 在 2244 端口用 autossh 映射了 server-53 的 22 端口，然后再找个公网机器用 frp 映射 yin3 的 2244 端口。这样在外部访问 frp 端口，就直接映射到了 server-53 的 22 端口，并且 server-53 对应的网段还检测不到。

### Sakura frp

```bash
# which sfrpc
# ~/.Local/bin/my/sfrp/sfrpc
# ln -s ~/.Local/bin/my/sfrp/sfrpc ~/.Local/bin/sfrpc
sfrpc -c ~/.Local/bin/my/sfrp/sfrpc.ini --natfrp_tls
```

## Autossh

1. Prepare two machines:

   Inner A

   - ip: 172.27.67.80
   - ssh port: 22
   - username: neiwang

   Public B

   - ip: 47.105.198.227
   - ssh port: 36000
   - username: gongwang

1. In Public B, edit `/etc/ssh/sshd_config`, change the settings below to `yes`, then restart ssh service.

   ```bash
   AllowTcpForwarding yes
   GatewayPorts yes

   sudo systemctl restart sshd
   ```

1. In Inner A, genetate ssh key，and copy it to Public B.

   ```bash
   ssh-keygen
   ssh-copy-id gongwang@47.105.198.227
   ```

1. In Inner A, install autossh, and execute the following command to create a reverse ssh tunnel.

   ```bash
   autossh -M 34000 -NfR 47.105.198.227:35000:localhost:22 -p 36000 gongwang@47.105.198.227

   # Test login:
   # NOTE: There must be `neiwang`, not `gongwang`.
   ssh -p 35000 neiwang@47.105.198.227
   ```

   Port occupation table:

   | Port  | Inner A | Public B | Note                                 |
   | ----- | ------- | -------- | ------------------------------------ |
   | 34000 | Y       | Y        | Monitor port                         |
   | 35000 |         | Y        | For logging in Inner A from Public B |
   | 22    | Y       |          | Inner A's ssh port                   |
   | 36000 | Y       | Y        | Public B's ssh port                  |

1. (optional) In Inner A, set auto start after reboot:

   ```bash
   sudo vim /etc/rc.local

   # Add the above code line
   autossh -M 34000 -NfR 47.105.198.227:35000:localhost:22 -p 36000 gongwang@47.105.198.227
   ```

1. kill

   - In Inner A, `ps aux | grep autossh`, kill -9 the corresponding PID.

   - In Inner A, `sudo lsof -i:34000`, kill -9 the corresponding PID.

   - In Public B, `sudo lsof -i:34000`, `sudo lsof -i:35000`, kill -9 the corresponding PIDs.
