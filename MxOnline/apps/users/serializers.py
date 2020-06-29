from rest_framework import serializers
from .models import  *

class BannerSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Banner
        fields = '__all__'