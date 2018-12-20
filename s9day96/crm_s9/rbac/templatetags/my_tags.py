#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: my_tags.py 
@time: 2018/10/27
@software: PyCharm  
"""  
from django import template

register = template.Library()

@register.inclusion_tag("menu.html")
def get_menu(request, ):
    menu_permission_list = request.session["menu_permission_list"]

    return {"menu_permission_list": menu_permission_list}
