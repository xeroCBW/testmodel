"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,include
from django.views.static import serve

# import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin
from goods.views import  GoodsListViewSet
from rest.settings import MEDIA_ROOT

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet,base_name='goods')

urlpatterns = [

    path('xadmin/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title="天天生鲜")),

]

