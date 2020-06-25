import json

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.forms import model_to_dict
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


# class RoleMenuListViewSet(viewsets.ModelViewSet):
#     '''
#     list:
#         部门列表数据
#
#     '''
#     # 这里要获取到角色,到手如何获取角色
#
#     serializer_class = RoleMenuSerializer
#
#     filter_backends = [SearchFilter,]
#     search_fields = ('role__name','role__id',)
#
#     # 实现多条件查询
#     # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
#     def get_queryset(self):
#
#         queryset = RoleMenu.objects.all()
#         role_name = self.request.query_params.get('role_name', None)
#         role_id = self.request.query_params.get('role_id', None)
#         menu_name = self.request.query_params.get('menu_name', None)
#         if role_name is not None:
#             queryset = queryset.filter(role__name=role_name)
#         if menu_name is not None:
#             queryset = queryset.filter(menu__name=menu_name)
#         if role_id is not None and role_id.isdigit():
#             queryset = queryset.filter(role__id=role_id)
#
#         return queryset
#
#
#     def get_serializer_class(self):
#         if self.action == "list":
#             return RoleMenuListSerializer
#         else:
#             return RoleMenuSerializer


    #
    # def update(self):
    #     pass


# class UserRoleListViewSet(viewsets.ModelViewSet):
#     '''
#     list:
#         部门列表数据
#
#     '''
#     # 这里要获取到角色,到手如何获取角色
#
#     serializer_class = UserRoleSerializer
#
#     filter_backends = [SearchFilter,]
#     search_fields = ('user__name','user__id',)
#
#     # 实现多条件查询
#     # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
#     def get_queryset(self):
#
#         queryset = UserRole.objects.all()
#         # role_name = self.request.query_params.get('role_name', None)
#         # role_id = self.request.query_params.get('role_id', None)
#         # menu_name = self.request.query_params.get('menu_name', None)
#         # if role_name is not None:
#         #     queryset = queryset.filter(role__name=role_name)
#         # if menu_name is not None:
#         #     queryset = queryset.filter(menu__name=menu_name)
#         # if role_id is not None and role_id.isdigit():
#         #     queryset = queryset.filter(role__id=role_id)
#
#         return queryset
#
#
#     def get_serializer_class(self):
#         if self.action == "list":
#             return UserRoleListSerializer
#         else:
#             return UserRoleSerializer
#

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






def build_tree(data, p_id, level=0):
    """
    生成树菜单
    :param data:    数据
    :param p_id:    上级分类
    :param level:   当前级别
    :return:
    """
    tree = []
    for row in data:
        if row['parent'] == p_id:
            row['level'] = level
            child = build_tree(data, row['id'], level+1)
            row['child'] = []
            if child:
                row['child'] += child
            tree.append(row)

    return tree


class UserPermissionListViewSet(RetrieveModelMixin,viewsets.GenericViewSet):
    '''
        list:根据用户名来查询菜单
    '''

    # 获取列表数据
    serializer_class =  serializers.Serializer

    def retrieve(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        user = User.objects.filter(id=id)[0]

        menu_list = []
        for role in user.role_list.all():
            for menu in role.menu_list.all():

                menu_list += [model_to_dict(menu,fields=('id','name','menu_type','url','icon','is_top','code','parent'))]

        menu_list = sorted(menu_list,key=lambda k:k['id'])
        # 对数据进行排序
        res = build_tree(data=menu_list,p_id=None,level=0)
        return Response({'data':res}, status=status.HTTP_202_ACCEPTED)

#

# class RolePermissionListViewSet(ListModelMixin,viewsets.GenericViewSet):
#     '''
#         list:根据用户名来查询菜单
#     '''
#
#     # 获取列表数据
#     serializer_class =  MenuListSerializer
#
#     def get_queryset(self):
#
#         queryset = Role.objects.all()
#         role_name = self.request.query_params.get('role_name', None)
#         role_id = self.request.query_params.get('role_id', None)
#
#         if role_name is not None:
#             queryset = queryset.filter(role__name=role_name)
#         if role_id is not None and role_id.isdigit():
#             queryset = queryset.filter(role__id=role_id)
#
#         role_menu_list = RoleMenu.objects.filter(role__id=queryset[0].id)
#
#         menu_list = []
#         for x in role_menu_list:
#             y = Menu.objects.get(id = x.menu.id)
#             if y.is_top:
#                 menu_list.append(y)
#
#         return  menu_list
#

class ChangePasswordtViewSet(UpdateModelMixin,viewsets.GenericViewSet):
    '''
    update:修改用户密码
    '''

    # update 不需要query_set  只有list才有query_set
    serializer_class = ChangePasswordSerializer


    def update(self, request, *args, **kwargs):

        user_id = kwargs['pk']

        new_password = request.data.get('new_password',None)
        old_password = request.data.get('old_password', None)

        user = User.objects.get(id = user_id)

        if not user:
            return Response({'msg':'用户不存在'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(old_password):
            return Response({'msg': '密码错误'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save()

        return Response({'msg': '修改密码成功'}, status=status.HTTP_202_ACCEPTED)




# class TestViewSet(viewsets.ModelViewSet):
#
#     def get_serializer_class(self):
#         if self.action == "list":
#             return RoleMenuListSerializer
#         elif self.action == 'update':
#             return RoleBulkUpdateSerializer
#         else:
#             return RoleMenuSerializer
#
#     def get_queryset(self):
#         queryset = RoleMenu.objects.all()
#         return queryset


class AlbumtViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerilizers