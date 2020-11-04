# -*- coding: utf-8 -*- 
'''
Created on 2015年11月11日

@author: SuYuanhong
'''

import serial

class COM_Object():
    '''
    pyvisa对不不支持ASCII的串口设备的配置没有走通，故这一类的COM单独使用python自带的库Serial
    '''
    def __init__(self,comport='COM2',baudRate=9600,timeout=0):
        
        self.instr=serial.Serial(str(comport),baudRate,timeout=timeout)
        
#         self.instr.setTimeout(0)
    
    
    def Write(self,cmd):
        self.instr.write(cmd)
        self.Read()
        
        
    def Read(self):
        
        return self.instr.readall()
            
    def Ask(self,cmd):
        self.instr.write(cmd)
        return self.Read()
    
    
# test=COM_Object(comport='COM1',baudRate=115200)
# print test.Ask("*IDN?")