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
```