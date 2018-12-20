from django.shortcuts import render, HttpResponse
from crm import models
from rbac.service.permission import *
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["pwd"]
        user_obj = models.UserInfo.objects.filter(name=username, password=pwd).first()

        # 登录用户存在
        if user_obj:

            # 将用户ID存入session
            request.session["user_id"] = user_obj.pk

            # 查询当前登录用户的所有权限，注册到session中
            initial_session(user_obj, request)

            return HttpResponse("登录成功！")

    return render(request, "login.html")
