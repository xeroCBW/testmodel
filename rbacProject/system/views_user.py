from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

from rbac.models import Role
from system.models import SystemSetup
from .forms import *
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db.models import Q

@login_required(login_url='/login')
def userView(request):
    ret = SystemSetup.getSystemSetupLastData()
    return render(request, 'system/users/user-list.html', ret)


@login_required(login_url='/login')
def userListView(request):

    fields = ['id', 'name', 'gender', 'mobile', 'email', 'department__title', 'post', 'superior__name', 'is_active']
    filters = dict()
    if 'select' in request.GET and request.GET.get('select'):
        filters['is_active'] = request.GET.get('select')
    ret = dict(data=list(User.objects.filter(**filters).values(*fields).exclude(username='admin')))
    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

@login_required(login_url='/login')
def userDetailView(request):
    user = get_object_or_404(User, pk=int(request.GET['id']))
    users = User.objects.exclude(Q(id=int(request.GET['id'])) | Q(username='admin'))
    structures = Structure.objects.values()
    roles = Role.objects.exclude(id=1)
    user_roles = user.roles.all()

    ret = {
        'user': user,
        'structures': structures,
        'users': users,
        'roles': roles,
        'user_roles': user_roles,

    }

    return render(request, 'system/users/user_detail.html', ret)


@login_required(login_url='/login')
def userUpdateView(request):
    if 'id' in request.POST and request.POST['id']:
        user = get_object_or_404(User, pk=int(request.POST['id']))
    else:
        user = get_object_or_404(User, pk=int(request.user.id))
    user_updata_form = UserUpdataForm(request.POST, instance=user)
    if user_updata_form.is_valid():
        user_updata_form.save()
        ret = {"status": "success"}
    else:
        ret = {'status': 'fail', 'message': user_updata_form.errors}
    return HttpResponse(json.dumps(ret), content_type='application/json')

@login_required(login_url='/login')
def userCreateView(request):

    if request.method == 'GET':
        users = User.objects.exclude(username='admin')
        structures = Structure.objects.values()
        roles = Role.objects.exclude(id=1)

        ret = {
            'users': users,
            'structures': structures,
            'roles': roles,
        }
        return render(request, 'system/users/user_create.html', ret)
    else:
        user_create_form = UserCreateForm(request.POST)
        if user_create_form.is_valid():
            new_user = user_create_form.save(commit=False)
            new_user.password = make_password(user_create_form.cleaned_data['password'])
            new_user.save()
            user_create_form.save_m2m()
            ret = {'status': 'success'}
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(user_create_form.errors)
            user_create_form_errors = re.findall(pattern, errors)
            ret = {
                'status': 'fail',
                'user_create_form_errors': user_create_form_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


@login_required(login_url='/login')
def userDeleteView(request):
    id_nums = request.POST.get('id')
    User.objects.extra(where=["id IN (" + id_nums + ")"]).delete()
    ret = {
        'result': 'true',
        'message': '数据删除成功！'
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

@login_required(login_url='/login')
def userEnableView(request):

    if 'id' in request.POST and request.POST['id']:
        id_nums = request.POST.get('id')
        queryset = User.objects.extra(where=["id IN(" + id_nums + ")"])
        queryset.filter(is_active=False).update(is_active=True)
        ret = {'result': 'True'}
    return HttpResponse(json.dumps(ret), content_type='application/json')

@login_required(login_url='/login')
def userDisableView(request):
    if 'id' in request.POST and request.POST['id']:
        id_nums = request.POST.get('id')
        queryset = User.objects.extra(where=["id IN(" + id_nums + ")"])
        queryset.filter(is_active=True).update(is_active=False)
        ret = {'result': 'True'}
    return HttpResponse(json.dumps(ret), content_type='application/json')

@login_required(login_url='/login')
def userAdminPasswordChangeView(request):
    if request.method == 'GET':
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            user = get_object_or_404(User, pk=int(request.GET.get('id')))
            ret['user'] = user
        return render(request, 'system/users/adminpasswd-change.html', ret)
    else:
        if 'id' in request.POST and request.POST['id']:
            user = get_object_or_404(User, pk=int(request.POST.get('id')))
            form = AdminPasswdChangeForm(request.POST)
            if form.is_valid():
                new_password = request.POST.get('password')
                user.set_password(new_password)
                user.save()
                ret = {'status': 'success'}
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(form.errors)
                admin_passwd_change_form_errors = re.findall(pattern, errors)
                ret = {
                    'status': 'fail',
                    'admin_passwd_change_form_errors': admin_passwd_change_form_errors[0]
                }
        return HttpResponse(json.dumps(ret), content_type='application/json')