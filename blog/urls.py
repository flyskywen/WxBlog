# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py
   Description :
   Author :        WX_PC
   Date：          2018-2018/9/26-9:12
   Email:          flyskywen@outlook.com
-------------------------------------------------
   Change Activity:
                   2018-2018/9/26-9:12
-------------------------------------------------
"""
__author__ = 'WX_PC'

# 在项目根目录的 MyBlog\ 目录下（即 settings.py 所在的目录），
# 原本就有一个 urls.py 文件，这是整个工程项目的 URL 配置文件。
# 而我们这里新建了一个 urls.py 文件，且位于 blog 应用下。
# 这个文件将用于 blog 应用相关的 URL 配置。不要把两个文件搞混了。

# from django.conf.urls import url
from django.urls import path
from . import views

# 通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，
# 这种技术叫做视图函数命名空间
app_name = 'blog'
urlpatterns = [
    # 绑定url和视图函数
    # 我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到
    # 首页
    # url(r'^$', views.index, name='index'),
    # 它的第一个参数是 URL 模式，第二个参数是视图函数 index。
    # 对 url 函数来说，第二个参数传入的值必须是一个函数。
    # 而 IndexView 是一个类，不能直接替代 index 函数。
    # 好在将类视图转换成函数视图非常简单，只需调用类视图的 as_view() 方法即可
    # url(r'^$', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('hot/', views.index, {'hot': True}, name='index_hot'),
    # re_path(r'^(/hot/)*$', views.index, name='index'), # 这个想法不太成熟

    # 分类页面 /category/id
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', views.category, name='category'),
    path('category/<int:pk>/hot/', views.category, {'hot': True}, name='category_hot'),

    # 标签Tag页面  /tag/id
    path('tag/<int:pk>/', views.tag, name='tag'),
    path('tag/<int:pk>/hot/', views.tag, {'hot': True}, name='tag_hot'),

    # <网站域名>/post/2/
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/', views.detail, name='detail'),

    # 归档页面 /archives/years/month
    # url中包含year和month参数 传递给archives视图函数
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),

    # 搜索页面,使用了haystack建立了更为复杂的搜索
    # path('search/', views.search, name='search'),
]
