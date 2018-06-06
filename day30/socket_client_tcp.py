#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: socket_client_tcp.py 
@time: 2018/05/28
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
# from socket import *
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
#
# tcp_client = socket(AF_INET, SOCK_STREAM)
# tcp_client.connect(ip_port) #=> 服务端是绑定ip_port，而客户端是连接，connect
#
# #=> 用到while True的时候考虑好break和continue的条件
# while True:
#     cmd = input('>>:').strip()
#     if not cmd:continue
#     if cmd == 'quit':break
#
#     tcp_client.send(cmd.encode('utf-8'))    #=> 发送时同样要encode
#     cmd_res = tcp_client.recv(buffer_size)  #=> 客户端、服务端接收时只需要传入buffer_size
#     print('命令执行的结果是', cmd_res.decode('gbk')) #=> 收到的数据必须decode，而且要与encode时的编码一致
#
# tcp_client.close()#=>最后要关闭连接

# low版解决粘包
# from socket import *
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
#
# tcp_client = socket(AF_INET, SOCK_STREAM)
# tcp_client.connect(ip_port) #=> 服务端是绑定ip_port，而客户端是连接，connect
#
# #=> 用到while True的时候考虑好break和continue的条件
# while True:
#     cmd = input('>>:').strip()
#     if not cmd:continue
#     if cmd == 'quit':break
#
#     tcp_client.send(cmd.encode('utf-8'))    #=> 发送时同样要encode
#
#     # 解决粘包
#     length = tcp_client.recv(buffer_size)  #=>从服务端接收到返回内容的长度
#     print('========>', length)
#     tcp_client.send(b'ready')#=>提示服务端客户端已做好接收返回内容的准备
#     length = int(length.decode('utf-8'))#=>接收的length是字节，转成int
#     recv_size = 0#=>表示已接收的内容长度
#     recv_msg = b''
#     #=>不断接收内容直到接收完毕
#     while recv_size < length:
#         recv_msg += tcp_client.recv(buffer_size)#=>将接收到的内容接在后面
#         recv_size = len(recv_msg)#=>更新已经接收到的长度
#     # cmd_res = tcp_client.recv(buffer_size)  #=> 客户端、服务端接收时只需要传入buffer_size
#     print('命令执行的结果是', recv_msg.decode('gbk')) #=> 收到的数据必须decode，而且要与encode时的编码一致
#
# tcp_client.close()#=>最后要关闭连接


from socket import *
import struct
from functools import partial
ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port) #=> 服务端是绑定ip_port，而客户端是连接，connect

#=> 用到while True的时候考虑好break和continue的条件
while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break

    tcp_client.send(cmd.encode('utf-8'))    #=> 发送时同样要encode

    # 解决粘包
    # length = tcp_client.recv(buffer_size)  #=>从服务端接收到返回内容的长度
    # tcp_client.send(b'ready')#=>提示服务端客户端已做好接收返回内容的准备
    # length = int(length.decode('utf-8'))#=>接收的length是字节，转成int
    # recv_size = 0#=>表示已接收的内容长度
    # recv_msg = b''
    # #=>不断接收内容直到接收完毕
    # while recv_size < length:
    #     recv_msg += tcp_client.recv(buffer_size)#=>将接收到的内容接在后面
    #     recv_size = len(recv_msg)#=>更新已经接收到的长度
    # cmd_res = tcp_client.recv(buffer_size)  #=> 客户端、服务端接收时只需要传入buffer_size
    #新解决粘包方法
    length_data = tcp_client.recv(4)#=>先开始接收4个字节，这4个字节肯定是内容长度信息
    length = struct.unpack('i', length_data)[0]#=>解压之后是个tuple，第一项是值
    # =>jion函数可以作用于迭代器，将多次接收的信息连接到一起，相当于for循环
    recv_msg = ''.join(iter(partial(tcp_client.recv, buffer_size), b''))
    print('命令执行的结果是', recv_msg.decode('gbk')) #=> 收到的数据必须decode，而且要与encode时的编码一致

tcp_client.close()#=>最后要关闭连接
