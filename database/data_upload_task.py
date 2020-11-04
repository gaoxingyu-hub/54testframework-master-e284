# -*-coding:utf-8 -*-

# @Time    : 2020/2/5 12:14
# @File    : data_upload_task.py
# @User    : yangchuan
# @Desc    : test result data uploads to upper application
from PyQt5.QtCore import QThread,pyqtSignal
from datetime import datetime
import time
import json
import requests

from common.logConfig import Logger

logger = Logger.module_logger("TaskDataResultUpload")
class TaskDataResultUpload(QThread):
    """
    test result data uploads to upper application
    _signal：signal for post operation status, caller has slot function for callback
    result: bool flag for post operation status
    """
    _signal = pyqtSignal(object)
    result = False

    def __init__(self,url,data,parent=None):
        """
        init function
        :param url: post url destination
        :param data: post data,dict object which is valid json format
        :param parent:
        """
        super().__init__()
        self.url = url
        self.data = data
        self._signal = None
        self.result = False

    def get_result(self):
        """
        get the post operation result
        :return: bool True or False
        """
        return self.result

    def run(self):
        """
        thread core function for post operation
        :return:
        """
        try:
            logger.info("TaskDataResultUpload start")
            headers = {'Content-Type': 'application/json'}
            s = json.dumps(self.data)
            r = requests.post(self.url, headers=headers,data=s)
            if r.status_code == 200:
                self.result = True
            if self._signal:
                if r.status_code == 200:
                    self._signal.emit("success")
                else:
                    self._signal.emit("fail")
            logger.info("TaskDataResultUpload post response status code" + str(r.status_code))
            logger.info("TaskDataResultUpload post response status code" + str(r.text))
            logger.info("TaskDataResultUpload finish")
        except ConnectionError as err1:
            if self._signal:
                self._signal.emit("fail")
            logger.error(str(err1))
        except BaseException as err2:
            if self._signal:
                self._signal.emit("fail")
            logger.error(str(err2))





