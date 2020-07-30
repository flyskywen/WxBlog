# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     context_processors
   Author:        flyskywen
   date:          2020/7/27
-------------------------------------------------
   Change Activity:
                  2020/7/27:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'flyskywen'


# from django.conf import settings
# from .utils import site_full_url


# 自定义上下文管理器
def settings_info(request):
    return {
        'site_logo_name': '璇',
        'site_end_title': 'izone',
        'site_description': 'izone 是一个使用 Django+Bootstrap4 搭建的个人博客类型网站',
        'site_keywords': 'izone,Django博客,个人博客',

        # 'tool_flag': settings.TOOL_FLAG,
        # 是否开放api
        'api_flag': 'TRUE',
        # 'cnzz_protocol': settings.CNZZ_PROTOCOL,
        # 备案
        # 'beian': settings.BEIAN,
        'my_github': 'https://github.com/flyskywen',

        # 'site_verification': settings.MY_SITE_VERIFICATION,
        # 'site_url': site_full_url(),
        # 导航
        # 'hao_console': settings.HAO_CONSOLE
    }
