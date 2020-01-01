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

from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from blog.feeds import AllPostsRssFeed

urlpatterns = [
    # django2.0之前的用法
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    # path('', include('comments.urls')),
    # url(r'^polls/', include('polls.urls')),
    # django2.0后的path方法
    # 建议把路径写在app.urls中,工程路径包含
    # 除了admin路由外，尽量给每个app设计自己独立的二级路由
    # include的import路径也发生了改变
    # from django.urls import path,include
    path('', include('polls.urls')),
    path('', include('comments.urls')),
    path('all/rss/', AllPostsRssFeed(), name='rss'),

    # 配置 URL，搜索的视图函数和 URL 模式 django haystack 都已经帮我们写好了，
    # 只需要项目的 urls.py 中包含它
    path('search/', include('haystack.urls'))
]
