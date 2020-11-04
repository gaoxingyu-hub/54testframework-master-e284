# -*- coding: utf-8 -*- 
'''
Created on 2015年11月11日

@author: SuYuanhong
'''

from .RS232COM import COM_Object

class DCPaths(COM_Object):
    '''
    九院5所脉冲试验测试项目中，集成直流输出模块控制部分驱动代码
    '''
    def __init__(self,comport='COM4',baudRate=9600):
        '''
                   
        '''
        COM_Object.__init__(self, comport,baudRate,timeout=0)
        self.DCPaths=self.instr
        self.pathsStatus=[False]*10#十个通道的状态控制，0代表断开，1代表导通
        self.pathvalue=[1,2,4,8,16,32,64,128,256,512]
        
    def ConnChek(self):
        '''
        连接确认
        '''
        if self.instr.isOpen()==False:
            self.instr.open()
        cmd='\xaa\xbb\x01\x00\x00\xcc'
        try:
            resultstring=self.Ask(cmd)
            if resultstring.find('\xaa')>=0:
                self.close()
                return True
            else:
                self.close()
                return False
        except:
            self.close()
            return False
    
    def PathsControlExecute(self):
        '''
        通断控制，运行这个之前，必须更新self.pathsStatus的值
        '''
        if self.instr.isOpen()==False:
            self.instr.open()
        totalControlNumber=0
        for i in range(len(self.pathsStatus)):
            if self.pathsStatus[i]==True:
                totalControlNumber=totalControlNumber+self.pathvalue[i]
        totalString=hex(totalControlNumber)
        if len(totalString)<3:
            raise Exception('数值个数错误')
        if len(totalString)==3:
            totalString=totalString[:2]+'000'+totalString[2:]
        elif len(totalString)==4:
            totalString=totalString[:2]+'00'+totalString[2:]
        elif len(totalString)==5:
            totalString=totalString[:2]+'0'+totalString[2:]
        totalString=totalString[2:]
        InitcmdString='\xaa\xbb\x02\x00\x00\xcc'
        initCmdByteArray=bytearray(InitcmdString)
        initcmdList=list(initCmdByteArray)
        initcmdList[3]=int(totalString[:2],16)
        initcmdList[4]=int(totalString[2:],16)
        initCmdByteArray=bytearray(initcmdList)
        cmdStringFinal=str(initCmdByteArray)
        
        
        
#         valueString='\x00'+totalString[2]+'\x00'+totalString[3:]
#         
#         cmdString='\xaa\xbb\x02'+valueString+'\xcc'
        
        result=self.Ask(cmdStringFinal)
        
        if result.find('\xaa')>=0:
            self.instr.close()
            return
        else:
            if self.ConnChek()==True:
                self.Ask(cmdStringFinal)#再次通信
                self.instr.close()
                return
            
    def close(self):
        '''
        关闭串口，每次操作完成后一定要运行
        '''
        self.instr.close() 
               
        
# import time               
# test= DCPaths()  
# test.ConnChek()
# test.pathsStatus=[True,True,False,True,True,True,True,True,True,True]
# test.PathsControlExecute()  
   
# for i in range(8,10):
#     print 'times'+str(i)+'\n'
#     time.sleep(1)
#     test.pathsStatus[i]=True
#     test.PathsControlExecute()
# test.close()

        