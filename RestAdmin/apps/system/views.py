from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Menu, Structure
from .serializer import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        用户列表数据
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer



class MenuListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        菜单列表数据
    '''

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class StructureListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class RoleListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        角色列表数据
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer