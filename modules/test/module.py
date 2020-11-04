# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from .Ui_module import Ui_TestModule


class TestModule(QDialog, Ui_TestModule):
    """
    Class documentation goes here.
    """
    signalTitle = pyqtSignal(str)
    signalStatus = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TestModule, self).__init__(parent)
        self.setupUi(self)
        self.page_index = 0
        self.disassemble_pic_index = 1
        self.pushButton_last.setVisible(False)
        self.pushButton_disassemble_previous.setVisible(False)
        self.steps2Name= {
            "0":"系统拆机详解",
            "1":"搭建测试系统",
            "2":"执行测试",
            "3":"测试数据管理",
        }
        self.label_imageview.setPixmap(QtGui.QPixmap("1.png"))


    def changePageIndex(self, flag):
        if flag == 1 and self.page_index == 3:
            self.pushButton_next.setVisible(False)
        elif flag == -1 and self.page_index == 0:
            self.pushButton_last.setVisible(False)
        else:
            self.pushButton_next.setVisible(True)
            self.pushButton_last.setVisible(True)
        self.label_test_steps.setText(self.steps2Name[str(self.page_index)])
        return

    def change_disassemble_picture_index(self,flag):
        if flag == 1 and self.disassemble_pic_index == 4:
            self.pushButton_disassemble_next.setVisible(False)
        elif flag == -1 and self.disassemble_pic_index == 1:
            self.pushButton_disassemble_previous.setVisible(False)
        else:
            self.pushButton_disassemble_next.setVisible(True)
            self.pushButton_disassemble_previous.setVisible(True)
        return
    
    @pyqtSlot()
    def on_pushButton_TestData_export_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestData_upload_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_cleardata_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_savedata_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_pre4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_do4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_next4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_pre3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_do3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_next3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_pre2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_do2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_next2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_pre1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_do1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_next1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_pre5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_do5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_TestExecute_next5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_testprepare_verify_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_Test_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        return
    
    @pyqtSlot()
    def on_pushButton_disassemble_previous_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.disassemble_pic_index > 0:
            self.disassemble_pic_index = self.disassemble_pic_index - 1
            self.change_disassemble_picture_index(-1)
            # print(str(self.disassemble_pic_index) + ".png")
            self.label_imageview.setPixmap(QtGui.QPixmap(str(self.disassemble_pic_index) + ".png"))
        return
    
    @pyqtSlot()
    def on_pushButton_disassemble_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.disassemble_pic_index < 5:
            self.disassemble_pic_index = self.disassemble_pic_index + 1
            self.change_disassemble_picture_index(1)
            # print(str(self.disassemble_pic_index) + ".png")
            self.label_imageview.setPixmap(QtGui.QPixmap(str(self.disassemble_pic_index) + ".png"))
        return
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.page_index < 3:
            self.page_index = self.page_index + 1
            self.changePageIndex(1)
            self.stackedWidget.setCurrentIndex(self.page_index)
        return
    
    @pyqtSlot()
    def on_pushButton_last_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.page_index > 0:
            self.page_index = self.page_index - 1
            self.changePageIndex(-1)
            self.stackedWidget.setCurrentIndex(self.page_index)
        return

    @pyqtSlot()
    def on_pushButton_close_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.signalTitle.emit("emit")
        self.close()
        return
