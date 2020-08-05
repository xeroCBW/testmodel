import json

import django_filters
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser

from rest_framework.viewsets import *
from rest_framework.mixins import *
from rest_pandas import PandasView, PandasViewSet, PandasSerializer
import pandas as pd
from system.filters import GoodFilter, ButtonFilter, RoleFilter, UserFilter, PageFilter,PatentFilter
from system.models import *
from system.serializer import *
from .utils.RestModelViewSet import *
from .paginations import GlobalPagination, NormalPagination
from .utils.custom_pandas_excel_render import CustomPandasExcelRender

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

    queryset = Menu.objects.values().all()
    serializer_class = StructureCreateSerializer


    def get_serializer_class(self):
        if self.action == "list":
            return MenuListSerializer
        else:
            return MenuSerializer



class RoleListViewSet(CustomBaseModelViewSet):
    '''
    list:
        角色列表数据
    '''

    queryset = Role.objects.all()
    serializer_class = RoleListSerializer
    pagination_class = GlobalPagination

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = RoleFilter
    search_fields = ('name',)
    ordering_fields = ('id', )


    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RoleListSerializer
        else:
            return RoleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            res = self.get_paginated_response(serializer.data)

            roles = [x['id'] for x in res.data['data']['items']]
            buttons_list = Button.objects.values('id', 'url', 'page', 'button_role').distinct()
            # 不知道为什么不会去重---加上filter(又会加上一个连接)
            buttons_list = [x for x in buttons_list if x['button_role'] in roles]

            pages_list = Page.objects.values('id','page_role').distinct()
            # 不知道为什么不会去重
            pages_list = [x for x in pages_list if x['page_role'] in roles]

            # 生成所有菜单的按钮
            page_id_list = {x['id'] for x in pages_list}
            page_id_list = list(page_id_list)
            actionsOptions = Button.objects.values('id','url','page').filter(page__in=page_id_list)
            actionsOptions_mp = {x:list() for x in page_id_list}
            for x in actionsOptions:
                actionsOptions_mp[x['page']] += [x['url']]

            roles_mp = dict()
            for role_id in roles:
                roles_mp[role_id] = dict()
                for x in pages_list:
                    if role_id == x['page_role']:
                        roles_mp[role_id][x['id']] = list()
            # 生成 角色 页面 按钮 数组
            for button in buttons_list:
                roles_mp[button['button_role']][button['page']] += [button['url']]


            for x in res.data['data']['items']:
                for y in x['pages']:
                    y['actionsOptions'] = actionsOptions_mp[y['id']]
                    y['checkAll'] = True if len(y['actionsOptions']) == len(roles_mp[x['id']][y['id']]) else False
                    y['selected'] = roles_mp[x['id']][y['id']]

            # print(json.dumps(res.data,indent=4,ensure_ascii=False))

            return res

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UserListViewSet(CustomBaseModelViewSet):
    '''
        list:
            用户列表数据

    '''

    serializer_class = UserProfileSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ('user__name', 'user__id',)
    pagination_class = GlobalPagination

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = UserFilter
    search_fields = ('name',)

    ordering_fields = ('id', )

    # 实现多条件查询
    # http://localhost:8000/system/role-menu/?role_id=2&menu_name=%E7%B3%BB%E7%BB%9F
    def get_queryset(self):

        queryset = UserProfile.objects.all()

        role_name = self.request.query_params.get('username', None)
        role_id = self.request.query_params.get('id', None)
        # menu_name = self.request.query_params.get('menu_name', None)
        if role_name is not None:
            queryset = queryset.filter(username__contains=role_name)
        # if menu_name is not None:
        #     queryset = queryset.filter(menu__name=menu_name)
        if role_id is not None and role_id.isdigit():
            queryset = queryset.filter(id__contains=role_id)

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


        roles_list = user.roles.all()
        roles = [x.code for x in roles_list]

        page_list = list()
        button_list = list()

        page_list = Page.objects.values('id','name','desc','state','url','order').filter(page_role__in=[x.id for x in roles_list]).distinct().order_by('order')
        # 将queryset 转成list
        page_list = list(page_list)
        select_button_list = Button.objects.values('id','name','desc','state','url','page').filter(button_role__in=[x.id for x in roles_list]).distinct()
        all_button_list = Button.objects.values('id','name','desc','state','url','page').filter(page__in=[x['id'] for x in page_list]).distinct()

        select_button_mp = dict()
        for x in select_button_list:
            if x['page'] in select_button_mp.keys():
                select_button_mp[x['page']] += [x['url']]
            else:
                select_button_mp[x['page']] = [x['url']]

        all_button_mp = dict()
        for x in all_button_list:
            if x['page'] in all_button_mp.keys():
                all_button_mp[x['page']] += [x['url']]
            else:
                all_button_mp[x['page']] = [x['url']]


        for x in page_list:
            x['code'] = x['url']
            del x['url']
            x['selected'] = select_button_mp[x['id']]
            x['actionsOptions'] = all_button_mp[x['id']]
            x['checkAll'] = True if len(x['selected']) == len(x['actionsOptions']) else False

        permissions = page_list

        res = {
            'permissions':permissions,
            'roles':roles,
            "avatar": user.avatar.url,
            "name": user.name,
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "state": user.is_active
        }

        return JsonResponse(data=res, msg="success", code=200,status=status.HTTP_200_OK,)


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
            return JsonResponse(data={}, msg="用户不存在", code=400, status=status.HTTP_400_BAD_REQUEST, )

        if not user.check_password(old_password):
            return JsonResponse(data={}, msg="密码错误", code=400, status=status.HTTP_400_BAD_REQUEST, )

        user.password = make_password(new_password)
        user.save()
        return JsonResponse(data={}, msg="修改密码成功", code=200, status=status.HTTP_200_OK,)

