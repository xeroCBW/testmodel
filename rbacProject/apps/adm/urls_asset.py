from django.urls import path
from adm import views_asset



app_name='[adm]'

urlpatterns = [

    path('', views_asset.AssetView, name='asset'),
    path('list/', views_asset.AssetListView, name="list"),
    path('create/', views_asset.AssetCreateView, name="create"),
    path('update/', views_asset.AssetUpdateView, name="update"),
    path('detail/', views_asset.AssetDetailView, name="asset-detail"),
    path('delete/', views_asset.AssetDeleteView, name='delete'),
    path('upload/', views_asset.AssetUploadView, name='upload'),
]
