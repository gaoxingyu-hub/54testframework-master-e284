# -*- coding: utf-8 -*-

"""
Module implementing DialogSimpleTestProcess1Btn.
"""

from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QGraphicsItem
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui, QtWidgets, QtCore
import os

from .Ui_SIMPLE_TEST_PROCESS_1BTN import Ui_Dialog
from common.info import Constants
from common.logConfig import Logger


logger = Logger.module_logger("DialogSimpleTestProcess1Btn")
class DialogSimpleTestProcess1Btn(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str, object)
    _msg = Constants.SIGNAL_NEXT

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogSimpleTestProcess1Btn, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
    """
        # 图片缩放比例
        self.Scale = 1
        # Key_Control键是否按下
        self.ctrlPressed = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlPressed = True
        return super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlPressed = False
        return super().keyReleaseEvent(event)

    def wheelEvent(self, event):
        if self.ctrlPressed:
            # 滚动的数值，单位为1/8度
            angle = event.angleDelta() / 8
            angleY = angle.y()
            # 放大
            if angleY > 0:
                self.Scale = self.Scale + 0.05
                self.item.setScale(self.Scale)
            elif angleY < 0:  # 滚轮下滚
                self.Scale = self.Scale - 0.05
                self.item.setScale(self.Scale)
        else:
            super().wheelEvent(event)
    """
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.reject()
        self.close()
        self._signalFinish.emit(self._msg, None)

    def set_contents(self,title,contents,img_file_path):
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
                    self.pixmap = self.pixmap.scaled(600, 600,
                                                     Qt.IgnoreAspectRatio | Qt.SmoothTransformation)
                    self.graphicsView.setPixmap(self.pixmap)
                    self.graphicsView.setAlignment(Qt.AlignCenter)
        except BaseException as e:
            logger.error(str(e))
        return

    def set_button_contents(self,button_contents):
        self.pushButton_1.setText(button_contents)


    def set_msg(self,msg):
        self._msg = msg
