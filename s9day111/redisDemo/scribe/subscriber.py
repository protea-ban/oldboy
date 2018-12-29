#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
