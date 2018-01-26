# -*- coding: utf-8 -*-

from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
import numpy as np
from command import trans_command
# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
IRCodes=[] 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addcode',methods=['GET','POST'])
def addCode():
    print('requested')
    if request.method == 'POST':
        IRcode={}
	IRcode['name']=request.form['name']	
	IRcode['code']=request.form['code']
	IRCodes.append(IRcode)
	print(IRCodes)
       	return jsonify(IRcode)
    else:
        return render_template('index.html')
@app.route('/code',methods=['POST'])
def transIRCode():
    print(request.form['code'])
    trans_command(request.form['code'])
    return 'success'

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に