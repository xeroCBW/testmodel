from django.urls import path
from . import views
from . import views_structure,views_user

app_name='[system]'

urlpatterns = [

    path('structure/', views_structure.structureView, name='structure'),
    path('structure/list', views_structure.structureListView, name='structure-list'),
    path('structure/detail', views_structure.structureDetailView, name='structure-detail'),
    path('structure/delete', views_structure.structureDeleteView, name='structure-delete'),
    path('structure/add_user', views_structure.structureAddUserView, name='structure-add_user'),

    path('user/', views_user.userView, name='user'),
    path('user/list', views_user.userListView, name='user-list'),
    path('user/detail', views_user.userDetailView, name='user-detail'),
    path('user/update', views_user.userUpdateView, name='user-update'),
    path('user/create', views_user.userCreateView, name='user-create'),
    path('user/delete', views_user.userDeleteView, name='user-delete'),
    path('user/enable', views_user.userEnableView, name='user-enable'),
    path('user/disable', views_user.userDisableView, name='user-disable'),
    path('user/adminpasswdchange', views_user.userAdminPasswordChangeView, name='user-adminpasswdchange'),



]