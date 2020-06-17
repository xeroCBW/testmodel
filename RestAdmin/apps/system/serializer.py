from rest_framework import serializers

from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    permissions = MenuSerializer(many=True)
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = '__all__'


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'

