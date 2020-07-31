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
                    CategoryListSet, DrfCategoryView, NewCategoryView, DrfPostView)

router = DefaultRouter()
router.register(r'users', UserListSet)
router.register(r'posts', PostListSet)
router.register(r'tags', TagListSet)
router.register(r'categorys', CategoryListSet)
# router.register(r'timelines', TimelineListSet)
# router.register(r'toollinks', ToolLinkListSet)


# 依赖于视图集，无法使用全自动路由
# router.register(r'drfcategory', DrfCategoryView)
# router.register(r'newdrfcategory', NewCategoryView)
# router.register(r'drfpost', DrfPostView)

# # drf练习
# path('drfcategory/', DrfCategoryView.as_view(), name='api_test'),
# path('drfcategory/<int:pk>/', DrfCategoryView.as_view()),
# # url(r'^drfcategore/(?P<pk>\d+)/$', DrfCategoryView.as_view()),
#
# path('newdrfcategory/', NewCategoryView.as_view(), name='new_api_test'),
# path('newdrfcategory/<int:pk>/', NewCategoryView.as_view(), name='new_api_test_1'),
#
# path('drfpost/', DrfPostView.as_view()),
