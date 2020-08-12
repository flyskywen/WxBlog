```bash
# 下载https://nodejs.org/zh-cn/
wget https://nodejs.org/dist/v14.8.0/node-v14.8.0-linux-x64.tar.xz
# 实际上我安装在主目录的APP文件目录下
sudo tar -zxvf node-v10.15.3-linux-x64.tar.gz -C /usr/local/

sudo ln -s /home/dk/App/node-v14.8.0-linux-x64/bin/node /usr/local/bin/
sudo ln -s /home/dk/App/node-v14.8.0-linux-x64/bin/npm /usr/local/bin/

node -v
v14.8.0

# 修改npm源为淘宝源
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org

# 这个命令生效了
npm config set registry=https://registry.npm.taobao.org

# 查看
npm config get registry
https://registry.npm.taobao.org/
npm config list
; cli configs
metrics-registry = "https://registry.npm.taobao.org/"
scope = ""
user-agent = "npm/6.14.7 node/v14.8.0 linux x64"

; userconfig /home/dk/.npmrc
registry = "https://registry.npm.taobao.org/"

; node bin location = /home/dk/App/node-v14.8.0-linux-x64/bin/node
; cwd = /home/dk
; HOME = /home/dk
; "npm config ls -l" to show all defaults.

# 最新稳定版
npm install vue -g
# 安装vue-cli脚手架构建工具
npm install vue-cli -g

# 直接运行vue，找不到命令，需要软链接（和我的安装位置有关）
sudo ln -s /home/dk/App/node-v14.8.0-linux-x64/bin/vue /usr/local/bin/vue
vue -V
2.9.6
```



```bash
# 启动项目报错
vue create vue-proj

  vue create is a Vue CLI 3 only command and you are using Vue CLI 2.9.6.
  You may want to run the following to upgrade to Vue CLI 3:

  npm uninstall -g vue-cli
  npm install -g @vue/cli

```

