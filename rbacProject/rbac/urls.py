from django.urls import path
from . import views
from . import views_menu

app_name='[rbac]'

urlpatterns = [

    # # 菜单管理
    # url(r'^menu/$', views_menu.MenuView.as_view(), name="menu"),
    # url(r'^menu/list$', views_menu.MenuListView.as_view(), name="menu-list"),
    # url(r'^menu/detail$', views_menu.MenuListDetailView.as_view(), name="menu-detail"),

    path('menu/',views_menu.menuView,name='menu'),
    path('menu/list',views_menu.menuListView,name='menu-list'),
    path('menu/detail',views_menu.menuDetailView,name='menu-detail'),
]