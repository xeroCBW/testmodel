from django.shortcuts import render
from .models import *
from .form import *
from django.http import HttpResponse

# Create your views here.
def indexView(request):


    if request.method == 'GET':

        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:

        product = ProductForm(request.POST)
        if product.is_valid():
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request,'data_form.html',locals())


def mode_indexView(request):

    

    return render(request,'data_form.html')