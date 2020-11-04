# -*- coding: utf-8 -*- 
'''
Created on 2015年11月11日

@author: SuYuanhong
'''

from .RS232COM import COM_Object
import time


class IOModule(COM_Object):
    '''
    IO模块控制部分驱动代码,控制输出高电平或低电平，以控制继电器开启或闭合
    '''
    def __init__(self,comport='COM2',baudRate=9600):
        '''
                   
        '''
        COM_Object.__init__(self, comport,baudRate,timeout=0)
        
    def powerOff(self):
        '''
        连接确认
        '''
        cmd='\x33\x01\x13\x00\x00\x00\x00\x47'
        self.instr.write(cmd)
    
    def powerOn(self):
        '''
        通断控制，运行这个之前，必须更新self.pathsStatus的值
        '''
        cmd='\x33\x01\x14\x00\x00\x00\x00\x48'
        self.instr.write(cmd)
           
    def close(self):
        '''
        关闭串口，每次操作完成后一定要运行
        '''
        self.instr.close() 
               
        

# test=IOModule()
# test.powerOff()
# time.sleep(3)
# test.powerOn()
# 33 01 13 00 00 00 00 47   #关
# 33 01 14 00 00 00 00 48   #开