from rest_framework import serializers

class CusButtonSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    desc = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=20)
    state = serializers.BooleanField()

class CusPageSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    desc = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=20)
    state = serializers.BooleanField()
    selected = CusButtonSerializer(many=True,read_only = True)
    options = CusButtonSerializer(many=True,read_only = True)

class CusRoleSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    desc = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=20)
    state = serializers.BooleanField()
    pages = CusPageSerializer(many=True,read_only = True)
