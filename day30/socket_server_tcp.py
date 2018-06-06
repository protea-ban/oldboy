#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: socket_server_tcp.py 
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
# import subprocess
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
#
# tcp_server = socket(AF_INET, SOCK_STREAM)   #=> 选择TCP模式
# tcp_server.bind(ip_port)    #=> 绑定服务端地址和端口
# tcp_server.listen(back_log) #=> 开始监听
#
# while True:
#     conn, addr = tcp_server.accept()
#     print('新的客户端链接', addr)
#     while True:
#         # 收
#         try:
#             cmd = conn.recv(buffer_size)
#             if not cmd:break
#             print('收到客户端的命令', cmd)
#
#             # 执行命令，得到命令的运行结果cmd_res
#             #=> 传过来的是字节，需要用decode解码，五个参数
#             res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
#                                    stderr=subprocess.PIPE,
#                                    stdout=subprocess.PIPE,
#                                    stdin=subprocess.PIPE)
#             err = res.stderr.read() #=> stderr保存的是错误信息
#             #=> 如果出错将报错信息赋值给cmd_res，否则将输出内容赋值
#             if err:
#                 cmd_res = err
#             else:
#                 cmd_res = res.stdout.read() #=> stdout保存的是输出信息
#
#             # 发
#             if not cmd_res: #=> 如果cmd_res不为空，发送给客户端
#                 cmd_res = '执行成功'.encode('gbk')  #=> 发送时要encode，Windows下中文编码为gbk
#             conn.send(cmd_res)
#         except Exception as e:
#             print(e)
#             break

#low版解决粘包
# from socket import *
# import subprocess
# ip_port = ('127.0.0.1', 8080)
# back_log = 5
# buffer_size = 1024
#
# tcp_server = socket(AF_INET, SOCK_STREAM)   #=> 选择TCP模式
# tcp_server.bind(ip_port)    #=> 绑定服务端地址和端口
# tcp_server.listen(back_log) #=> 开始监听
#
# while True:
#     conn, addr = tcp_server.accept()
#     print('新的客户端链接', addr)
#     while True:
#         # 收
#         try:
#             cmd = conn.recv(buffer_size)
#             if not cmd:break
#             print('收到客户端的命令', cmd)
#
#             # 执行命令，得到命令的运行结果cmd_res
#             #=> 传过来的是字节，需要用decode解码，五个参数
#             res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
#                                    stderr=subprocess.PIPE,
#                                    stdout=subprocess.PIPE,
#                                    stdin=subprocess.PIPE)
#             err = res.stderr.read() #=> stderr保存的是错误信息
#             #=> 如果出错将报错信息赋值给cmd_res，否则将输出内容赋值
#             if err:
#                 cmd_res = err
#             else:
#                 cmd_res = res.stdout.read() #=> stdout保存的是输出信息
#
#             # 发
#             if not cmd_res: #=> 如果cmd_res不为空，发送给客户端
#                 cmd_res = '执行成功'.encode('gbk')  #=> 发送时要encode，Windows下中文编码为gbk
#             length = len(cmd_res)#=>执行命令后要返回内容的长度
#             conn.send(str(length).encode('utf-8'))#=>将长度发送给客户端
#             client_ready = conn.recv(buffer_size)#=>用来接收客户端准备好接收的指令
#             if client_ready == b'ready':#=>确定客户端准备接收后发送内容
#                 conn.send(cmd_res)
#         except Exception as e:
#             print(e)
#             break


from socket import *
import subprocess
import struct
ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)   #=> 选择TCP模式
tcp_server.bind(ip_port)    #=> 绑定服务端地址和端口
tcp_server.listen(back_log) #=> 开始监听

while True:
    conn, addr = tcp_server.accept()
    print('新的客户端链接', addr)
    while True:
        # 收
        try:
            cmd = conn.recv(buffer_size)
            if not cmd:break
            print('收到客户端的命令', cmd)

            # 执行命令，得到命令的运行结果cmd_res
            #=> 传过来的是字节，需要用decode解码，五个参数
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            err = res.stderr.read() #=> stderr保存的是错误信息
            #=> 如果出错将报错信息赋值给cmd_res，否则将输出内容赋值
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read() #=> stdout保存的是输出信息

            # 发
            if not cmd_res: #=> 如果cmd_res不为空，发送给客户端
                cmd_res = '执行成功'.encode('gbk')  #=> 发送时要encode，Windows下中文编码为gbk
            length = len(cmd_res)#=>执行命令后要返回内容的长度
            # conn.send(str(length).encode('utf-8'))#=>将长度发送给客户端
            # client_ready = conn.recv(buffer_size)#=>用来接收客户端准备好接收的指令
            # if client_ready == b'ready':#=>确定客户端准备接收后发送内容
            data_length = struct.pack('i', length)#=>将返回内容的长度打包成int的长度，即4bytes
            conn.send(data_length)
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break
