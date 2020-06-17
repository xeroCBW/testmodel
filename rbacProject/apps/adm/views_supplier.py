import json
import re

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from adm.forms import EquipmentUpdateForm, EquipmentCreateForm
from adm.models import EquipmentType, Customer, Equipment, ServiceInfo, Supplier
from rbac.models import Menu
from system.models import SystemSetup
from datetime import datetime, timedelta
from django.shortcuts import render


def supplierView(request):

    if request.method == 'GET':
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/supplier.html', ret)


def supplierListView(request):
    filters = dict()
    if request.user.department_id == 9:
        filters['belongs_to_id'] = request.user.id
    ret = dict(data=list(Supplier.objects.values().filter(**filters)))
    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


def supplierDetailView(request):
    if request.method == 'GET':
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            supplier = get_object_or_404(Supplier, pk=request.GET.get('id'))
            ret['supplier'] = supplier
        users = User.objects.exclude(id=request.user.id)
        ret['users'] = users
        return render(request, 'adm/bsm/supplier_detail.html', ret)

    else:
        # res = dict(result=False)
        # if 'id' in request.POST and request.POST['id']:
        #     supplier = get_object_or_404(Supplier, pk=request.POST.get('id'))
        # else:
        #     supplier = Supplier()
        # supplier_form = SupplierForm(request.POST, instance=supplier)
        # if supplier_form.is_valid():
        #     supplier_form.save()
        #     res['result'] = True
        # return HttpResponse(json.dumps(res), content_type='application/json')
        res = {}
        if 'id' in request.POST and request.POST['id']:
            supplier = get_object_or_404(Supplier, pk=request.POST.get('id'))
            supplier_update_form = SupplierUpdateForm(request.POST, instance=supplier)
            if supplier_update_form.is_valid():
                supplier_update_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(supplier_update_form.errors)
                supplier_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'supplier_form_errors': supplier_form_errors[0]
                }

        else:
            supplier = Supplier()
            supplier_create_form = SupplierCreateForm(request.POST, instance=supplier)
            if supplier_create_form.is_valid():
                supplier_create_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(supplier_create_form.errors)
                supplier_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'supplier_form_errors': supplier_form_errors[0]
                }
        return HttpResponse(json.dumps(res), content_type='application/json')



def supplierDeleteView(request):
    if request.method == 'POST':
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Supplier.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')
