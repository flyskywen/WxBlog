#!/bin/sh

# 安装依赖,本地使用国内镜像
# pip install -r requirements.txt -i https://pypi.douban.com/simple

python manage.py makemigrations
python manage.py migrate
#python manage.py compilemessages
python manage.py runserver 0.0.0.0:8000


#python manage.py collectstatic --noinput &&
#python manage.py makemigrations &&
#python manage.py migrate &&
#python manage.py runserver 0.0.0.0:8080