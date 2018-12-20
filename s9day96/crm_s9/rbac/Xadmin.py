#!/usr/bin/env python  
#-*- coding:utf-8 -*-  


from Xadmin.service.Xadmin import site
from .models import *
from Xadmin.service.Xadmin import ModelXadmin


site.register(User)
site.register(Role)


class PermissionConfig(ModelXadmin):
    list_display = ["id", "title", "url", "group", "action"]


site.register(Permission, PermissionConfig)
site.register(PermissionGroup)
