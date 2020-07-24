# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     urls
   Author:        dk
   date:          2020/7/23
-------------------------------------------------
   Change Activity:
                  2020/7/23:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'dk'

from rest_framework.routers import DefaultRouter
from .views import (UserListSet, PostListSet, TagListSet,
                    CategoryListSet)

router = DefaultRouter()
router.register(r'users', UserListSet)
router.register(r'posts', PostListSet)
router.register(r'tags', TagListSet)
router.register(r'categorys', CategoryListSet)
# router.register(r'timelines', TimelineListSet)
# router.register(r'toollinks', ToolLinkListSet)
