# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-03-22 10:05:23
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-03-22 10:22:21
from urllib import response
from flask import Flask , request , make_response , redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response
    

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return 'Hello World Platzi! ,  tu IP es {}'.format(user_ip)