FROM python:3.8-alpine
MAINTAINER flyskywen<flyskywen@outlook.com>

# python环境变量
ENV PYTHONUNBUFFERED 1

RUN apk update

#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
#使用sed工具将字符串dl-cdn.alpinelinux.org替换为mirrors.aliyun.com

# Pillow dependencies
RUN apk add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
#RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev gcc

# 在镜像中创建目录，用来存放本机中的django项目
RUN mkdir /usr/src/app
# 将项目中所有文件都拷贝到容器中指定目录
# docker-compose已经挂载
#COPY ../../../ /usr/src/app
# 将/usr/src/app指定为工作目录
WORKDIR /usr/src/app

# 更新pip
RUN pip3 install pip --upgrade

# 目录取决于docker-compose的context

# 安装依赖
COPY  ./requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

#COPY Pipfile /app/Pipfile
#COPY Pipfile.lock /app/Pipfile.lock
#RUN pipenv install

# 开放容器的8080端口，允许外部链接这个端口
# EXPOSE 8000

# 运行start.sh
COPY ./compose/local/Django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

