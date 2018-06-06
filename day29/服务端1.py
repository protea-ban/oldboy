#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: 服务端1.py
@time: 2018/05/26
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
from socket import *

phone = socket(AF_INET, SOCK_STREAM)
phone.bind(('127.0.0.1', 8000))
phone.listen(5)
print('===>')
conn, addr = phone.accept()

msg = conn.recv(1024)
print('客户端发来的信息是：', msg)
conn.send(msg.upper())

conn.close()
phone.close()