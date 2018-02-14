# pythonIRServer

a http server to make raspberry pi remote controller

I used 
- http://bit-trade-one.co.jp/support/download/

## Overview

`pythonIRServer` is a server with Python library, [Flask](http://flask.pocoo.org), to change raspberry pi into remote controller,  
with learning remote controller ( [ADRSIR](http://bit-trade-one.co.jp/product/module/adrsir/) ).  

## Features

- easy to get IR code and output it

## Requirements

- Python 3 or more
- pip, which is to install python library (smbus)

## Usage

1. open shell and command `sudo python app.py`

``` terminal
pi@raspberrypi:~$ cd pythonIRServer/
pi@raspberrypi:~/pythonIRServer$ sudo python app.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 204-077-648
```

2. go to http://xxx.xxx(your raspberry pi's IP):5000/  
or using postman 
`GET http://______/code-from/(your switch number)`
NOTE: thenumber startt at 0 to 9

`POST http://_____/code/(IR code)`


