#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: settings.py 
@time: 2018/06/04
@contact: banshaohuan@163.com
@software: PyCharm  
"""  

import os
BASE_DIR =PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


IP = "127.0.0.1"
PORT = 8080

ACCOUNT_PATH = os.path.join(BASE_DIR, "conf", "accounts.cfg")#=> 存放账户信息的文件添加到配置文件当中

# if __name__ == '__main__':
#     print(ACCOUNT_PATH)
