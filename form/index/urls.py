from django.urls import path
from . import views

urlpatterns = [

    path('',views.indexView),
    path('<int:id>.html',views.mode_indexView)


]