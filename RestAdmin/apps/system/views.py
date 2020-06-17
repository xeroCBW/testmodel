from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from system.filter import UserFilter
from .models import Menu, Structure
from .serializer import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class UserListViewSet(ModelViewSet):
    '''
    list:
        用户列表数据
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    # 过滤
    filter_class = UserFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('=name', 'gender')
    # 排序
    ordering_fields = ('id', 'name')




class MenuListViewSet(ModelViewSet):
    '''
    list:
        菜单列表数据
    '''

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class StructureListViewSet(ModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class RoleListViewSet(ModelViewSet):
    '''
    list:
        角色列表数据
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer