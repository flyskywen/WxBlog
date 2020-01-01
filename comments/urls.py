#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :        WX_PC
   Date：          2018-2018/9/27-14:38
   Email:          flyskywen@outlook.com
-------------------------------------------------
   Change Activity:
                   2018-2018/9/27-14:38
-------------------------------------------------
"""
__author__ = 'WX_PC'

from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/post/<int:post_pk>/', views.post_comment, name='post_comment')
]
