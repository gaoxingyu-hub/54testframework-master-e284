# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from common.info import SystemLanguage
from .Ui_AUTO_TEST_LOOP import Ui_Dialog
import os
from InstrumentDrivers.VNADriver import AgilentN5242
from PyQt5.Qt import QMessageBox
import numpy as np
from InstrumentDrivers.SignalGeneratorDriver import SignalGenerator
from InstrumentDrivers.SpectrumAnalyzerDriver import SpectrumAnalyzer
import time
if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
    from .high_freq_constant import ModuleConstants
else:
    from .high_freq_constant_fr import ModuleConstants

class AUTO_TEST_LOOP(QDialog, Ui_Dialog):
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
        super(AUTO_TEST_LOOP, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.demo = True
        self.action = 'finish_all'
    
    def initUi(self,mConfig):
        self.addr_sg= ModuleConstants.IP_SG
        self.addr_sa= ModuleConstants.IP_SA
        freq_sg= mConfig.test_case_detail[3]["test_para"][0]
        power_sg= mConfig.test_case_detail[3]["test_para"][1]
        freq_sa= mConfig.test_case_detail[3]["test_para"][2]
        bw_sa= mConfig.test_case_detail[3]["test_para"][3]
        self.lineEdit_freq_sg.setText(freq_sg)
        self.lineEdit_power_sg.setText(power_sg)
        self.lineEdit_freq_sa.setText(freq_sa)
        self.lineEdit_bw_sa.setText(bw_sa)
        self.thresholdL = float(mConfig.test_case_detail[3]["threshold"][0])
        self.thresholdH = float(mConfig.test_case_detail[3]["threshold"][1])
    
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
            self.freq_sg=float(self.lineEdit_freq_sg.text())*1e6
            self.power_sg=float(self.lineEdit_power_sg.text())
            self.freq_sa=float(self.lineEdit_freq_sa.text())*1e6
            self.bw_sa=float(self.lineEdit_bw_sa.text())*1e6
            addr_sg=str(self.addr_sg)
            addr_sa=str(self.addr_sa)
        except:
            QMessageBox.warning(self, ModuleConstants.QMESSAGEBOX_WARN, 
                                ModuleConstants.QMESSAGEBOX_WARN_INPUT_PARAMETER_NOT_ENOUGH)
            return
        addr_sg="TCPIP0::"+addr_sg+"::inst0::INSTR"
        addr_sa = "TCPIP0::" + addr_sa + "::inst0::INSTR"
        self.test_result=test_results()
        if not self.demo:
            try:
                self.sa=SpectrumAnalyzer.SpectrumAnalyzer(addr_sa)
                self.sg = SignalGenerator.SignalGenerator(addr_sg)
            except:
                QMessageBox.warning(self,ModuleConstants.QMESSAGEBOX_WARN, 
                                    ModuleConstants.QMESSAGEBOX_WARN_INSTR_NOT_VALID)
                return
        self.test_result.test_item = ModuleConstants.TESTITEM_LOOP
        self.test_result.test_condition = ModuleConstants.TESTCONDITION_FREQ+self.lineEdit_freq_sg.text()+\
                                          ModuleConstants.TESTCONDITION_FREQ_UNIT+'，'+ModuleConstants.TESTCONDITION_POWER+\
                                          self.lineEdit_power_sg.text()+ModuleConstants.TESTCONDITION_POWER_UNIT
 
        self.test_result.test_results=self.testProcess()
        if self.thresholdL<self.test_result.test_results <self.thresholdH:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_NORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_PASS
        else:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.TESTITEM_LOOP+
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_ABNORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_FAIL
        self._signalTest.emit("test")
        self.accept()
        self.close()
    
    
    def testProcess(self):
        if not self.demo:
            self.sg.SetFrequency(self.freq_sg)
            self.sg.SetRFPower(self.power_sg)
            self.sg.SetModeState(0)
            self.sg.SetOutputState(1)
            self.sa.SetCenterFrequency(self.freq_sa)
            self.sa.SetSpan(self.bw_sa)
            self.sa.AutoRefLevel()
            self.sa.SetMarkerMode('POS')
            self.sa.SetMarkerFreq(self.freq_sa)
            mres=self.sa.GetMarkerValueViaIndex(1)
            time.sleep(0.5)
            self.sa.Preset()
            self.sg.Preset()

        else:
            mres =float(2+ np.random.random(1))
        return round(float(mres),3)
    
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