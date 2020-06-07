from django.http import HttpResponse
from django.shortcuts import render,redirect

from index.forms import ProductModelForm
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def indexView(request):

    type_list = Type.objects.values('type_name').distinct()
    name_list = Product.objects.values('name','type__type_name')
    # 设置首页信息
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html',context=context, status=200)


def shoppingCarView(request):

    # 返回购物车

    return render(request,'shopoingCar.html',locals())


def productAddView(request):

    if request.method == 'GET':

        product = ProductModelForm()

        return render(request,'data_form.html',locals())

    else:

        product = ProductModelForm(request.POST)
        if product.is_valid():
            product.save()
            return HttpResponse('提交成功')
        else:
            # 这里会将product传出去
            return render(request,'data_form.html',locals())

