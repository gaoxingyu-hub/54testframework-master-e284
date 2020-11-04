# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from common.info import SystemLanguage
from .Ui_AUTO_TEST_COUPLER import Ui_Dialog
import os
from InstrumentDrivers.VNADriver import AgilentN5242
from PyQt5.Qt import QMessageBox
import numpy as np
if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
    from .high_freq_constant import ModuleConstants
else:
    from .high_freq_constant_fr import ModuleConstants

class AUTO_TEST_COUPLER(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalTest = pyqtSignal(str)
    _signalFinish = pyqtSignal(str,object)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(AUTO_TEST_COUPLER, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.demo = True
        self.action = 'finish_all'

    def initUi(self,mConfig):
        self.addr_na= self.addr_na= ModuleConstants.IP_NA
        freq_na= mConfig.test_case_detail[6]["test_para"][0]
        bw_na= mConfig.test_case_detail[6]["test_para"][1]
        self.lineEdit_freq_na.setText(freq_na)
        self.lineEdit_bw_na.setText(bw_na)
        self.thresholdL = float(mConfig.test_case_detail[6]["threshold"][0])
        self.thresholdH = float(mConfig.test_case_detail[6]["threshold"][1])
    
    def set_contents(self,title,contents):
        self.setWindowTitle(title)
#         self.textBrowser_contents.setText(contents)
        # if os.access(img_file_path, os.W_OK):
        #     self.label_img.setPixmap(QtGui.QPixmap(img_file_path))
        # return
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            self.freq_na=float(self.lineEdit_freq_na.text())*1e6
            self.bw_na=float(self.lineEdit_bw_na.text())*1e6
            addr_na=str(self.addr_na)
        except:
            QMessageBox.warning(self, ModuleConstants.QMESSAGEBOX_WARN, 
                                ModuleConstants.QMESSAGEBOX_WARN_INPUT_PARAMETER_NOT_ENOUGH)
            return
        addr_na="TCPIP0::"+addr_na+"::inst0::INSTR"

        self.test_result=test_results()
        if not self.demo:
            try:
                self.na=AgilentN5242.VNA_AgilentN5242(addr_na)
            except:
                QMessageBox.warning(self,ModuleConstants.QMESSAGEBOX_WARN, 
                                    ModuleConstants.QMESSAGEBOX_WARN_INSTR_NOT_VALID)
                return
        self.test_result.test_item = ModuleConstants.TESTITEM_COUPLER
#         self.test_result.test_condition = '频率:4400,4700,5000'+self.lineEdit_freq_na.text()+'MHz，带宽:'+self.lineEdit_bw_na.text()+'MHz'
        self.test_result.test_condition = ModuleConstants.TESTCONDITION_FREQ+'4400,4700,5000'
        mTemp=self.testProcess()
        self.test_result.test_results=str(mTemp[0])+', '+str(mTemp[1]) +', '+str(mTemp[2])
        if self.thresholdL<mTemp[0]<self.thresholdH and self.thresholdL<mTemp[1]<self.thresholdH and self.thresholdL<mTemp[2]<self.thresholdH:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_NORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_PASS
        else:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.TESTITEM_COUPLER+
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_ABNORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_FAIL
        self._signalTest.emit("test")
        self.accept()
        self.close()
    
    
    def testProcess(self):
        temp =[]
        if not self.demo:
            self.na.SetCentreFreq(self.freq_na)
            self.na.SetSpan(self.bw_na)
            self.na.SelectMeas('1')
            self.na.SetMarkerMode('NORM')
            self.na.SetMarkerX(self.freq_na-300000000)
            mTemp1 = float(self.na.GetMarkerY())
            mTemp1 = round(mTemp1,3)
            
            self.na.SetMarkerX(self.freq_na)
            mTemp2 = float(self.na.GetMarkerY())
            mTemp2 = round(mTemp2,3)
            
            self.na.SetMarkerX(self.freq_na+300000000)
            mTemp3 = float(self.na.GetMarkerY())
            mTemp3 = round(mTemp3,3)
            
            temp.append(mTemp1) 
            temp.append(mTemp2)
            temp.append(mTemp3)
        else:
            temp.append(float(7+ np.random.random(1)))
            temp.append(float(7+ np.random.random(1)))
            temp.append(float(7+ np.random.random(1)))
        return temp
    
    @pyqtSlot()
    def closeEvent(self, event):
        if self.action == 'finish_all':
            self._signalFinish.emit('finish_all', None)
        event.accept()
        
class test_results:
    def __init__(self):
        self.test_item=''
        self.test_condition=''
        self.test_results=0.0
        self.test_conclusion='PASS'
# 
# mres =float(7+ np.random.random(1))
# print(round(mres,3))