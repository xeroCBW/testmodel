from rest_framework import serializers

from course.models import *


class CourseSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
    pass

class CourseResourceSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CourseResource
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'