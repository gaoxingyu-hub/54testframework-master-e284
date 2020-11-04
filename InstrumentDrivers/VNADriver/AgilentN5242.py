# -*- coding: utf-8 -*- 
'''
Created on 2015.10.14

@author: Penghan Xie
'''


from InstrumentDrivers.VNADriver.VectorNetworkAnalyzer import VNA
import re,string



        
class VNA_AgilentN5242(VNA):
    '''
    矢量网络分析仪AgilentN5242底层驱动
    '''
    
    def __init__(self,Addr):
        VNA.__init__(self,Addr)
    
    def PeakSearch(self):   
        self.Write('CALC:MARK:FUNC:EXEC MAX' )
        temp=self.Ask('CALC:MARKer:FUNC:RESult?')
        return temp.split(',')
    
    def SetMarkerX(self,value):
        '''
        起始频率，单位Hz
        '''
        cmd='CALC:MARK:X '+str(value)
        self.Write(cmd)
    
    def GetMarkerY(self):
        temp=self.Ask('CALC:MARK:Y?')
        return temp.split(',')[0]

    
    def SetStartFreq(self,StartFreq):
        '''
        起始频率，单位Hz
        '''
        cmd='SENS:FREQ:STAR '+str(StartFreq)
        self.Write(cmd)
        
    def GetStartFreq(self):  
        cmd='SENS:FREQ:STAR?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring)    
    
    def SetStopFreq(self,StopFreq):    
        '''
        截止频率
        '''
        cmd='SENS:FREQ:STOP '+str(StopFreq)
        self.Write(cmd)
        
    def GetStopFreq(self):  
        cmd='SENS:FREQ:STOP?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring)
        
    def SetSpan(self,Span):    
        '''
        频率范围，扫频有两种描述方式：
    1. 起始频率和截止频率；
    2. 中心频率和频率范围
        '''
        cmd='SENS:FREQ:SPAN '+str(Span)
        self.Write(cmd)
        
    def GetSpan(self):  
        cmd='SENS:FREQ:SPAN?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring)
    
    def SetCentreFreq(self,Freq):
        cmd='SENS:FREQ:CENT '+str(Freq)
        self.Write(cmd)
        
    def GetCentreFreq(self):  
        cmd='SENS:FREQ:CENT?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring)
    
    def SetIFBW(self,IFBW):
        '''
        中频带宽IFBW
        '''
        cmd='SENS:BWID '+str(IFBW)
        self.Write(cmd)    
    
    def GetIFBW(self):  
        cmd='SENS:BWID?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring) 
    
    def SetAverageStatus(self,Status):
        cmd='SENS:AVER '+ str(Status)
        self.Write(cmd)    
    
    def GetAverageStatus(self):
        cmd='SENS:AVER?'
        resultstring= self.Ask(cmd)
        return self.GetReturnNumberFromString(resultstring)>0
    
    def SetAverageTimes(self,times):
        
        cmd='SENS:AVER:COUN '+ str(times)
        self.Write(cmd)
    
    def SetOutputPower(self,dBm):
        '''
        设置矢网源功率输出大小
        '''
        cmd='SOUR:POW '+ str(dBm)
        self.Write(cmd)
            
    def SetTracePoint(self,point):   
        '''
        设置扫描点数
        '''
        cmd='SENS:SWE:POIN '+ str(point)
        self.Write(cmd)
        
    def SetMeasFormat(self,format):
        '''
        设置矢网的测量格式：
        MLINear,
        MLOGarithmic,
        PHASe,
        IMAGinary,
        REAL,
        POLar,
        SMITh,
        SWR,
        GDELay
        '''
        cmd='CALC:FORM '+ str(format)
        self.Write(cmd)
        
    def DeleteAllMeas(self):    
        '''
        删除所有的测量
        '''
        cmd='CALC:PAR:DEL:ALL'
        self.Write(cmd)
        
    def SetReceiverMode(self):
        '''
        设置为接收机模式
        '''
        cmd='ROUT1:PATH:LOOP EXT'
        self.Write(cmd)
        
    def SelectTrace(self,TraceName):
        '''
        选择一条测量迹线
        ''' 
        cmd='CALC:PAR:SEL '+"'"+TraceName+"'"
        self.Write(cmd)
        
    def CreateMeas(self,TraceName,MeasType):
        '''
        创建一个测量，该测量对应迹线名称为：TraceName,该测量的测量类型为：MeasType;
   MeasType的类型包括：
   1. S参数：S11，S21，S12，S22...
   2. ratioed measurements
   3. non-ratioed measurements
   4. ADC measurements
   5. Balanced Measurements
   CALC4:PAR:EXT 'ch4_S33', 'S33' 'Defines an S33 measurement
   calculate2:parameter:define:extended 'ch1_a', 'b9/a10,1'
        '''
        cmd='CALC:PAR:EXT '+"'"+TraceName+"'"+"'"+MeasType+"'"
        self.Write(cmd)
        
    def SetOutputStatus(self,status):
        
        if (status):
            self.Write('OUTP:STAT ON')
        else:
            self.Write('OUTP:STAT OFF')
    
    def DisplayMeas(self,TraceName):  
        cmd = 'DISP:WIND:TRACE:FEED '+"'"+TraceName+"'" 
        self.Write(cmd)
        
    def SelectMeas(self,TraceName):
        cmd = 'CALC:PAR'+str(TraceName)+':SEL'
        self.Write(cmd)
        
    def DeletAllMeas(self):
        cmd='CALC:PAR:DEL:ALL'
        self.Write(cmd)   
        
        
    def SelectCalKit(self,CalKitNo):
        cmd= 'SENS:CORR:COLL:CKIT '+str(CalKitNo)
        self.Write(cmd)
        
    def SetCalType(self,caltype):
        cmd='SENS:CORR:COLL:METH '+str(caltype)
        self.Write(cmd)
        
    def SimulTwoPortCal(self,status):
        cmd='SENS:CORR:TST '+status
        self.Write(cmd)
        
    def SetAcquisitionDirection(self,Dirction):
        '''
        1代表正向，0代表反向
        '''
        cmd='SENS:CORR:SFOR '+str(Dirction)
        self.Write(cmd)
    
    def MeasureStandard(self,standard):
        cmd='SENS:CORR:COLL '+str(standard)
        self.Write(cmd)

    def DisplayAlwaysOn(self):   
        self.Write(':SYSTEM:DISPLAY:UPDATE ON')
    def CalKitSelect(self,ConnetorType,CalkitName):
        self.Write(':SENSE:CORR:CKIT:SEL '+"'"+ConnetorType+"'"+','+"'"+CalkitName+"'")
    def ConnectorSelectForPort1(self,ConnetorType,gender):
        cmd=':SENSE1:CORRECTION:COLLECT:SCONNECTION1 '+"'"+ConnetorType+"'"+gender
        self.Write(cmd)
    
    def ConnectorSelectForPort2(self,ConnetorType,gender):
        self.Write(':SENSE1:CORRECTION:COLLECT:SCONNECTION2 '+"'"+ConnetorType+"'"+gender)
        
    def DefineTOSMMethod(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',TOSM,1,2'
        self.Write(cmd)  
        
    def DefineTRLMethod(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',TRL,1,2'
        self.Write(cmd)  
    
    def ThoughCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected THRough, 1, 2')
        
    
    def StoreCalResult(self,filename):
        cmd=':MMEMORY:STORE:CORRection 1, '+"'"+filename+'.cal'+"'"
        self.Write(cmd)
           
    def LoadCalResult(self,filename):
        cmd=':MMEMORY:LOAD:CORRection 1, '+"'"+filename+'.cal'+"'"
        self.Write(cmd)
        
        
    def GetIdn(self):
        return self.Ask('*IDN?')
        
    def SetMarkerMode(self,value):
        self.Write('CALC:MARK1 '+str(value))
# inst=VNA_AgilentN5242("TCPIP::192.168.1.223::INSTR")
# print (inst.Ask("*IDN?"))
# inst.SetMarkerMode('NORM')
# inst.SetMarkerX(1000000000)
# mres1 = inst.GetMarkerY()
# print(mres1)
# inst.SelectMeas('2')
# mres2 = inst.GetMarkerY()
# print(mres2)
# inst.Write("*RST")
# inst.Write(":CHANNEL1:DISPLAY ON")
# inst.Write(":TIMebase:SCALe 1e-8")
# inst.Write(":CHANnel1:OFFSet 0.1")
# inst.Write(":SINGle")