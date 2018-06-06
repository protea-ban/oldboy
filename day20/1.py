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

# def test():
#     for i in range(4):
#         yield i
#
# t = test()
#
# for i in t:
#     print(i)
#
# t1 = (i for i in t)
# print(list(t1))

import time
def cal(l):
    res = 0
    start_time = time.time()
    for i in l:
        time.sleep(0.01)
        res += i
    stop_time = time.time()
    print('函数运行时间为%s'%(stop_time - start_time))
    return res

print(cal(range(100)))

def home():
    pass

def index():
    pass