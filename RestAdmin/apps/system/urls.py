from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import MenuListViewSet

router = DefaultRouter()

#配置goods的url
# router.register(r'user', UserListViewSet,base_name='user')
router.register('menu', MenuListViewSet,base_name='menu')


urlpatterns = [


    path('', include(router.urls)),


]

