from django.urls import path,include
from personal import views,views_worker_order

urlpatterns = [

    path('', views.personalView,name='personal'),
    path('userinfo/', views.userInfoView,name = 'personal-user_info'),
    path('uploadimage/', views.uploadImageView, name="personal-uploadimage"),
    path('passwordchange/', views.passwdChangeView, name="personal-passwordchange"),
    path('phonebook/', views.phoneBookView, name="personal-phonebook"),
    path('workorder_Icrt/', views_worker_order.workOrderView, name="personal-workorder_Icrt"),
    path('workorder_Icrt/list/', views_worker_order.wrkOrderListView, name="personal-workorder-list"),
    path('workorder_Icrt/create/', views_worker_order.workOrderCreateView, name="personal-workorder-create"),
    path('workorder_Icrt/detail/', views_worker_order.workOrderDetailView, name="personal-workorder-detail"),
    path('workorder_Icrt/delete/', views_worker_order.workOrderDeleteView, name="personal-workorder-delete"),
    path('workorder_Icrt/update/', views_worker_order.workOrderUpdateView, name="personal-workorder-update"),
    path('workorder_app/', views_worker_order.workOrderView, name="personal-workorder_app"),
    path('workorder_app/send/', views_worker_order.wrokOrderSendView, name="personal-workorder-send"),
    path('workorder_rec/', views_worker_order.workOrderView, name="personal-workorder_rec"),
    path('workorder_rec/execute/', views_worker_order.workOrderExecuteView, name="personal-workorder-execute"),
    path('workorder_rec/finish/', views_worker_order.workOrderFinishView, name="personal-workorder-finish"),
    path('workorder_rec/upload/', views_worker_order.workOrderUploadView, name="personal-workorder-upload"),
    path('workorder_rec/return/', views_worker_order.workOrderReturnView, name="personal-workorder-return"),
    path('workorder_Icrt/upload/', views_worker_order.workOrderProjectUploadView,
        name="personal-workorder-project-upload"),
    path('workorder_all/', views_worker_order.workOrderView, name="personal-workorder_all"),
    path('document/', views_worker_order.workOrderDocumentView, name="personal-document"),
    path('document/list/', views_worker_order.workOrderDocumentListView, name="personal-document-list"),

    ]