#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: client_非法.py 
@time: 2018/06/04
@contact: banshaohuan@163.com
@software: PyCharm  
"""  
#_*_coding:utf-8_*_
from socket import *

def client_handler(ip_port,bufsize=1024):
    tcp_socket_client=socket(AF_INET,SOCK_STREAM)
    tcp_socket_client.connect(ip_port)

    while True:
        data=input('>>: ').strip()
        if not data:continue
        if data == 'quit':break

        tcp_socket_client.sendall(data.encode('utf-8'))
        respone=tcp_socket_client.recv(bufsize)
        print(respone.decode('utf-8'))
    tcp_socket_client.close()

if __name__ == '__main__':
    ip_port=('127.0.0.1',9999)
    bufsize=1024
    client_handler(ip_port,bufsize)