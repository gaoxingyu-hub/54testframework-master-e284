# -*- coding: utf-8 -*- 
'''
Created on 2015年5月14日

@author: SYH
'''
import string
from visa import *

class SpectrumAnalyzer():
    '''
            频谱仪的基类，基本连接，读写操作和一般驱动,底层驱动基于FSW43
    '''
    
    class MarkerFunctionType:
        '''
        Marker的功能模式，
        '''
        BandIntervalDensity="BDEN"
        BandIntervalPower="BPOWer"
        Noise="NOISe"
    
    
    class MarkerMode:
        '''
        Marker的类型
        '''
        Poisitong="POSition"
        Delta="DELTa"
        Band="BAND"
        Span="SPAN"
        off="OFF"
     
    
        
    
#     def __init__(self,Addr):
#         '''
#                         初始化频谱仪，根据给定的地址进行初始化，并获得操作句柄
#         '''
#         PyVisaInstr.pyVisaInstr.__init__(self,Addr)  
#         self.SA=self.instr
# #         self.SA='test'
    def __init__(self,Addr):
        '''
                        初始化频谱仪，根据给定的地址进行初始化，并获得操作句柄
        '''
#         PyVisaInstr.pyVisaInstr.__init__(self,Addr)  
#         self.SA=self.instr
        rm=ResourceManager('@py')
        print("Specturm Analyzer connection....")
        print("连接地址： {}".format(Addr))
        try:
            self.instr = rm.open_resource(Addr)
            self.SA=self.instr
        except Exception as ex:
            print(ex)
        
        
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
      
    def Read(self):
        '''
        加入询问OPC操作
        '''
        result=self.instr.read()
        self.instr.query('*OPC?')
        return result
         
    def AskForNumber(self,cmd):
        '''
                        功  能同Ask，但将返回值转成数字 
        '''
        result=self.Ask(str(cmd))
        return result
         
    def ReadForNumber(self):
        '''
                        功能同Read，但将返回值转成数字 
        ''' 
        result=self.Read()
        return result   
   
    def GetCenterFrequency(self):
        '''
                        读频谱仪的中心频率
        '''
        return self.AskForNumber("FREQ:CENT?")   
    
    def SetCenterFrequency(self,value):
        '''
                        写频谱仪的中心频率
        '''
        self.Write("FREQ:CENT "+str(value))
     
    
    
    def GetSpan(self):
        '''
                        读频谱仪的扫描带宽span
        '''
        return self.AskForNumber("FREQ:SPAN?")
    
    def SetSpan(self,value):
        '''
                        写频谱仪的扫描带宽span
        '''
        self.Write("FREQ:SPAN "+str(value))
     
    def GetRBW(self):
        '''
                        读频谱仪的射频分辨带宽RBW
        '''
        return self.AskForNumber("BAND?")
    
    
    
    def SetRBW(self,value):
        '''
                        写频谱仪的分辨率带宽RBW
        '''
        self.Write("BAND "+str(value))
    
    def GetRefLevel(self):
        '''
                    读频谱仪的参考电平Reflevel
        '''
        return self.AskForNumber("DISP:TRAC:Y:RLEV?")
    
    def SetRefLevel(self,value):
        '''
                        写频谱仪的参考电平RefLevel
        '''
        self.Write("DISP:TRAC:Y:RLEV "+str(value))
    
    
    def GetSweepPoints(self):
        '''
                        读取频谱仪的扫描点数
        '''
        return self.AskForNumber("SWEep:POINts?")
    
    def SetSweepPoints(self,value):
        '''
        写频谱仪的扫描点数
        '''
        self.Write("SWEep:POINts "+str(value))
    
        
    def GetSweepTime(self):
        '''
        读取频谱仪的扫描时间
        '''
        return self.AskForNumber("SWE:TIME?")
    def SetSweepTime(self,value):
        '''
        写频谱仪‘扫描时间
        '''
        self.Write("SWE:TIME "+str(value))
    
    
    
    def GetVBW(self):
        '''
        读取频谱仪的VBW
        '''
        return self.AskForNumber("BAND:VID?")
    
    def SetVBW(self,value):
        '''
        写频谱仪的VBW
        '''
        self.Write("BAND:VID "+str(value))
    
    
    def GetAmpOffset(self):
        '''
        读取频谱仪的幅度偏置
        '''
        return self.AskForNumber("DISP:TRAC:Y:RLEV:OFFS?")
    
    def SetAmpOffset(self,value):
        '''
        设置频谱仪的幅度偏置
        '''
        self.Write("DISP:TRAC:Y:RLEV:OFFS "+str(value))
        
    def GetContinuousSweepState(self):
        '''
        读取目前扫描方式是否连续扫描,返回True或False
        '''
        return self.AskForNumber(':INITiate:CONTinuous?')>0
    
    def SetContinuousSweepState(self,value):
        '''
        设置连续模式，value取值为bool
        '''
        if value:
            cmdstring='ON'
        else :
            cmdstring ='OFF'
            
        self.Write(':INITiate:CONTinuous '+cmdstring)
    
    
    
        
    def Sweep(self):
        '''
        在单次扫描到情况下，出发一次单独扫描
        '''
        self.Write(':INITiate:IMMediate')
    
    
    def SaveStateToPath(self,filePathAndNme):
        '''
        将频谱仪当前的state设置存储到指定的文件
        '''
        self.Write(':MMEMory:STORe:STATe 1,"'+str(filePathAndNme)+'"')
      
      
        
    def LoadStateFromPath(self,filePathAndName):
        '''
         从指定路径指定文件读取state文件
        '''   
        self.Write(':MMEMory:STORe:STATe 1,"'+str(filePathAndName)+'"')
        
    
    def Preset(self):
        '''
        仪表preset
        '''
        self.Write('*RST')
    
    def ModePreset(self):
        '''
        MODE preset
        '''
        self.Write('INIT:CONT ON')
        
        
    def SAmode(self):
        '''
        进入频谱分析模式，最基本的模式
        '''
        self.Write('NST:SEL SA')
        
    def CreatMarkerViaIndex(self,markerMode,markerIndex):
        '''
        创建一个MarkerType类型的，编号为markerIndex的Marker
        '''
        self.Write(':CALCulate:MARKer'+str(markerIndex)+':MODE '+markerMode) 
    
        
    def SetMarkerFunctionViaIndex(self,markerFunction,markerIndex):
        '''
       根据MarkerIndex指定marker的funcin功能 
       
        '''
        self.Write(':CALCulate:MARKer'+str(markerIndex)+':FUNCtion '+markerFunction)
        
        
    def GetMarkerValueViaIndex(self,markerIndex):
        '''
        获取Marker的值
        '''
        return self.AskForNumber(':CALCulate:MARKer'+str(markerIndex)+':Y?')    
    
    def GetFreqValueViaIndex(self,markerIndex):
        '''
        获取Marker的值
        '''
        return self.AskForNumber(':CALCulate:MARKer'+str(markerIndex)+':X?') 
    
    def GetStartFreq(self):
        '''
        读取起始频率的值
        '''
        return self.AskForNumber('FREQ:STAR?')    
    
    def SetStartFreq(self,value):
        '''
        设置起始频率的值
        '''
        self.Write('FREQ:STAR '+str(value))
    
    
    def GetRF_Power(self,value):
        return self.AskForNumber('MEASure:RFPower?')
    def GetStopFreq(self):
        '''
        读取截止频率的值
        '''
        return self.AskForNumber('FREQ:STOP?')
    
    def SetStopFreq(self,value):
        '''
        设置截止频率的值
        '''
        self.Write('FREQ:STOP '+str(value))
