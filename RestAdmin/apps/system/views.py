import json
import re

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework import mixins, viewsets, filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from system import permissions
from system.filter import UserFilter
from .models import Menu, Structure
from .serializer import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserListViewSet(viewsets.ModelViewSet):
    '''
    list:
        用户列表数据
    '''

    # permission_classes = (permissions.IsOwnerOrReadOnly,)

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



class MenuListViewSet(viewsets.ModelViewSet):
    '''
    list:
        菜单列表数据
    '''

    # permission_classes = [permissions.UserTypePermission]

    queryset = Menu.objects.filter(is_top=True)
    # 这里是菜单的修改,所以是展示所有的菜单----也可以树状展示
    # queryset = Menu.objects.all()
    serializer_class = CategorySerializer


    # def get_queryset(self):
    #     # 只能查看当前登录用户的收藏，不会获取所有用户的收藏
    #     return Menu.objects.filter(user=self.request.user)



class StructureListViewSet(viewsets.ModelViewSet):
    '''
    list:
        部门列表数据
    '''

    queryset = Structure.objects.filter(parent__isnull=True)
    serializer_class = StructureSerializer

class RoleListViewSet(viewsets.ModelViewSet):
    '''
    list:
        角色列表数据
    '''
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class GlobalListView(generics.GenericAPIView):
    '''
    list:
        全局菜单列表数据
    '''

    def get(self, request):
        print('-----')
        print(request.user.is_authenticated)
        top_menu, reveal_menu, permission_url_list = self.get_menu(request)
        a = {

            'top_menu': top_menu,
            'reveal_menu': reveal_menu,
            'permission_url_list': permission_url_list,
        }
        return HttpResponse(json.dumps(a), content_type='application/json')


    def get_menu(self, request):
        """
        获取用户权限菜单：这个地方真的好乱，没有更好的实现方法只能先忍受下吧
        :param request:
        :return:
        """

        if request.user.is_authenticated:

            user = request.user
            permissions_item_list = user.roles.values('permissions__id',
                                                      'permissions__title',
                                                      'permissions__url',
                                                      'permissions__icon',
                                                      'permissions__code',
                                                      'permissions__parent').distinct()

            permission_url_list = []
            permission_menu_list = []

            for item in permissions_item_list:
                # print('-----',item['permissions__url'])
                permission_url_list.append(item['permissions__url'])
                if item['permissions__id']:
                    menu = {
                        'id': item['permissions__id'],
                        'title': item['permissions__title'],
                        'url': item['permissions__url'],
                        'icon': item['permissions__icon'],
                        'code': item['permissions__code'],
                        'parent': item['permissions__parent'],
                        'status': False,
                        'sub_menu': [],

                    }
                    permission_menu_list.append(menu)

            request_url = request.path_info
            top_menu = []
            permission_menu_dict = {}
            for menu in permission_menu_list:

                url = menu['url']
                if url and re.match(url, request_url):
                    menu['status'] = True
                if menu['parent'] is None:
                    top_menu.insert(0, menu)
                permission_menu_dict[menu['id']] = menu

            menu_data = []
            for i in permission_menu_dict:
                if permission_menu_dict[i]['parent']:
                    pid = permission_menu_dict[i]['parent']
                    parent_menu = permission_menu_dict[pid]
                    parent_menu['sub_menu'].append(permission_menu_dict[i])
                else:
                    menu_data.append(permission_menu_dict[i])

            if [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url]:
                reveal_menu = [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url][0]
            else:
                reveal_menu = None

            return top_menu, reveal_menu, permission_url_list
        else:
            pass


class PermissionViewSet(ReadOnlyModelViewSet):
    '''
    list:
        角色列表数据
    '''


    queryset = Role.objects.all()
    serializer_class = RoleSerializer



