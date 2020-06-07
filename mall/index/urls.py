from django.urls import path
from . import views

urlpatterns = [

    path('', views.indexView,name='index'),
    path('shoppingCar/', views.shoppingCarView,name='shoppingCar'),

]