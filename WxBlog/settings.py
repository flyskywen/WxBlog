"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 文件目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    'blog',
    'comments',
    # 较为复杂的搜索应用
    'haystack'
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

# 设置静态文件 文件夹
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_files"),
)
