import time
from random import Random

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from system.models import *

class StructureSerializer3(serializers.ModelSerializer):

    class Meta:
        model = Structure
        fields = '__all__'


class StructureSerializer2(serializers.ModelSerializer):

    sub_structure = StructureSerializer3(many=True,required=False)
    class Meta:
        model = Structure
        fields = '__all__'

class StructureSerializer(serializers.ModelSerializer):

    sub_structure = StructureSerializer2(many=True,required=False)
    class Meta:
        model = Structure
        fields = '__all__'


class StructureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'

class MenuList3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuList2Serializer(serializers.ModelSerializer):
    sub_menu = MenuList3Serializer(many=True)
    class Meta:
        model = Menu
        fields = '__all__'

class MenuListSerializer(serializers.ModelSerializer):
    sub_menu = MenuList2Serializer(many=True)
    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

class ButtonSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = '__all__'

class ButtonPageSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = ['id','code','name','desc','state','page']

class PageSerilizer(serializers.ModelSerializer):

    # permissions = serializers.SlugRelatedField(
    #     source='page_button',
    #     many=True,
    #     read_only=True,
    #     slug_field='url'
    # )

    permissions = ButtonPageSerilizer(many=True,source='page_button',read_only=True)
    # permissions = ButtonSerilizer(many=True,source='page_button',read_only=True)
    class Meta:
        model = Page
        fields = '__all__'







# class Button2Serilizer(serializers.ModelSerializer):
#
#     def to_representation(self, instance):
#         return instance.url
#     class Meta:
#         model = Button
#         fields = ('url',)


# class Page2Serilizer(serializers.ModelSerializer):
#
#     # user = serializers.HiddenField(
#     #     default=serializers.CurrentUserDefault()
#     # )
#
#     actionsOptions = serializers.SerializerMethodField()
#     selected = serializers.SerializerMethodField()
#     checkAll = serializers.SerializerMethodField()
#
#     def get_actionsOptions(self,obj):
#         # print('-----------1-----------')
#         buttons = Button.objects.filter(page=obj.id)
#         return Button2Serilizer(buttons,many=True, read_only=True,).data
#
#     def get_selected(self,obj):
#         # print('***********1-----------')
#         role = self.context['role']
#         buttons = selected_button = Button.objects.filter(page=obj.id).filter(button_role=role.id)
#         return Button2Serilizer(buttons,many=True,context={'request': self.context['request']},read_only=True).data
#
#     def get_checkAll(self,obj):
#         # print('~~~~~~~~~~~1-----------')
#         role = self.context['role']
#         all_buttons_cnt = Button.objects.values('id').filter(page=obj.id).count()
#         selected_buttons_cnt = selected_button = Button.objects.values('id').filter(
#             page=obj.id).filter(button_role=role.id).count()
#         res = True if all_buttons_cnt == selected_buttons_cnt else False
#         return res
#
#     class Meta:
#         model = Page
#         fields = ('id','name','desc','state','url','checkAll','selected','actionsOptions')

# class Button3Serializer(serializers.ModelSerializer):
#     def to_representation(self, instance):
#         return  instance.url
#     class Meta:
#         model = Button
#         exclude = ('id','name','desc','state','page','create_time','update_time')
#
#
class Page3Serializer(serializers.ModelSerializer):

    # actionsOptions = serializers.PrimaryKeyRelatedField(many=True,read_only=True,source='page_button')
    # actionsOptions = Button3Serializer(read_only=True,many=True,source='page_button')
    # actionsOptions = serializers.SlugRelatedField(many=True,source='page_button',read_only=True,slug_field='url')
    class Meta:
        model = Page
        fields = ('id','name','desc','code','order','state',)#'actionsOptions')


class RoleListSerializer(serializers.ModelSerializer):

    # pages = Page3Serializer(many=True,read_only=True,source='page_list')

    pages = serializers.SerializerMethodField()

    def get_pages(self,obj):

        # print('=================')
        # 这个是通过manytomany 进行查询
        # pages = Role.get_page_list_by_id(obj.id)
        # 这个是通过中间关联 的主键查询的
        pages = Page.objects.values('id','name','desc','code','order','state').filter(page_role=obj.id).order_by('order')

        return Page3Serializer(pages,many=True, read_only=True).data

    # pages = serializers.SerializerMethodField()
    # def get_pages(self,obj):
        # print('=====================================')
        # print(obj['page_list'])
        # page_list = obj.page_list.all()
        # page_list = Page.objects.filter(page_role=obj)
        # return Page2Serilizer(page_list,many=True,context={
        #     'request': self.context['request'],
        #     'role':obj
        #                                                   }).data

    class Meta:
        model = Role
        fields = ('id','name','code','desc','state','pages',)



class PatentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patent
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    # pages = serializers.SlugRelatedField(read_only=True,many=True,source='page_list',slug_field='url')
    # buttons = serializers.SlugRelatedField(read_only=True, many=True,source='button_list', slug_field='url')



    # def update(self, instance, validated_data):
    #
    #     instance = super().update(instance,validated_data)
    #
    #     return instance



    class Meta:
        model = Role
        fields = '__all__'
        # exclude = ('page_list','button_list')

class UserProfileListSerializer(serializers.ModelSerializer):


    # role_list = serializers.StringRelatedField(many=True)
    # role_list = serializers.HyperlinkedRelatedField( many=True,read_only=True, view_name='role-detail')
    roles  = serializers.SlugRelatedField(many=True,slug_field='code',read_only=True,)
    class Meta:
        model = UserProfile
        exclude = ('groups','user_permissions','password','last_login')






