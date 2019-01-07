#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: s1.py 
@time: 2019/01/07
@software: PyCharm  
"""

from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello():
    return "Hello World"


if __name__ == '__main__':

    app.run()
