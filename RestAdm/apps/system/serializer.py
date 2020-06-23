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

class RoleMenuListSerializer(serializers.ModelSerializer):

    '''
    角色菜单列表展示
    '''
    role = RoleSerializer()

    # 序列化的作用是将ID 转化成对象
    # 注意,这里不可以设置成many=True
    menu = MenuSerializer()
    class Meta:
        model = RoleMenu
        fields = '__all__'


class RoleMenuTreeSerializer(serializers.ModelSerializer):

    # role = RoleSerializer()
    # menu = serializers.SerializerMethodField()
    #
    # def get_menu(self,obj):
    #
    #     print(obj)
    #
    #
    #     # # user = self.request.user
    #     # # print(user)
    #     # user = UserProfile.objects.filter(id=2)[0]
    #     # # print(user.id)
    #     #
    #     # userRole = UserRole.objects.filter(user = user.id)[0]
    #     #
    #     # # print(userRole.role.id)
    #     #
    #     # menu_list = RoleMenu.objects.values('menu').filter(role__id=userRole.role.id)
    #     # print(menu_list)
    #
    #     return  None

    class Meta:
        model = RoleMenu
        fields = ('role','menu')


class RoleMenuSerializer(serializers.ModelSerializer):


    class Meta:
        # validate实现唯一联合，一个菜单只能被角色设置一次
        validators = [
            UniqueTogetherValidator(
                queryset=RoleMenu.objects.all(),
                fields=('role', 'menu'),
                # message的信息可以自定义
                message="已经设置"
            )
        ]
        model = RoleMenu
        fields = '__all__'


class UserProfileListSerializer(serializers.ModelSerializer):


    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserRoleListSerializer(serializers.ModelSerializer):

    '''
    角色菜单列表展示
    '''
    user = UserProfileSerializer()
    role = RoleSerializer()

    # 序列化的作用是将ID 转化成对象
    # 注意,这里不可以设置成many=True

    class Meta:
        model = UserRole
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):


    class Meta:
        # validate实现唯一联合，一个菜单只能被角色设置一次
        validators = [
            UniqueTogetherValidator(
                queryset=UserRole.objects.all(),
                fields=('role', 'user'),
                # message的信息可以自定义
                message="已经设置"
            )
        ]
        model = UserRole
        fields = '__all__'

