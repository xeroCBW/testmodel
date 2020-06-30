import time
from random import Random

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):


    # song_dynamic = DynamicSerializer(read_only=True)
    # song_comment = CommentSerializer(read_only=True,many=True)

    class Meta:
        model = Song
        fields = '__all__'

class DynamicSerializer(serializers.ModelSerializer):


    song = SongSerializer(read_only=True)

    class Meta:
        model = Dynamic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

