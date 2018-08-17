from django.shortcuts import render, redirect

# 导入用于装饰器修复技术的包
from functools import wraps
# Create your views here.

"""
session会用到数据库，所以使用之前需要初始化数据库，
即执行makemigrations migrate

1. 设置session
2. 获取session
3. 删除session
"""


# 装饰器函数，用来判断是否登录
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        # 1. 获取cookie中的随机字符串
        # 2. 根据随机字符串去数据库取 session_data --> 解密 --> 反序列化成字典
        # 3. 在字典里面 根据 is_login 取具体的数据

        if ret == "1":
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            next_url = request.path_info
            return redirect("/app02/login/?next={}".format(next_url))
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
                rep = redirect("/app02/home/")

            # 设置session
            request.session["is_login"] = "1"
            request.session["name"] = username

            # 设置session7秒后失效
            # request.session.set_expiry(7)

            return rep

    return render(request, "app02/login.html")


@check_login
def home(request):
    # 获取从session中设置的值
    user = request.session.get("name")
    return render(request, "app02/home.html", {"user": user})


# 注销函数
def logout(request):
    # 只删除session数据
    # request.session.delete()

    # 删除session数据和cookie
    request.session.flush()

    return redirect("/app02/login/")


@check_login
def index(request):
    return render(request, "app02/index.html")
