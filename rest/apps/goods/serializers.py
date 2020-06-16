from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(default="",max_length=20)
    click_num = serializers.IntegerField(default=0,)
    goods_front_image = serializers.ImageField()