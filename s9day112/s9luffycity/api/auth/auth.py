#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: auth.py 
@time: 2018/12/16
@software: PyCharm  
"""  
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

# 登录认证
class LufyyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserToken.objects.filter(token=token).first()

        if not obj:
            raise AuthenticationFailed({'code':1001, 'error':'认证失败'})

        return (obj.user.user, obj)