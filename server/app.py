#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/6/9
# @Author  : jenkins
# @Version : V1.0
# @Features: ipa分发系统

from flask import Flask, jsonify
from flask_cors import CORS
import os
import random

# Set up the app and point it to Vue
app = Flask(__name__, static_folder='../dist/',    static_url_path='/')
CORS(app)

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

#随机数
@app.route('/api/getRandomNum')
def get_random_num():
    res = {
        'getRandomNum': random.randint(1, 100)
    }
    return jsonify(res)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Pong!')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)