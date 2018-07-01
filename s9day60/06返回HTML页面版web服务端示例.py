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

def yimi(url):
    with open("yimi.html", 'rb') as f:
        ret = f.read()
    return ret

def xiaohei(url):
    with open("xiaohei.html", 'rb') as f:
        ret = f.read()
    return ret

# 404函数
def f404(url):
    ret = "你访问的这个{} 找不到".format(url)
    return bytes(ret, encoding="utf-8")

url_func = [
    ("/yimi/", yimi),
    ("/xiaohei/", xiaohei),
]

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
    url = data_req[1]
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text.html;charset=utf-8\r\n\r\n')

    # 根据不同的URL返回不同的内容
    # 去url_func里面找对应关系
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    # 找不到对应关系就默认执行f404函数
    else:
        func = f404

    # 拿到函数的执行结果
    response = func(url)
    print(response)
    conn.send(response)

    # 关闭
    conn.close()


