from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-


from oauth.models import Ouser
# from blog.models import Article, Tag, Category, Timeline
from blog.models import Post, Tag, Category
# from tool.models import ToolLink
from .serializers import (UserSerializer, PostSerializer,
                          TagSerializer, CategorySerializer)
from rest_framework import viewsets, permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


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
