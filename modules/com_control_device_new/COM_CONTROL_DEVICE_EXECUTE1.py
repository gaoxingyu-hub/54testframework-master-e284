# -*- coding: utf-8 -*-

"""
Module implementing DIALOG_COM_CONTROL_DEVICE_EXECUTE1.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
import os

from .Ui_COM_CONTROL_DEVICE_EXECUTE1 import Ui_Dialog
from .testResult import TestDataProtocolTransferBoard
from common.data_checker import ThDataChecker
from common.network_tools import ThNetworkTestCase
from common.logConfig import Logger
from common.info import Constants
from .com_control_device_constant import ModuleConstants

logger = Logger.module_logger("DialogComControlDeviceExecute1")
class DialogComControlDeviceExecute1(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str,object)
    test_result = {}

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogComControlDeviceExecute1, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1

    def set_contents(self,title,contents,img_file_path):
        """
        set gui display information
        :param title: dialog window title
        :param contents: dialog content browser information
        :param img_file_path: if it has,the image file full path
        :return:
        """
        try:
            self.setWindowTitle(title)
            self.textBrowser_contents.setText(contents)
            if os.path.isfile(img_file_path) and os.access(img_file_path, os.W_OK):
                self.label_img.setPixmap(QtGui.QPixmap(img_file_path))
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_execute_clicked(self):
        """
        executes the test process
        """
        ip = self.lineEdit_ip.text()
        if not ThDataChecker.is_ip(ip):
            QMessageBox.warning(self, ModuleConstants.QMESSAGEBOX_WARN,
                                ModuleConstants.QMESSAGEBOX_WARN_IP_NOT_VALID)
            return
        try:
            if self.textBrowser_log.document().blockCount() > 10:
                self.textBrowser_log.clear()
            result = ThNetworkTestCase.ping(ip, 2, 4)
            self.test_result[self.windowTitle()] = result[0]
            if result[1] != None:
                self.textBrowser_log.append("")
                for item in result[1]:
                    self.textBrowser_log.append(str(item))
            self.textBrowser_log.append("ping test:" + str(result[0]))
        except BaseException as e:
            logger.error(str(e))
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        next test case
        """
        temp = TestDataProtocolTransferBoard()
        temp.lan2 = "succcess"
        temp.lan3 = "succcess"
        temp.lan4 = "succcess"
        temp.lan5 = "succcess"
        temp.lan6 = "succcess"
        temp.lan7 = "succcess"
        temp.lan8 = "succcess"
        temp = temp.to_list()

        self._signalFinish.emit(Constants.SIGNAL_TEST_RESULT,temp)
        self._signalFinish.emit(ModuleConstants.PROCESS_CONTROL_NEXT,temp)
        self.accept()
        self.close()
