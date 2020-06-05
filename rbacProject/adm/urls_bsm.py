from django.urls import path
from adm import views_bsm

app_name='[adm]'

urlpatterns = [

    path('supplier/', views_bsm.supplierView, name="supplier"),
    path('supplier/list/', views_bsm.supplierListView, name="supplier-list"),
    path('supplier/detail/', views_bsm.supplierDetailView, name="supplier-detail"),
    path('supplier/delete/', views_bsm.supplierDeleteView, name="supplier-delete"),

    path('assettype/', views_bsm.assetTypeView, name="assettype"),
    path('assettype/list/', views_bsm.assetTypeListView, name="assettype-list"),
    path('assettype/detail/', views_bsm.assetTypeDetailView, name="assettype-detail"),
    path('assettype/delete/', views_bsm.assetTypeDeleteView, name="assettype-delete"),

    path('customer/', views_bsm.customerView, name="customer"),
    path('customer/list/', views_bsm.customerListView, name="customer-list"),
    path('customer/detail/', views_bsm.customerDetailView, name="customer-detail"),
    path('customer/delete/', views_bsm.customerDeleteView, name="customer-delete"),

    path('equipmenttype/', views_bsm.equipmentTypeView, name="equipmenttype"),
    path('equipmenttype/list/', views_bsm.equipmentTypeListView, name="equipmenttype-list"),
    path('equipmenttype/detail/', views_bsm.equipmentTypeDetailView, name="equipmenttype-detail"),
    path('equipmenttype/delete/', views_bsm.equipmentTypeDeleteView, name="equipmenttype-delete"),

]