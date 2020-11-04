# -*- coding: utf-8 -*- 
'''
Created on 2015.10.14

@author: Penghan Xie
'''

from .VectorNetworkAnalyzer import VNA
import re,string,os
import time
# from enable.enable_traits import LineStyle
# from enaml.qt.editor.generate_browser_safe import filename

class RS_ZVT(VNA):
    '''
    R&S矢量网络分析仪底层驱动，包括ZVA,ZVB,ZVT系列
    '''
    def __init__(self,Addr):
        VNA.__init__(self,Addr)
        
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
    
    def setSweepTime(self,SweepTime):
        cmd='SENSe:SWEep:TIME '+ str(SweepTime) 
        self.Write(cmd)
        
    def SweepTimeAuto(self,status):
        cmd='SENSe:SWEep:TIME:AUTO '+status 
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
        
    def DeletAllMeas(self):
        cmd='CALC:PAR:DEL:ALL'
        self.Write(cmd) 
        
    def CreateMeas(self,TraceName,MeasType):
        '''
        CALCulate<Ch>:PARameter:DEFine '<string>', S11 | ... | S44 | A | B | C | D | R1 | R2
| R3 | R4 | AB | AC | AD | BA | BC | BD | CA | CB | CD | DA | DB | DC | AR1 | ... | DR4 |
R1A | ... | R4D | R1R2 | ... | R4R3, [<numeric_value>
        '''
        cmd='CALC:PAR:SDEF '+"'"+TraceName+"'"+','+"'"+MeasType+"'"
        self.Write(cmd) 
        
    def DisplayMultiTrace(self,traceNO,TraceName):  
        cmd = 'DISP:WIND:TRACE'+str(traceNO)+':FEED '+"'"+TraceName+"'" 
        self.Write(cmd)
           
    def DisplayMeas(self,TraceName):  
        cmd = 'DISP:WIND:TRACE:FEED '+"'"+TraceName+"'" 
        self.Write(cmd)
        
    def SelectMeas(self,TraceName):
        cmd = 'CALC:PAR:SEL '+"'"+TraceName+"'"
        self.Write(cmd)
        
    def DataFormat(self):
        self.Write('FORMat ASCII')  
    def setExtTigger(self):
          
        cmd='trig:sour ext'
        self.Write(cmd)
        time.sleep(0.02)
    def GetTraceData(self,DataFormat):
        cmd='CALC:DATA? '+str(DataFormat)
        time.sleep(1)
        Temp=self.Ask(cmd)
        #TraceData=Temp.Spilt('')
        return Temp.split(',')
    
    def MeasQ_F_Loss(self):
        self.Write('CALC:MARK:FUNC:BWID:MODE BPAS')   
        self.Write('CALC:MARK:FUNC:BWID:GMC OFF')   
        self.Write('CALC:MARK:FUNC:BWID:GMC OFF')   
        self.Write('CALC:MARK:FUNC:EXEC BFIL')
        self.Write('CALC:MARK:SEAR:BFIL:RES ON')
        self.Write('CALC:MARK:BWID 3')
        Temp=self.Ask('CALC:MARK:BWID?')
        return Temp.split(',')
    
    def MarkerSearchLeft(self):
        '''
        This command is the ZVR-compatible equivalent of
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:EXECute LPEak
        '''
        cmd='CALCulate:MARKer:SEARch:LEFT'
        self.Write(cmd)
        
    def MarkerSearchRight(self):
        '''
        This command is the ZVR-compatible equivalent of
        CALCulate<Chn>:MARKer<Mk>:FUNCtion:EXECute RPEak
        '''
        cmd='CALCulate:MARKer:SEARch:RIGHt'
        self.Write(cmd)
        
    def SetMarker(self,MarkerNO,status):
        cmd='CALC:MARK'+str(MarkerNO)+' '+str(status)
        self.Write(cmd)

    def DefineMarkerXValue(self,markerno,X):
        cmd='CALC:MARK'+str(markerno)+':X '+str(X)
        self.Write(cmd)   
        
    def GetXValueofMarker(self,markerno):
        cmd='CALC:MARK'+str(markerno)+':X?'
        return float(self.Ask(cmd))
    def GetYValueofMarker(self,markerno):
        cmd='CALC:MARK'+str(markerno)+':Y?'
        value=self.Ask(cmd)
        time.sleep(0.1)
        return float(value) 
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
    def DefTwoPortThrough(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',FRTRans,1,2'
        self.Write(cmd)    
    def DefineTRLMethod(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',TRL,1,2'
        self.Write(cmd)  
    def DefOnePortNormalizeMethodForPort2(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',RSHort,2'
        self.Write(cmd)
        
        
    def DefFullOnePort2(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',FOP,2'
        self.Write(cmd)
    def DefOnePortNormalizeMethodForPort1(self,calname):
        cmd=':SENSe1:CORRection:COLLect:METHod:DEFine '+"'"+calname+"'"+',RSHort,1'
        self.Write(cmd)
    def ThoughCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected THRough, 1, 2')
        
    def Port1OpenCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected OPEN, 1')
        
    def Port2OpenCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected OPEN, 2')
        
    def Port1ShortCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected SHORT, 1')
        
    def Port2ShortCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected SHORT, 2')
        
        
        
    def Port1MathchCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected MATCH, 1')   
        
    def Port2MathchCal(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected MATCH, 2')    
        
    def Port1Reflect(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected REFL, 1')
        
    def Port2Reflect(self):
        self.Write(':SENSe1:CORRection:COLLect:ACQuire:SELected REFL, 2')
        
    def LineCal(self):
        cmd=':SENSe1:CORRection:COLLect:ACQuire:SELected LINE1, 1,2'
        self.Write(cmd)

    def LineCal2(self):
        cmd = ':SENSe1:CORRection:COLLect:ACQuire:SELected LINE2, 1,2'
        self.Write(cmd)
    
    def ApplyCal(self):
        self.Write(':SENSe1:CORRection:COLLect:SAVE:SELected')
        
        
    def StoreCalResult(self,filename):
        cmd='MMEMory:STORe:STATe 1, '+"'"+filename+".znx'"
#         cmd = ':MMEMORY:STORE:CORRection 1, ' + "'" + filename + '.cal' + "'"
        self.Write(cmd)
        time.sleep(1)
        
    def MakeNewDirectory(self,dir):
        exits = self.Ask('MMEMory:CATalog:ALL? "'+dir+'"')

        if exits=='':
            self.Write('*cls')
            cmd='MMEMory:MDIRectory "'+dir+'"'
            self.Write(cmd)
    def file_exists(self,finlename):
        
        return True
           
#     def LoadCalResult(self,filename):
#         dir,name = os.path.split(filename)
#         cmd="MMEMory:CDIRectory "+"'"+dir+"'"
#         print cmd
#         print name
#         self.Write(cmd)
#         cmd='MMEMory:LOAD:CORRection 1, '+"'"+name+".cal'"
#         self.Write(cmd)
#         time.sleep(1)
        
    def LoadCalResult(self,filename):
        cmd='MMEMory:LOAD:STATe 1, '+"'"+filename+".znx'"
        self.Write(cmd)
        time.sleep(1)
#         cmd=':MMEMORY:LOAD:CORRection 1, '+"'"+filename+'.cal'+"'"
#         self.Write(cmd)
        
    def create_sub_dir(self,dir):
        fawk_name=dir+'.txt'
        parent_dir=os.path.dirname(fawk_name)
        result=self.Ask("MMEMory:CATalog? "+"'"+parent_dir+"'")
        result=result.replace(' ','')
        result_list = result.split(',')
        only_dir_name=dir.replace(parent_dir,'')
        only_dir_name=only_dir_name.replace('\\','')
        if only_dir_name.lower() in result_list:
            return
        else:
        
            cmd='MMEMory:MDIRectory '+"'"+dir+"'"    
            self.Write(cmd)                             
        
    def PeakSearch(self):   
        self.Write('CALC:MARK:FUNC:EXEC MAX' )
        temp=self.Ask('CALC:MARKer:FUNC:RESult?')
        return temp.split(',')
    
    def SingleSweep(self):
        self.Write(':INITIATE:CONTINUOUS OFF')
        self.Write(':INITiate1:IMMediate')
        self.Write('*WAI')
        time.sleep(1)
        
    def ContinuousSweep(self):
        self.Write('INIT:CONT:ALL ON')
    def AutoScale(self):
        cmd='DISP:WIND:TRAC:Y:AUTO ONCE'
        self.Write(cmd)
        
    def WaitOpc(self):
        cmd='*OPC?'
        self.ask(cmd)
        
    def CWMode(self):
        cmd='SENS:SWEEP:TYPE CW'
        self.Write(cmd)
        
    def pulseMode(self):
        cmd='swe:type puls'
        self.Write(cmd)
#         cmd='puls:time:star -10 us;stop 200 us'
#         self.Write(cmd)
        self.SetTracePoint(1601)
        
    def setcwfreq(self,freqinHz):
        cmd='sour:freq:cw '+str(freqinHz)
        self.Write(cmd)
        
    def max_maker_value(self):
        cmd='calc:mark on'
        self.Write(cmd)
        cmd=':calc:mark:func:exec max'
        self.Write(cmd)
        
        return self.GetYValueofMarker(1)
    
    def min_maker_value(self):
        cmd='calc:mark on'
        self.Write(cmd)
        cmd=':calc:mark:func:exec min'
        self.Write(cmd)
        time.sleep(0.02)
        
        return self.GetYValueofMarker(1)
    
    def setMannulTrigger(self):
        cmd='trig:sour man'
        self.Write(cmd)
        time.sleep(0.02)
        pass
        
    def trigger_man(self):
        cmd='*trg'
        self.Write(cmd)
        time.sleep(0.02)
        pass
    
    def SetExternalRef(self):
        cmd='ROSC EXT'
        self.Write(cmd)
        time.sleep(0.02)
        
    def screenshot_save(self,filename):
        '''
        抓取屏幕截图
        '''
        self.Write('HCOP:DEST "MMEM"')
        self.Write('HCOP:DEV:LANG PNG')
        self.Write('MMEM:NAME "C:\Temp\Print.png"')
        self.Write('HCOP:IMMediate') 
        data=self.Ask('MMEM:DATA? "C:\Temp\Print.png"')    
        time.sleep(0.5)
        startIndex=data.find('\x89PNG')
        record=open(str(filename),'wb')
        record.write(data[startIndex:])
        record.close()
        return
    