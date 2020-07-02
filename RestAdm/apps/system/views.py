import json

import django_filters
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework.viewsets import *
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import *
from rest_framework.views import APIView

from system.filters import GoodFilter
from system.models import *
from system.serializer import *
from .utils.RestModelViewSet import *

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

class StructureListViewSet(CustomBaseModelViewSet):
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


class MenuListViewSet(CustomBaseModelViewSet):
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


class RoleListViewSet(CustomBaseModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# class RoleMenuListViewSet(CustomBaseModelViewSet):
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


# class UserRoleListViewSet(CustomBaseModelViewSet):
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

class UserListViewSet(CustomBaseModelViewSet):
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


class UserPermissionListViewSet(CustomBaseRetrieveModelMixin,viewsets.GenericViewSet):
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
        return JsonResponse(data=res, msg="success", code=200,status=status.HTTP_200_OK,)
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

class ChangePasswordtViewSet(CustomBaseUpdateModelMixin,viewsets.GenericViewSet):
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



class UserAddressViewSet(CustomBaseModelViewSet):

    '''
    收货地址管理
    list:收货地址列表
    create:创建收货地址
    update:更新收货地址
    delete:删除收货地址

    '''
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
class UserMessageViewSet(CustomBaseModelViewSet):

    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer


class CategoryViewSet(CustomBaseModelViewSet):



    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(is_top=True)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategorySerializer

class GoodViewSet(CustomBaseModelViewSet):

    '''
    list:获取所有商品的详情
    retrieve:是获取点击商品的次数,可以看做是page View
    '''

    queryset = Good.objects.all()
    serializer_class = GooodSerializer

    # 设置过滤/多个字段查找
    #做个是显示过滤的控件
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = GoodFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

class UserFavorateViewSet(CustomBaseModelViewSet):
    # 搜索的时候用的good的id,注意不能使用双下划线
    # 默认是pk
    lookup_field = 'pk'
    # lookup_field = 'good_id'
    serializer_class = UserFavorateSerializer
    queryset = UserFavorate.objects.all()


    # def get_queryset(self):
    #     # if self.request.user
    #
    #     return UserFavorate.objects.filter(user=self.request.user)


    # 将喜欢数+1
    # 或者使用信号量
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     good = instance.good
    #     good.favorate_num += 1
    #     good.save()

class BannerViewSet(CustomBaseModelViewSet):

    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerilizer

class CartViewSet(CustomBaseModelViewSet):
    '''
    购物车
    list:获取购物车列表
    update:更新某样商品
    retrieve:获取某项商品详情
    '''
    def get_serializer_class(self):
        if self.action == 'list':
            return CartListSerializer
        else:
            return CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

# 订单不能删除,智能取消
class OrderViewSet(CustomBaseListModelMixin,CustomBaseCreateModelMixin,CustomBaseRetrieveModelMixin,CustomBaseDestroyModelMixin,GenericViewSet):
    '''
    list:获取当前用户订单
    retrieve:获取订单详情
    create:创建订单
    destroy:取消订单
    '''
    def get_serializer_class(self):
        if self.action == 'list':
            return OrderSerilizer
        if self.action == 'retrieve':
            return OrderGoodListSerilizer
        return OrderSerilizer
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        # 设置订单保存
        order = serializer.save()

        cart = Cart.objects.filter(user=self.request.user)
        for x in cart:
            order_good = OrderGood()
            order_good.good = x.good
            order_good.num = x.num
            order_good.order = order
            order_good.save()
            # 删除数据---这是一个对象,并不是删除list中的元素,而是删除orm元素
            x.delete()
        return order

class OrderGoodViewSet(CustomBaseModelViewSet):

    queryset = OrderGood.objects.all()
    serializer_class = OrderGoodSerilizer

# class TestViewSet(CustomBaseModelViewSet):
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


class AlbumtViewSet(CustomBaseModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class TrackViewSet(CustomBaseModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerilizers

class AlbumImageViewSet(CustomBaseModelViewSet):

    queryset = AlbumImage.objects.all()
    serializer_class = AlbumImageSerilizers