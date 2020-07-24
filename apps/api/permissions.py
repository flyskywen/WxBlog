# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     permissions
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

from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
