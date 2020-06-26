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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProfileListSerializer(serializers.ModelSerializer):


    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

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


