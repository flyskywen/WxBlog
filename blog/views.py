#!/usr/bin/python
# -*- coding: utf-8 -*-
# 视图函数

import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# 美化中文toc锚点
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


def get_paginator(request, post_list, num):
    # 实现分页,不用试图类
    # 5个文章一页
    paginator = Paginator(post_list, num)
    page = request.GET.get('page')
    try:
        post_list_page = paginator.page(page)
    except PageNotAnInteger:
        # 请求的页码不是整数,显示第一页
        post_list_page = paginator.page(1)
    except EmptyPage:
        # 请求页码超过了最大页码,显示最后一页
        post_list_page = paginator.page(paginator.num_pages)
    return post_list_page


# 首页视图函数context={} 可以简化为 {}
def index(request):
    # 元数据Meta默认按照-created_time排序
    post_list = Post.objects.all()

    post_list = get_paginator(request, post_list, 5)
    # left_ellipsis = True if (page - 1) > 4 else False
    # right_ellipsis= True if(paginator.num_pages - page) > 2 else False
    # render 可以传递参数
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })

    # return HttpResponse("欢迎访问我的博客首页！")

    # 可以传递参数到html页面
    # return render(request, 'blog/index.html', context={
    #    'title': '我的博客首页',
    #    'welcome': '欢迎访问我的博客首页'
    # })


# 分类页面
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')

    post_list = get_paginator(request, post_list, 5)
    return render(request, 'blog/category.html', context={
        'post_list': post_list,
        'category': cate
    })


# 标签页面
def tag(request, pk):
    ta = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=ta).order_by('-created_time')

    post_list = get_paginator(request, post_list, 5)
    return render(request, 'blog/tag.html', context={
        'post_list': post_list,
        'tag': ta
    })


# 归档页面,还没写
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 阅读量+1
    post.increase_views()
    # markdown转换为html
    md = markdown.Markdown(extensions=[
        # 支持 ```
        'markdown.extensions.extra',
        # 代码高亮
        'markdown.extensions.codehilite',
        # toc
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])
    # 正文
    post.body = md.convert(post.body)
    # TOC目录
    post.toc = md.toc

    # 导入form类
    form = CommentForm()
    # 获取post下的全部评论
    comment_list = post.comment_set.all()
    for comment in comment_list:
        # 实现评论展示支持markdown
        comment.text = markdown.markdown(comment.text,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)

# 实现复杂搜索是就不用这个视图函数了

# 简易搜索功能的实现
# 实现搜索功能,添加Q对象
# Q 对象。Q 对象用于包装查询表达式，其作用是为了提供复杂的查询逻辑。
# 例如这里 Q(title__icontains=q) | Q(body__icontains=q)
# 表示标题（title）含有关键词 q 或者正文（body）含有关键词 q ，或逻辑使用 | 符号。
# 如果不用 Q 对象，就只能写成 title__icontains=q, body__icontains=q，
# 这就变成标题（title）含有关键词 q 且正文（body）含有关键词 q，就达不到我们想要的目的。
# def search(request):
#     q = request.GET.get('q')
#     error_msg = ''
#     if not q:
#         error_msg = '请输入关键词'
#         return render(request, 'blog/index.html', {'error_msg': error_msg})
#
#     post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
#     return render(request, 'blog/index.html', {'error_msg': error_msg,
#                                                'post_list': post_list})
