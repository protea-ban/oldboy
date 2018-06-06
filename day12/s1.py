#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: s1.py 
@time: 2018/05/08
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

# li = [11, 22, 33, 44]
# v = li.pop()
# li.reverse()
# li.sort(reverse=True)
# print(li)

# li = [11,22,33,"123","alex"]
# r = str(li) # '[11,22,33,"123","alex"]'
# print(r)
# s = ""
# for i in li:
#     s = s + str(i)
#
# print(s)

# li = ["123", "alex"]
# s = "".join(li)
# print(s)

# v = "alex"
# v = v.replace('l','el')
# v[0] = "A"
# print(v)


dic = {
    "k1": 'v1',
    "k2": 'v2'
}
# 1 根据序列，创建字典，并指定统一的值
# v = dict.fromkeys(["k1",123,"999"],123)
# v = dic['k111']
v = dic.get('k11', 'ban')
print(v)

