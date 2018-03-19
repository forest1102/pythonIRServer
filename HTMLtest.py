# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)


#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('/home/pi/.ssl/cert.crt',
#        '/home/pi/.ssl/server_secret.key')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',  threaded=True, debug=True)
