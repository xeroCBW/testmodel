from rest_framework import viewsets, filters, mixins

from .models import *
from .serializers import *

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

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DynamicViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = Dynamic.objects.all()
    serializer_class = DynamicSerializer