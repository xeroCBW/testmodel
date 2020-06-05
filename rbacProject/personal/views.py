from django.shortcuts import render

# Create your views here.
from personal.models import WorkOrder
from rbac.models import Menu, Role
from system.models import SystemSetup
import calendar
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from django.db.models import Q
from utils.toolkit import get_month_work_order_count, get_year_work_order_count



def personalView(request):


    if request.method == 'GET':

        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        # (('0', '工单已退回'), ('1', '新建-保存'), ('2', '提交-等待审批'), ('3', '已审批-等待执行'), ('4', '已执行-等待确认'), ('5', '工单已完成'))
        # 当月个人工单状态统计
        work_order = WorkOrder.objects.filter(Q(add_time__range=(start_date, end_date)),
                                              Q(proposer_id=request.user.id) |
                                              Q(receiver_id=request.user.id) |
                                              Q(approver_id=request.user.id)
                                              )
        ret['work_order_1'] = work_order.filter(status="1").count()
        ret['work_order_2'] = work_order.filter(status="2").count()
        ret['work_order_3'] = work_order.filter(status="3").count()
        ret['work_order_4'] = work_order.filter(status="4").count()
        ret['start_date'] = start_date

        role = Role.objects.get(title='销售')
        if 'value' in request.GET and int(request.GET['value']) == 1:
            role = Role.objects.get(title='技术')
        if role:
            users = role.userprofile_set.filter(is_active=1).values('id', 'name')
            month_work_order_count = get_month_work_order_count(users, value=int(request.GET.get('value', 0)))
            year_work_order_count = get_year_work_order_count(users, value=int(request.GET.get('value', 0)))
            ret['month_work_order_count'] = month_work_order_count
            ret['year_work_order_count'] = year_work_order_count

        return render(request, 'personal/personal_index.html', ret)


    return None


def userInfoView(request):
    return None


def uploadImageView(request):
    return None


def passwdChangeView(request):
    return None


def phoneBookView(request):
    return None