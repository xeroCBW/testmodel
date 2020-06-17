from django.urls import path
from . import views
from . import views_menu,views_role

app_name='[rbac]'

urlpatterns = [

    # # 菜单管理
    # url(r'^menu/$', views_menu.MenuView.as_view(), name="menu"),
    # url(r'^menu/list$', views_menu.MenuListView.as_view(), name="menu-list"),
    # url(r'^menu/detail$', views_menu.MenuListDetailView.as_view(), name="menu-detail"),

    path('menu/',views_menu.menuView,name='menu'),
    path('menu/list',views_menu.menuListView,name='menu-list'),
    path('menu/detail',views_menu.menuDetailView,name='menu-detail'),

    path('role/',views_role.roleView,name='role'),
    path('role/list',views_role.roleListView,name='role-list'),
    path('role/detail',views_role.roleDetailView,name='role-detail'),
    path('role/delete',views_role.roleDeleteView,name='role-delete'),
    path('role/role_menu',views_role.role2MenuView,name='role-role_menu'),
    path('role/role_menu_list',views_role.role2MenuListView,name='role-role_menu_list'),
    path('role/role_user',views_role.role2UserView,name='role-role_user'),

]