#     def GetSweepPoints(self):
#         '''
#         读取扫描点数的值
#         '''
#         return self.AskForNumber('SWEep:POINts?')
#     
#     def SetSweepPoints(self,value):
#         '''
#         设置读取扫描点数
#         '''
#         self.Write('SWEep:POINts '+str(value))
    
    def GetTraceXaxis(self):
        '''
        获取当前测试Trce的横轴值X值
        '''
        startFreq=self.GetStartFreq()
        stopFreq=self.GetStopFreq()
        points=self.GetSweepPoints()
        step=(stopFreq-startFreq)/(points-1)
        xValue=[]
        for i in range(points):
            xValue.append(startFreq+step*i)
        return xValue
        
    def GetTraceYvalue(self,filename):
        '''
        读取TraceValue,Y轴值
        以文件形式存放在硬盘
        '''
        record=open(str(filename),'wb')
        self.Write("MMEM:STOR1:TRAC 1,'C:\TESTResult11.ASC'")   
        data=self.Ask(':mmem:data? "C:\TESTResult11.ASC"')
        record.write(data)
        
    def GetTraceYvalueString(self):
        '''
        读取TraceValue,Y轴值
        以字符串形式返回
        '''
#         record=open(str(filename),'wb')
        self.Write("MMEM:STOR1:TRAC 1,'C:\TESTResult11.ASC'")   
        data=self.Ask(':mmem:data? "C:\TESTResult11.ASC"')
        return data  
        
    def screenshot_save(self,filename):
        '''
        抓取屏幕截图
        '''
        record=open(str(filename),'wb')
    
        self.Write('hcop:file "D:\myfile.png"')
        data=self.Ask('mmem:tran? "D:\myfile.png"')    
        
        startIndex=data.find('\x89PNG')
        record.write(data[startIndex:])
        record.close()
        return    
        
    def SetRMSDetector(self):
        '''
        
        '''
        self.Write('DET RMS')
    def SetSweepMode(self,mode):
        '''
        WRIT/AVER/MAXH/MINH/WIEW/BLAN
        '''
        cmd='DISP:TRAC:MODE '+str(mode)
        self.Write(cmd)   
        
    def MaxHoldSweepMode(self,sweeptimes):
        self.Write('INIT:COUNT OFF')
        self.Write('SWE:COUN '+str(sweeptimes))
        self.SetSweepMode('MAXH')
        self.Write('INIT')
        self.Write('*WAI')
        
    def SetSweepTimeAuto(self,state):
        cmd='SWEep:TIME:AUTO '+str(state)
        self.Write(cmd)
        
    def PeakSearch(self):
        cmd='CALCulate:PEAKsearch' 
        self.Write(cmd)
    def SingleSweep(self):
        self.Write('INIT:CONT OFF')
        self.Write(':INITiate:IMMediate')
        self.Write('*WAI')
        
    def AllMarkerOff(self):
        self.Write('CALC:MARK:AOFF')
        
    def AutoRefLevel(self):
        cmd='ADJ:LEV'
        self.Write(cmd)
    
    def IFOverLoad_check(self):
        tmp=int(self.Ask('STAT:QUES:POW?'))
