from rest_framework import serializers
from .models import *
import django_filters


class CitySerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CityDict
        fields = '__all__'

class CourseOrganizationSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CourseOrg
        fields = '__all__'