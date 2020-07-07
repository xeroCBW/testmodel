from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router = DefaultRouter()

#配置goods的url
# router.register('user', UserListViewSet,base_name='user')
# router.register('menu', MenuListViewSet,base_name='menu')
# router.register('structure', StructureListViewSet,base_name='structure')
router.register('role', RoleListViewSet,basename='role')
# router.register('role-menu', RoleMenuListViewSet,base_name='role-menu')
# router.register('user-role', UserRoleListViewSet,base_name='user-role')
router.register('user', UserListViewSet,basename='user')
router.register('user-permission', UserPermissionListViewSet,basename='user-permission')
# router.register('role-permission', RolePermissionListViewSet,base_name='role-permission')
# router.register('change-password', ChangePasswordtViewSet,base_name='change-password')
# router.register('logout', LogoutViewSet,base_name='logout')


# router.register('user-address', UserAddressViewSet,base_name='user-address')
# router.register('user-message', UserMessageViewSet,base_name='user-message')
# router.register('category', CategoryViewSet,base_name='category')
router.register('good',GoodViewSet,basename='good')
# router.register('banner',BannerViewSet,base_name='banner')
# router.register('user-fav',UserFavorateViewSet,base_name='user-fav')
# router.register('cart',CartViewSet,base_name='cart')
# router.register('order',OrderViewSet,base_name='order')
# router.register('order-good',OrderGoodViewSet,base_name='order-good')

# router.register('album', AlbumtViewSet,base_name='album')
# router.register('track', TrackViewSet,base_name='track')
# router.register('album-image', AlbumImageViewSet,base_name='album-image')


router.register('page', PageViewSet,basename='page')
router.register('button', ButtonViewSet,basename='button')
router.register('download/button', ButtonRenderViewSets,basename='download/button')


urlpatterns = [

    path('', include(router.urls)),

]
