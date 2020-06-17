from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder

from rbac.models import Menu
from system.models import SystemSetup
from users.models import Structure
from .forms import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login')
def structureView(request):

    ret = Menu.getMenuByRequestUrl(url=request.path_info)
    ret.update(SystemSetup.getSystemSetupLastData())

    return render(request,'system/structure/structure-list.html',ret)

@login_required(login_url='/login')
def structureListView(request):

    fields = ['id', 'title', 'type', 'parent__title']
    ret = dict(data=list(Structure.objects.values(*fields)))
    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

@login_required(login_url='/login')
def structureAddUserView(request):

    if request.method == 'GET':



        if 'id' in request.GET and request.GET['id']:

            structure = get_object_or_404(Structure, pk=int(request.GET.get('id')))

            added_users = structure.userprofile_set.all()
            all_users = User.objects.exclude(username='admin')
            un_add_users = set(all_users).difference(added_users)

            ret = dict(structure=structure, added_users=added_users, un_add_users=list(un_add_users))
        return render(request, 'system/structure/structure_user.html', ret)
    else:
        res = dict(result=False)
        id_list = None
        structure = get_object_or_404(Structure, pk=int(request.POST.get('id')))
        if 'to' in request.POST and request.POST['to']:
            id_list = map(int, request.POST.getlist('to', []))
        structure.userprofile_set.clear()
        if id_list:
            for user in User.objects.filter(id__in=id_list):
                structure.userprofile_set.add(user)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')

@login_required(login_url='/login')
def structureDetailView(request):

    if request.method == 'GET':
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            structure = get_object_or_404(Structure, pk=request.GET.get('id'))
            structures = Structure.objects.exclude(id=request.GET.get('id'))
            ret['structure'] = structure

        else:
            structures = Structure.objects.all()
        ret['structures'] = structures
        return render(request, 'system/structure/structure_detail.html', ret)
    else:
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            structure = get_object_or_404(Structure, pk=request.POST.get('id'))
        else:
            structure = Structure()
        structure_update_form = StructureUpdateForm(request.POST, instance=structure)
        if structure_update_form.is_valid():
            structure_update_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')

@login_required(login_url='/login')
def structureDeleteView(request):

    ret = dict(result=False)
    if 'id' in request.POST and request.POST['id']:
        id_list = map(int, request.POST.get('id').split(','))
        Structure.objects.filter(id__in=id_list).delete()
        ret['result'] = True
    return HttpResponse(json.dumps(ret), content_type='application/json')