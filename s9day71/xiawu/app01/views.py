from django.shortcuts import render, redirect

# 导入用于装饰器修复技术的包
from functools import wraps
# Create your views here.


# 装饰器函数，用来判断是否登录
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="ban")
        if ret == "1":
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            next_url = request.path_info
            return redirect("/app01/login/?next={}".format(next_url))
    return inner


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        next_url = request.GET.get("next")

        if username == "alex" and pwd == "dsb":
            # return redirect("/home/")
            # 服务器返回的响应对象

            # 通过URL中的next参数指定跳转的页面，如果为空，默认跳转到home页面
            if next_url:
                rep = redirect(next_url)
            else:
                print("ban")
                rep = redirect("/app01/home/")

            # 1. 设置cookie
            # rep.set_cookie("is_login", "1")

            # 2. 设置加盐cookie,max_age是cookie的生存时间
            rep.set_signed_cookie("is_login", "1", salt="ban", max_age=100)
            return rep

    return render(request, "app01/login.html")


def home(request):
    # 获取cookie并判断
    # if request.COOKIES.get("is_login", 0) == "1":
    # 获取加盐cookie并判断
    ret = request.get_signed_cookie("is_login", default="0", salt="ban")
    if ret == "1":
        return render(request, "app01/home.html")
    else:
        return redirect("/app01/login/")


# 注销函数
def logout(request):
    # 删除cookie,操作的是响应对象，最后需要返回
    rep = redirect("/app01/login/")
    rep.delete_cookie("is_login")
    return rep


@check_login
def index(request):
    return render(request, "app01/index.html")
