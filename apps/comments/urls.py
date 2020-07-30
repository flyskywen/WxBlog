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
    # path('comment/post/<int:post_pk>/', views.post_comment, name='post_comment')
    path('add/', views.AddcommentView, name='add_comment'),

    path('notification/', views.NotificationView, name='notification'),
    path('notification/no-read/', views.NotificationView, {'is_read': 'false'}, name='notification_no_read'),
    path('notification/mark-to-read/', views.mark_to_read, name='mark_to_read'),
    path('notification/mark-to-delete/', views.mark_to_delete, name='mark_to_delete'),
]
