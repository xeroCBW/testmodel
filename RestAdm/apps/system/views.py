import json

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, mixins
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import *
from rest_framework.views import APIView

from system.models import *
from system.serializer import *

from rest_framework.filters import SearchFilter
User = get_user_model()


# class CustomBackend(ModelBackend):
#     """
#     自定义用户验证
#     """
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             #用户名和手机都能登录
#             user = User.objects.get(
#                 Q(username=username) | Q(mobile=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None

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

            # print(Menu.objects.filter(is_top=True))
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


class UserRoleListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据

    '''
    # 这里要获取到角色,到手如何获取角色

    serializer_class = UserRoleSerializer

    filter_backends = [SearchFilter,]
    search_fields = ('user__name','user__id',)

    # 实现多条件查询
    # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
    def get_queryset(self):

        queryset = UserRole.objects.all()
        # role_name = self.request.query_params.get('role_name', None)
        # role_id = self.request.query_params.get('role_id', None)
        # menu_name = self.request.query_params.get('menu_name', None)
        # if role_name is not None:
        #     queryset = queryset.filter(role__name=role_name)
        # if menu_name is not None:
        #     queryset = queryset.filter(menu__name=menu_name)
        # if role_id is not None and role_id.isdigit():
        #     queryset = queryset.filter(role__id=role_id)

        return queryset


    def get_serializer_class(self):
        if self.action == "list":
            return UserRoleListSerializer
        else:
            return UserRoleSerializer


class UserListViewSet(viewsets.ModelViewSet):
    '''
        list:
            用户列表数据

    '''

    serializer_class = UserProfileSerializer

    filter_backends = [SearchFilter, ]
    search_fields = ('user__name', 'user__id',)

    # 实现多条件查询
    # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
    def get_queryset(self):

        queryset = UserProfile.objects.all()
        # role_name = self.request.query_params.get('role_name', None)
        # role_id = self.request.query_params.get('role_id', None)
        # menu_name = self.request.query_params.get('menu_name', None)
        # if role_name is not None:
        #     queryset = queryset.filter(role__name=role_name)
        # if menu_name is not None:
        #     queryset = queryset.filter(menu__name=menu_name)
        # if role_id is not None and role_id.isdigit():
        #     queryset = queryset.filter(role__id=role_id)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer
        else:
            return UserProfileSerializer





class UserPermissionListViewSet(ListModelMixin,viewsets.GenericViewSet):
    '''
        list:根据用户名来查询菜单
    '''

    # 获取列表数据
    serializer_class =  MenuListSerializer

    def get_queryset(self):

        if self.request.user:

            user = UserProfile.objects.filter(id=self.request.user.id)[0]

            print('----start----')
            print(user.id)
            print('----end----')


            user_role = UserRole.objects.filter(user = user.id)[0]

            role_menu_list = RoleMenu.objects.filter(role__id = user_role.role.id)

            menu_list = []
            for x in role_menu_list:
                y = Menu.objects.get(id = x.menu.id)
                if y.is_top:
                    menu_list.append(y)

            return  menu_list


        else:
            pass


class RolePermissionListViewSet(ListModelMixin,viewsets.GenericViewSet):
    '''
        list:根据用户名来查询菜单
    '''

    # 获取列表数据
    serializer_class =  MenuListSerializer

    def get_queryset(self):

        queryset = Role.objects.all()
        role_name = self.request.query_params.get('role_name', None)
        role_id = self.request.query_params.get('role_id', None)

        if role_name is not None:
            queryset = queryset.filter(role__name=role_name)
        if role_id is not None and role_id.isdigit():
            queryset = queryset.filter(role__id=role_id)

        role_menu_list = RoleMenu.objects.filter(role__id=queryset[0].id)

        menu_list = []
        for x in role_menu_list:
            y = Menu.objects.get(id = x.menu.id)
            if y.is_top:
                menu_list.append(y)

        return  menu_list



