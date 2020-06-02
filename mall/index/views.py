from django.shortcuts import render

# Create your views here.
def indexView(request):

    # 设置基本数据
    return render(request,'index.html',locals())