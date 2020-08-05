# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     production
   Author:        dk
   date:          2020/8/4
-------------------------------------------------
   Change Activity:
                  2020/8/4:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'dk'

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yg3m1a5d8o^64ov@u#h+!69mutxfmcrrm$%_v@gmx40=29qi3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']
# 指定了 ALLOWED_HOSTS 的值后，django 将只允许通过指定的域名访问我们的应用，
# 比如这里只允许通过 127.0.0.1，localhost 以及 zmrenwu.com 和其任意子域名（域名前加一个点表示允许访问该域名下的子域名）访问（即 HTTP 报文头部中 Host 的值必须是以上指定的域名，
# 通常你在浏览器输入域名访问网站时，Host 的值就会被设置为网站的域名），这样可以避免 HTTP Host 头攻击。
