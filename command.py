#coding: utf-8
#
# ****コマンドベース　実行コマンド　ファイル単位
#読み込みコマンド（ｒ:read）：、読込先の記憶No.（memo_no)、保存ファイル名（filename)
#書き込みコマンド（ｗ:write）：、書込先の記憶No.（memo_no)、読込ファイル名（filename)
#送信コマンド(t)：、読み込みファイル名（filename)
#ＰＩＣ→ラズハ゜イ　ディレクトリ読込コマンド（rd:read　directry)：、保存ディレクトリ名（dir_name)
#ＰＩＣ←ラズハ゜イ　ディレクトリ書込コマンド（wd:write　directry)：、読込ディレクトリ名（dir_name)
#　e　コマンド：終了
#

import smbus
import time
from time import sleep
##import commands
import subprocess
import os
import sys

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus               = smbus.SMBus(1)

# This must match in the Arduino Sketch
#SLAVE_ADDRESS    = 0x04
SLAVE_ADDRESS     = 0x52
data_numH         = 0x31
data_numL         = 0x32
data_numHL        = [0x00,0x31,0x32]
data_num          = 10
memo_no           = 0
block             = []

#command
R1_memo_no_write  = 0x15 #bus-write(ADR,cmd,1)
R2_data_num_read  = 0x25 #bus-read(ADR,cmd,3)
R3_data_read      = 0x35 #bus-read(ADR,cmd,n)
W1_memo_no_write  = 0x19 #bus-write(ADR,cmd,1)
W2_data_num_write = 0x29 #bus-write(ADR,cmd,3)
W3_data_write     = 0x39 #bus-read(ADR,cmd,n)
W4_flash_write    = 0x49 #bus-read(ADR,cmd,n)
T1_trans_start    = 0x59 #bus-write(ADR,cmd,1)

############# read command

def read_command(memo_no):
# cmd R1_memo_no_write 0x15 bus-write(ADR,cmd,1)
    print("memo_no write=",memo_no)
    bus.write_i2c_block_data(SLAVE_ADDRESS, R1_memo_no_write ,memo_no )   #= 0x15  #bus-write(ADR,cmd,1)

# cmd R2_data_num_read 0x25 bus-read(ADR,cmd,3)
    data_numHL = bus.read_i2c_block_data(SLAVE_ADDRESS, R2_data_num_read ,3 )#= 0x25 #bus-read(ADR,cmd,3)
    data_num = data_numHL[1]
    data_num *= 256
    data_num += data_numHL[2]
    print("data_num =",data_num )

# cmd R3_data_read           0x35 bus-read(ADR,cmd,n)
    block = []
    block_dat  = bus.read_i2c_block_data(SLAVE_ADDRESS, R3_data_read , 1)       #= 0x35 #bus-read(ADR,cmd,n)
    for i in range(data_num ):
     block_dat  = bus.read_i2c_block_data(SLAVE_ADDRESS, R3_data_read , 4)       #= 0x35 #bus-read(ADR,cmd,n)
     block.append(block_dat[0])
     block.append(block_dat[1])
     block.append(block_dat[2])
     block.append(block_dat[3])
    print(block)  #for denug
    return data_num
################# write command


# #############trans command
def trans_command(block2 ):
    
    print(block2)
    print(len(block2))
    str_tmp = ""
    int_tmp = []
    for i in range(len(block2)//2):
        str_tmp = block2[i*2] + block2[i*2+1]
        int_tmp.append( int(str_tmp, 16))
    print(int_tmp)  
    print(len(int_tmp))
# cmd W2_data_num_write 0x29 bus-write(ADR,cmd,3)
    data_num = len(int_tmp)//4  #for test
    data_numHL = [0x31,0x32] #for test
    data_numHL[0] = data_num//256
    data_numHL[1] = data_num%256
    bus.write_i2c_block_data(SLAVE_ADDRESS, W2_data_num_write ,  data_numHL)   #= 
# cmd W3_data_write           0x39 bus-read(ADR,cmd,n)
    print(data_num)
    data_numHL = [0x31,0x32,0x33,0x34] #for test 
    for i in range(data_num):
         data_numHL[0] = int_tmp[i*4+0]
         data_numHL[1] = int_tmp[i*4+1]
         data_numHL[2] = int_tmp[i*4+2]
         data_numHL[3] = int_tmp[i*4+3]
         bus.write_i2c_block_data(SLAVE_ADDRESS, W3_data_write , data_numHL)   #= 
 # cmd T1_trans_start             0x59 bus-write(ADR,cmd,1)
    memo_no = [0x00 ] #for dummy
    bus.write_i2c_block_data(SLAVE_ADDRESS, T1_trans_start,memo_no )   #=
    



