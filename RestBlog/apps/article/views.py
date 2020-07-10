from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .serializers import *

User = get_user_model()


def post_list(request,category_id=None,tag_id=None):

    # content = 'post_list category_id={category_id},tag_id = {tag_id}'.format(
    #     category_id = category_id,
    #     tag_id = tag_id
    # )
    # return HttpResponse(content=content)



    

    return render(request,'blog/list.html',context={'name':'post_list'})

def post_detail(request,post_id):
    return HttpResponse('detail')


def links(request):
    return HttpResponse('links')
