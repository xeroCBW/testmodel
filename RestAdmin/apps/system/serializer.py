from rest_framework import serializers

from .models import *


class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model = Menu
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    '''
    二级分类
    '''
    #在parent_category字段中定义的related_name="sub_cat"
    sub_menu = CategorySerializer3(many=True)
    class Meta:
        model = Menu
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_menu = CategorySerializer2(many=True)
    class Meta:
        model = Menu
        fields = "__all__"




class MenuSerializer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Menu
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    permissions = MenuSerializer(many=True,required=False)
    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):

        role = Role.objects.create(**validated_data)
        permissions = validated_data["permissions"]

        if permissions:
            role.permissions = permissions
        return role

    def update(self, instance, validated_data):

        permissions = validated_data["permissions"]
        title = validated_data["title"]

        instance.title = title

        print(instance.permissions)

        # instance.permissions = permissions
        # 要进行保存,否则不会有修改
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = '__all__'


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'

