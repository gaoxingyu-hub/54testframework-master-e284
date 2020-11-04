# -*- coding: utf-8 -*- 
'''
Created on 2016年5月23日

@author: ariza
'''

from InstrumentDrivers import PyVisaInstr
import string


class PowerMeter(PyVisaInstr.pyVisaInstr):
    '''
            示波器的基类，基本连接，读写操作和一般驱动基于pyvisa
    '''
    def __init__(self,Addr):
        '''
                        初始化示波器，根据给定的地址进行初始化，并获得操作句柄
        '''
        PyVisaInstr.pyVisaInstr.__init__(self, Addr)
        self.PM=self.instr
    
    def WriteWithoutOPC(self,cmd):
        self.instr.write(str(cmd))
    
    def Preset(self):
        '''
        重置仪表
        '''
        self.Write('*RST')
        
        
    def Ask(self,cmd):
        '''
        重写Ask，加入询问OPC操作
        '''
        result=self.instr.query(str(cmd))
        self.instr.query('*OPC?')
        return result
      
    def Write(self,cmd):
        '''
        加入询问OPC操作
        '''
        self.instr.write(str(cmd))
        self.instr.query('*OPC?')
        self.instr.write('*cls')
      
    def Read(self):
        '''
        加入询问OPC操作
        '''
        result=self.instr.read()
        self.instr.ask('*OPC?')
        return result
         
    def AskForNumber(self,cmd):
        '''
                        功  能同Ask，但将返回值转成数字 
        '''
        result=self.Ask(str(cmd))
        return string.atof(result)
         
    def ReadForNumber(self):
        '''
                        功能同Read，但将返回值转成数字 
        ''' 
        result=self.Read()
        return string.atof(result)