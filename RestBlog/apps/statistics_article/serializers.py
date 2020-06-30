import time
from random import Random

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class ReadNumSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadNum
        fields = '__all__'

class ReadDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadDetail
        fields = '__all__'