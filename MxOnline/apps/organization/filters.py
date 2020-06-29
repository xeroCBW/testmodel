import django_filters

from .models import *


class CourseOrgFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = CourseOrg
        fields = ['click_nums','fav_nums','city',]

