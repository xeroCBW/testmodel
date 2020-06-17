from django.urls import path
from adm import views_supplier

app_name='[adm]'

urlpatterns = [

    path('', views_supplier.supplierView, name="supplier"),
    path('list/', views_supplier.supplierListView, name="supplier-list"),
    path('detail/', views_supplier.supplierDetailView, name="supplier-detail"),
    path('delete/', views_supplier.supplierDeleteView, name="supplier-delete"),


]