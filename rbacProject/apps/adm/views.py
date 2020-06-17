from django.shortcuts import render

# Create your views here.
from rbac.models import Menu
from system.models import SystemSetup


def indexView(request):
    ret = Menu.getMenuByRequestUrl(url=request.path_info)
    ret.update(SystemSetup.getSystemSetupLastData())
    return render(request, 'adm/adm_index.html', ret)
