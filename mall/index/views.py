from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render,redirect

from index.forms import ProductModelForm
from .models import *
from django.contrib.auth import login,logout,authenticate



def indexView(request):

    type_list = Type.objects.values('type_name').distinct()
    name_list = Product.objects.values('name','type__type_name')
    title = '首页'


    product = request.GET.get('product', '')
    price = request.GET.get('price', '')
    if product:
        # 获取存储在Session的数据，如果Session不存在product_info，则返回一个空列表
        product_list = request.session.get('product_info', [])
        # 判断当前请求参数是否已存储在Session
        if not product in product_list:
            # 将当前参数存储在列表product_list
            product_list.append({'price': price, 'product': product})
        # 更新存储在Session的数据
        request.session['product_info'] = product_list
        return redirect('/')

    return render(request, 'index.html',locals())


@login_required(login_url = '/user/login')
def shoppingCarView(request):
    # 获取存储在Session的数据，如果Session不存在product_info，则返回一个空列表
    product_list = request.session.get('product_info', [])
    # 获取GET请求参数，如果没有请求参数，返回空值
    del_product = request.GET.get('product', '')
    # 判断是否为空，若非空，删除Session里的商品信息


    print(product_list)
    print(del_product)

    if del_product:
        # 删除Session里某个商品数据
        for i in product_list:
            if i['product'] == del_product:
                product_list.remove(i)
        # 将删除后的数据覆盖原来的Session
        request.session['product_info'] = product_list
        return redirect('/shoppingCar')
    return render(request, 'shoppingCar.html', locals())


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


def paginationView(request,page):

    product_list = Product.objects.all()
    paginator = Paginator(product_list,3)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page的数据类型不是整型，则返回第一页数据
        pageInfo = paginator.page(1)
    except EmptyPage:
        # 用户访问的页数大于实际页数，则返回最后一页的数据
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'pagination.html', locals())