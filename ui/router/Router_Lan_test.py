# -*- coding: utf-8 -*-

"""
Module implementing DialogRouterLanTest.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Router_Lan_test import Ui_Dialog


class DialogRouterLanTest(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogRouterLanTest, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_process_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
