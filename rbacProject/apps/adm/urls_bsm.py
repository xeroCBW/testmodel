from django.urls import path
from adm import views_supplier,views_assettype,views_customer,views_equipmenttype

app_name='[adm]'

urlpatterns = [

    path('supplier/', views_supplier.supplierView, name="supplier"),
    path('supplier/list/', views_supplier.supplierListView, name="supplier-list"),
    path('supplier/detail/', views_supplier.supplierDetailView, name="supplier-detail"),
    path('supplier/delete/', views_supplier.supplierDeleteView, name="supplier-delete"),

    path('assettype/', views_assettype.assetTypeView, name="assettype"),
    path('assettype/list/', views_assettype.assetTypeListView, name="assettype-list"),
    path('assettype/detail/', views_assettype.assetTypeDetailView, name="assettype-detail"),
    path('assettype/delete/', views_assettype.assetTypeDeleteView, name="assettype-delete"),

    path('customer/', views_customer.customerView, name="customer"),
    path('customer/list/', views_customer.customerListView, name="customer-list"),
    path('customer/detail/', views_customer.customerDetailView, name="customer-detail"),
    path('customer/delete/', views_customer.customerDeleteView, name="customer-delete"),

    path('equipmenttype/', views_equipmenttype.equipmentTypeView, name="equipmenttype"),
    path('equipmenttype/list/', views_equipmenttype.equipmentTypeListView, name="equipmenttype-list"),
    path('equipmenttype/detail/', views_equipmenttype.equipmentTypeDetailView, name="equipmenttype-detail"),
    path('equipmenttype/delete/', views_equipmenttype.equipmentTypeDeleteView, name="equipmenttype-delete"),

]