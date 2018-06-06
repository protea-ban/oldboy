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
# import socket
from socket import *
ip_port=('192.168.83.128',8080)
back_log=5
buffer_size=1024

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    print('服务端开始运行了')
    conn,addr=tcp_server.accept() #服务端阻塞
    print('双向链接是',conn)
    print('客户端地址',addr)

    while True:
        try:
            data=conn.recv(buffer_size)
            print('客户端发来的消息是',data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            break
    conn.close()

tcp_server.close()

