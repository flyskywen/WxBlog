#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     feeds.py
   Description :
   Author :        WX_PC
   Date：          2018-2018/9/28-14:58
   Email:          flyskywen@outlook.com
-------------------------------------------------
   Change Activity:
                   2018-2018/9/28-14:58
-------------------------------------------------
"""
__author__ = 'WX_PC'

# 在 blog 应用的根目录下（models.py 所在目录）新建一个 feeds.py 文件
# 以存放和 RSS 功能相关的代码。

from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Django 博客教程演示项目"

    # 通过聚合阅读器跳转到网站的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    description = "Django 博客教程演示项目测试文章"

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body
