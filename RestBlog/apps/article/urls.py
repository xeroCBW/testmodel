from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import post_list,post_detail,links,IndexView


router = DefaultRouter()
# router.register('blog', BlogViewSet,base_name='blog')
# router.register('content-type', BlogTypeViewSet,base_name='content-type')



urlpatterns = [

    # path('', include(router.urls)),
    # path('role-menu-query',RoleMenuQueryView.as_view())

    # path('',post_list,name = 'post-list'),# post_list--最后进入的函数
    # path('post/<int:post_id>.html',post_detail,name = 'post-detail'),# post_detail--最后进入的函数
    # path('links/',links)

    # 这里开始使用view
    path('', IndexView.as_view(), name='post-list'),  # post_list--最后进入的函数
    path('post/<int:post_id>.html', post_detail, name='post-detail'),  # post_detail--最后进入的函数
    path('links/', links)
]
