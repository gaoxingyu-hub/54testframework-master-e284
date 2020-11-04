# -*- coding: utf-8 -*-

"""
Module implementing DialogSimpleTestProcess2Btn.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_SIMPLE_TEST_PROCESS_2BTN import Ui_Dialog


class DialogSimpleTestProcess2Btn(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogSimpleTestProcess2Btn, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
