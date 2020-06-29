from rest_framework import viewsets,filters
from course.serializers import *
from course.models import *
from .filters import *

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseResourceViewSet(viewsets.ModelViewSet):

    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializer


class LessonViewSet(viewsets.ModelViewSet):

    filter_backends = (filters.SearchFilter,filters.OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)

    # 一定要将字段放进去,否则排序将不起作用
    ordering_fields = ('course', )
    search_fields = ('id','name' )
    filter_class = LessonFilter

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class VideoViewSet(viewsets.ModelViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer