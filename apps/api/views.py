from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-


from oauth.models import Ouser
# from blog.models import Article, Tag, Category, Timeline
from blog.models import Post, Tag, Category
# from tool.models import ToolLink
from .serializers import (UserSerializer, PostSerializer,
                          TagSerializer, CategorySerializer)
# from rest_framework import viewsets, permissions
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


# from rest_framework.permissions import IsAdminUser
# from .permissions import IsAdminUserOrReadOnly

# RESEful API VIEWS
class UserListSet(viewsets.ModelViewSet):
    queryset = Ouser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class PostListSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagListSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class CategoryListSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


# class TimelineListSet(viewsets.ModelViewSet):
#     queryset = Timeline.objects.all()
#     serializer_class = TimelineSerializer
#     permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
#
#
# class ToolLinkListSet(viewsets.ModelViewSet):
#     queryset = ToolLink.objects.all()
#     serializer_class = ToolLinkSerializer
#     permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


# 测试APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class DrfCategoryView(APIView):
    # 展示所有文章api
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            obj = Category.objects.all().values()
            data = list(obj)
            return Response(data)  # from rest_framework.response import Response
        else:
            obj = Category.objects.filter(pk=pk).first()
            data = model_to_dict(obj)  # 将对象转化为dict
            return Response(data)

    # 接口：实现创建文章类型

    def post(self, request, *args, **kwargs):
        # name = request.Post.get('name')
        # description = request.Post.get('description') 这种用法不正确

        # request.data 返回解析之后的请求体数据
        name = request.data['name']
        description = request.data['description']

        category_obj = Category(name=name, description=description)
        category_obj.save()
        return Response('添加文章类型成功')

    # 更新category api
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        # request.data 返回解析之后的请求体数据
        Category.objects.filter(id=pk).update(**request.data)
        return Response('更新成功')

    # 删除文章api
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response('删除失败，没有该条数据')
        Post.objects.filter(pk=pk).delete()
        return Response('删除成功')


# request.data 返回解析之后的请求体数据
# 包含了解析之后的文件和非文件数据
# 包含了对POST、PUT、PATCH请求方式解析后的数据
# 利用了REST framework的parsers解析器，不仅支持表单类型数据，也支持JSON数据
#
# request.query_params.get('xx')类似于django的GET方法


# 基于上一个代码添加校验功能，测试序列化

from rest_framework import serializers


class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ['id', 'name']


class NewCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = Category.objects.all()
            # 序列化
            ser = NewCategorySerializer(instance=queryset, many=True)
            return Response(ser.data)
        else:
            model_object = Category.objects.filter(id=pk).first()
            ser = NewCategorySerializer(instance=model_object, many=False)
            return Response(ser.data)

    def post(self, request, *args, **kwargs):
        ser = NewCategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        category_object = Category.objects.filter(id=pk).first()
        ser = NewCategorySerializer(instance=category_object, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        Category.objects.filter(id=pk).delete()
        return Response('删除成功')

    # 局部更新
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        article_obj = Post.objects.filter(pk=pk).first()
        ser = PostSerializer(instance=article_obj, data=request.data, partial=True)  # partial=True
        if ser.is_valid():
            ser.save()
            return Response('更新成功')
        return Response(ser.errors)


from rest_framework.pagination import PageNumberPagination


# 测试分页

# 重写原生方法
class MyPageNumberPagination(PageNumberPagination):
    # 默认一页显示3个
    page_size = 3
    # 获取URL参数中传入的页码key字段
    page_query_param = 'page'
    # 指定单页最大值的字段
    page_size_query_param = 'size'
    # 设置单次取的最大值
    max_page_size = None


class DrfPostView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        # 方式二：数据 + 分页信息
        pg = MyPageNumberPagination()
        result = pg.paginate_queryset(queryset, request, self)
        # 序列化
        ser = PostSerializer(instance=result, many=True)
        # return Response(ser.data)
        # 使用drf分页方法，可以显示上一页和下一页链接
        return pg.get_paginated_response(ser.data)
