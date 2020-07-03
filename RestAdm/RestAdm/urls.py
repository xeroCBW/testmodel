"""RestAdm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import include,path
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from system.views import LogoutViewSet

from rest_framework.documentation import include_docs_urls

# 设置图片位置
from RestAdm.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('system.urls')),
    # path('system/', include('system.urls')),
    path('docs',include_docs_urls(title='后台管理系统')),
    path('user/login', obtain_jwt_token),
    path('user/refresh_token', refresh_jwt_token),


    #文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
]
