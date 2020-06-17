from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder

from rbac.models import Menu
from system.models import SystemSetup
from users.models import Structure
from system.forms import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required


def menuView(request):
    ret = Menu.getMenuByRequestUrl(url=request.path_info)
    ret.update(SystemSetup.getSystemSetupLastData())
    print(ret)
    return render(request, 'system/rbac/menu-list.html', ret)



def menuListView(request):
    if request.method == 'GET':
        fields = ['id', 'title', 'code', 'url', 'is_top', 'parent__title']
        ret = dict(data=list(Menu.objects.values(*fields).order_by('id')))
        return HttpResponse(json.dumps(ret), content_type='application/json')


def menuDetailView(request):


    if request.method == 'GET':


        ret = dict()
        if 'id' in request.GET and request.GET['id']:

            print ('=========',id,'===========')


            menu = get_object_or_404(Menu, pk=request.GET.get('id'))
            ret['menu'] = menu
        menu_list = Menu.objects.exclude(id=request.GET.get('id'))
        ret['menu_list'] = menu_list

        # print ('--------')
        # print (menu_list)

        return render(request, 'system/rbac/menu_detail.html', ret)

    else:
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            menu = get_object_or_404(Menu, pk=request.POST.get('id'))
        else:
            menu = Menu()
        menu_form = MenuForm(request.POST, instance=menu)
        if menu_form.is_valid():
            # 这个save 可以实现新增和修改
            menu_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')
