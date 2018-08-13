#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: urls.py 
@time: 2018/07/24
@software: PyCharm  
"""  
from django.conf.urls import url
from app02 import views

urlpatterns = [
    # 原先的url形式
    # url(r'^home/', views.home),
    # 起别名
    # url(r'^home/', views.home, name="house_home"),
    # 有命名空间时，别名可以重复
    url(r'^home/', views.home, name="home"),
]