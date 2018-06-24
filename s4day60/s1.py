#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaohuan
@file: s1.py 
@time: 2018/06/23
@contact: banshaohuan@163.com
@software: PyCharm  
"""  
import pymysql

username = input("username:")
pwd = input("password:")

conn = pymysql.connect(host="localhost",user="root",password="",database="db666")

cursor = conn.cursor()
sql = "select * from userinfo WHERE username=%s AND password=%s"

print(sql)
cursor.execute(sql)
result = cursor.fetchone()

print(result)
cursor.close()
conn.close()