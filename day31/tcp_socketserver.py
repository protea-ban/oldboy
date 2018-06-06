#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: tcp_socketserver.py 
@time: 2018/06/01
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
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is:', self.request)
        print('addr is:', self.client_address)

        while True:
            try:
                # 收消息
                data = self.request.recv(1024)
                if not data:break
                print('收到客户端的消息是',data, self.client_address)

                # 发消息
                self.request.sendall(data.upper())

            except Exception  as e:
                print(e)
                break


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)  #多线程

    print(s.server_address)
    print(s.RequestHandlerClass)
    print(MyServer)
    print(s.socket)
    print(s.server_address)
    s.serve_forever()
