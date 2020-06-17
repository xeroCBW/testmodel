from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required

def loginView(request):

    # 设置基本数据
    if request.method == 'GET':

        if not request.user.is_authenticated:
            return render(request,'system/users/login.html')
        else:
            return redirect('/')
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
                else:
                    msg='用户未激活'
            else:
                msg = '用户名或密码错误'
        else:
            msg = '用户和密码不能为空！'
        return render(request,'system/users/login.html',locals())


def logoutView(request):

    logout(request)

    return redirect('/')


@login_required(login_url='/login')
def indexView(request):

    return render(request,'index.html')


@login_required(login_url='/login')
def systemView(request):

    return render(request,'system/system_index.html')

