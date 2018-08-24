from django.shortcuts import render, HttpResponse
from app01 import models
from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your views here.


def register(request):
    return render(request, "register.html")


def check_user(request):
    check_name = request.POST.get("name")
    ret = models.UserInfo.objects.filter(name=check_name)
    if ret:
        msg = "用户名已被注册！"
    else:
        msg = "用户名可用！"

    return HttpResponse(msg)


# Django Form组件的使用
class RegForm(forms.Form):
    name = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="用户名",
        error_messages={
            "required": "该字段不能为空",
        },
        # widget控制的是生成HTML代码相关的规则
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )
    pwd = forms.CharField(
        label="密码",
        min_length=6,
        max_length=10,
        # render_value=True 提交后输入框内容依然存在
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空！"
        }
    )
    re_pwd = forms.CharField(
        label="确认密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空！"
        }
    )
    email = forms.EmailField(
        label="邮箱",
        widget=widgets.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空"
        }
    )
    mobile = forms.CharField(
        label="手机",
        # 自己定制校验规则
        validators=[
            RegexValidator(r'^[0-9]+$',"手机号必须是数字"),
            RegexValidator(r'^1[3-9][0-9]{9}$', "手机格式不正确")
        ],
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空"
        }
    )
    city = forms.ChoiceField(
        choices=models.City.objects.all().values_list("id", "name"),
        label="所在城市",
        initial=1,
        widget=widgets.Select(attrs={"class": "form-control"})
    )

    # 重写父类的初始化方法, 每次实例化类的时候都调用
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 每次实例化类的时候都重新给choices赋值，保证更新数据库时数据同步更新
        self.fields["city"].widget.choices = models.City.objects.all().values_list("id", "name")

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if "中国" in name:
            raise ValidationError("不要脸")
        return name

    # 重写父类的clean方法，进行自定义校验
    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd != re_pwd:
            self.add_error("re_pwd", ValidationError("两次密码不一致！"))
            # raise ValidationError("两次密码不一致")
        return self.cleaned_data


def reg(request):
    form_obj = RegForm()

    # 填写表单提交时，重新赋值form对象
    if request.method == "POST":
        # 更新form_obj的内容
        form_obj = RegForm(request.POST)
        # form自己可以做校验
        if form_obj.is_valid():
            # 1. form_obj.cleaned_data存储form校验后的内容，需要在is-valid函数后使用
            del form_obj.cleaned_data["re_pwd"]
            # 存储到数据库中
            models.UserInfo.objects.create(**form_obj.cleaned_data)
            return HttpResponse("恭喜！注册成功")
    return render(request, "reg.html", {"form_obj": form_obj})

