#FROM nginx:1.17.1

# 替换为国内源 我的服务器不需要这个步骤
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
#COPY ./compose/production/nginx/sources.list /etc/apt/

#RUN apt-get update && apt-get install -y --allow-unauthenticated certbot python-certbot-nginx

#RUN rm /etc/nginx/conf.d/default.conf

# Proxy configurations
#COPY ./compose/production/nginx/includes/ /etc/nginx/includes/


# 使用docker仓库中的基础nginx镜像
FROM nginx
# 开放端口
EXPOSE 80 8000
# 删除nginx原有配置文件
RUN rm /etc/nginx/conf.d/default.conf
# 将自己写的配置文件添加到容器
#ADD conf.d/nginx.conf /etc/nginx/conf.d/
COPY conf.d/nginx.conf /etc/nginx/conf.d/nginx.conf
# 创建web应用的静态文件存储
RUN mkdir -p /usr/share/nginx/html/static
RUN mkdir -p /usr/share/nginx/html/media
