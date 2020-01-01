#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :        WX_PC
   Date：          2018-2018/9/26-9:52
   Email:          flyskywen@outlook.com
-------------------------------------------------
   Change Activity:
                   2018-2018/9/26-9:52
-------------------------------------------------
"""
__author__ = 'WX_PC'

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^polls/', views.index, name='index'),
]
