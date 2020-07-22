#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     blog_tags
   Description :
   Author :        WX_PC
   Date：          2018-2018/9/27-10:44
   Email:          flyskywen@outlook.com
--打印本页　 关闭窗口
中国人民银行授权全国银行间同业拆借中心公布，2020年7月20日贷款市场报价利率（LPR）为：1年期LPR为3.85%，5年期以上LPR为4.65%。以上LPR在下一次发布LPR之前有效。

-----------------------------------------------
   Change Activity:
                   2018-2018/9/27-10:44
-------------------------------------------------
"""
__author__ = 'WX_PC'

from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count
import re
from django.utils.html import mark_safe

register = template.Library()


# 获取数据库中前 num 篇文章，这里 num 默认为 5
# register注册模块
# @register.simple_tag
# def get_recent_posts(num=5):
#     return Post.objects.all()[:num]


# 归档模版标签
# 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
# 且是 Python 的 date 对象，精确到月份，降序排列。
# 接受的三个参数值表明了这些含义，一个是 created_time ，
# 即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）。
# 例如我们写了 3 篇文章，分别发布于 2017 年 2 月 21 日、2017 年 3 月 25 日、2017 年 3 月 28 日，
# 那么 dates 函数将返回 2017 年 3 月 和 2017 年 2 月这样一个时间列表，
# 且降序排列，从而帮助我们实现按月归档的目的。
@register.simple_tag
def archives(num=5):
    return Post.objects.dates('created_time', 'month', order='DESC')[:num]


# 分类模版标签
# @register.simple_tag
# def get_categories():
# 返回标签类对象
# return Category.objects.all()


# Count统计分类下有多少文章,返回所有标签类,给类添加num_posts属性
@register.simple_tag
def get_category_list():
    # Count 计算分类下的文章数,其接受的参数为需要统计的模型的名称
    # Category.objects.annotate 方法和 Category.objects.all 有点类似，
    # 它会返回数据库中全部 Category 的记录，但同时它还会做一些额外的事情，
    # 在这里我们希望它做的额外事情就是去统计返回的 Category 记录的集合中每条记录下的文章数。
    # 代码中的 Count 方法为我们做了这个事，它接收一个和 Categoty 相关联的模型参数名
    # （这里是 Post，通过 ForeignKey 关联的），
    # 然后它便会统计 Category 记录的集合中每条记录下的与之关联的 Post 记录的行数，
    # 也就是文章数，最后把这个值保存到 num_posts 属性中。
    # 此外，我们还对结果集做了一个过滤，使用 filter 方法把 num_posts 的值小于 1 的分类过滤掉。
    # 因为 num_posts 的值小于 1 表示该分类下没有文章，没有文章的分类我们不希望它在页面中显示。
    # 关于 filter 函数以及查询表达式（双下划线）在之前已经讲过，具体请参考 分类与归档。

    # 现在在 Category 列表中每一项都新增了一个 num_posts 属性记录该 Category 下的文章数量，
    # 我们就可以在模板中引用这个属性来显示分类下的文章数量了。
    # {{ category.post_all.count }} 改的html文档，也可以,但这样每个分类都要调用一次数据库
    # 这样只用调用一次数据库
    # 文章评论数也可以这样实现,comments/templatetags/comments_tags.py
    # 但评论数只用调用一次数据库,就不需要这种做法
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
# 实现标签云的方式和分类侧边栏的方式类似
def get_tag_list():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_post_list(sort=None, num=None):
    # 获取置顶排序方式和数量的文章
    if sort:
        if num:
            return Post.objects.order_by(sort)[:num]
    if num:
        return Post.objects.all()[:num]
    return Post.objects.all()


@register.simple_tag
def get_carousel_list():
    # 获取轮播图片
    return Post.objects.filter(is_carousel=True)


@register.simple_tag
def get_request_param(request, param, default=None):
    # 获取url请求的参数
    return request.POST.get(param) or request.GET.get(param, default)


@register.simple_tag
def my_highlight(text, q):
    '''自定义标题搜索词高亮函数，忽略大小写'''
    if len(q) > 1:
        try:
            text = re.sub(q, lambda a: '<span class="highlighted">{}</span>'.format(a.group()),
                          text, flags=re.IGNORECASE)
            text = mark_safe(text)
        except:
            pass
    return text
