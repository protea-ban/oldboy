#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: udp客户端.py 
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
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:BanShaoHuan
@file: udp服务端.py
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
ip_port = ('192.168.83.128', 8668)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)

    data, addr = udp_client.recvfrom(buffer_size)
    print('ntp服务器的标准时间是', data.decode('utf-8'))
