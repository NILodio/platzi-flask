# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-03-22 10:05:23
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-03-22 10:06:57
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'