from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from functools import wraps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


# def check_login(f):
#     @wraps(f)
#     def inner(request, *args, **kwargs):
#         if request.session.get("is_login") == "1":
#             return f(request, *args, **kwargs)
#         else:
#             return redirect('/login/')
#     return inner


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = models.User.objects.filter(username=username, password=password)
#
#         if user:
#             request.session["is_login"] = "1"
#             request.session["user_id"] = user[0].id
#
#             return redirect('/index/')
#     return render(request, "login.html")
#
#
# @check_login
# def index(request):
#     user_id = request.session.get("user_id")
#     user = models.User.objects.filter(id=user_id)
#
#     return render(request, "index.html", {"user": user[0]})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)

            return redirect('/index/')
    return render(request, "login.html")


@login_required
def index(request):
    return render(request, "index.html", {"user": request.user})


def logout(request):
    auth.logout(request)
    return redirect("/login/")


# def reg(request):
#     # 创建用户
#     user_obj = User.objects.create_user(username="ban2", password="ban111111")
#
#     # 修改密码
#     user_obj.set_password("ban222222")
#     user_obj.save()
#
#     return HttpResponse("O98k")


def reg(request):
    # 创建用户
    user_obj = models.UserInfo.objects.create_user(username="ban3", password="ban333333")

    # # 修改密码
    # user_obj.set_password("ban222222")
    # user_obj.save()

    return HttpResponse("O98k")
