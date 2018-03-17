# -*- coding: utf-8 -*-
import json
from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
from command import trans_command,read_command
# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

class IRCode:
    def __init__(self,phrase,memo_no,code=None):
        self.phrase=phrase.strip(" ")
        self.code=code or codeFrom(memo_no)
    def zipped(self):
        return {''+self.phrase:self.code}
    def rawDict(self):
        return {'phrase':self.phrase,
                'code':self.code}
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/')
def index():
    print(request)
    return render_template('index.html')

@app.route('/codes')
def codes():
    with open('config/ir.json','r') as f:
        d=json.load(f)
        return jsonify(d)

#
@app.route('/addcode-from/<int:memo_no>',methods=['POST'])
def addCodeFrom(memo_no):
    IRcode=IRCode(phrase=request.form['phrase'],
                  memo_no=memo_no)
    with open('config/ir.json','r+') as f:
        data=json.load(f)
        tmp=data
        data.update(IRcode.zipped())
        f.seek(0)
        json.dump(data,f)
        f.truncate()
    return jsonify(IRcode.rawDict())    
#

@app.route('/addcode',methods=['POST'])
def addCode():
    print('requested')
    if request.method == 'POST':
        IRcode=IRCode(phrase=request.form['phrase'],
                    code=request.form['code']
        with open('config/ir.json','r+') as f:
            data=json.load(f)
            tmp=data
            data.update(IRcode)
            f.seek(0)
            json.dump(data,f)
            f.truncate()
       	return jsonify(request.form)
    else:
        return render_template('index.html')

@app.route('/code',methods=['GET','POST'])
def transIRCode():
    response={}
    if 'code' in request.form:
        print(request.form['code'])
        if request.method=='POST':
            trans_command(request.form['code'])
        return request.form['code'] 
    elif 'phrase' in request.form: 
        phrase=request.form['phrase'].strip(" ")
        with open('config/ir.json','r') as f:
            IRCodes=json.load(f)
            if phrase in IRCodes:
                code=IRCodes[phrase]
                print(code)
                if request.method=='POST':
                    trans_command(code)
                return u"""
                code:{0},
                phrase:{1}
                """.format(code,phrase)
        abort(400,u'unregistered the phrase: {}'.format(phrase))
    else:
        abort(400,u'request form is invalid')
@app.route('/code-from/<int:memo_no>')
def codeFrom(memo_no):
    str=''
    for d in read_command([memo_no]):
        str+='{:02X}'.format(d)
    print(str)
    return str


if __name__ == "__main__":
    app.run(host='0.0.0.0',  threaded=True, debug=True)