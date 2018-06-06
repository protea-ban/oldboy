#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 利用描述符自定制property.py 
@time: 2018/05/24
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
class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        res = self.func(instance)
        return res

class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    @Lazyproperty
    def area(self):
        return self.length * self.width


r1 = Room('ban', 2, 2)
print(r1.area)  # 此处想要运行就得是r1.area，而不能是r1.area()
print(r1.__dict__)