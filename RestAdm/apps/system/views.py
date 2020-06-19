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
    # role = Role(id=2)
    # 这里要获取到角色,到手如何获取角色
    queryset = RoleMenu.objects.all()
    serializer_class = RoleMenuSerializer

    filter_backends = [SearchFilter]
    search_fields = ('role__name',)


    def get_serializer_class(self):
        if self.action == "list":
            return RoleMenuListSerializer
        else:
            return RoleMenuSerializer



class RoleMenuQueryView(ListAPIView):

    '''
    通过角色 来查询所有菜单
    '''
    serializer_class = RoleMenuQuerySerializer
    def get_queryset(self):

        queryset = RoleMenu.objects.all()
        role = self.request.query_params.get('role', None)
        menu = self.request.query_params.get('menu', None)

        aQ = Q()
        if role is not None:
            aQ.add(Q(role=role), Q.AND)
        if menu is not None:
            aQ.add(Q(menu=menu), Q.AND)
        queryset = queryset.filter(aQ).order_by("-id")

        return queryset









