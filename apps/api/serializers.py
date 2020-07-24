# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     serializers
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

from rest_framework import serializers
from oauth.models import Ouser
# from blog.models import Post, Tag, Category, Timeline
from blog.models import Post, Tag, Category


# from tool.models import ToolLink, ToolCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ouser
        fields = ('id', 'username', 'first_name', 'link', 'avatar')
        # fields = '__all__'
        # exclude = ('password','email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(
        many=True,
        read_only=True,
    )

    # 我的model暂时没有设定keywords，设想中可以讲keywords等同于tags
    # keywords = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )

    class Meta:
        model = Post
        # fields = ('id', 'author', 'title', 'views', 'category', 'tags')
        # fields = '__all__'
        exclude = ('body',)

# class TimelineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Timeline
#         fields = '__all__'


# class ToolCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToolCategory
#         fields = '__all__'


# class ToolLinkSerializer(serializers.ModelSerializer):
#     category = ToolCategorySerializer()
#
#     class Meta:
#         model = ToolLink
#         fields = '__all__'