class LogoutViewSet(CustomBaseCreateModelMixin,GenericViewSet):

    serializer_class = serializers.Serializer

    def create(self, request, *args, **kwargs):
        user = request.user
        user.user_secret = uuid4()
        user.save()
        return JsonResponse(data={}, msg="登出成功", code=200, status=status.HTTP_200_OK, )




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
    pagination_class = GlobalPagination

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


class PageViewSet(CustomBaseModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerilizer
    pagination_class = GlobalPagination

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = PageFilter
    search_fields = ('name',)
    ordering_fields = ('id', )

class ButtonViewSet(CustomBaseModelViewSet):

    queryset = Button.objects.all()
    serializer_class = ButtonSerilizer
    pagination_class = GlobalPagination

    # 自定义将这个去掉了
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = ButtonFilter
    search_fields = ('name',)
    ordering_fields = ('id', )

    def get_renderers(self):
        if self.action == 'download':
            return [CustomPandasExcelRender,]
        else:
            return super().get_renderers()


       # @action(methods=['get'], detail=False)
    # def download(self,request):
    #
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return serializer.data
    # return JsonResponse(data={},msg='success',code=200,status=status.HTTP_200_OK)


# class ButtonRenderViewSets(viewsets.GenericViewSet,mixins.ListModelMixin):

class PatentDownloadViewSets(PandasViewSet):

    serializer_class = PatentSerializer
    queryset = Patent.objects.all()
    # 暂时不支持,分页功能的下载
    pagination_class = NormalPagination
    # 自定义将这个去掉了
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = PatentFilter
    search_fields = ('=id', 'name',)

    renderer_classes = [CustomPandasExcelRender,]

    list_serializer_class = PandasSerializer


class PatentUploadViewSets(viewsets.ModelViewSet):

    serializer_class = serializers.Serializer
    queryset = Button.objects.all()

    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES["file"]

        excel_raw_data_dict = pd.read_excel(file_obj, sheet_name=['Sheet1',])
        excel_raw_data_1 = excel_raw_data_dict['Sheet1']
        excel_raw_data_1 = excel_raw_data_1.fillna('-----')

        res = list()
        for i in range(excel_raw_data_1.shape[0]):
            t = dict()
            for k, v in excel_raw_data_1.to_dict().items():
                t[k] = v[i]
            res += [t]

        mp = {
            '文献号':'document_no',
            '申请号':'apply_no',
            '申请日':'apply_time',
            '公开号':'public_no',
            '公开(公告)日':'public_time',
            '名称':'name',
            '申请人':'apply_user',
            '地址':'address',
            '发明人':'inventor',
            '优先权':'priority',
            '分类号':'category_no',
            '主分类号':'main_category_no',
            '国省代码':'nation_province',

            '国际公布':'internation_publish',
            '国际公开日':'internation_publish_time',
            '同族数':'phrator_date',
            '被引证数':'quote_number',
            '引证专利':'quote_patent',
            '摘要':'abstract',
            '摘要附图':'abstract_pic',
        }

        ans = []
        for x in res:
            t = {}
            for k,v in x.items():
                t[mp[k]] = v
            ans.append(t)

        print(ans)

        try:
            ans =  PatentSerializer(data=ans,many=True)
            ans.is_valid(raise_exception=True)
            ans.save()
        except Exception as e:
            print(e)


        return JsonResponse(data=res,msg='success',code=201,status=status.HTTP_201_CREATED)


class PatentViewSets(CustomBaseModelViewSet):

    serializer_class = PatentSerializer
    queryset = Patent.objects.all()
    pagination_class = GlobalPagination

    # 自定义将这个去掉了
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = PatentFilter
    search_fields = ('name',)
    ordering_fields = ('id', )



    def get_queryset(self):

        queryset = Patent.objects.all()

        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)


        if name is not None:
            queryset = queryset.filter(name__contains=name)
        if id is not None and id.isdigit():
            queryset = queryset.filter(id__contains=id)

        return queryset
