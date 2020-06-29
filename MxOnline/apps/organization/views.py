from rest_framework import viewsets, mixins,filters
from .serializers import *
from .filters import *

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = CityDict.objects.all()


class CourseOrganizationViewSet(viewsets.ModelViewSet):

    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)

    # 一定要将字段放进去,否则排序将不起作用
    ordering_fields = ('click_nums', 'fav_nums','id')
    search_fields = ('address', )
    filter_class = CourseOrgFilter

    serializer_class = CourseOrganizationSerializer
    queryset = CourseOrg.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer