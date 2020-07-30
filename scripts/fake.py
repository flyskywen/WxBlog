# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     Faker
   Author:        dk
   date:          2020/1/10
-------------------------------------------------
   Change Activity:
                  2020/1/10:
-------------------------------------------------
   Description:
                  自动生成测试文章脚本
------------------------------------------------
"""
__author__ = 'dk'

import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    # 首先设置 DJANGO_SETTINGS_MODULE 环境变量，这将指定 django 启动时使用的配置文件，然后运行 django.setup() 启动 django。
    # 这是关键步骤，只有在 django 启动后，我们才能使用 django 的 ORM 系统。django 启动后，就可以导入各个模型，以便创建数据。
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WxBlog.settings")
    django.setup()

    from blog.models import Category, Post, Tag
    from comments.models import PostComment, Notification
    # PostComment保存好，Notification自动更新
    # from django.contrib.auth.models import User
    from oauth.models import Ouser

    # 清除旧数据，因此每次运行脚本，都会清除原有数据，然后重新生成
    print('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    PostComment.objects.all().delete()
    Ouser.objects.all().delete()

    # 生成测试数据
    print('create a blog user')
    # user = User.objects.create_superuser('admin', 'admin@hellogithub.com', 'admin')
    user = Ouser.objects.create_superuser('testID', 'admin@hellogithub.com', 'mike7452')
    re_user = Ouser.objects.create_user('test', 'test@qq.com', 'mike7452')

    category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Docker', 'Nginx', 'Elasticsearch', 'Gunicorn', 'Supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)

    print('create categories and tags')
    for cate in category_list:
        Category.objects.create(name=cate, description='分类描述')

    for tag in tag_list:
        Tag.objects.create(name=tag, description='标签描述')

    # 需要把自动生成创建时间和修改时间的字段写好
    print('create a markdown sample post')
    Post.objects.create(
        title='Markdown 与代码高亮测试',
        body=pathlib.Path(BASE_DIR).joinpath('scripts', 'sample.md').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown测试'),
        # tags=Tag.objects.create(name='Markdown标签测试'),
        author=user,
        is_carousel=True,
    )

    # 生成大量英文post
    print('create some faked posts published within the past year')
    # fake = faker.Faker()  # English
    fake = faker.Faker('zh_CN')
    for x in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=user,
        )
        post.tags.add(tag1, tag2)
        post.save()

        print(f'create {x} parent comments')
        PostComment.objects.create(
            author=user,
            content='测试评论',
            belong=post
        )
        PostComment.objects.create(
            author=re_user,
            content='测试评论',
            belong=post
        )
