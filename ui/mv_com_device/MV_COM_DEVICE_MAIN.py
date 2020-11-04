# -*- coding: utf-8 -*-

"""
Module implementing DialogMvComDeviceMain.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_MV_COM_DEVICE_MAIN import Ui_Dialog


class DialogMvComDeviceMain(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogMvComDeviceMain, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_restart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_close_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
