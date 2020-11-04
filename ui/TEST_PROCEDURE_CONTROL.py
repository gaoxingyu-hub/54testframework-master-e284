# -*- coding: utf-8 -*-

"""
Module implementing TEST_PROCEDURE_CONTROL.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_TEST_PROCEDURE_CONTROL import Ui_Dialog


class TEST_PROCEDURE_CONTROL(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TEST_PROCEDURE_CONTROL, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_control_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
