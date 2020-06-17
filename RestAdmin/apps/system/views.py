from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from .models import Menu
from .serializer import MenuSerializer


class MenuListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    '''

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer