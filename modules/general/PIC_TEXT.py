"""
Module implementing PIC_TEXT.
"""

from PyQt5.QtCore import pyqtSlot, QPoint, Qt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QDialog, QGraphicsItem, QScrollArea
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal

from .Ui_PIC_TEXT import Ui_Dialog
import os


class DialogPicText(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str, object)

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogPicText, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1

    """
        # 图片缩放比例
        self.Scale = 1
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
    """

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
        self.reject()
        self.close()
        self._signalFinish.emit("next", None)
