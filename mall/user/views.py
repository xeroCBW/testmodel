from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# 前面加/user 是绝对路径
def loginView(request):

    title = '登录'

    unit_2 = '/user/register/'
    unit_2_name = '立即注册'

    unit_1 = '/user/setpassword/'
    unit_1_name = '修改密码'

    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    return render(request, 'user.html', locals())


def logoutView(request):

    logout(request)
    return redirect('/')

def registerView(request):

    title = '注册'
    unit_2 = '/user/login'
    unit_2_name = '立即登录'
    unit_1 = '/user/setpassword'
    unit_1_name = '修改密码'

    if request.method == 'GET':
        return render(request,'user.html',locals())
    else:
        user_name = request.POST['username']
        pass_word = request.POST['password']

        if User.objects.filter(username=user_name):
            tips = '用户已经存在'
        else:
            user = User.objects.create_user(username=user_name,password=pass_word)
            tips = '注册成功,请登录'
            user.save()
        return render(request,'user.html',locals())


def setpasswordView(request):

    title = '修改密码'
    unit_2 = '/user/login'
    unit_2_name = '立即登录'
    unit_1 = '/user/register'
    unit_1_name = '立即注册'
    new_password = True

    if request.method == 'POST':
        # 如果没有获取就为空(进行默认填充)
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            # 判断用户的账号密码是否正确
            if user:
                user.set_password(new_password)
                user.save()
                tips = '密码修改成功'
            else:
                tips = '原始密码不正确'
        else:
            tips = '用户不存在'

    return render(request, 'user.html', locals())






