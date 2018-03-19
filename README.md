# pythonIRServer

ウェブサーバを立てて、`raspberry pi` をリモコンにします。  

以下のサイトのソースコードを参考にしました。
- http://bit-trade-one.co.jp/support/download/

## 概要 

`pythonIRServer` は、FlaskというPythonライブラリーを用いて、`raspberry pi` を赤外線リモコンへと変化させます。
今回、赤外線リモコン基板としてADRSIRを使用しました。( [ADRSIR](http://bit-trade-one.co.jp/product/module/adrsir/) ).  

## 特徴

- 赤外線コードを調べる必要なく簡単にリモコン化させることができます。

## 必要なもの

- raspberry pi
- ADRSIR(リモコン基板)
- Python 3 以上
- pip(smbusという赤外線を送受信するインストール用)

## 使い方  


1. 自身の`raspberry pi` にこれをクローンします。

2. `raspberry pi`のコマンドターミナルを開き、以下のコマンドを入力します。 

``` terminal
pi@raspberrypi:~$ sudo python app.py
pi@raspberrypi:~$ cd pythonIRServer/
pi@raspberrypi:~/pythonIRServer$ sudo python app.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 204-077-648
```

3. http://xxx.xxx(your raspberry pi's IP):5000/  
を開きます。  
`GET http://______/code-from/(your switch number)`
NOTE: thenumber startt at 0 to 9

`POST http://_____/code/(IR code)`


