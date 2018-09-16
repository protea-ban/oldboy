"""
BBS用到的Form类
"""

from blog import models
from django import forms
from django.core.exceptions import ValidationError


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length": "用户名最长16位",
            "required": "用户名不能为空",
        },
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )

    )

    password = forms.CharField(
        min_length=6,
        label="密码",
        error_messages={
            "min_length": "密码至少6位！",
            "required": "密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        )
    )

    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        error_messages={
            "min_length": "确认密码至少6位！",
            "required": "确认密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        )
    )

    email = forms.EmailField(
        label="邮箱",
        error_messages={
            "invalid": "邮箱格式不正确",
            "required": "邮箱不能为空"
        },
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"},

        )
    )

    # 重写clean方法，对确认密码进行比对
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data

    # 重写username的钩子方法，对用户名是否存在进行校验
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exist = models.UserInfo.objects.filter(username=username)

        if is_exist:
            self.add_error("username", ValidationError("用户名已存在！"))
        else:
            return username

    # 重写email的钩子方法，对邮箱是否已被注册进行校验
    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exist = models.UserInfo.objects.filter(email=email)

        if is_exist:
            self.add_error("email", ValidationError("邮箱已被注册！"))
        else:
            return email
