from django.shortcuts import render
from .models import *
from .serializers import *
from .utils.basemodelviewsets import *
# Create your views here.



class ButtonTypeViewSets(CustomBaseModelViewSet):
    serializer_class = ButtonTypeSerializer
    queryset = ButtonType.objects.all()

class PermissionViewSets(CustomBaseModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

class RoleViewSets(CustomBaseModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class UserViewSets(CustomBaseModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
