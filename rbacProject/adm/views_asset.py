from django.shortcuts import render

from adm.models import Asset, AssetType
from rbac.models import Menu
from system.models import SystemSetup


def AssetView(request):

    if request.method == 'GET':
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        status_list = []
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_types = AssetType.objects.all()
        ret['status_list'] = status_list
        ret['asset_types'] = asset_types
        return render(request, 'adm/asset/asset.html', ret)

def AssetListView():
    return None

def AssetCreateView():
    return None


def AssetUpdateView():
    return None


def AssetDetailView():
    return None


def AssetDeleteView():
    return None


def AssetUploadView():
    return None