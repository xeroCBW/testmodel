from django.shortcuts import render
from .models import *
# Create your views here.
def indexView(request):

    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    # 设置首页信息
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html',context=context, status=200)