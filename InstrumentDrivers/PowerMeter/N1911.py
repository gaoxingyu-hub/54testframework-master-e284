# -*- coding:utf-8 -*- 
'''
Created on 2017年4月13日

@author: xiaowei.xu
'''

from InstrumentDrivers.PowerMeter import PowerMeter

class N1911(PowerMeter.PowerMeter):
    '''
    classdocs
    '''

    def __init__(self, Addr):
        '''
        Constructor
        '''
        PowerMeter.PowerMeter.__init__(self, Addr)
    
    def SetMeasPath(self,mPath):
        '''
                        设置测试通道，0~2
        '''
        self.Write('SENS:RANG ' +str(mPath))
        
    def SetRangeAuto(self,mState):
        '''
                        设置自动范围，ON | OFF
        '''
        self.Write('SENS:RANG:AUTO '+str(mState))
    
    def SetPowerUnit(self,mUnit):
        '''
                        设置功率单位，DBM | W | DBUV
        '''
        self.Write('UNIT:POW' + str(mUnit))
        
    def SetMeasMode(self,mMode):
        '''
                        设置测试模式，Continuous| Burst | Timeslot | Trace
        '''
        if(mMode == 'Continuous'):
            mCmd = 'POWer:AVG'
        elif(mMode == 'Burst'):
            mCmd = 'POWer:Burst:AVG'
        elif(mMode == 'Timeslot'):
            mCmd = 'POWer:TSL:AVG'
        elif(mMode == 'Trace'):
            mCmd = 'XTIM:POW'
        self.Write('SENS:FUNC '+mCmd)
        
    def SetAvgCount(self,mCount):
        '''
                        设置平均次数，1~65536
        '''
        self.Write('SENS:AVER:COUN '+ str(mCount))
        
    def SetAvgState(self,mState):
        '''
                        设置平均状态，ON | OFF
        '''
        self.Write('SENS:AVER:STAT ' + str(mState))
        
    def SetAvgCountState(self,mState):
        '''
                        设置平均次数状态，ON | OFF | ONCE
        '''
        self.Write('SENS:AVER:COUN:AUTO '+ str(mState))
        
    def SetFreq(self,mFreq):
        '''
                        设置频率，单位Hz
        '''
        self.Write('SENS:FREQ '+ str(mFreq))
    
    def SetContinuousState(self,mState):
        '''
                        设置连续测试状态，ON | OFF 
        '''
        self.Write('INIT:CONT '+str(mState))
        
    def GetPower(self):
        temp = self.Ask('FETC?')
        return temp
    def GetIdn(self):
        return self.Ask('*IDN?')
        
# mPM=N1911('TCPIP0::192.168.1.145::inst0::INSTR')
# mPM.SetAvgState('ON')
# mPM.SetRangeAuto('ON')
#  
# mval=mPM.GetPower()
# mIDN= mPM.GetIdn()
#  
# print(mval)
# print(mIDN)

        
        