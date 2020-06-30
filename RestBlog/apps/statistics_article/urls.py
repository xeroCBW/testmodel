from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

from .views import *

router = DefaultRouter()
router.register('read-num', ReadNumViewSet,base_name='read-num')
router.register('read-detail', ReadDetailViewSet,base_name='read-detail')


urlpatterns = [
    path('', include(router.urls)),
]
