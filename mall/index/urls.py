from django.urls import path
from . import views

urlpatterns = [

    path('', views.indexView,name='index'),

    path('shoppingCar/', views.shoppingCarView,name='shoppingCar'),
    path('product_add/', views.productAddView,name='productAdd'),
    path('pagination/<int:page>.html', views.paginationView,name='pagination'),

]