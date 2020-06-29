from rest_framework import serializers
from .models import *

class UserCourseSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserCourse
        fields = '__all__'

class UserAskSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserAsk
        fields = '__all__'


class UserMessageSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = UserMessage
        fields = '__all__'


class CourseCommentsSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CourseComments
        fields = '__all__'