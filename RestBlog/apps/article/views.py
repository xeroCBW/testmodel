from django.contrib.auth import get_user_model
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Post,SliderBar
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
        'slidebars':SliderBar.get_all(),
    }

    context.update(Category.get_navs())
    return render(request,'blog/list.html',context=context)

def post_detail(request,post_id):

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post':post,
        'slidebars': SliderBar.get_all(),
    }

    context.update(Category.get_navs())

    return render(request,'blog/detail.html',context=context)

def links(request):
    return HttpResponse('links')


class CommonViewMixin:

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'slidebars': SliderBar.get_all(),
            }
        )
        context.update(Category.get_navs())

        return context

class IndexView(CommonViewMixin,ListView):

    queryset = Post.lastest_post()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


