#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: s1.py 
@time: 2019/01/07
@software: PyCharm  
"""

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

def run(environ, strat_response):
    return [b"asdf"]


if __name__ == '__main__':

    run_simple("localhost", 4000, run)
