# -*- coding: utf-8 -*-

"""
Module implementing DialogEcomNs2Ping.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_ECOM_NS2_Ping import Ui_Dialog


class DialogEcomNs2Ping(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogEcomNs2Ping, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_ping_clicked(self):
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
