from django.shortcuts import render, HttpResponse
from rbac import models
import re
from rbac.service.permission import *

class Per(object):
    def __init__(self, actions):
        self.actions = actions

    def add(self):
        return "add" in self.actions

    def delete(self):
        return "delete" in self.actions

    def edit(self):
        return "edit" in self.actions

    def list(self):
        return "list" in self.actions

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
    id = request.session.get("user_id")
    user = models.User.objects.filter(id=id).first()
    permission_list = request.session.get("permission_list")
    # actions = request.session.get("actions")
    per = Per(request.actions)
    # menu_permission_list = request.session["menu_permission_list"]
    return render(request, "users.html", locals())


def add_user(request):
    return HttpResponse("添加用户")


def delete_user(request, id):
    return HttpResponse("删除用户"+id)


def edit_user(request, id):
    return HttpResponse("编辑用户"+id)


def roles(request):
    id = request.session.get("user_id")
    user = models.User.objects.filter(id=id).first()
    roles_list = models.Role.objects.all()
    per = Per(request.actions)
    # menu_permission_list = request.session["menu_permission_list"]
    return render(request, "roles.html", locals())


def add_roles(request):
    return HttpResponse("添加角色")


def delete_roles(request, id):
    return HttpResponse("删除角色"+id)


def edit_roles(request, id):
    return HttpResponse("编辑角色"+id)
