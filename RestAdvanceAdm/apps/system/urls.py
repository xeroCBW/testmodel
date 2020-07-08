from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router = DefaultRouter()

# router.register('button-type', ButtonTypeViewSets,base_name='button-type')
router.register('permission', PermissionViewSets,basename='permission')
router.register('role', RoleViewSets,basename='role')
router.register('user', UserViewSets,basename='user')
router.register('user-permission', UserPermissionViewSets,basename='user-permission')
router.register('change-password', ChangePasswordtViewSet,basename='change-password')

urlpatterns = [

    path('', include(router.urls)),

]
