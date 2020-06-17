"""RestAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#配置goods的url
# router.register(r'goods', GoodsListViewSet,base_name='goods')
# router.register(r'categorys', CategoryViewSet, base_name="categorys")
# router.register(r'banners', BannerViewset, base_name="banners")
# router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

# urlpatterns = [
#
#     path('xadmin/', xadmin.site.urls),
#     path('api-auth/',include('rest_framework.urls')),
#     path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
#     path('', include(router.urls)),
#     path('docs/', include_docs_urls(title="天天生鲜")),
#     # path('jwt-auth/', obtain_jwt_token),
#
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('system/basic/', include('system.urls')),
    path('docs',include_docs_urls(title='后台管理系统')),
    path('login', obtain_jwt_token ),
]
