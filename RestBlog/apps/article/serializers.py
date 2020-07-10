import time
from random import Random

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

# class BlogTypeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = BlogType
#         fields = '__all__'
#
# class BlogSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Blog
#         fields = '__all__'