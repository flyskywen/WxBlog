# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     urls.py
   Author:        dk
   date:          2020/7/15
-------------------------------------------------
   Change Activity:
                  2020/7/15:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'dk'

from django.urls import path
from .views import profile_view, change_profile_view

# 写app_name 和在 总urls.py写 namespace效果相同
app_name = 'oauth'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/change/', change_profile_view, name='change_profile'),

]
