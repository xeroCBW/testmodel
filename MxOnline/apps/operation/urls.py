from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router =  DefaultRouter()
router.register('user-course',UserCourseViewSet,base_name='user-course')
router.register('user-ask',UserAskViewSet,base_name='user-ask')
router.register('user-message',UserMessageViewSet,base_name='user-message')
router.register('course-comment',CourseCommentsViewSet,base_name='course-comment')


urlpatterns = [
    path('',include(router.urls))
]