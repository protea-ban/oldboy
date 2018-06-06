#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 验证功能装饰器.py 
@time: 2018/05/03
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

user_list = [
    {'name':'alex', 'passwd':'123'},
    {'name':'linhaifeng', 'passwd':'123'},
    {'name':'wupeiqi', 'passwd':'123'},
    {'name':'yuanhao', 'passwd':'123'}
]

current_dic = {'username':None, 'login':False}

def auth_func(func):
    def wrapper(*args, **kwargs):
        if current_dic['username'] and current_dic['login']:
            res = func(*args, **kwargs)
            return res
        username = input('用户名：').strip()
        passwd = input('密码：').strip()
        for user_dic in user_list:
            if username == user_dic['name'] and passwd == user_dic['passwd']:
                current_dic['username'] = username
                current_dic['login'] = True
                res = func(*args, **kwargs)
                return res
        else:
            print('用户名或密码错误')
    return wrapper

@auth_func
def index():
    print('欢迎来到京东主页')

@auth_func
def home(name):
    print('欢迎回家%s' %name)

@auth_func
def shopping_car(name):
    print('%s的购物车有[%s, %s, %s]'%(name,'奶茶','妹妹', '娃娃'))

index()
home('ban')
shopping_car('ban')