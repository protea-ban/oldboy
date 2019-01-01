#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: response.py 
@time: 2018/12/31
@software: PyCharm  
"""  

class BaseResponse(object):
    """
    响应体基础类
    """

    def __init__(self):
        self.data = None
        self.code = 1000
        self.error = None

    @property
    def dict(self):
        return self.__dict__
