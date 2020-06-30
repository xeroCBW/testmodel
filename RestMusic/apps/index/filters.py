import django_filters

from .models import *


class CommentFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = Comment
        fields = ['user','song']


class DynamicFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Dynamic
        fields = ['song',]

class SongFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Song
        fields = ['label',]