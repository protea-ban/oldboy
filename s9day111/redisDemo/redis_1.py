#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: redis_1.py 
@time: 2018/12/27
@software: PyCharm  
"""  
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))

