#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: main.py 
@time: 2018/06/04
@contact: banshaohuan@163.com
@software: PyCharm

服务端实现主要功能的文件
"""  

import optparse
import socketserver

from conf import settings
from core import server

#=> 这个类用来处理在服务端传进来的参数
class ArgvHandler():

    #=> 通过optparse模块来获得命令行的参数
    def __init__(self):
        self.op = optparse.OptionParser()   #=> 初始化optparse对象

        # self.op.add_option("-s", "--server", dest="server")#=> add_option的用法
        # self.op.add_option("-P", "--port", dest="port")

        options, args = self.op.parse_args()    #=> parse_args()函数得到两种方式传进来的参数

        self.verify_args(options, args)

    def verify_args(self, options, args):
        '''
        验证命令行传进来的参数
        :param options:
        :param args:
        :return:
        '''
        cmd = args[0]
        #=> 传进来的参数存在，则执行
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func()

    def start(self):
        '''
        开始命令，开启服务端
        :return:
        '''
        print("the server is working...")
        s = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), server.ServerHandler) #=> 多线程的TCP客户端
        s.serve_forever()   #=> 持续运行
        pass

    def help(self):
        pass