# domain

## 1. Prerequisites

1. Public IP address, or a VPS with public IP address.

2. Your service is running on the server with public IP address, and you can access it by `http://<PUBLIC_IP>:<SERVICE_PORT>`.

3. Buy domain from <https://www.namecheap.com/>, for example, your domain is `example.com`.

## 2. Configure domain's DNS

> Ref: <https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/>

1. Namecheap dashboard -> "Domain List" -> "Manage" -> "Advanced DNS" -> "Host Records" -> "Add New Record"

   ```text
   Type: A Record
   Host: @
   Value: <PUBLIC_IP>
   TTL: Automatic
   ```

2. If you also want to enable `www` for `www.example.com` support, add another record:

   ```text
   Type: A Record
   Host: www
   Value: example.com
   TTL: Automatic
   ```

3. If you also want to add `app` subdomain for `app.example.com` support, add another record:

   ```text
   Type: CNAME Record
   Host: www
   Value: example.com
   TTL: Automatic
   ```

## 3. Install nginx on public IP address server

1. ssh to your server with public IP address.

   ```bash
   ssh -p <YOUR_PORT> <YOUR_USERNAME>@<PUBLIC_IP>
   ```

2. Install nginx

   ```bash
   # For Debian/Ubuntu
   sudo apt update
   sudo apt install nginx
   ```

   Open firewall for nginx, also, you should open your cloud provider's firewall for port 80 and 443.

   ```bash
   # sudo ufw allow 'Nginx Full'
   # Or
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```

## 3. Configure nginx forword rules for your current service

```bash
sudo vim /etc/nginx/sites-available/<SERIVICE_NAME>
```

Add the following content to the file, replace `<SERVICE_PORT>` with your service port.

Note: you should replace `example.com` with your domain name, and if you also want to support `www.example.com`, you can add it to `server_name` as well.

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location / {
        proxy_pass http://<PUBLIC_IP>:<SERVICE_PORT>;
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the nginx configuration and restart nginx.

```bash
sudo ln -s /etc/nginx/sites-available/<SERIVICE_NAME> /etc/nginx/sites-enabled/<SERIVICE_NAME>
sudo nginx -t
sudo systemctl restart nginx
```

Then, visit `http://example.com` in your browser, you should see your service is accessible through the domain name.

## 4. Add HTTPS support with certbot

```bash
# Install certbot with snap:
# sudo apt install snapd
# sudo snap install certbot --classic
# Or install certbot with apt:
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
```

Follow the prompts to complete the certificate installation. After that, your domain will be accessible via HTTPS.
