from django.urls import path
from . import views
from . import views_structure

app_name='[system]'

urlpatterns = [

    path('structure/', views_structure.structureView, name='structure'),
    path('structure/list', views_structure.structureListView, name='structure-list'),
    path('structure/detail', views_structure.structureDetailView, name='structure-detail'),
    path('structure/delete', views_structure.structureDeleteView, name='structure-delete'),
    path('structure/add_user', views_structure.structureAddUserView, name='structure-add_user'),



]