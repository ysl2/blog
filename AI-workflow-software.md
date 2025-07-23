# AI workflow software

## Openai official ChatGPT

需要：
ios设备，梯子环境，美区账号(地区在美国五个免税州内)，支付宝，chatgpt账号

步骤：

- ios设备，地区切换到美国，系统语言切换英文
- 美区账号下载chatgpt app
- 通过支付宝小程序给美区账号充值礼品卡
- chatgpt app登录账号，通过美区账号充值gpt4

其他：到这个[链接](https://platform.openai.com/api-keys)中登录获取api key,然后部署到其他地方(但由于后面好像还要充值，没再继续部署)

## gemini-cli

```bash
git clone git@github.com:ysl2/gemini-cli.git
cd gemini-cli
npm run clean && npm run build && npm install -g .
```

Usage:

```bash
# For google login:
NODE_NO_WARNINGS=1 http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOOGLE_CLOUD_PROJECT=test-project-key gemini -m gemini-2.5-pro

# For openai API models:
NODE_NO_WARNINGS=1 OPENAI_API_KEY=test-api-key OPENAI_BASE_URL=https://api.example.com OPENAI_MODEL=test-model gemini
```
