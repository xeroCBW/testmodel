import json
import re

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import HttpResponse

from adm.models import Customer
from personal.forms import WorkOrderCreateForm, WorkOrderUpdateForm
from personal.models import WorkOrderRecord, WorkOrder
from rbac.models import Menu, Role
from django.shortcuts import render, redirect, get_object_or_404

from utils.toolkit import ToolKit, SendMessage


def workOrderView(request):

    ret = Menu.getMenuByRequestUrl(url=request.path_info)
    status_list = []
    filters = dict()
    for work_order_status in WorkOrder.status_choices:
        status_dict = dict(item=work_order_status[0], value=work_order_status[1])
        status_list.append(status_dict)
    if request.user.department_id == 9:  # 销售部门只能看自己的设备信息
        filters['belongs_to_id'] = request.user.id
    customers = Customer.objects.filter(**filters).order_by('unit')
    ret['status_list'] = status_list
    ret['customers'] = customers
    return render(request, 'personal/workorder/workorder.html', ret)



def wrkOrderListView(request):
    fields = ['id', 'number', 'title', 'type', 'status', 'do_time', 'customer__unit', 'proposer__name']
    filters = dict()
    if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_Icrt/':
        filters['proposer_id'] = request.user.id
    if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_app/':
        filters['approver_id'] = request.user.id
        filters['status__in'] = ['0', '2', '3', '4', '5']  # 审批人视图可以看到的工单状态
    if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_rec/':
        filters['receiver_id'] = request.user.id
    if 'number' in request.GET and request.GET['number']:
        filters['number__icontains'] = request.GET['number']
    if 'workorder_status' in request.GET and request.GET['workorder_status']:
        filters['status'] = request.GET['workorder_status']
    if 'customer' in request.GET and request.GET['customer']:
        filters['customer_id'] = request.GET['customer']
    ret = dict(data=list(WorkOrder.objects.filter(**filters).values(*fields).order_by('-add_time')))

    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


def workOrderCreateView(request):

    if request.method == 'GET':
        type_list = []
        filters = dict()
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:  # 新建工单时销售部门只能选择自己的用户信息
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        try:
            number = WorkOrder.objects.latest('number').number
        except WorkOrder.DoesNotExist:
            number = ""
        new_number = ToolKit.bulidNumber('SX', 9, number)
        ret = {
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
            'new_number': new_number
        }
        return render(request, 'personal/workorder/workorder_create.html', ret)
    else:
        res = dict()
        work_order = WorkOrder()
        work_order_form = WorkOrderCreateForm(request.POST, instance=work_order)
        if work_order_form.is_valid():
            work_order_form.save()
            res['status'] = 'success'
            if work_order.status == "2":
                res['status'] = 'submit'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'submit_send'
                except Exception:
                    pass
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(work_order_form.errors)
            work_order_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'work_order_form_errors': work_order_form_errors[0]
            }
        return HttpResponse(json.dumps(res), content_type='application/json')


def workOrderDetailView(request):

    if request.method == 'GET':
        ret = dict()
        admin_user_list = []
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
            work_order_record = work_order.workorderrecord_set.all().order_by('add_time')
            try:
                role = Role.objects.get(title="管理")
                admin_user_ids = role.userprofile_set.values('id')
                for admin_user_id in admin_user_ids:
                    admin_user_list.append(admin_user_id['id'])
            except Exception:
                pass
            user_list = [work_order.proposer_id, work_order.approver_id, work_order.receiver_id]
            user_list.extend(admin_user_list)

            # 和工单无关联的用户禁止通过手动指定ID的形式非法获取数据
            if request.user.id in user_list:
                ret['work_order'] = work_order
                ret['work_order_record'] = work_order_record
            else:
                ret['ban'] = 'ban'
        return render(request, 'personal/workorder/workorder_detail.html', ret)


def workOrderDeleteView(request):
    if request.method == 'POST':
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            status = get_object_or_404(WorkOrder, pk=request.POST['id']).status
            if int(status) <= 1:
                id_list = map(int, request.POST.get('id').split(','))
                WorkOrder.objects.filter(id__in=id_list).delete()
                ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


def workOrderUpdateView(request):
    if request.method == 'GET':
        type_list = []
        filters = dict()
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        ret = {
            'work_order': work_order,
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
        }
        return render(request, 'personal/workorder/workorder_update.html', ret)

    else:
        res = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.POST['id'])
        work_order_form = WorkOrderUpdateForm(request.POST, instance=work_order)
        if int(work_order.status) <= 1:
            if work_order_form.is_valid():
                work_order_form.save()
                res['status'] = 'success'
                if work_order.status == "2":
                    res['status'] = 'submit'
                    try:
                        SendMessage.send_workorder_email(request.POST['number'])
                        res['status'] = 'submit_send'
                    except Exception:
                        pass
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(work_order_form.errors)
                work_order_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'work_order_form_errors': work_order_form_errors[0]
                }
        else:
            res['status'] = 'ban'
        return HttpResponse(json.dumps(res), content_type='application/json')




def wrokOrderSendView(request):
    return None


def workOrderExecuteView(request):
    return None


def workOrderFinishView(request):
    return None


def workOrderUploadView(request):
    return None


def workOrderReturnView(request):
    return None


def workOrderProjectUploadView(request):
    return None


def workOrderDocumentView(request):
    if request.method == 'GET':
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        return render(request, 'personal/workorder/document.html', ret)



def workOrderDocumentListView(request):

    fields = ['work_order__number', 'work_order__customer__unit', 'name__name', 'add_time', 'file_content']
    ret = dict(data=list(WorkOrderRecord.objects.filter(~Q(file_content='')).values(*fields).order_by('-add_time')))

    return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')
