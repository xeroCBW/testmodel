import django_filters

from .models import *


class LessonFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = Lesson
        fields = ['course','name',]

