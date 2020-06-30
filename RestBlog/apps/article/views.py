from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters, mixins


from .models import *
from .serializers import *

# User = get_user_model()


class BlogTypeViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = BlogType.objects.all()
    serializer_class = BlogTypeSerializer

class BlogViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer