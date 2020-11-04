# -*- coding: utf-8 -*-
'''
Created on 2016年5月11日

@author: ariza
'''

from .RS232COM import COM_Object
import time


class SwitchMatrix(COM_Object):
    '''
    多通道天线测试仪开关矩阵采用串口控制方式
    '''  
    def __init__(self,comport='COM1',baudRate=115200):
        
        COM_Object.__init__(self, comport,baudRate,timeout=0.1)
        self.switch=self.instr
        
#     def Ask(self,cmd):
#         self.switch.write(cmd.encode('utf-8'))
#         return self.switch.readall()    
    
    def switch_RST(self):
        self.switch.write('*RST')
        time.sleep(0.02)
        
    def IDN_query(self):
        cmd='*IDN?'
        return self.instr.Ask()
#         return self.Ask(cmd)
        
        
    def MatrixConnection(self,outchannel):
        channel=int(outchannel)
        if channel==1:
            tmp=8
        elif channel==2:
            tmp=7
        elif channel==3:
            tmp=6
        elif channel==4:
            tmp=5
        elif channel==5:
            tmp=4
        elif channel==6:
            tmp=3
        elif channel==7:
            tmp=2
        elif channel==8:
            tmp=1
        cmd = 'SETROUTE:'  + str(tmp)
        temp=self.Ask(cmd)
        if temp.find("OK")>=0:
            return True
        else:
            return False
        
    def set_all_switch_checkbox_off(self):
        cmd = 'SETALLOFF' 
        self.Write(cmd)
        
#x        
    def switch_readroute(self,inputchannel):
        cmd = 'READROUTE:'  + str(inputchannel)
        self.switch.write(cmd)
        return self.switch.readall()   
    
    def close(self):
        '''
        关闭串口，每次操作完成后一定要运行
        '''
        self.instr.close()
# test=SwitchMatrix()
# # print test.portstr
# b=test.IDN_query()
# a=test.MatrixConnection(5)
# print a
# print b