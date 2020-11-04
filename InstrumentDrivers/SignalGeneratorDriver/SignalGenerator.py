# -*- coding: utf-8 -*- 
'''
Created on 2015年5月14日
  
@author: SYH
'''
from InstrumentDrivers import PyVisaInstr
import string
import visa
class SignalGenerator(PyVisaInstr.pyVisaInstr):
    '''
            信号源的基类，基本连接，读写操作和一般驱动,底层驱动基于Agilent 8257模拟信号源
    '''
    def __init__(self,Addr):
        '''
                        初始化频谱仪，根据给定的地址进行初始化，并获得操作句柄
        '''
#         PyVisaInstr.pyVisaInstr.__init__(self, Addr)
#         self.SG=self.instr
        rm=visa.ResourceManager('@py')
        print("SignalGenerator connection....")
        print("连接地址： {}".format(Addr))
        try:
            self.instr = rm.open_resource(Addr)
            self.SG=self.instr
        except Exception as ex:
            print(ex)
    def Ask(self,cmd):
        '''
        重写Ask，加入询问OPC操作
        '''
        result=self.instr.ask(str(cmd))
        self.instr.ask('*OPC?')
        return result
      
    def Write(self,cmd):
        '''
        加入询问OPC操作
        '''
        self.instr.write(str(cmd))
        self.instr.ask('*OPC?')
      
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
    
    
          
    def ReadOutputState(self): 
        '''
        读取信号源的输出是否打开，打开为True，否则为False
        '''
        return self.AskForNumber(":OUTPut:STATe?")>0  
      
    def SetOutputState(self,value):
        '''
        根据value值设定输出或关断，value=0或False为关断，其余为开启
        '''
        if value==0:
            cmd="OFF"
        else:
            cmd="ON"
        self.Write(":OUTPut:STATe "+cmd)
    
    def GetRFPower(self):
        '''
        读取信号源输出功率
        '''
        return self.AskForNumber(":SOURce:POWer:LEVel:IMMediate:AMPLitude?")
      
    def SetRFPower(self,value):
        '''
        写信号源输出功率
        '''
        self.Write(":SOURce:POWer:LEVel:IMMediate:AMPLitude "+str(value))
    
    def GetAmpOffset(self):
        '''
        读取幅度偏置值
        '''
        return self.AskForNumber(":SOURce:pow:offset?")         
    
    def SetAmpOffset(self,value):
        '''
        设置信号源幅度偏置
        '''
        self.Write(":SOURce:pow:offset "+str(value))  
    
    def GetFrequency(self):
        '''
        读取信号源输出频率
        '''
        return self.AskForNumber(":SOURce:FREQuency:FIXed?")
    
    def SetFrequency(self,value):
        '''
        设置信号源输出频率
        '''
        self.Write(":SOURce:FREQuency:FIXed "+str(value))
        
    def SetAM_ModState(self,state):
        self.Write("AM:STAT "+state)
        
    def SetFM_ModState(self,state):
        self.Write("FM:STAT "+state)
        
    def SetModeState(self,value):
        if value==0:
            cmd="OFF"
        else:
            cmd="ON"
        self.Write("MOD:STAT "+cmd)
        
    def Preset(self):
        '''
        重置仪表
        '''
        self.Write('*RST')
        
    def GetIdn(self):
        return self.Ask('*IDN?')
# mSG=SignalGenerator('TCPIP::192.168.1.221::INSTR"')
# mSG.SetFrequency(30000000)
# midn=mSG.GetIdn()
# print(midn) 
# mSG.Preset()
    
      
