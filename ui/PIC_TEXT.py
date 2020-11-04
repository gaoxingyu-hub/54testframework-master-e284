# -*- coding: utf-8 -*-

"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_PIC_TEXT import Ui_Dialog


class PIC_TEXT(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PIC_TEXT, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):

        pass
