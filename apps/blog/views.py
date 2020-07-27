#!/usr/bin/python
# -*- coding: utf-8 -*-
# 视图函数

import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
# from comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

from django.views.generic import ListView, DetailView

# 美化中文toc锚点
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

# detail缓存
from django.core.cache import cache
import time, datetime


# 指定三个属性
# model。将 model 指定为 Post，告诉 django 我要获取的模型是 Post。
# template_name。指定这个视图渲染的模板。
# context_object_name。指定获取的模型列表数据保存的变量名，这个变量会被传递给模板。

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10

    # 不清楚这个属性的意义
    paginate_orphans = 5

    # 排序
    def get_ordering(self):
        hot = self.kwargs.get('hot')
        if hot:
            return '-views', '-created_time', '-id'
        else:
            return '-is_top', '-created_time'


class CategoryView(ListView):
    model = Post
    template_name = 'blog/category.html'

    context_object_name = 'post_list'

    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10

    # 不清楚这个属性的意义
    paginate_orphans = 5

    def get_ordering(self):
        hot = self.kwargs.get('hot')
        if hot:
            return '-views', '-created_time', '-id'
        return '-created_time'

    def get_queryset(self):
        # 筛选
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data()
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        context_data['search_tag'] = '文章分类'
        context_data['search_instance'] = cate
        return context_data


class TagView(ListView):
    model = Post
    template_name = 'blog/tag.html'
    context_object_name = 'post_list'
    paginate_by = 10
    paginate_orphans = 5

    def get_ordering(self):
        hot = self.kwargs.get('hot')
        if hot:
            return '-views', '-created_time', '-id'
        return '-created_time'

    # def get_ordering(self):
    #     ordering = super(TagView, self).get_ordering()
    #     hot = self.kwargs.get('hot')
    #     if hot:
    #         return '-views', '-update_date', '-id'
    #     return ordering

    def get_queryset(self):
        ta = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=ta)

    def get_context_data(self, **kwargs):
        context_data = super(TagView, self).get_context_data()
        ta = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        context_data['search_tag'] = '文章标签'
        context_data['search_instance'] = ta
        return context_data


class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过半小时才重新统计阅览量,作者浏览忽略
        u = self.request.user
        ses = self.request.session
        # the_key = 'is_read_{}'.format(obj.id)
        the_key = f'is_read_{obj.id}'  # 是否阅读本篇文章
        is_read_time = ses.get(the_key)
        if u != obj.author:
            # 非作者
            if not is_read_time:
                # 无key参数，更新阅览量
                obj.increase_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 60 * 30:
                    # 阅览半小时，更新阅览量
                    obj.increase_views()
                    ses[the_key] = time.time()

        # 获取文章更新的时间，判断是否从缓存中取文章的markdown,可以避免每次都转换

        # ud = obj.update_date.strftime("%Y%m%d%H%M%S")
        # 修改的时间
        ud = obj.modified_time.strftime("%Y%m%d%H%M%S")
        md_key = '{}_md_{}'.format(obj.id, ud)
        cache_md = cache.get(md_key)
        print(cache_md)
        if cache_md:
            obj.body, obj.toc = cache_md
            # obj.boy = cache_md
        else:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                TocExtension(slugify=slugify),
            ])
            obj.body = md.convert(obj.body)
            obj.toc = md.toc
            # 暂时没有用上toc，之后可以使用body_to_markdownandtoc方法实现
            # 很离奇，使用markdown.Markdown，可以正确是safe
            # 而markdown.markdown，却无法正确的safe

            obj.body = obj.body_to_markdown()
            cache.set(md_key, (obj.body, obj.toc), 60 * 60 * 12)
            # cache.set(md_key, obj.body, 60 * 60 * 12)

        return obj


def get_paginator(request, post_list, num):
    # 实现分页,不用视图类
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


def change_hot(request, post_list, hot):
    if hot:
        # 按访问量降序排列
        post_list = post_list.order_by('-views')
    return post_list


# 首页视图函数context={} 可以简化为 {}
def index(request, hot=False):
    # 元数据Meta默认按照-created_time排序
    post_list = Post.objects.all()

    # 是否按照热度排序
    post_list = change_hot(request, post_list, hot)
    post_list = get_paginator(request, post_list, 5)

    # render 可以传递参数
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })

    # return HttpResponse("欢迎访问我的博客首页！")

    # 可以传递参数到html页面
    # return render(request, 'blog/index.html', context={
    #    'title': '我的博客首页',
    #    'welcome': '欢迎访问我的博客首页'
    # })


# 分类页面
def category(request, pk, hot=False):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')

    # 是否按照热度排序
    post_list = change_hot(request, post_list, hot)
    post_list = get_paginator(request, post_list, 5)
    return render(request, 'blog/category.html', context={
        'post_list': post_list,
        'category': cate
    })


# 标签页面
def tag(request, pk, hot=False):
    ta = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=ta).order_by('-created_time')

    # 是否按照热度排序
    post_list = change_hot(request, post_list, hot)
    post_list = get_paginator(request, post_list, 5)
    return render(request, 'blog/tag.html', context={
        'post_list': post_list,
        'tag': ta,
    })


# 归档页面
# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month).order_by('-created_time')
#     return render(request, 'blog/index.html', context={
#         'post_list': post_list
#     })
def archives(request):
    post_list = Post.objects.all()
    return render(request, 'blog/archive.html', context={
        'post_list': post_list
    })


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 上一篇文章，下一篇文章
    # previous_post = post.get_pre()
    # next_post = post.get_next()

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
    # form = CommentForm()
    # 获取post下的全部评论
    # comment_list = post.comment_set.all()
    # comment_list = post.post_comments_set.all()
    # belong = models.ForeignKey(Post, related_name='post_comments', verbose_name='所属文章',
    #                            on_delete=models.CASCADE)
    comment_list = post.post_comments.all()

    for comment in comment_list:
        # 实现评论展示支持markdown
        comment.text = markdown.markdown(comment.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
    context = {
        'post': post,
        # 'form': form,
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
# from django.db.models import Q
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
