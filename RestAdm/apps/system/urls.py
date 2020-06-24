from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router = DefaultRouter()

#配置goods的url
# router.register('user', UserListViewSet,base_name='user')
router.register('menu', MenuListViewSet,base_name='menu')
router.register('structure', StructureListViewSet,base_name='structure')
router.register('role', RoleListViewSet,base_name='role')
# router.register('role-menu', RoleMenuListViewSet,base_name='role-menu')
# router.register('user-role', UserRoleListViewSet,base_name='user-role')
router.register('user', UserListViewSet,base_name='user')
router.register('user-permission', UserPermissionListViewSet,base_name='user-permission')
# router.register('role-permission', RolePermissionListViewSet,base_name='role-permission')
router.register('change-password', ChangePasswordtViewSet,base_name='change-password')

# router.register('test', TestViewSet,base_name='test')

urlpatterns = [

    path('', include(router.urls)),
    # path('role-menu-query',RoleMenuQueryView.as_view())


]
