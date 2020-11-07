from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QDialog, QGraphicsItem, QScrollArea
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

from modules.mw1500_device.Ui_TEST3 import Ui_Dialog
import os
from PyQt5.QtCore import pyqtSignal
from common.info import Constants
from PyQt5 import QtGui
from common.logConfig import Logger
from PyQt5.QtWidgets import QMessageBox

from modules.mw1500_device.mw1500_constant import ModuleConstants

logger = Logger.module_logger("")
#
class DialogTest3(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    signalTest = pyqtSignal(object)
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogTest3, self).__init__(parent)
        self.setupUi(self)
        self.demo=True
        self.action = 'finish_all'
        self.test_result=test_results()

    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        self.test_result.test_item =ModuleConstants.qinwuhua
        self.test_result.test_condition = ''
        self.test_result.test_results = ''
        self.test_result.test_conclusion = 'PASS'
        QMessageBox.information(self, ModuleConstants.tip,ModuleConstants.qinwuhua_normal, QMessageBox.Ok)
        self.signalTest.emit('test')
        self.close()


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.test_result.test_item = ModuleConstants.qinwuhua
        self.test_result.test_condition = ''
        self.test_result.test_results = ''
        self.test_result.test_conclusion = 'FAIL'
        QMessageBox.information(self, ModuleConstants.tip, ModuleConstants.qinwuhua_panne, QMessageBox.Ok)
        self.signalTest.emit('test')
        self.close()



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
    def closeEvent(self, event):
        if self.action == 'finish_all':
            self.signalFinish1.emit('finish_all', None)
        event.accept()


class test_results:
    def __init__(self):
        self.test_item = ''
        self.test_condition = ''
        self.test_results = ''
        self.test_conclusion = ''
