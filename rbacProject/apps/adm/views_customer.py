from django.shortcuts import render

from rbac.models import Menu
from system.models import SystemSetup


def customerView(request):
    if request.method == 'GET':
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/customer.html', ret)


def customerListView():
    return None


def customerDetailView():
    return None


def customerDeleteView():
    return None