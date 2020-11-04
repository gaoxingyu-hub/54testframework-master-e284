# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from ui.Ui_AUTO_TEST import Ui_Dialog
import os
from InstrumentDrivers.VNADriver import AgilentN5242
from PyQt5.Qt import QMessageBox
import numpy as np

class AUTO_TEST(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalTest = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(AUTO_TEST, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.demo = True

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
            addr_sg=str(self.lineEdit_addr_sg.text())
            addr_sa=str(self.lineEdit_addr_sa.text())
        except:
            QMessageBox.warning(self, "警告", "测试参数输入不完整或格式不正确！")
            return
        addr_sg="TCPIP0::"+addr_sg+"::inst0::INSTR"
        addr_sa = "TCPIP0::" + addr_sa + "::inst0::INSTR"
        self.test_result=test_results()
        if not self.demo:
            try:
                self.sa=AgilentN5242.VNA_AgilentN5242(addr_sa)
                self.sg = AgilentN5242.VNA_AgilentN5242(addr_sg)
            except:
                QMessageBox.warning(self, "警告", "仪表连接错误！")
                print('仪表连接错误，请确认！')
                return
        self.test_result.test_item = '收发单元发射通道'
        self.test_result.test_condition = '频率:'+self.lineEdit_freq_sg.text()+'MHz，功率:'+self.lineEdit_power_sg.text()+'dBm'
        self.test_result.test_results=1+np.random.random(1)
        self.test_result.test_conclusion='PASS'
        self._signalTest.emit("test")
        self.accept()
        self.close()
    
    
    def testProcess(self):
        mres =1+ round(np.random.random(1),2)
        return mres
    
class test_results:
    def __init__(self):
        self.test_item=''
        self.test_condition=''
        self.test_results=0.0
        self.test_conclusion='PASS'