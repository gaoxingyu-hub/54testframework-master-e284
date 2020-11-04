# -*- coding: utf-8 -*-

"""
Module implementing DialogComControlDeviceExecute4.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
import os

from .Ui_COM_CONTROL_DEVICE_EXECUTE4 import Ui_Dialog
from common.info import Constants,ThCommonNoticeInfo
from .testResult import TestDataProtocolTransferAndControl3
from .test_process import ThComControlDeviceTestProcess,UdpServerThread
from common.data_checker import ThDataChecker
from common.logConfig import Logger
from .com_control_device_constant import ModuleConstants

logger = Logger.module_logger("DialogComControlDeviceExecute4")
class DialogComControlDeviceExecute4(QDialog, Ui_Dialog):
    """
    _signalFinish:str,signal for com_control_device main form
                    to send information or results
    test_result:dict,test result
    """
    _signalFinish = pyqtSignal(str, object)
    test_result = {}

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogComControlDeviceExecute4, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
    
    @pyqtSlot()
    def on_radioButton_rs232_clicked(self):
        """
        set device setting as rs232
        """
        self.radioButton_rs232.setChecked(True)
        self.radioButton_rs485.setChecked(False)
    
    @pyqtSlot()
    def on_radioButton_rs485_clicked(self):
        """
        set device setting as rs485
        """
        self.radioButton_rs232.setChecked(False)
        self.radioButton_rs485.setChecked(True)
    
    @pyqtSlot()
    def on_pushButton_test_clicked(self):
        """
        start test:send udp packet
        """
        self.udp_sender = ThComControlDeviceTestProcess()
        self.udp_sender.udp_send(self.remote_ip, self.remote_port)
    
    @pyqtSlot()
    def on_pushButton_remote_link_clicked(self):
        """
        create local udp server and listen
        """
        self.local_ip = self.lineEdit_local_ip.text()
        self.local_port = self.lineEdit_local_port.text()
        self.remote_ip = self.lineEdit_remote_ip.text()
        self.remote_port = self.lineEdit_remote_port.text()

        if not ThDataChecker.is_ip(self.local_ip) or not ThDataChecker.is_ip(self.remote_ip):
            QMessageBox.warning(self, ThCommonNoticeInfo.WARN, ThCommonNoticeInfo.ILLEGAL_IP_ADDRESS)
            return
        self.udp_server = UdpServerThread(self.local_ip, self.local_port, ModuleConstants.UDP_SEND_CONTENTS)
        self.udp_server._signalInfo.connect(self.signal_slot)
        self.udp_server.start()
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        next test case
        """
        temp = TestDataProtocolTransferAndControl3()
        temp.com9 = "succcess"
        temp = temp.to_list()
        self._signalFinish.emit(Constants.SIGNAL_TEST_RESULT, temp)
        self._signalFinish.emit(ModuleConstants.PROCESS_CONTROL_FINISH, temp)
        self.accept()
        self.close()


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

    def signal_slot(self,signal,para):
        """
        test process thread signal slot
        :param signal: Constant Signal
        :param para: object,str or dict
        :return:
        """
        if signal == Constants.SIGNAL_INFORMATION:
            if self.textBrowser_log.document().blockCount() > 10:
                self.textBrowser_log.clear()
            self.textBrowser_log.append(para)
        elif signal == Constants.SIGNAL_TEST_RESULT:
            self.test_result.update(para)
