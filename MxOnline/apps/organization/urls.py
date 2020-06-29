from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('course-org',CourseOrganizationViewSet,base_name='organization-org')
router.register('city',CityViewSet,base_name='organization-city')
# router.register('category',CategoryViewSet,base_name='category')

urlpatterns = [

    path('',include(router.urls)),
]