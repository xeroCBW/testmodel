from django.shortcuts import render
from rest_framework import viewsets,mixins
from .models import *
from .serializers import *

class BannerViewSets(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer