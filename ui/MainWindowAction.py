# -*- coding: utf-8 -*-

"""
Module implementing MainWindowAction.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_MainWindow import Ui_MainWindow


class MainWindowAction(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindowAction, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action_about_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_action_help_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
