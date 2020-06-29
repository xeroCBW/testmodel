from rest_framework import serializers
from .models import *


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


class TeacherSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'