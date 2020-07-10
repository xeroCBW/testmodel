from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import post_list,post_detail,links


router = DefaultRouter()
# router.register('blog', BlogViewSet,base_name='blog')
# router.register('content-type', BlogTypeViewSet,base_name='content-type')



urlpatterns = [

    # path('', include(router.urls)),
    # path('role-menu-query',RoleMenuQueryView.as_view())
    path('',post_list),
    path('post/<int:post_id>',post_detail),
    path('links/',links)
]
