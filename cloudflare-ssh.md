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

## Part 1: Server Side (Headless)

### 1. Install `cloudflared`

Download and install the package (example for Debian/Ubuntu/amd64):

```bash
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
```

### 2. Authenticate

Run the login command. It will generate a URL.

```bash
cloudflared tunnel login
```

- **Action:** Copy the URL printed in the terminal, open it in a browser on your _PC/Laptop_, and authorize the domain.
- **Result:** A certificate `cert.pem` will be downloaded to `~/.cloudflared/`.

### 3. Create the Tunnel

Create a tunnel named `myssh`.

```bash
cloudflared tunnel create myssh
```

- **Note:** Save the **Tunnel ID** (UUID) from the output.
- **Result:** A JSON credentials file is created in `~/.cloudflared/`.

### 4. Configure DNS Routing

Map a subdomain (e.g., `ssh.example.com`) to the tunnel.

```bash
# Replace ssh.example.com with your desired subdomain
cloudflared tunnel route dns myssh ssh.example.com
```

### 5. Create Configuration File

Create the config file using `nano` or `vim`:

```bash
vim ~/.cloudflared/config.yml
```

Paste the following content (replace `<UUID>` with the ID from Step 3):

```yaml
tunnel: <UUID>
credentials-file: /root/.cloudflared/<UUID>.json

ingress:
  - hostname: ssh.example.com
    service: ssh://localhost:22
  - service: http_status:404
```

### 6. Run as a Service

Install and start the tunnel as a system service for persistence.

```bash
sudo cloudflared service install
sudo systemctl start cloudflared
sudo systemctl enable cloudflared
```

## Part 2: Client Side (Your PC/Mac)

### 1. Install `cloudflared`

You must have the `cloudflared` binary installed on your local machine as well (via Brew, Winget, or direct download).

### 2. Configure SSH Client

Edit your SSH config file (`~/.ssh/config` on Linux/macOS or `C:\Users\You\.ssh\config` on Windows).

Add the following entry:

```text
Host ssh.example.com
ProxyCommand cloudflared access ssh --hostname %h
```

## Part 3: Connect

Run the standard SSH command from your client terminal:

```bash
ssh <username>@ssh.example.com
```

## Part 4: (Optional but recommend) Cloudflare Zero Trust (Email Authentication)

This step ensures that even if someone knows your domain, they cannot attempt an SSH connection without first authenticating via email.

### 1. Create Access Application

1. Navigate to the **[Cloudflare Zero Trust Dashboard](https://one.dash.cloudflare.com/)**.
1. Go to **Access** > **Applications** > **Add an Application**.
1. Select **Self-hosted**.
1. **Configuration**:
   - **Application Name**: `myssh`
   - **Session Duration**: `24h` (How often you need to re-login)
   - **Application Domain**: `ssh` . `example.com` (Must match your Tunnel route)

1. Click **Next**.

### 2. Define Policy (Email Rule)

1. **Policy Name**: `Allow Admin`
1. **Action**: `Allow`
1. **Configure Rules**:
   - **Include** > **Selector**: `Email`
   - **Value**: `your.email@example.com`

1. Click **Next** > **Add Application**.

### 3. How to Connect (Client Side Changes)

No config file changes are needed if you used the `ProxyCommand` from the previous guide. The behavior simply changes:

1. **Run SSH**:

   ```bash
   ssh <username>@ssh.example.com
   ```

1. **Authenticate**:
   - `cloudflared` will automatically open a browser window (or print a URL in the terminal).
   - Enter your email in the browser and input the OTP code sent to your inbox.
1. **Access Granted**:
   - Once approved in the browser, the terminal will automatically establish the SSH connection.

### 4. Troubleshooting

If the browser does not open automatically, update your client-side `~/.ssh/config` to force the login prompt:

```text
Host ssh.example.com
ProxyCommand cloudflared access ssh --hostname %h --id <your-client-id> --secret <your-client-secret>
```

(Note: Usually not required for basic Email OTP; the standard command works for interactive sessions)
