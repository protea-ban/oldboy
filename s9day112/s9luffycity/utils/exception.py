#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: exception.py 
@time: 2018/12/31
@software: PyCharm  
"""  


class PricePolicyInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg
