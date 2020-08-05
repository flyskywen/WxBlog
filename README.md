# Django个人博客  

重新开始

```text
django==2.2

# 文章搜索功能
# 在win 中多安装了一个 haystack库
django-haystack
whoosh
jieba

# 实现文章显示markdown
Pygments
Markdown

# Django上传图片
pillow

# Faker 快速生成测试数据
Faker

＃ 第三方图片处理
django-imagekit

#　第三方用户管理
django-allauth

# 美化表单
django-crispy-forms

# API
djangorestframework django-filter

# 测试脚本
faker

# 异步
# 暂时不使用celery，未搞清楚原理
#celery
#django-celery


# 缓存
django-redis

# 生产环境中使用的服务进程
pip install supervisor
```

＃ Tips
```text
学习redis, blog/views.py

docker redis配置未完成，django无法正确连接redis

# 安装docker-compose
pip install docker-compose

# 实际上就是把所有static文件收集在static文件夹中
python manage.py collectstatic

# 所以nginx中有个一个设置是有问题的 不能使用static_files配置

# nginx 静态资源指向 static文件夹和media文件夹 就解决了,就修改了docker-compose挂载而已
```