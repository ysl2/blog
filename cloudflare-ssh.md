# cloudflare-ssh

> Ref:
>
> - <https://www.namecheap.com/>
> - <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/>
> - <https://blog.csdn.net/SmileHergo/article/details/148078652>
> - <https://blog.csdn.net/hvdanyan/article/details/142265145>

## Prerequisites

1. **Cloudflare**: Ensure the domain is active in your Cloudflare dashboard.
1. **Namecheap**: In your Namecheap dashboard, set **Nameservers** to **Custom DNS** and input the nameservers provided by your Cloudflare account.

## Installation (Server side)

1. [Common part (for both macOS and Linux)](.assets/cloudflare-ssh/install_common.sh)
1. [Linux specific part (run common part above first!!!)](.assets/cloudflare-ssh/install_linux_specific.sh)
1. [macOS specific part (run common part above first!!!)](.assets/cloudflare-ssh/install_mac_specific.sh)
1. NixOS specific (Do not run scripts above, just run these below):

   ```bash
   cloudflared tunnel login
   cloudflared tunnel create myssh
   cloudflared tunnel route dns myssh myssh.example.com
   # Remember the <UUID> generated in output.

   UUID="$(cloudflared tunnel list | grep myssh | awk '{print $1}')"

   CRED_DIR=/var/lib/secrets/cloudflared
   sudo mkdir -p "$CRED_DIR"
   sudo cp ~/.cloudflared/"$UUID".json "$CRED_DIR"
   sudo chmod 600 "$CRED_DIR"/"$UUID".json

   cd /etc/nixos
   sudo su
   vim configuration.nix
   # Add this below:
   ```

   ```nix
   services.cloudflared = {
     enable = true;
     tunnels = {
       "<put the UUID generated above>" = {
         credentialsFile = "/var/lib/secrets/cloudflared/<put the UUID generated above>.json";
         ingress = {
           "myssh.example.com" = "ssh://127.0.0.1:22";
         };
         default = "http_status:404";
       };
     };
   };
   ```

   ```bash
   HTTP_PROXY=http://127.0.0.1:7897 HTTPS_PROXY=http://127.0.0.1:7897 nixos-rebuild switch --flake .

   # Verify
   cloudflared tunnel info "$UUID"
   ```

## SSH connection (Client side)

1. Install `cloudflared` on client side.

   You must have the `cloudflared` binary installed on your local machine as well (via Brew, Winget, or direct download).

2. Configure client side.

   Edit your SSH config file (`~/.ssh/config` on Linux/macOS or `C:\Users\You\.ssh\config` on Windows).

   Add the following entry:

   ```text
   Host *.example.com
       ProxyCommand cloudflared access ssh --hostname %h
   ```

3. Start connection

   Run the standard SSH command from your client terminal:

   ```bash
   ssh <username>@myssh.example.com
   ```

## Advance setting: Cloudflare Zero Trust (Email Authentication)

This step ensures that even if someone knows your domain, they cannot attempt an SSH connection without first authenticating via email.

1. Create Access Application
   - Navigate to the **[Cloudflare Zero Trust Dashboard](https://one.dash.cloudflare.com/)**.
   - Go to **Access** > **Applications** > **Add an Application**.
   - Select **Self-hosted**.
   - **Configuration**:
     - **Application Name**: `myssh`
     - **Session Duration**: `24h` (How often you need to re-login)
     - **Application Domain**: `myssh` . `example.com` (Must match your Tunnel route)
   - Click **Next**.

1. Define Policy (Email Rule)
   - **Policy Name**: `Allow Admin`
   - **Action**: `Allow`
   - **Configure Rules**:
     - **Include** > **Selector**: `Email`
     - **Value**: `your.email@example.com`

   - Click **Next** > **Add Application**.

1. How to Connect (Client Side Changes)

   No config file changes are needed if you used the `ProxyCommand` from the previous guide. The behavior simply changes:
   - **Run SSH**:

     ```bash
     ssh <username>@myssh.example.com
     ```

   - **Authenticate**:
     - `cloudflared` will automatically open a browser window (or print a URL in the terminal).
     - Enter your email in the browser and input the OTP code sent to your inbox.
   - **Access Granted**:
     - Once approved in the browser, the terminal will automatically establish the SSH connection.

1. Troubleshooting

   If the browser does not open automatically, you should manually copy the url and manually open with browser.

   Or, you can choose to disable browser auth, but not safe!!!
   Update your client-side `~/.ssh/config` to force the login prompt:

   ```text
   Host *.example.com
       ProxyCommand cloudflared access ssh --hostname %h --id <your-client-id> --secret <your-client-secret>
   ```

   (Note: Usually not required for basic Email OTP; the standard command works for interactive sessions)

## Uninstall (Server side)

1. [Common part (for both macOS and Linux)](.assets/cloudflare-ssh/uninstall_common.sh)
1. [Linux specific part (run common part above first!!!)](.assets/cloudflare-ssh/uninstall_linux_specific.sh)
1. [macOS specific part (run common part above first!!!)](.assets/cloudflare-ssh/uninstall_mac_specific.sh)
