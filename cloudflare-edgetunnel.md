# cloudflare-edgetunnel

> Ref: https://x.com/Pangty06116/status/2040265254719078441?s=20

## 🛠️ 第一步：搞定免费域名，并托管到 CF

注意：千万别用 CF 自带的 <http://workers.dev> 域名，早就被墙烂了。

1. 去 DNSHE 平台注册个免费域名（推荐 .us.ci 这种冷门后缀，容易过)。注册免费域名： <https://www.dnshe.com/>

1. 登录 Cloudflare（免费注册即可），把刚申请的域名添加进去托管。注册 cloudflare 账号：<https://cloudflare.com/zh-cn/>

1. 回到 DNSHE，把域名的 DNS 修改成 CF 提供的地址，耐心等 CF 状态变成“有效”。

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-08-05.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-10-52.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-11-13.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-11-38.png" alt="" width=100% style="display: block; margin: auto;"></p>

## ⚙️ 第二步：部署核心后端 (Pages)

这步我们用 CF Pages 部署开源项目 Edgetunnel，比老旧的 Workers 方法更稳定。

在 CF 后台点「存储和数据库」->「Workers KV」，随便建个命名空间（名字自定义随便取）。

转到「Workers 和 Pages」，选择创建 Pages。

把准备好的 edgetunnel 代码包传上去（Zip上传或连 GitHub 部署都行）。由 CMliu 开源的程序源码地址：<https://github.com/cmliu/edgetunnel/>；或者小白直接下载现成的压缩包：<https://github.com/cmliu/edgetunnel/archive/refs/heads/main.zip>


<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-14-42.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-15-03.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-15-22.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-15-40.png" alt="" width=100% style="display: block; margin: auto;"></p>

## 🔒 第三步：绑定域名与安全配置（环境变量设置）

1. 部署完成后点击 继续处理站点 后，选择 设置 > 环境变量 > 制作为生产环境定义变量 > 添加变量。 变量名称填写ADMIN，值则为你的管理员密码，后点击 保存 即可。返回 部署 选项卡，在右下角点击 创建新部署 后，重新上传 [main.zip](https://github.com/cmliu/edgetunnel/archive/refs/heads/main.zip) 文件后点击 保存并部署 即可。

1. 绑定 KV 命名空间：
在 设置选项卡中选择 绑定 > + 添加 > KV 命名空间，然后选择一个已有的命名空间或创建一个新的命名空间进行绑定。
变量名称填写KV，然后点击 保存后重试部署即可。

1. 给 Pages绑定 CNAME自定义域：
在 Pages控制台的 自定义域 选项卡，下方点击 设置自定义域。
填入你的自定义次级域名，注意不要使用你的根域名，例如： 您分配到的域名是 [xxxxxx.us.ci](xxxxxx.us.ci)，则添加自定义域填入 [xxxxxx.us.ci](xxxxxx.us.ci) 即可；
按照 CF 的要求将返回你的域名DNS服务商，添加 该自定义域 lizi的 CNAME记录 <http://edgetunnel.pages.dev> 后，点击 激活域 即可。

1. 访问后台：
例如：以我的后台为实例访问： <https://pangty06116.us.ci/admin>
输入管理员密码即可登录后台。

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-16-11.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-16-23.png" alt="" width=100% style="display: block; margin: auto;"></p>

## 🚀 第四步：获取节点，速度拉满

浏览器访问 你的域名/你的UUID，进入酷炫的后台页面，直接复制 VLESS 节点或者通用订阅链接。

打开客户端（如 v2rayN、小火箭）导入链接。

🔥 敲黑板（高阶玩法）：直接连可能慢。可自选下列“CF 优选 IP”，或者网上自选资源。把客户端里的「地址(Address)」改成优选 IP，但「伪装域名(SNI)」必须保持你的免费域名不变！这样网速直接起飞！小白不愿意折腾直接默认PROXYIP自选即可。通用订阅链接基本能满足主流代理软件使用。

当然如果你需要自定义更多的选项，比如优选订阅地址，指定ProxyIP订阅，那么可以点击顶部的：我是高手！我就是要折腾！

优选订阅地址：

- Cm.Soso.Edu.Kg
- Sub.Cmliussss.Net
- Owo.O00o.Ooo

PROXYIP 订阅:

- ProxyIP.US.CMLiussss.Net
- ProxyIP.SG.CMLiussss.Net
- ProxyIP.JP.CMLiussss.Net

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-16-55.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-17-11.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-17-24.png" alt="" width=100% style="display: block; margin: auto;"></p>

<p><img src=".assets/cloudflare-edgetunnel/img/2026-04-07-15-17-38.png" alt="" width=100% style="display: block; margin: auto;"></p>
