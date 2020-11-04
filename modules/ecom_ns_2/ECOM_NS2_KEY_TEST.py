# -*- coding: utf-8 -*-

"""
Module implementing DialogEcomNs2KeyTest.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
import os
import frozen_dir

from .Ui_ECOM_NS2_KEY_TEST import Ui_Dialog
from common.logConfig import Logger
from .ecom_ns2_test_process import TestProcessEcomNs2
from common.config import EcomNs2TestModuleConfig
from common.info import Constants, ThCommonNoticeInfo, SystemLanguage

SETUP_DIR = frozen_dir.app_path()
logger = Logger.module_logger("DialogEcomNs2KeyTest")
class DialogEcomNs2KeyTest(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str, object)
    current_test_case = ()
    current_test_step = 1
    current_test_item = 1
    max_test_steps = 24
    test_result = {}
    current_test_button_status = "next"

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogEcomNs2KeyTest, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.current_test_case = (1, 2)
        self.current_test_step = 1
        self.current_test_item = 1
        self.max_test_steps = 24
        self.test_process_object = None

        if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
            self.config_file_path = os.path.join(
                SETUP_DIR, "conf","fr" , "ecom_ns_2_cases.json")
        else:
            self.config_file_path = os.path.join(
                SETUP_DIR, "conf", "cn", "ecom_ns_2_cases.json")
        self.test_config = EcomNs2TestModuleConfig(self.config_file_path)

        port1 = 2 * (self.current_test_item - 1) + 1
        port2 = 2 * self.current_test_item
        self.current_test_case = (port1, port2)
        self.update_test_step_display(port1, port2)
        self.current_test_button_status = self.test_config.steps[self.current_test_step - 1]["status"]
        self.textBrowser_tips.setText(self.test_config.steps[self.current_test_step - 1]["contents"])
        self.pushButton_process.setText(self.test_config.steps[self.current_test_step - 1]["button"])
    
    @pyqtSlot()
    def on_pushButton_process_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.current_test_step >= self.max_test_steps:
            self._signalFinish.emit(Constants.SIGNAL_TEST_RESULT, self.test_result)
            self._signalFinish.emit(Constants.SIGNAL_NEXT, "")
            # self._signalFinish.emit(self.windowTitle(), self.test_result)
            self.accept()
            self.close()
        elif self.pushButton_process.text() == "测试结束":
            self._signalFinish.emit(Constants.SIGNAL_TEST_RESULT, self.test_result)
            self._signalFinish.emit(Constants.SIGNAL_NEXT, "")
            # self._signalFinish.emit(self.windowTitle(), self.test_result)
            self.accept()
            self.close()
        else:
            self.current_test_step = self.current_test_step + 1
            if self.current_test_button_status == "before":
                try:
                    self.pushButton_process.setVisible(False)
                    if not self.test_process_object:
                        self.test_process_object = TestProcessEcomNs2()
                        self.test_process_object._signal.connect(self.slot_test_process)
                        self.test_process_object._signalInfo.connect(self.slot_test_process_information)
                    self.test_process_object.set_test_para(self.current_test_case)
                    self.test_process_object.start()
                    self.test_step_control("next")
                except BaseException as e:
                    logger.error(str(e))
            else:
                self.current_test_item = self.current_test_item + 1
                port1 = 2 * (self.current_test_item - 1) + 1
                port2 = 2 * self.current_test_item
                self.current_test_case = (port1, port2)
                self.update_test_step_display(port1, port2)
                self.test_step_control("next")

    def set_contents(self,title,contents,img_file_path):
        try:
            self.setWindowTitle(title)
            # self.textBrowser_tips.setText(contents)
        except BaseException as e:
            logger.error(str(e))

    def slot_test_process(self,para1,para2):
        """
        test process thread return parameter slot
        :param para1: parameter1
        :param para2: parameter2
        :return: none
        """
        self.current_test_step = self.current_test_step + 1
        self.pushButton_process.setVisible(True)
        temp_result_flag = True
        temp_result_str = ""
        for k,v in para2.items():
            temp_result_str += "\n" + str(k) + ":" + str(v)
            if v == Constants.NETWORK_PORT_TEST_ABNORMAL:
                temp_result_flag = False

        if para1 and para2:
            self.test_result.update(para2)

        if not temp_result_flag:
            self.current_test_button_status = "fail"
            self.textBrowser_tips.setText(self.test_config.steps[self.current_test_step - 1]["contents"]
                                          + "\n" + temp_result_str)
            self.pushButton_process.setText(ThCommonNoticeInfo.FINISH_TEST)
        else:
            self.current_test_button_status = self.test_config.steps[self.current_test_step - 1]["status"]
            self.textBrowser_tips.setText((self.test_config.steps[self.current_test_step - 1]["contents"]
                                           + "\n" + str(temp_result_str)))
            self.pushButton_process.setText(self.test_config.steps[self.current_test_step - 1]["button"])
        # self.test_step_control("next")

    def update_test_step_display(self,port1,port2):
        self.listWidget_port1.setCurrentRow(port1 - 1)
        self.listWidget_port2.setCurrentRow(port2 - 1)

    def test_step_control(self,action):
        if action == "next":
            self.current_test_button_status = self.test_config.steps[self.current_test_step-1]["status"]
            self.textBrowser_tips.setText(self.test_config.steps[self.current_test_step-1]["contents"])
            self.pushButton_process.setText(self.test_config.steps[self.current_test_step-1]["button"])

    def slot_test_process_information(self,signal,para1):
        self.update_display_log(para1)

    def update_display_log(self,contents):
        if self.textBrowser_log.document().blockCount() > 50:
            self.textBrowser_log.clear()
        self.textBrowser_log.append(contents)

