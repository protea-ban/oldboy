#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: views.py 
@time: 2018/07/01
@software: PyCharm  
"""  
from django.shortcuts import HttpResponse, render, redirect

def yimi(request):
    return HttpResponse("hello yimi!")

def xiaohei(request):
    return HttpResponse("hello xiaohei! 你可真黑啊")

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

def baobao(request):
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)
    # print(email, pwd)
    if email == "banshaohuan@163.com" and pwd == "banshaohuan":
        return HttpResponse("登录成功")
    else:
        return HttpResponse("登录失败")