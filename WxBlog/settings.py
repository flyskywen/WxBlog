"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 文件目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yg3m1a5d8o^64ov@u#h+!69mutxfmcrrm$%_v@gmx40=29qi3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',

    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',  # 添加人性化过滤器
    'django.contrib.sitemaps',  # 网站地图

    'oauth',  # 自定义用户

    # 第三方用户管理
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

    # 美化表单
    'crispy_forms',

    # 较为复杂的搜索应用
    'haystack',  # tendocode说全文搜索应用 这个要放在其他应用之前，但我没看出为啥要放在之前
    'blog',
    'comments',

    # RESTful API
    'rest_framework',

]

# HAYSTACK_CONNECTIONS 的 ENGINE 指定了 django haystack 使用的搜索引擎，
# 这里我们使用了 blog.whoosh_cn_backend.WhooshEngine，
# 虽然目前这个引擎还不存在，但我们接下来会创建它。
# PATH 指定了索引文件需要存放的位置，
# 我们设置为项目根目录 BASE_DIR 下的 whoosh_index 文件夹（在建立索引是会自动创建）。

# HAYSTACK_SEARCH_RESULTS_PER_PAGE 指定如何对搜索结果分页，
# 这里设置为每 10 项结果为一页。

# HAYSTACK_SIGNAL_PROCESSOR 指定什么时候更新索引，
# 这里我们使用 haystack.signals.RealtimeSignalProcessor，
# 作用是每当有文章更新时就更新索引。由于博客文章更新不会太频繁，因此实时更新没有问题。


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WxBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # BASE_DIR 工程目录 即MyBlog/     最外层目录
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WxBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 注册mysql数据库
# options中设置sql模式,暂时看不懂
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'NAME': 'myblog',
#         'USER': 'root',
#         'PASSWORD': '920212',
#         # 这个问题本质上是由MySQL的模式引起的，它分宽松模式，严格模式，还有一大堆乱七八糟的模式。
#         # 有些模式即将过时。所以，才报上面的警告！
#         # http://www.testpub.cn/t/116
#         # 'OPTIONS': {
#         #    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         # },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# 修改语言和时区
# LANGUAGE_CODE = 'en-us'

# win
# LANGUAGE_CODE = 'zh_Hans'
# linux
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 解决mysql 时区不正确的问题,filter过滤月份开始不正常,也失去了时区功能!
# USE_TZ = True
USE_TZ = False

# 自定义

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

# 设置静态文件 文件夹
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_files"),
)

# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'oauth.Ouser'

# allauth配置
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# allauth需要的配置
# 当出现"SocialApp matching query does not exist"这种报错的时候就需要更换这个ID
# 默认：未指定
# 当前站点在django_site数据库表中的ID，一个整数，从1开始计数。
# 很多人都不知道Django是支持多站点同时运行的。
# 通常我们都只有一个站点，所以不关心这个选项。如果你同时运行了多个站点，
# 那么每个app就得知道自己是为那个站点或哪些站点服务的，这就需要SITE_ID参数了。

SITE_ID = 1

# 设置登录和注册成功后重定向的页面，默认是/accounts/profile/
LOGIN_REDIRECT_URL = "/"
# LOGIN_REDIRECT_URL = '/accounts/profile/'

# Email setting
# 注册中邮件验证方法:“强制（mandatory）”,“可选（optional）【默认】”或“否（none）”之一。
# 开启邮箱验证的话，如果邮箱配置不可用会报错，所以默认关闭，根据需要自行开启
# ACCOUNT_EMAIL_VERIFICATION = os.getenv('IZONE_ACCOUNT_EMAIL_VERIFICATION', 'none')
ACCOUNT_EMAIL_VERIFICATION = "optional"
# 登录方式，选择用户名或者邮箱都能登录
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# 设置用户注册的时候必须填写邮箱地址
ACCOUNT_EMAIL_REQUIRED = True

# 登出直接退出，不用确认
ACCOUNT_LOGOUT_ON_GET = True

# 邮箱配置  授权码：lqcgzxohyszrebji
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'runoobkui@qq.com'  # 你的 QQ 账号和授权码
EMAIL_HOST_PASSWORD = 'lqcgzxohyszrebji'
EMAIL_TIMEOUT = 5

EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
EMAIL_FROM = 'runoobkui@qq.com'  # 你的 QQ 账号
DEFAULT_FROM_EMAIL = '测试博客 <runoobkui@qq.com>'

# # 邮箱配置
# EMAIL_HOST = os.getenv('IZONE_EMAIL_HOST', 'smtp.163.com')
# EMAIL_HOST_USER = os.getenv('IZONE_EMAIL_HOST_USER', 'your-email-address')
# EMAIL_HOST_PASSWORD = os.getenv('IZONE_EMAIL_HOST_PASSWORD', 'your-email-password')  # 这个不是邮箱密码，而是授权码
# EMAIL_PORT = os.getenv('IZONE_EMAIL_PORT', 465)  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# EMAIL_TIMEOUT = 5
# # 是否使用了SSL 或者TLS，为了用465端口，要使用这个
# EMAIL_USE_SSL = os.getenv('IZONE_EMAIL_USE_SSL', 'True').upper() == 'TRUE'
# # 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
# DEFAULT_FROM_EMAIL = os.getenv('IZONE_DEFAULT_FROM_EMAIL', 'TendCode博客 <your-email-address>')
