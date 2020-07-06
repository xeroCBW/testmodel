from rest_framework import serializers
from rest_framework.validators import *
from .models import *

class ButtonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ButtonType
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id','name','desc','code','type','icon','order_num','parent_id',)



class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('password','groups','user_permissions')
