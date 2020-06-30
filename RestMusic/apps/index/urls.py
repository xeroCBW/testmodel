from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router = DefaultRouter()

router.register('label',LableViewSet ,base_name='label')
router.register('song',SongViewSet ,base_name='song')
router.register('comment',CommentViewSet ,base_name='comment')
router.register('dynamic',DynamicViewSet ,base_name='dynamic')

urlpatterns = [

    path('', include(router.urls)),

]
