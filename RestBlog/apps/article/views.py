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

    category = None
    tag = None

    if category_id:
        post_list,category = Post.get_by_category(category_id)
    elif tag_id:
        post_list,tag = Post.get_by_tag(tag_id)
    else:
        post_list = Post.objects.all()

    context = {
        'name':'post_list',
        'post_list':post_list,
        'category':category,
        'tag':tag,
    }
    context.update(Category.get_navs())
    return render(request,'blog/list.html',context=context)

def post_detail(request,post_id):

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post':post
    }

    context.update(Category.get_navs())

    return render(request,'blog/detail.html',context=context)

def links(request):
    return HttpResponse('links')
