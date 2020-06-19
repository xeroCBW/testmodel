import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView

from system.models import *
from system.serializer import *

from rest_framework.filters import SearchFilter


class StructureListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Structure.objects.all()
    serializer_class = StructureCreateSerializer

    def get_queryset(self):
        if self.action == "list":
            return Structure.objects.filter(parent__isnull=True)
        else:
            return Structure.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StructureSerializer
        else:
            return StructureCreateSerializer


class MenuListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Menu.objects.all()
    serializer_class = StructureCreateSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        else:
            return MenuSerializer



    def get_queryset(self):
        if self.action == "list":
            return Menu.objects.filter(is_top=True)
        else:
            return Menu.objects.all()


class RoleListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleMenuListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据

    '''
    # 这里要获取到角色,到手如何获取角色

    serializer_class = RoleMenuSerializer

    filter_backends = [SearchFilter,]
    search_fields = ('role__name','role__id',)

    # 实现多条件查询
    # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
    def get_queryset(self):

        queryset = RoleMenu.objects.all()
        role_name = self.request.query_params.get('role_name', None)
        role_id = self.request.query_params.get('role_id', None)
        menu_name = self.request.query_params.get('menu_name', None)
        if role_name is not None:
            queryset = queryset.filter(role__name=role_name)
        if menu_name is not None:
            queryset = queryset.filter(menu__name=menu_name)
        if role_id is not None and role_id.isdigit():
            queryset = queryset.filter(role__id=role_id)

        return queryset


    def get_serializer_class(self):
        if self.action == "list":
            return RoleMenuListSerializer
        else:
            return RoleMenuSerializer












