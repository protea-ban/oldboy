#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: app.py 
@time: 2019/01/07
@software: PyCharm  
"""  

from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
# Flask的秘钥
app.secret_key = "fasd"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'ban' and pwd == 'ban':
        session['user'] = user
        return redirect('/index')

    return render_template('login.html', error="用户名或密码错误")

@app.route('/index')
def index():
    user = session.get('user')
    if not user:
        redirect('/login')

    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run()
