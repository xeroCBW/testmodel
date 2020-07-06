from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router = DefaultRouter()

#配置goods的url
# router.register('button-type', ButtonTypeViewSets,base_name='button-type')
router.register('permission', PermissionViewSets,base_name='permission')
router.register('role', RoleViewSets,base_name='role')
router.register('user', UserViewSets,base_name='user')
router.register('user-permission', UserPermissionViewSets,base_name='user-permission')
urlpatterns = [

    path('', include(router.urls)),

]
