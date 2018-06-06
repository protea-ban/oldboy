#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: ftp_server.py 
@time: 2018/06/04
@contact: banshaohuan@163.com
@software: PyCharm

服务端入口文件，通过运行该文件实现交互
"""  

#=> 将该项目路径加到系统路径中，以便导入其他路径中的包

import os,sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main

if __name__ == '__main__':
    main.ArgvHandler()