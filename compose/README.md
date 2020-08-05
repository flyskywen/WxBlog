# 文件结构
```txt
+----.env                 # 设置docker-compose的环境变量（文件需要自己创建）
+----db                   # db的挂载目录，挂载到容器
|    +----my.cnf          # db的配置文件，挂载到容器
+----docker-compose.yml   # docker-compose的运行文件
+----Dockerfile           # 生成python3镜像
+----Dockerfile-alpine    # 使用alpine生成python3镜像
+----nginx                # nginx挂载目录，挂载到容器
|    +----conf.d          # nginx服务配置目录，挂载到容器
|    |    +----nginx.conf # nginx服务配置文件，挂载到容器
```