from django.shortcuts import render

from rbac.models import Menu
from system.models import SystemSetup


def assetTypeView(request):
    if request.method == 'GET':
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/assettype.html', ret)


def assetTypeListView():
    return None


def assetTypeDetailView():
    return None


def assetTypeDeleteView():
    return None