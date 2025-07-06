---
title: Lobe Chat
number: 105
url: https://github.com/ysl2/.dotfiles/discussions/105
createdAt: 2025-02-16T10:09:59Z
lastEditedAt: 2025-06-27T14:44:49Z
updatedAt: 2025-06-27T14:45:10Z
author: ysl2
category: common
labels: []
countZH: 320
countEN: 470
filename: 2502-Lobe-Chat
---

```
lobe chat main branch, commit: 2dc712a9be7a8a62a677bfd4220b686eeb0f6b11
```

注意：重新安装时，只需要删掉lobe-chat容器，然后拉取最新lobe-chat容器，执行`docker compose up -d`。不要删除`docker-compose.yml`和`init_data.json`，也不要删除`data`和`s3_data`。否则之前的数据就丢失了。代码是否拉取最新的无所谓。因为使用的并不是最新代码提供的docker compose文件，而是本地的。

```bash
docker rm -f lobe-chat
docker pull lobehub/lobe-chat-database:latest
docker compose up -d  # Or: docker-compose up -d
```

```bash
pwd
# /Users/yusongli/Documents/lobe-chat/docker-compose

docker rm -f lobe-chat lobe-minio lobe-casdoor lobe-network lobe-postgres
rm -rf data s3_data
cp local/docker-compose.yml local/init_data.json .
cp local/.env.example .env
sed -i 's#./server --createDatabase=true#sleep 5; ./server --createDatabase=true#g' docker-compose.yml
# Add `S3_SET_ACL=0` to lobe chat for minio
# sed -i "0,/^\\([ \t]*\\).*S3_BUCKET.*/ { // { h; s//\\1- 'S3_SET_ACL=0'/; H; x; } }" docker-compose.yml
# For embedding:
echo "\nDEFAULT_FILES_CONFIG=embedding_model=siliconcloud/Pro/BAAI/bge-m3" >> .env
sed -i "0,/^\\([ \t]*\\).*NEXT_AUTH_SSO_PROVIDERS.*/ { // { h; s//\\1- 'DEFAULT_FILES_CONFIG=\${DEFAULT_FILES_CONFIG}'/; H; x; } }" docker-compose.yml
# sed -i 's/host=postgresql/host="host.docker.internal"/g' docker-compose.yml
# sed -i 's/postgresql:5432/host.docker.internal:5432/g' docker-compose.yml
patch < diff
bash setup.sh
docker compose up -d  # Or: docker-compose up -d
```

```diff
diff --git a/docker-compose/setup.sh b/docker-compose/setup.sh
index c52770aac..fcd1dbeb3 100644
--- a/docker-compose/setup.sh
+++ b/docker-compose/setup.sh
@@ -6,13 +6,13 @@
 
 # check operating system
 # ref: https://github.com/lobehub/lobe-chat/pull/5247
-if [[ "$OSTYPE" == "darwin"* ]]; then
-    # macOS
-    SED_COMMAND="sed -i ''"
-else
+# if [[ "$OSTYPE" == "darwin"* ]]; then
+#     # macOS
+#     SED_COMMAND="sed -i ''"
+# else
     # not macOS
     SED_COMMAND="sed -i"
-fi
+# fi
 
 # ======================
 # == Process the args ==
@@ -446,8 +446,8 @@ section_download_files(){
 if [ -d "data" ] || [ -d "s3_data" ]; then
     show_message "tips_already_installed"
     exit 0
-else
-    section_download_files
+# else
+#     section_download_files
 fi
 
 section_configurate_host() {
@@ -480,7 +480,11 @@ section_configurate_host() {
     
     # If user not specify host, try to get the server ip
     if [ -z "$HOST" ]; then
-        HOST=$(hostname -I | awk '{print $1}')
+        if [[ "$OSTYPE" == "darwin"* ]]; then
+            HOST=$(ifconfig en0 |awk '/inet / {print $2; }')
+        else
+            HOST=$(hostname -I | awk '{print $1}')
+        fi
         # If the host is a private ip and the deploy mode is port mode
         if [[ "$DEPLOY_MODE" == "1" ]] && ([[ "$HOST" == "192.168."* ]] || [[ "$HOST" == "172."* ]] || [[ "$HOST" == "10."* ]]); then
             echo $(show_message "tips_private_ip_detected")
```

---

同样的问题，使用env进行配置时，向量化时返回的错误时401, provider: siliconcloud, 但如果通过webui配置openai key为对应的SILICONCLOUD_API_KEY, 向量化返回的错误是413, 可判断出来embedding model是用了siliconcloud，但是key还是用的openai key...

关键的env配置如下

SILICONCLOUD_API_KEY=sk-xxxxxxxxxxxx
SILICONCLOUD_PROXY_URL=https://api.siliconflow.cn/v1/
DEFAULT_FILES_CONFIG=embedding_model=siliconcloud/netease-youdao/bce-embedding-base_v1
刚刚去看了代码实现，代码实现是通过从DEFAULT_FILES_CONFIG 截取 PROVIDER 来组合提取env中存在的${PROVIDER}_API_KEY,${PROVIDER}_PROXY_URL 来构建对应的请求的，如果没有${PROVIDER}_API_KEY会使用OPENAI_API_KEY来兜底，兜底这个行为本身需要斟酌，因为可能导致没有正确配置的环境把openai的key暴露到不匹配的provider，但是代码逻辑本身没有问题。
最后我使用相同环境下重新部署了一次，没有再次复现这个问题。

PS: 413是因为该模型不支持1024维，换了BAAI后正常。

## 把这里换成siliconflow的key和proxy，用于embedding模型

<img width="1708" alt="Image" src="https://github.com/user-attachments/assets/8813109b-a98c-49d0-86a2-c764cf1566c5" />