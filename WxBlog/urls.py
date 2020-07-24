"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from blog.feeds import AllPostsRssFeed

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from api.views import DrfCategoryView, NewCategoryView, DrfPostView

router = routers.DefaultRouter()

urlpatterns = [
                  # django2.0之前的用法,用正则进行匹配
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('blog.urls')),

                  # django2.0后的path方法
                  # 建议把路径写在app.urls中,工程路径包含
                  # 除了admin路由外，尽量给每个app设计自己独立的二级路由
                  # include的import路径也发生了改变
                  # from django.urls import path,include

                  path('', include('comments.urls')),

                  # path('', include('polls.urls'))  之前测试用的
                  # url(r'^polls/', include('polls.urls')),

                  # rss订阅
                  path('all/rss/', AllPostsRssFeed(), name='rss'),

                  # 配置 URL，搜索的视图函数和 URL 模式 django haystack 都已经帮我们写好了，
                  # 只需要项目的 urls.py 中包含它
                  path('search/', include('haystack.urls')),

                  # 第三方登录注册
                  path('accounts/', include('allauth.urls')),

                  # 用户信息
                  path('oauth/', include('oauth.urls')),

                  # restful api
                  # path("api/", include(router.urls)),
                  # path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

                  # drf练习
                  path('drfcategory/', DrfCategoryView.as_view(), name='api_test'),
                  path('drfcategory/<int:pk>/', DrfCategoryView.as_view()),
                  # url(r'^drfcategore/(?P<pk>\d+)/$', DrfCategoryView.as_view()),

                  path('newdrfcategory/', NewCategoryView.as_view(), name='new_api_test'),
                  path('newdrfcategory/<int:pk>/', NewCategoryView.as_view(), name='new_api_test_1'),

                  path('drfpost/', DrfPostView.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 我选择将文件夹放入静态文件夹中
# 加入这个才能显示media文件,添加静态文件夹路径

# if settings.API_FLAG:
from api.urls import router

urlpatterns.append(path('api/v1/', include((router.urls, router.root_view_name), namespace='api')))  # restframework
