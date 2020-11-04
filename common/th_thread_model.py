#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 9:42
# @Author  : chuan.yang
# @File    : th_thread_model.py
# @Desc    : python multiple thread model

import threading
from PyQt5.QtCore import QThread,pyqtSignal
from datetime import datetime
import time

class ThThreadModelBase(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.exitFlag = False
        pass

    def run(self):
        pass

class ThQtThreadModelBase(QThread):
    _signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__()
        pass



class ThThreadTimerUpdateTestTime(QThread):
    """
    thread model for test duration updates used in pyqt gui
    """
    _signal = pyqtSignal(object)

    def __init__(self,parent=None):
        super().__init__()
        self.exitFlag = False
        self.modifyFlag = False
        self.start_datetime = None
        self.time_duration = 0
        self.thread_status = False

    def run(self):
        """
        thread core methods:
        update test duration by one seconds
        emit signal to upper application
        :return:
        """
        self.start_datetime = datetime.now()
        try:
            while True:
                self.thread_status = True
                if self.exitFlag:
                    break
                if self.modifyFlag:
                    self.start_datetime = datetime.now()
                    self.modifyFlag = False
                else:
                    temp = datetime.now()
                    self.time_duration = temp - self.start_datetime
                    self._signal.emit(self.time_duration.total_seconds())
                time.sleep(1)
        except BaseException as e:
            print(str(e))
        self.thread_status = False

    def restart(self):
        self.modifyFlag = True




