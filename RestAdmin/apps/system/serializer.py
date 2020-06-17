from rest_framework import serializers

from .models import *

class MenuSerializer(serializers.ModelSerializer):
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

