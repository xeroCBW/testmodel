"""rbacProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from system import views
from django.urls import re_path
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.indexView),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('system/', views.systemView, name='system'),

    path('system/basic/', include('system.urls',namespace='system-basic')),
    path('system/rbac/', include('rbac.urls',namespace='system-rbac')),



    path('adm/',include('adm.urls')),
    path('personal/',include('personal.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


    # url(r'^personal/$', personal_views.PersonalView.as_view(), name="personal"),
    # url(r'^personal/userinfo', personal_views.UserInfoView.as_view(), name="personal-user_info"),
    # url(r'^personal/uploadimage', personal_views.UploadImageView.as_view(), name="personal-uploadimage"),
    # url(r'^personal/passwordchange', personal_views.PasswdChangeView.as_view(), name="personal-passwordchange"),
    # url(r'^personal/phonebook', personal_views.PhoneBookView.as_view(), name="personal-phonebook"),
    # url(r'^personal/workorder_Icrt/$', order.WorkOrderView.as_view(), name="personal-workorder_Icrt"),
    # url(r'^personal/workorder_Icrt/list', order.WorkOrderListView.as_view(), name="personal-workorder-list"),
    # url(r'^personal/workorder_Icrt/create', order.WorkOrderCreateView.as_view(), name="personal-workorder-create"),
    # url(r'^personal/workorder_Icrt/detail', order.WorkOrderDetailView.as_view(), name="personal-workorder-detail"),
    # url(r'^personal/workorder_Icrt/delete', order.WorkOrderDeleteView.as_view(), name="personal-workorder-delete"),
    # url(r'^personal/workorder_Icrt/update', order.WorkOrderUpdateView.as_view(), name="personal-workorder-update"),
    # url(r'^personal/workorder_app/$', order.WorkOrderView.as_view(), name="personal-workorder_app"),
    # url(r'^personal/workorder_app/send', order.WrokOrderSendView.as_view(), name="personal-workorder-send"),
    # url(r'^personal/workorder_rec/$', order.WorkOrderView.as_view(), name="personal-workorder_rec"),
    # url(r'^personal/workorder_rec/execute', order.WorkOrderExecuteView.as_view(), name="personal-workorder-execute"),
    # url(r'^personal/workorder_rec/finish', order.WorkOrderFinishView.as_view(), name="personal-workorder-finish"),
    # url(r'^personal/workorder_rec/upload', order.WorkOrderUploadView.as_view(), name="personal-workorder-upload"),
    # url(r'^personal/workorder_rec/return', order.WorkOrderReturnView.as_view(), name="personal-workorder-return"),
    # url(r'^personal/workorder_Icrt/upload', order.WorkOrderProjectUploadView.as_view(),
    #     name="personal-workorder-project-upload"),
    # url(r'^personal/workorder_all/$', order.WorkOrderView.as_view(), name="personal-workorder_all"),
    # url(r'^personal/document/$', order.WorkOrderDocumentView.as_view(), name="personal-document"),
    # url(r'^personal/document/list', order.WorkOrderDocumentListView.as_view(), name="personal-document-list"),






]
