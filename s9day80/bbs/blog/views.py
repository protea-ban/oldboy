from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from blog import forms, models
from geetest import GeetestLib
from django.http import JsonResponse
from django.db.models import Count
# Create your views here.


def index(request):
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username)
#         user = auth.authenticate(username=username, password=password)
#
#         if user:
#             auth.login(request, user)
#
#             return redirect('/index/')
#
#     return render(request, "login.html")


def login(request):
    # if request.is_ajax():  # 如果是AJAX请求
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login2.html")


def logout(request):
    auth.logout(request)
    return redirect('/index/')

# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


# 处理极验 获取验证码的视图
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def register(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)

        if form_obj.is_valid():

            # 校验通过，在数据库中创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            return JsonResponse(ret)

    form_obj = forms.RegForm()
    return render(request, "register.html", {"form_obj": form_obj})


def check_username_exist(request):
    ret = {"status": "", "msg": ""}
    username = request.GET.get("username")
    is_exist = models.UserInfo.objects.filter(username=username)

    if is_exist:
        ret["status"] = 1
        ret["msg"] = "用户名已经存在！"

    return JsonResponse(ret)


def home(request, username):
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("home404")

    blog = user.blog

    article_list = models.Article.objects.filter(user=user)
    # # category_list = models.Category.objects.filter(blog=blog)
    # # 按文章分类统计
    # category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    #
    # # 按标签统计
    # tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    #
    # # 按日期归档
    # archive_list = models.Article.objects.filter(user=user).extra(
    #     select={"archive_ym": "date_format(create_time, '%%Y-%%m')"}
    # ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    return render(request, "home.html", {
        "username": username,
        "blog": blog,
        "article_list": article_list,
    })


def article_detail(request, username, pk):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    if not user:
        return HttpResponse(username)

    article_obj = models.Article.objects.filter(pk=pk).first()
    comment_list = models.Comment.objects.filter(article_id=pk)

    return render(
        request,
        "article_detail.html",
        {
            "username": username,
            "blog": blog,
            "article": article_obj,
            "comment_list": comment_list,
        }
    )


import json
from django.db.models import F

def up_down(request):
    article_id = request.POST.get("article_id")
    user = request.user
    is_up = json.loads(request.POST.get("is_up"))

    data = {"status": True}
    try:
        models.ArticleUpDown.objects.create(article_id=article_id, user=user, is_up=is_up)
        models.Article.objects.filter(pk=article_id).update(up_count=F("up_count")+1)

    except Exception:
        data["status"] = False
        data["first_action"] = models.ArticleUpDown.objects.filter(article_id=article_id, user=user).first().is_up

    return JsonResponse(data)


def comment(request):
    print(request.POST)

    pid = request.POST.get("pid")
    article_id = request.POST.get("article_id")
    content = request.POST.get("content")
    user_pk = request.user.pk
    response = {}

    # 根评论
    if not pid:
        comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_pk, content=content)
    else:
        comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_pk, content=content, parent_comment_id=pid)

    response["content"] = comment_obj.content
    # 时间对象不可由json序列化，转成字符串即可
    response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %H:%M")
    response["username"] = comment_obj.user.username

    return JsonResponse(response)


def comment_tree(request, article_id):

    ret = list(models.Comment.objects.filter(article_id=article_id).values("pk", "parent_comment_id", "content", "user__username", "create_time"))
    return JsonResponse(ret, safe=False)
