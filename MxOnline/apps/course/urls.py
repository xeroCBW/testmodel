from rest_framework.routers import DefaultRouter
from course.views import CourseViewset
from django.urls import path,include

router =  DefaultRouter()
router.register('course',CourseViewset,base_name='course')




urlpatterns = [
    path('',include(router.urls))
]