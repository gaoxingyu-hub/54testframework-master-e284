from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QDialog, QGraphicsItem, QScrollArea
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from modules.mw1500_device.Ui_TEST6 import Ui_Dialog
import os
#
from PyQt5.QtCore import pyqtSignal
from common.info import Constants
from PyQt5 import QtGui
from common.logConfig import Logger
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import time

from modules.mw1500_device.mw1500_constant import ModuleConstants


class DialogTest6(QDialog, Ui_Dialog):
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
        super(DialogTest6, self).__init__(parent)
        self.setupUi(self)
        self.action = 'finish_all'
        self.demo=True
        self.test_result=test_results()
    def initUi(self, mConfig):
        self.mConfig=mConfig
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
        for i in range(6):
            self.lineEdit_1.setText(self.mConfig.test_case_detail[2]["test_para1"][i])
            self.lineEdit_2.setText(self.mConfig.test_case_detail[2]["test_para"][0])
            self.lineEdit_3.setText(self.mConfig.test_case_detail[2]["test_para1"][i + 6])
            self.lineEdit_4.setText(self.mConfig.test_case_detail[2]["test_para"][1])
            self.lineEdit_5.setText(self.mConfig.test_case_detail[2]["test_para"][0])
            # 设置信号源和频谱仪
            if not self.demo:
                pass
            else:
                self.test_result.test_results = self.testProcess()
                if self.test_result.test_results < -55 or self.test_result.test_results > -15:
                    self.test_result.test_item = ModuleConstants.LNA_shepinzhq_cscl
                    self.test_result.test_condition = str(self.label_1.text()) + ':' + str(self.lineEdit_1.text()) + str(self.comboBox_1.currentText()) + \
                        ',' + str(self.label_2.text()) + ':' + str(self.lineEdit_2.text()) + str(self.comboBox_2.currentText()) + \
                        ',' + str(self.label_3.text()) + ':' + str(self.lineEdit_3.text()) + str(self.comboBox_3.currentText()) + \
                        ',' + str(self.label_4.text()) + ':' + str(self.lineEdit_4.text()) + str(self.comboBox_4.currentText()) + \
                        ',' + str(self.label_5.text()) + ':' + str(self.lineEdit_5.text()) + str(self.comboBox_5.currentText())
                    self.test_result.test_conclusion = 'FAIL'
                    QMessageBox.warning(self, ModuleConstants.warning,ModuleConstants.zihuanqi_gz,QMessageBox.Ok)
                    self.signalTest.emit('test')
                    break
                else:
                    self.test_result.test_item =ModuleConstants.LNA_shepinzhq_cscl
                    self.test_result.test_condition = str(self.label_1.text())+':'+str(self.lineEdit_1.text())+str(self.comboBox_1.currentText())+\
                    ','+str(self.label_2.text())+':'+str(self.lineEdit_2.text())+str(self.comboBox_2.currentText())+\
                    ','+str(self.label_3.text())+':'+str(self.lineEdit_3.text())+str(self.comboBox_3.currentText())+\
                    ','+str(self.label_4.text())+':'+str(self.lineEdit_4.text())+str(self.comboBox_4.currentText())+\
                    ','+str(self.label_5.text())+':'+str(self.lineEdit_5.text())+str(self.comboBox_5.currentText())
                    self.test_result.test_conclusion = 'PASS'
                    self.signalTest.emit('test')
        self.signalFinish1.emit('next',None)
        self.close()
    def testProcess(self):
        if not self.demo:
            pass
        else:
            temp=float(30+ np.random.random(1))
        return temp

    @pyqtSlot()
    def closeEvent(self, event):
        if self.action == 'finish_all':
            self.signalFinish1.emit('finish_all', None)
        event.accept()
class test_results:
    def __init__(self):
        self.test_item=''
        self.test_condition=''
        self.test_results=''
        self.test_conclusion=''

