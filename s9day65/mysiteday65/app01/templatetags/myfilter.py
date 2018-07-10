#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: myfilter.py 
@time: 2018/07/08
@software: PyCharm  
"""  
from django import template
register = template.Library()

@register.filter(name="addstr")
def add_str(arg, arg1):
    return f'{arg} is {arg1}.'

@register.inclusion_tag(filename='results.html')
def show_ul(n):
    n = 1 if n < 1 else int(n)
    results = [f'这是第{i}项' for i in range(1, n+1)]
    return {"results":results}