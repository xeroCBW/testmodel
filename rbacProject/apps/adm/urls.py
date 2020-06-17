# url(r'^adm/$', AdmView.as_view(), name="adm-main"),
# url(r'^adm/bsm/', include('adm.urls', namespace='adm-bsm')),
# url(r'^adm/equipment/', include('adm.urls_equipment', namespace='adm-equipment')),
# url(r'^adm/asset/', include('adm.urls_asset', namespace='adm-asset')),


from django.urls import path,include
from adm import views


# app_name='[adm]'

urlpatterns = [

    path('', views.indexView,name='adm-main'),
    path('bsm/',  include('adm.urls_bsm', namespace='adm-bsm')),

    path('equipment/', include('adm.urls_equipment', namespace='adm-equipment')),
    path('asset/',include('adm.urls_asset', namespace='adm-asset')),



    ]