from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from common.info import SystemLanguage
from modules.mw1500_device.Ui_TEST5 import Ui_Dialog
import os
from InstrumentDrivers.VNADriver import AgilentN5242
from PyQt5.Qt import QMessageBox
import numpy as np
from database.data_storage import ThTestResultsStorage
import json
from database.test_results_model import TestResultBase
from modules.mw1500_device.mw1500_constant import ModuleConstants


class DialogTest5(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    signalTest = pyqtSignal(str)
    signalFinish1 = pyqtSignal(str, object)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogTest5, self).__init__(parent)
        self.setupUi(self)
        self.action = 'finish_all'
        self.test_result=test_results()
    def set_contents(self, title, contents, img_file_path):
        try:
            self.setWindowTitle(title)
            self.textBrowser_contents.setText(contents)
            if img_file_path and img_file_path != "":
                if os.path.isfile(img_file_path) and os.access(img_file_path, os.W_OK):
                    self.pixmap = QtGui.QPixmap(img_file_path)
                    self.pixmap = self.pixmap.scaled(560,400,
                                                     Qt.KeepAspectRatio | Qt.SmoothTransformation)
                    self.label_img.setPixmap(self.pixmap)
                    self.label_img.setAlignment(Qt.AlignCenter)
        except:
            pass
        return

    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if str(self.comboBox.currentText())==ModuleConstants.ceshi_normal:
            self.test_result.test_item =ModuleConstants.shoufaxinji_nbdycs
            self.test_result.test_condition = ''
            self.test_result.test_results = str(self.comboBox.currentText())
            self.test_result.test_conclusion='PASS'
        else:
            self.test_result.test_item = ModuleConstants.shoufaxinji_nbdycs
            self.test_result.test_condition = ''
            self.test_result.test_results = str(self.comboBox.currentText())
            self.test_result.test_conclusion = 'FAIL'
            QMessageBox.information(self, ModuleConstants.tip, ModuleConstants.shoudianpingdi_gj, QMessageBox.Ok)

        self.signalTest.emit("test")
        self.signalFinish1.emit('next',None)
        self.close()
    @pyqtSlot()
    def closeEvent(self, event):
        if self.action == 'finish_all':
            self._signalFinish.emit('finish_all', None)
        event.accept()


class test_results:
    def __init__(self):
        self.test_item = ''
        self.test_condition = ''
        self.test_results = ''
        self.test_conclusion = ''