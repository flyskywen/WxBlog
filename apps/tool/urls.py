# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     urls.py
   Author:        dk
   date:          2020/8/7
-------------------------------------------------
   Change Activity:
                  2020/8/7:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'dk'

from . import views
from django.urls import path

app_name = 'tool'
urlpatterns = [
    path('', views.ToolView.as_view(), name='total'),  # 工具汇总页
    path('markdown-editor/', views.editor_view, name='markdown_editor'),  # editor.md 工具
]
