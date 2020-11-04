# -*- coding: utf-8 -*-

"""
Module implementing DIALOG_COM_CONTROL_DEVICE_EXECUTE1.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_COM_CONTROL_DEVICE_EXECUTE1 import Ui_Dialog


class DIALOG_COM_CONTROL_DEVICE_EXECUTE1(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DIALOG_COM_CONTROL_DEVICE_EXECUTE1, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_execute_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
