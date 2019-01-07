#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: s1.py 
@time: 2019/01/07
@software: PyCharm  
"""

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

@Request.application
def hello(request):
    return Response('Hello World')


if __name__ == '__main__':

    run_simple("localhost", 4000, hello)