class UserProfileSerializer(serializers.ModelSerializer):

    roles = serializers.SlugRelatedField(many=True, slug_field='code', queryset=Role.objects.all())

    class Meta:
        model = UserProfile
        exclude = ('groups', 'user_permissions','last_login',)

    # 注意要使用active时候才可以登录
    def create(self, validated_data):
        user = super(UserProfileSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = '__all__'


class UserMessageSerializer(serializers.ModelSerializer):



    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = UserMessage
        fields = '__all__'


# class UserRoleListSerializer(serializers.ModelSerializer):
#
#     '''
#     角色菜单列表展示
#     '''
#     user = UserProfileSerializer()
#     role = RoleSerializer()
#
#
#     # def get_role(self,obj):
#     #
#     #     response = dict()
#     #     response['type'] = obj.role
#     #     response['name'] = obj.get_role_display()
#     #
#     #     return response
#
#
#     # 序列化的作用是将ID 转化成对象
#     # 注意,这里不可以设置成many=True
#
#     class Meta:
#         model = UserRole
#         fields = '__all__'

# class UserRoleSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         # validate实现唯一联合，一个菜单只能被角色设置一次
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=UserRole.objects.all(),
#                 fields=('role', 'user'),
#                 # message的信息可以自定义
#                 message="已经设置"
#             )
#         ]
#         model = UserRole
#         fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)




class AlbumSerializers(serializers.ModelSerializer):

    '''
    track_list 只是一个外键链接,并不是自己model所拥有的字段
    '''
    # track_list = serializers.StringRelatedField(many=True)
    # 一定要设置成query_set=Menu.objects.all()
    #或者设置成read_only = True
    # 默认是主键
    track_list = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # 设置超链接
    # track_list = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='track-detail')
    image = serializers.ImageField(source='album_image.image',read_only=True)


    class Meta:
        model = Album
        fields = ['album_name','artist','track_list','image']


class TrackSerilizers(serializers.ModelSerializer):

    # update_user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault().user.id)
    # create_user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault().user.id)

    # def validate_create_user(self,data):
    #
    #
    #
    #     return data



    class Meta:
        model = Track
        fields = '__all__'



class AlbumImageSerilizers(serializers.ModelSerializer):

    # 设置默认用户,不用用户填,也不用显示
    # 这样设置会默认不显示
    # update_user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    # 这个不能再这里进行序列化,否则会出问题
    # 或者设置成readOnly 这个可以看做是补充
    # album = AlbumSerializers(read_only=True)

    class Meta:
        model = AlbumImage
        fields = '__all__'





class CategorySerializer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    # update_user = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault(),
    # )
    #
    # create_user = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault(),
    # )

    class Meta:
        model = Category
        fields = '__all__'


class CategoryList2Serializer(serializers.ModelSerializer):
    sub_category = CategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    '''
    是以总的反向的来看的,这里没有显式的写sub_category
    '''
    sub_category = CategoryList2Serializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class GooodSerializer(serializers.ModelSerializer):

    id = serializers.HyperlinkedRelatedField(read_only=True,view_name='good-detail')

    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Good
        fields = '__all__'

class UserFavorateSerializer(serializers.ModelSerializer):


    id = serializers.HyperlinkedRelatedField(read_only=True,view_name='user-fav-detail')
    # good = GooodSerializer(read_only=True)
    user = serializers.HiddenField(

        default=serializers.CurrentUserDefault(),
    )

    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)



    class Meta:
        validators= [
            UniqueTogetherValidator(
                queryset=UserFavorate.objects.all(),
                fields = ('user','good'),
                message='已经收藏,清重新选择'
            )

        ]
        model = UserFavorate
        fields = '__all__'


class BannerSerilizer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Banner
        fields = '__all__'

class CartListSerializer(serializers.ModelSerializer):

    good = GooodSerializer(read_only=True)
    id = serializers.HyperlinkedRelatedField(read_only=True,view_name='cart-detail')
    class Meta:
        model = Cart
        fields = ('good','num','id')

class CartSerializer(serializers.Serializer):

    create_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)
    # 使用当前用户,并且隐藏这个字段
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    num = serializers.IntegerField(required=True,
                                   label='数量',
                                   min_value=1,
                                   error_messages={
                                     'min_value' :'商品的数量不能小于1','required':'请输入商品数量'
                                   },
                                   )
    good = serializers.PrimaryKeyRelatedField(queryset=Good.objects.all(),required=True)

    #有就利用原来的,没有就创建一个新的,整理不需要去验证唯一性
    def create(self, validated_data):

        user = self.context['request'].user
        num = validated_data['num']
        good = validated_data['good']

        existed = Cart.objects.filter(user=user,good=good)

        if existed:
            existed = existed[0]
            existed.num += num
            existed.save()
        else:
            existed = Cart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        instance.num = validated_data['num']
        instance.save()
        return instance


class OrderSerilizer(serializers.ModelSerializer):

    id = serializers.HyperlinkedRelatedField(read_only=True,view_name='order-detail')
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    nonce_str = serializers.CharField(read_only=True)
    pay_type = serializers.IntegerField(read_only=True)

    def generate_order_sn(self):

        order_sn = '{time_str}{user_id}{random_str}'.format(
            time_str = time.strftime('%Y%m%d%H%M%S'),
            user_id = self.context['request'].user.id,
            random_str = Random().randint(10,99)
        )
        return order_sn
    # 自定义订单号
    def validate(self, attrs):
        attrs['order_sn'] = self.generate_order_sn()
        return attrs

    class Meta:

        model = Order
        fields = '__all__'


class OrderGoodSerilizer(serializers.ModelSerializer):

    good = GooodSerializer()
    class Meta:
        model = OrderGood
        fields = '__all__'

class OrderGoodListSerilizer(serializers.ModelSerializer):
    # 查询出多个商品
    good_list = OrderGoodSerilizer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
