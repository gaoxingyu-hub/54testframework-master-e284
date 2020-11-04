# -*- coding: utf-8 -*- 
'''
Created on 2015.10.14

@author: XiePenghan
'''


from InstrumentDrivers import PyVisaInstr


class VNA(PyVisaInstr.pyVisaInstr):
    '''
            矢网的基类，基于pyVisa连接
    '''
    def __init__(self,Addr):
        '''
                        初始化示波器，根据给定的地址进行初始化，并获得操作句柄
        '''
        PyVisaInstr.pyVisaInstr.__init__(self, Addr)
        self.VNA=self.instr
    
    
    def Preset(self):
        '''
        Preset功能
        '''
        self.Write('*RST')
        
        


      
        
        
        
        