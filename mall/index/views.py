from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def indexView(request):

    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    # 设置首页信息
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}

    return render(request, 'index.html',context=context, status=200)


def shoppingCarView(request):

    # 返回购物车

    return render(request,'shopoingCar.html',locals())


def loginView(request):

    return None


def logoutView(request):


    logout(request)

    return redirect('/')