# -*- coding: utf-8 -*-

"""
Module implementing Dialog_COM_CONTROL_DEVICE_EXECUTE3.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_COM_CONTROL_DEVICE_EXECUTE3 import Ui_Dialog


class Dialog_COM_CONTROL_DEVICE_EXECUTE3(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_COM_CONTROL_DEVICE_EXECUTE3, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_local_disconnect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_remote_link_clicked(self):
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
