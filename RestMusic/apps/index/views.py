from rest_framework import viewsets, filters, mixins

from .models import *
from .serializers import *
from .filters import *
from .paginations import *

class LableViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = Label.objects.all()
    serializer_class = LabelSerializer

class SongViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = Song.objects.all()
    serializer_class = SongSerializer

class CommentViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    filter_backends = (filters.SearchFilter,filters.OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)

    # 一定要将字段放进去,否则排序将不起作用
    ordering_fields = ('create_time', )
    search_fields = ('user','song','text' )
    filter_class = CommentFilter

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class DynamicViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    filter_backends = (filters.SearchFilter,filters.OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)

    # 一定要将字段放进去,否则排序将不起作用
    ordering_fields = ('create_time', )
    search_fields = ('song__name', )
    filter_class = DynamicFilter
    # 设置分页
    pagination_class = GlobalPagination

    queryset = Dynamic.objects.all().order_by('-play_num')
    serializer_class = DynamicSerializer