"""admindemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render, HttpResponse

def my_view(request):
    return HttpResponse("my_view")


def my_change(request, id):
    return HttpResponse("my_change")

def my_delete(request, id):
    return HttpResponse("my_delete")

# 返回第二级url内容，即操作
def get_urls2():
    temp = []
    temp.append(url(r'^$', my_view))
    temp.append(url(r'^(\d+)/change/$', my_change))
    temp.append(url(r'^(\d+)/delete/$', my_delete))

    return temp

# 返回一级url的函数
def get_urls():
    temp = []

    # admin.site._registry {Book:modelAdmin(Book)},存储model类对象和admin类
    for model, admin_class_obj in admin.site._registry.items():

        # model对象对应的app名
        app_name = model._meta.app_label
        # model对象名
        model_name = model._meta.model_name

        # 在此处进行第二级url拼接
        temp.append(url(r'^{0}/{1}/'.format(app_name, model_name), (get_urls2(), None, None)))

    return temp

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Xadmin的URL由两级组成，第一级为app_name/model_name，第二级为操作
    url(r'^Xadmin/',(get_urls(), None, None))
]
