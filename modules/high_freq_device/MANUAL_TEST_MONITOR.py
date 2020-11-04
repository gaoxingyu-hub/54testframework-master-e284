# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from common.info import SystemLanguage
from .Ui_MONITOR_TEST import Ui_Dialog
import os
from PyQt5.Qt import QMessageBox
import numpy as np
if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
    from .high_freq_constant import ModuleConstants
else:
    from .high_freq_constant_fr import ModuleConstants

class MANUAL_TEST_MONITOR(QDialog, Ui_Dialog):
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
        super(MANUAL_TEST_MONITOR, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.action = 'finish_all'
    
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

        self.test_result=test_results()

        self.test_result.test_item = ModuleConstants.TESTITEM_MONITOR
        self.test_result.test_condition = '--'
        mTemp=self.testProcess()
        self.test_result.test_results=mTemp
        self.test_result.test_conclusion=mTemp
        self._signalTest.emit("test_monitor")
        if (self.checkBox_v2.isChecked() == True and 
            self.checkBox_v3.isChecked() == True and
            self.checkBox_v4.isChecked() == True and
            self.checkBox_v5.isChecked() == True and
            self.checkBox_v6.isChecked() == True and 
            self.checkBox_v8.isChecked() == True and
            self.checkBox_v9.isChecked() == True and
            self.checkBox_v10.isChecked() == True and
            self.checkBox_v11.isChecked() == True and
            self.checkBox_v12.isChecked() == True and
            self.checkBox_v13.isChecked() == True):
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_NORMAL,QMessageBox.Ok)
        else:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.TESTITEM_MONITOR+
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_ABNORMAL,QMessageBox.Ok)
        self.accept()
        self.close()
    
    
    def testProcess(self):
        temp =[]
        if self.checkBox_v2.isChecked() == True:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V2_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V2_ABNORM)
        if (self.checkBox_v3.isChecked() == False and
            self.checkBox_v4.isChecked() == False and
            self.checkBox_v5.isChecked() == False and
            self.checkBox_v6.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V3_ABNORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V3_NORM)
        if(self.checkBox_v8.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V8_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V8_ABNORM)
        if(self.checkBox_v9.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V9_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V9_ABNORM)
        if(self.checkBox_v10.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V10_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V10_ABNORM)
        if(self.checkBox_v11.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V11_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V11_ABNORM)
        if(self.checkBox_v12.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V12_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V12_ABNORM)
        if(self.checkBox_v13.isChecked() == False):
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V13_NORM)
        else:
            temp.append(ModuleConstants.TESTRESULT_MONITOR_V13_ABNORM)
            
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
        self.test_results='无本振告警'
        self.test_conclusion='PASS'