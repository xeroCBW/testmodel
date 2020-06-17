from django.urls import path
from adm import views_equipment

app_name='[adm]'

urlpatterns = [

    path('', views_equipment.equipmentView, name='equipment'),
    path('list/', views_equipment.equipmentListView, name="list"),
    path('create/', views_equipment.equipmentCreateView, name="create"),
    path('detail/', views_equipment.equipmentDetailView, name="equipment-detail"),
    path('delete/', views_equipment.equipmentDeleteView, name='delete'),
    path('serviceinfoupdate/', views_equipment.serviceInfoUpdateView, name='service-info-update'),
]