from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.

# 登录用的函数
def login(request):
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        # print(email, pwd)
        if email == "banshaohuan@163.com" and pwd == "banshaohuan":
            return redirect("https://www.cnblogs.com/banshaohuan/")
        else:
            error_msg = "邮箱或密码错误"

    return render(request, "login.html", {"error":error_msg})

# 展示所有用户信息列表的函数
def user_list(request):
    # 利用ORM去查询数据库，得到数据
    ret = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'user_list':ret})

# 添加用户的函数
def add_user(request):
    if request.method == 'POST':
        ret = request.POST.get('username')
        models.UserInfo.objects.create(name=ret)
        return redirect('/user_list/')
    return render(request, 'add_user.html')

