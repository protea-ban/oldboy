#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: 01不完整的web服务端示例.py 
@time: 2018/06/30
@software: PyCharm  
"""  

import socket
# 生成socket实例
sk = socket.socket()
# 绑定IP和端口
sk.bind(("127.0.0.1", 8080))
# 监听
sk.listen()

# 写一个死循环，一直等待客户端的连接
while 1:
    # 获取与客户端的连接
    conn, _ = sk.accept()
    # 接收客户端发来的信息
    data = conn.recv(8096)
    # 把收到的数据转成字符串类型
    data_str = str(data, encoding="utf-8")
    # print(data_str)
    data_li = data_str.split('\r\n')
    data_req = data_li[0].split()
    url = data_req[0]
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text.html;charset=utf-8\r\n\r\n')
    if url == '/xiaohei/':
        response = b'<h1>hello xiaohei!</h1>'
    elif url == '/xiaoban/':
        response = b'<h1>hello xiaoban!</h1>'
    else:
        response = b'<h1>404 not found!</h1>'
    conn.send(response)

    # 关闭
    conn.close()


