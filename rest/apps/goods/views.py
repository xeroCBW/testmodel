from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.


class GoodsListView(APIView):
    '''
    商品列表
    '''
    def get(self,request,format=None):
        goods = Goods.objects.all()
        goods_serialzer = GoodsSerializer(goods,many=True)
        return Response(goods_serialzer.data)