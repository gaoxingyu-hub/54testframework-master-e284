# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from common.info import SystemLanguage
from .Ui_SWITCH_TEST import Ui_Dialog
import os
from PyQt5.Qt import QMessageBox
import numpy as np
if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
    from .high_freq_constant import ModuleConstants
else:
    from .high_freq_constant_fr import ModuleConstants

class MANUAL_TEST_SWITCH(QDialog, Ui_Dialog):
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
        super(MANUAL_TEST_SWITCH, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.demo = True
        self.action = 'finish_all'
    
    def initUi(self,mConfig):
        self.threshold = mConfig.test_case_detail[5]["threshold"][0]
    
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

        self.test_result.test_item = ModuleConstants.TESTITEM_SWITCH
        self.test_result.test_condition = '--'
        self.test_result.test_results=str(self.testProcess())
        if self.test_result.test_results ==self.threshold:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_NORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_PASS
        else:
            QMessageBox.information(self,ModuleConstants.QMESSAGEBOX_INFO,ModuleConstants.TESTITEM_SWITCH+
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_ABNORMAL,QMessageBox.Ok)
            self.test_result.test_conclusion=ModuleConstants.TESTRESULT_FAIL

        self._signalTest.emit("test_switch")
        self.accept()
        self.close()
    
    
    def testProcess(self):
        mres = str(self.comboBox_sg_addr.currentText())
        return mres
    
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