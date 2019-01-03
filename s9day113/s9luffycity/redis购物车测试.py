#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: redis购物车测试.py 
@time: 2018/12/31
@software: PyCharm  
"""  
import redis
import json

conn = redis.Redis(host='127.0.0.1',port=6379)
title = conn.hget('luffy_shopping_car_1_1', "title")
title_str = title.decode("utf-8")
print(title_str)
