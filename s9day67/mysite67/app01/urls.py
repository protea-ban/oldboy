#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: urls.py 
@time: 2018/07/24
@software: PyCharm  
"""  
from django.conf.urls import url
from app01 import views

urlpatterns = [
    # url(r'^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book),
    url(r'^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book, name="book"),
    # 原先的url形式
    # url(r'^home/', views.home)
    # 给url起别名
    # url(r'^home/', views.home, name="car_home")
    # 有命名空间时，别名可以重复
    url(r'^home/', views.home, name="home")
]