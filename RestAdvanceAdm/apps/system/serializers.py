from rest_framework import serializers
from .models import *

class ButtonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ButtonType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Permission
        fields = ('id','name','desc','code','type','icon','order_num','parent_id','sub_permission')
    def get_related_field(self, model_field):
        return PermissionSerializer()

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('password','groups','user_permissions')
