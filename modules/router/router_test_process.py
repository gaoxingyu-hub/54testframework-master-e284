# -*-coding:utf-8 -*-

# @Time    : 2020/2/2 14:22
# @File    : ecom_ns2_test_process.py
# @User    : yangchuan
# @Desc    : ecom ns2 switcher test process
from PyQt5.QtCore import QThread,pyqtSignal
import time

from modules.general.frame_loss import start_test
from renix_py_api import renix
from common.logConfig import Logger
import random
from common.info import Constants
from renix_py_api.renix_common_api import get_sys_entry
from renix_py_api.renix import *
import logging, time
from renix_py_api.api_gen import *
from renix_py_api.core import EnumRelationDirection
from renix_py_api.rom_manager import *


logger = Logger.module_logger("TestProcessRouter")


class TestProcessRouter(QThread):
    """
    Ecom Ns2 switcher test process thread
    """
    _signal = pyqtSignal(str,object)
    _signalInfo = pyqtSignal(str, object)
    port1 = ""
    port2 =""

    def __init__(self,parent=None):
        super(TestProcessRouter,self).__init__()
        self.test_case = None

    def set_test_para(self,para):
        """
        test parameter set method
        :param script:
        :param para:
        :return:
        """
        self.test_case = para
        self.port1 = para[0]
        self.port2 = para[1]
        return

    def run(self):
        """
        thread core methods:
        emit signal to upper application
        :return:
        """
        try:
            logger.info("TestProcessEcomNs2 test start")
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION,"TestProcessEcomNs2 test start:"
                                  + str(self.port1) + " " + str(self.port2))
            test_result = {}
            initialize()
            sys_entry = get_sys_entry()
            result = start_test(sys_entry)
            shutdown()
            if result:
                for k,v in result.items():
                    self._signalInfo.emit(Constants.SIGNAL_INFORMATION, k + ":" + str(v))

                if "uplink_loss_frames" in result:
                    if result["uplink_loss_frames"] < 100:
                        test_result["lan" + str(self.test_case[1])] = Constants.NETWORK_PORT_TEST_NORMAL
                    else:
                        test_result["lan" + str(self.test_case[1])] = Constants.NETWORK_PORT_TEST_ABNORMAL
                else:
                    test_result["lan" + str(self.test_case[1])] = Constants.NETWORK_PORT_TEST_ABNORMAL

                if "downlink_loss_frames" in result:
                    if result["downlink_loss_frames"] < 100:
                        test_result["lan" + str(self.test_case[0])] = Constants.NETWORK_PORT_TEST_NORMAL
                    else:
                        test_result["lan" + str(self.test_case[0])] = Constants.NETWORK_PORT_TEST_ABNORMAL
                else:
                    test_result["lan" + str(self.test_case[0])] = Constants.NETWORK_PORT_TEST_ABNORMAL
            self._signal.emit(Constants.SIGNAL_TEST_RESULT,test_result)

            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, "lan " + str(self.test_case[0]) +
                                  ":" + test_result["lan" + str(self.test_case[0])])
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, "lan " + str(self.test_case[1]) +
                                  ":" + test_result["lan" + str(self.test_case[1])])

            # self._signal.emit(Constants.SIGNAL_NEXT, test_result)
            logger.info("TestProcessEcomNs2 test finish")
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, "TestProcessEcomNs2 test finish:"+
                                  str(self.port1) + " " +str(self.port2))
        except BaseException as e:
            logger.error(str(e))


