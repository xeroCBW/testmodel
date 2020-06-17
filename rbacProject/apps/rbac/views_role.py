from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder

from rbac.models import Menu, Role
from system.models import SystemSetup
from users.models import Structure
from system.forms import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required


def roleView(request):

    ret = Menu.getMenuByRequestUrl(url=request.path_info)
    ret.update(SystemSetup.getSystemSetupLastData())
    return render(request, 'system/rbac/role-list.html', ret)



def roleListView(request):

    fields = ['id', 'title']
    ret = dict(data=list(Role.objects.values(*fields).exclude(id=1)))
    return HttpResponse(json.dumps(ret), content_type='application/json')


def roleDetailView(request):
    if request.method == 'GET':

        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            ret = dict(role=get_object_or_404(Role, pk=request.GET.get('id')))
        return render(request, 'system/rbac/role_detail.html', ret)

    else:
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            role = get_object_or_404(Role, pk=request.POST.get('id'))
        else:
            role = Role()
        if request.POST.get('title'):
            role.title = request.POST.get('title')
            role.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


def roleDeleteView(request):
    ret = dict(result=False)
    if 'id' in request.POST and request.POST['id']:
        id_list = map(int, request.POST.get('id').split(','))
        Role.objects.filter(id__in=id_list).delete()
        ret['result'] = True
    return HttpResponse(json.dumps(ret), content_type='application/json')


def role2MenuView(request):
    if request.method == 'GET':
        if 'id' in request.GET and request.GET['id']:
            role = get_object_or_404(Role, pk=request.GET.get('id'))
            ret = dict(role=role)
            return render(request, 'system/rbac/role_menu.html', ret)
    else:

        res = dict(result=False)
        role = get_object_or_404(Role, pk=request.POST.get('id'))
        tree = json.loads(request.POST['tree'])
        role.permissions.clear()
        for menu in tree:
            if menu['checked'] is True:
                menu_checked = get_object_or_404(Menu, pk=menu['id'])
                role.permissions.add(menu_checked)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


def role2MenuListView(request):
    fields = ['id', 'title', 'parent']
    if 'id' in request.GET and request.GET['id']:
        role = Role.objects.get(id=request.GET.get('id'))
        role_menus = role.permissions.values(*fields)
        ret = dict(data=list(role_menus))
    else:
        menus = Menu.objects.all()
        ret = dict(data=list(menus.values(*fields)))
    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


def role2UserView(request):
    if request.method == 'GET':

        if 'id' in request.GET and request.GET['id']:
            role = get_object_or_404(Role, pk=int(request.GET.get('id')))
            added_users = role.userprofile_set.all()
            all_users = User.objects.exclude(username='admin')
            un_add_users = set(all_users).difference(added_users)
            ret = dict(role=role, added_users=added_users, un_add_users=list(un_add_users))
        return render(request, 'system/rbac/role_user.html', ret)

    else:
        res = dict(result=False)
        id_list = None
        role = get_object_or_404(Role, pk=int(request.POST.get('id')))
        if 'to' in request.POST and request.POST['to']:
            id_list = map(int, request.POST.getlist('to', []))
        role.userprofile_set.clear()
        if id_list:
            for user in User.objects.filter(id__in=id_list):
                role.userprofile_set.add(user)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')