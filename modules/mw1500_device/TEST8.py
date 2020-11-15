from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QDialog, QGraphicsItem, QScrollArea
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from modules.mw1500_device.Ui_TEST8 import Ui_Dialog
import os
#
from PyQt5.QtCore import pyqtSignal
from common.info import Constants
from PyQt5 import QtGui
from common.logConfig import Logger
from PyQt5.QtWidgets import QMessageBox
from modules.mw1500_device.mw1500_constant import ModuleConstants


class DialogTest8(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    signalFinish1 = pyqtSignal(str, object)
    signalTest = pyqtSignal(object)
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogTest8, self).__init__(parent)
        self.setupUi(self)
        self.action = 'finish_all'
        self.test_result = test_results()
    def initUi(self, mConfig):
        self.lineEdit_1.setText(mConfig.test_case_detail[2]["test_para"][2])
        self.lineEdit_2.setText(mConfig.test_case_detail[2]["test_para"][3])
    def set_contents(self, title, contents, img_file_path):
        """
        set gui display information
        :param title: dialog window title
        :param contents: tips
        :param img_file_path:image file full path
        :return: none
        """
        try:
            self.setWindowTitle(title)
            self.textBrowser_contents.setText(contents)
            if img_file_path and img_file_path != "":
                if os.path.isfile(img_file_path) and os.access(img_file_path, os.W_OK):
                    self.pixmap = QtGui.QPixmap(img_file_path)
                    self.pixmap = self.pixmap.scaled(560, 400,
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
        if str(self.comboBox.currentText())==ModuleConstants.ceshi_normal:
            self.test_result.test_item=ModuleConstants.shuanggongqi_cs
            self.test_result.test_condition = ''
            self.test_result.test_results = str(self.comboBox.currentText())
            self.test_result.test_conclusion = 'PASS'
            QMessageBox.information(self, ModuleConstants.tip,str(self.comboBox.currentText()), QMessageBox.Ok)
            self.signalTest.emit('test')
            self.signalFinish1.emit('next', None)

        else:
            self.test_result.test_item =ModuleConstants.shuanggongqi_cs
            self.test_result.test_condition = ''
            self.test_result.test_results = str(self.comboBox.currentText())
            self.test_result.test_conclusion = 'FAIL'
            QMessageBox.information(self, ModuleConstants.tip,ModuleConstants.shuanggingqi_gz, QMessageBox.Ok)
            self.signalTest.emit('test')
        self.close()

class test_results:
    def __init__(self):
        self.test_item = ''
        self.test_condition = ''
        self.test_results = ''
        self.test_conclusion = ''