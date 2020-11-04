# -*- coding: utf-8 -*-

"""
Module implementing DialogEcomNs1KeyTest.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_ECOM_NS1_KEY_TEST import Ui_Dialog


class DialogEcomNs1KeyTest(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogEcomNs1KeyTest, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_process_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