#         print tmp
#         status=bin(tmp)[2:]
#         print status
        if tmp!=0:
            return True
        else:
            return False
        
    def DisplayAlwaysOn(self):   
        self.Write(':SYSTEM:DISPLAY:UPDATE ON')
        
    def GetInputAtt(self):
        cmd='INP:ATT?'
        return self.AskForNumber(cmd)
    def SetInputAtt(self,att):
        cmd='INP:ATT '+str(att)+'dB'
        self.Write(cmd)
        
    def SetTriggerSource(self,source):
        '''
        IMM,EXT,IFP,RFP,VID,BBP,PSEN
        '''
        cmd='TRIG:SOUR '+str(source)
        self.Write(cmd)
        
    def SetVideoTriggerLevel(self,level):
        cmd='TRIG:LEV:VID '+str(level)+'PCT'
        self.Write(cmd)
        
    def PhaseNoiseTestMode(self):
        self.Write('CALC:MARK:FUNC:PNO ON')
        self.Write('CALC:DELT:FUNC:PNO ON')
        
    def DeltaMarkerSetting(self,freq):
        cmd='CALC:DELT:X '+str(freq)
        self.Write(cmd)
    def GetDeltaMarkerXValue(self):
        cmd='CALC:DELT:X ?'
        return self.AskForNumber(cmd)
    def GetDeltaMarkerYValue(self):
        cmd='CALC:DELT:Y ?'
        return self.AskForNumber(cmd)
    def GetPhaseNoiseResult(self):
        cmd='CALC:DELT:FUNC:PNO:RES?'
        return self.AskForNumber(cmd)
    def MarkerToCenter(self):
        self.Write('CALC:MARK:FUNC:CENT')
      
    def GetIdn(self):
        return self.Ask('*IDN?')
    
    def SetMarkerState(self,value):
        self.Write('CALC:MARK1 '+str(value))
        
    def SetMarkerFreq(self,value):
        self.Write('CALC:MARK1:X '+str(value))
        
    def SetMarkerDisp(self):
        self.Write('DISP:MTAB ON')
        
    def SetMarkerMode(self,value):
        self.Write('CALC:MARK1:MODE '+str(value))
#mins = SpectrumAnalyzer('TCPIP0::192.168.1.222::inst0::INSTR')
#print(mins.GetIdn())
#mins.SetCenterFrequency(700000000)






