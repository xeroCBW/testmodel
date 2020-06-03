from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login')
def structureView(request):

    return render(request,'system/structure/structure-list.html')


def structureListView(request):
    return None


def structureAddUserView(request):
    return None


def structureDetailView(request):
    return None


def structureDeleteView(request):
    return None