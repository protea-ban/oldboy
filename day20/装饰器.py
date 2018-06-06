#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 1.py 
@time: 2018/04/29
@contact: banshaohuan@163.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import time
def timer(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('time of the program is %s' %(stop_time - start_time))
        return res
    return wapper
        





@timer
def cal(l):
    res = 0
    for i in l:
        time.sleep(0.01)
        res += i
    return res

# print(cal(range(100)))

def test1():
    for i in range(3):
        if i > 4:
            print(i)
            return 0
    else:
        print('this is a test')

test1()
