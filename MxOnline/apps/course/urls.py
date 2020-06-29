from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import *

router =  DefaultRouter()
router.register('course',CourseViewSet,base_name='course')
router.register('resource',CourseResourceViewSet,base_name='resource')
router.register('lesson',LessonViewSet,base_name='lesson')
router.register('video',VideoViewSet,base_name='video')

urlpatterns = [
    path('',include(router.urls))
]