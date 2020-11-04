# -*- coding: utf-8 -*- 
'''
Created on 2015年7月6日

@author: SuYuanhong

modified on 2020.1.2
update pyvisa latest version and support python3
@author: chuan.yang
'''
import pyvisa
import string

class pyVisaInstr(object):
    '''
    将pyvisa的底层通信固化成类，便于管理和调试
    '''
    def __init__(self,Addr):
    
        '''
                    初始化示波器，根据给定的地址进行初始化，并获得操作句柄
        '''
        self.Addr=str(Addr)
        rm = pyvisa.ResourceManager()
        self.instr=rm.open_resource(self.Addr)#11.16change instrument to Instrument
        
    def Ask(self,cmd):
        '''
        Ask,对应pyvisa中的Ask，对仪表进行先写后读的操作，增加opc查询命令
        '''
        result=self.instr.query(str(cmd))
        return result
      
    def Write(self,cmd):
        '''
        Write,对仪表进行写操作，无返回值
        '''
        self.instr.write(str(cmd))
      
    def Read(self):
        '''
        Read,对仪表进行读操作，读取结果
        '''
        result=self.instr.read()
        return result
         
    def AskForNumber(self,cmd):
        '''
                        功  能同Ask，但将返回值转成数字 
        '''
        result=self.query(str(cmd))
        return string.atof(result)
         
    def ReadForNumber(self):
        '''
                        功能同Read，但将返回值转成数字 
        ''' 
        result=self.Read()
        return string.atof(result)
# a=pyVisaInstr('192.168.1.1')

