#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: server.py 
@time: 2018/06/04
@contact: banshaohuan@163.com
@software: PyCharm

实现服务端的主要功能
"""

# 添加系统变量，使改文件能够运行，测试开发时使用，上线时只需保留入口文件中的该语句
# import os,sys
#
# PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PATH)


import socketserver
import json
import configparser
import os

from conf import settings

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",

    800 : "the file exist,but not enough ,is continue? ",
    801 : "the file exist !",
    802 : "ready to receive datas",

    900 : "md5 valdate success"

}


class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            #conn = self.request
            data = self.request.recv(1024).strip()
            data = json.loads(data.decode("utf-8"))

            '''
            {
                "action":"auth",
                "username":"ban",
                "pwd","123"

            }
           '''

            if data.get("action"):
                if hasattr(self, data.get("action")):
                    func = getattr(self, data.get("action"))
                    func(**data)
                else:
                    print("First Invaild cmd")
            else:
                print("Invaild cmd")

    def send_response(self, status_code):
        response = {
            "status_code":status_code,
        }
        self.request.sendall(json.dumps(response).encode("utf-8"))

    def auth(self, **data):
        # print("get data:", data)
        username = data["username"]
        password = data["password"]

        user= self.authenticate(username, password)
        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def authenticate(self, user, pwd):
        cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)

        if user in cfg.sections():

            if cfg[user]["Password"] == pwd:
                # => 当输入信息验证成功后，将user赋值给类，使得类全局都可使用该user
                self.user = user
                #=> 将路径加到主路径当中
                self.mainPath = os.path.join(settings.BASE_DIR, "home", self.user)
                print("passed authentication")
                return user


    def put(self, **data):
        has_recived = 0#=> 该变量判断是否文件全部上传
        # print("data", data)
        file_name = data.get("file_name")
        file_size = data.get("file_size")
        target_path = data.get("target_path")

        #=> 将主路径、目标路径、文件名拼接起来构成要上传文件的绝对路径
        abs_path = os.path.join(self.mainPath, target_path, file_name)

        '''
        几种情况：
        1.没有该文件，直接上传
        2.有该文件
            2.1. 完整，不需要传
            2.2. 不完整，续传
        '''

        if os.path.exists(abs_path):
            file_has_size = os.stat(abs_path).st_size
            if file_has_size < file_size:
                # 断点续传
                self.request.sendall("800".encode("utf-8"))
                choice = self.request.recv(1024).decode("utf-8")
                if choice == "Y":
                    #=> 先将已经上传文件的大小给客户端返回去
                    self.request.sendall(str(file_has_size).encode("utf-8"))
                    has_recived += file_has_size#=> 更新已经上传的大小
                    f = open(abs_path, "ab")#=> 以ab方式打开，即为追加写入
                else:
                    #=> 不断点续传，就是重新传，跟文件不存在一样
                    f = open(abs_path, "wb")  # => 不同的情况用不同的方式打开文件
            else:
                # 文件完全存在
                self.request.sendall("801".encode("utf-8"))
                return


        else:
            self.request.sendall("802".encode("utf-8"))
            f = open(abs_path, "wb")#=> 不同的情况用不同的方式打开文件



        while has_recived < file_size:
            #=> Windows下传输中断开会报错，在此进行异常处理
            try:
                data = self.request.recv(1024)
            except Exception as e:
                break
            f.write(data)
            has_recived += len(data)

        f.close()

    def ls(self, **data):
        file_list = os.listdir(self.mainPath)

        file_str = "\n".join(file_list)
        if not len(file_list):
            file_str = "<empty dir>"
        self.request.sendall(file_str.encode("utf-8"))

    def cd(self, **data):
        dirname = data.get("dirname")

        if dirname == "..":
            self.mainPath = os.path.dirname(self.mainPath)
        else:
            self.mainPath = os.path.join(self.mainPath, dirname)

        self.request.sendall(self.mainPath.encode("utf-8"))

    def mkdir(self, **data):
        dirname = data.get("dirname")

        #=> 拼接成绝对路径
        path = os.path.join(self.mainPath, dirname)
        if not os.path.exists(path):
            if "/" in dirname:
                os.makedirs(path)
            else:
                os.mkdir(path)
            self.request.sendall(("create dir 【%s】 successfully" % dirname).encode("utf-8"))
        else:
            self.request.sendall(("【%s】 exist"%dirname).encode("utf-8"))



# python ftp_client.py -s 127.0.0.1 -P 8080 -u ban -p 123

