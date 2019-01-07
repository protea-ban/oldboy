#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: s1.py 
@time: 2019/01/07
@software: PyCharm  
"""

class Foo(object):

    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')

obj = Foo()
obj()
