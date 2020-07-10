from django.contrib.auth import get_user_model
import json
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
from .serializers import *

User = get_user_model()


def post_list(request,category_id=None,tag_id=None):

    # content = 'post_list category_id={category_id},tag_id = {tag_id}'.format(
    #     category_id = category_id,
    #     tag_id = tag_id
    # )
    # return HttpResponse(content=content)




    context = {
        'name':'post_list',
        'post_list':Post.objects.all(),
        'category_list':Category.objects.all(),
        'tag_list':Tag.objects.all(),

    }


    return render(request,'blog/list.html',context=context)

def post_detail(request,post_id):
    return HttpResponse('detail')


def links(request):
    return HttpResponse('links')
