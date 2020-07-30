# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     form
   Author:        dk
   date:          2020/7/14
-------------------------------------------------
   Change Activity:
                  2020/7/14:
-------------------------------------------------
   Description:
                  Description
------------------------------------------------
"""
__author__ = 'dk'

from django import forms
from .models import Ouser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ouser
        fields = ['link', 'avatar']
