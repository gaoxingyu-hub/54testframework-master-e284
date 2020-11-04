# -*- coding: utf-8 -*-

"""
Module implementing DialogEcomNs2Ping.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
import os

from .Ui_ECOM_NS2_Ping import Ui_Dialog
from common.logConfig import Logger
from common.data_checker import ThDataChecker
from common.network_tools import ThNetworkTestCase
from ..sdsl.SDSL_CONSTANT import ModuleConstants

logger = Logger.module_logger("EcomNs2Ping")
class EcomNs2Ping(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str, object)
    test_result = {}

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(EcomNs2Ping, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
    
    @pyqtSlot()
    def on_pushButton_ping_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ip = self.lineEdit_ip_address.text()
        if not ThDataChecker.is_ip(ip):
            QMessageBox.warning(self, ModuleConstants.QMESSAGEBOX_WARN, ModuleConstants.QMESSAGEBOX_WARN_IP_NOT_VALID)
            return

        if self.textBrowser_log.document().blockCount() > 10:
            self.textBrowser_log.clear()
        result = ThNetworkTestCase.ping(ip, 2, 4)
        self.test_result[self.windowTitle()] = result[0]
        if result[1] != None:
            self.textBrowser_log.append("")
            for item in result[1]:
                self.textBrowser_log.append(str(item))
        self.textBrowser_log.append("ping test:" + str(result[0]))

    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        data = None
        self._signalFinish.emit(self.windowTitle(), self.test_result)
        self.accept()
        self.close()

    def set_contents(self,title,contents,img_file_path):
        try:
            self.setWindowTitle(title)
            self.textBrowser_tips.setText(contents)
        except BaseException as e:
            logger.error(str(e))
