# -*- coding: utf-8 -*-

"""
Module implementing DialogTestProcess.
"""
import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog

from modules.general.frame_loss import start_test
from renix_py_api.renix_common_api import get_sys_entry
from renix_py_api.renix import *
from renix_py_api.api_gen import *
from renix_py_api.core import EnumRelationDirection
from renix_py_api.rom_manager import *

from common.logConfig import Logger
from renix_py_api.renix import initialize
from .Ui_TestProcess import Ui_Dialog

logger = Logger.module_logger("TestProcess")


class DialogTestProcess(QDialog, Ui_Dialog):
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
        super(DialogTestProcess, self).__init__(parent)
        self.setupUi(self)
        self.result = 'fail'


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        initialize()
        sys_entry = get_sys_entry()
        self.result = start_test(sys_entry)
        if self.result == 'pass':
            # IP数据加解密
            self.test_result["IP数据加解密"] = "正常"
        else:
            self.test_result["IP数据加解密"] = "不正常"
        shutdown()
        self._signalFinish.emit(self.windowTitle(), self.test_result)
        self.accept()
        self.close()

    def set_contents(self, title, contents, img_file_path):
        """
        set Dialog's contents (在Lan测试中参数)
        :param title:
        :param contents:
        :param img_file_path:
        :return:
        """
        try:
            self.setWindowTitle(title)
            self.label.setText(contents)
        except BaseException as e:
            logger.error(str(e))

