# -*- coding: utf-8 -*-

"""
Module implementing TestInfo.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_testInfo import Ui_Dialog


class TestInfo(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TestInfo, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        # self.setWindowTitle("213")

    @pyqtSlot()
    def on_pushButton_verify_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.accept()
        if not self.lineEdit_main_name.text().strip() or \
                not self.lineEdit_main_tuhao.text().strip() or \
                not self.lineEdit_main_serialno.text().strip():
            self.flag = -1
        return

    def set_dialog_title(self,title):
        self.setWindowTitle(title)

