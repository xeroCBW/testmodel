from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters, mixins


from .models import *
from .serializers import *

# User = get_user_model()


class ReadNumViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = ReadNum.objects.all()
    serializer_class = ReadNumSerializer

class ReadDetailViewSet(viewsets.ModelViewSet):
    '''
    list:
        列表数据
    '''

    queryset = ReadDetail.objects.all()
    serializer_class = ReadDetailSerializer