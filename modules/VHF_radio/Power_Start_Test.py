# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from .UI.UI_radio_start import Ui_Dialog
import os
from InstrumentDrivers.VNADriver import AgilentN5242
from PyQt5.Qt import QMessageBox
import numpy as np
from database.data_storage import ThTestResultsStorage
import json
from database.test_results_model import TestResultBase
from InstrumentDrivers.SpectrumAnalyzerDriver import SpectrumAnalyzer
from .vhf_radio_constant import ModuleConstants


class Power_Start_Test(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalTest = pyqtSignal(str)
    _signalFinish = pyqtSignal(str, object)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Power_Start_Test, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.demo = True
        self.action = 'finish_all'

    #         self.testData()

    def initUi(self, mConfig):
        self.maddress = ModuleConstants.IP_SA
        self.threshold = mConfig.test_case_detail[0]["threshold"][0]

    #         self.lineEdit_addr_sa.setText(maddress)

    def set_contents(self, title, contents):
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

        self.test_result = test_results()
        addr_sa = str(self.maddress)
        addr_sa = "TCPIP0::" + addr_sa + "::inst0::INSTR"
        if not self.demo:
            try:
                self.sa = SpectrumAnalyzer.SpectrumAnalyzer(addr_sa)
            except:
                QMessageBox.warning(self, ModuleConstants.QMESSAGEBOX_WARN,
                                    ModuleConstants.QMESSAGEBOX_WARN_INSTR_NOT_VALID)
                return
        self.test_result.test_item = ModuleConstants.TESTITEM_TR_LO
        self.test_result.test_condition = '--'
        self.test_result.test_results = str(self.testProcess())
        if self.test_result.test_results == self.threshold:
            QMessageBox.information(self, ModuleConstants.QMESSAGEBOX_INFO,
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_NORMAL, QMessageBox.Ok)
            self.test_result.test_conclusion = ModuleConstants.TESTRESULT_PASS
        else:
            QMessageBox.information(self, ModuleConstants.QMESSAGEBOX_INFO, ModuleConstants.TESTITEM_TR_LO +
                                    ModuleConstants.QMESSAGEBOX_CONTENTS_TEST_ABNORMAL, QMessageBox.Ok)
            self.test_result.test_conclusion = ModuleConstants.TESTRESULT_FAIL
        self._signalTest.emit("test_lo")
        self.accept()
        self.close()

    def testProcess(self):

        mres = str(self.comboBox_sg_addr.currentText())
        return mres

    def testData(self):
        temp = TestResultBase()
        temp.testObjName = "1"
        temp.stationName = "2"
        temp.stationDrawingNbr = "3"
        temp.stationSn = "4"
        temp.unitName = "5"
        temp.unitDrawingNbr = "6"
        temp.unitSn = "7"
        temp.dutName = "8"
        temp.dutDrawingNbr = "9"
        temp.dutSn = "10"
        temp.testTime = "2020-02-14 12:00:00"

        temp.testItems = test_results()
        temp.testItems.test_item = '本振故障定位'
        temp.testItems.test_condition = '--'
        temp.testItems.test_results = '无告警'
        temp.testItems.test_conclusion = 'PASS'
        ThTestResultsStorage.test_case_result_storage(temp)

    #     @pyqtSlot()
    #     def closeEvent(self, event, mAction = ''):
    #
    #         self._signalFinish.emit('finish', None)
    #
    #         event.accept()

    @pyqtSlot()
    def closeEvent(self, event):
        if self.action == 'finish_all':
            self._signalFinish.emit('finish_all', None)
        event.accept()


#         reply = QMessageBox.information(self,                         #使用infomation信息框
#                                     u"正在测试中！",
#                                     u"请确认是否退出后续所有测试",
#                                     QMessageBox.Yes | QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             self._signalFinish.emit('finish', None)
#             event.accept()
# #                 sys.exit(app.exec_())
#         else:
#             self._signalFinish.emit('next', None)
#             event.ignore()


class test_results:
    def __init__(self):
        self.test_item = ''
        self.test_condition = ''
        self.test_results = '无本振告警'
        self.test_conclusion = 'PASS'



