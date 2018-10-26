from django.shortcuts import render, HttpResponse
from rbac import models
import re
from rbac.service.permission import *


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["pwd"]
        user_obj = models.User.objects.filter(name=username, pwd=pwd).first()

        # 登录用户存在
        if user_obj:

            # 将用户ID存入session
            request.session["user_id"] = user_obj.pk

            # 查询当前登录用户的所有权限，注册到session中
            initial_session(user_obj, request)

            return HttpResponse("登录成功！")

    return render(request, "login.html")


def users(request):

    users_list = models.User.objects.all()

    return render(request, "users.html", {"users_list": users_list})


def add_user(request):
    return HttpResponse("添加用户")


def edit_user(request, id):
    return HttpResponse("编辑用户")


def roles(request):

    roles_list = models.Role.objects.all()

    return render(request, "roles.html", {"roles_list": roles_list})


def add_roles(request):
    return HttpResponse("添加角色")
