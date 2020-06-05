from django.shortcuts import render

from rbac.models import Menu
from system.models import SystemSetup


def equipmentTypeView(request):
    if request.method == 'GET':

        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/equipmenttype.html', ret)


def equipmentTypeListView():
    return None


def equipmentTypeDetailView():
    return None


def equipmentTypeDeleteView():
    return None