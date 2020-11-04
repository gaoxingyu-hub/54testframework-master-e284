#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 18:16
# @Author  : chuan.yang
# @File    : test_process.py
# @Desc    :
import subprocess
import socket
from common.info import Constants
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore

from .com_control_device_constant import ModuleConstants
from common.logConfig import Logger
logger = Logger.module_logger("ThComControlDeviceTestProcess")
class ThComControlDeviceTestProcess:
    """
    udp client sender
    """

    def __init__(self):
        self.udp_remote_client = None
        self.udp_local_server = None
        self.com_contents = ModuleConstants.UDP_SEND_CONTENTS
        self.udp_test_result = False
        self.local_udp_server_alive = True

    def test_ip_connection(self, url):
        """
        test ip destination can be connected
        :param url: ip address
        :return:
        """
        try:
            num = 1
            wait = 1000
            ping = subprocess.Popen("ping -n {} -w {} {}".format(num, wait, url),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            exit_code = ping.wait()
            if exit_code != 0:
                return False
            else:
                return True
        except BaseException as e:
            logger.error(str(e))

    def udp_send(self,host,port,contents=ModuleConstants.UDP_SEND_CONTENTS):
        """
        udp sends method
        :param host: str,ip address
        :param port: str,ip address port
        :param contents: str,send information
        :return:
        """
        self.com_contents = contents
        logger.info("udp_send")
        try:
            socket.setdefaulttimeout(1)
            serverAddressPort = (host, int(port))
            self.udp_remote_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            result = self.udp_remote_client.sendto(self.com_contents.encode("utf-8"), serverAddressPort)
            if result > 0:
                return True
            else:
                return False
        except BaseException as e:
            logger.error(str(e))



class UdpServerThread(QtCore.QThread):
    """
    local udp server for listen and receive information
    _signalInfo:signal for caller
    """
    _signalInfo = pyqtSignal(str,object)

    def __init__(self,host:str,port:str,verify_contents:str):
        """
        init method
        :param host:str,ip address
        :param port:str,ip address port
        :param verify_contents: str,information waitting to be checked
        """
        super(UdpServerThread, self).__init__()
        self.local_host = host
        self.local_port = int(port)
        self.verify_contents = verify_contents
        self.local_udp_server_alive = True
        self._signalInfo.emit(Constants.SIGNAL_INFORMATION,"thread start")

    def __del__(self):
        self.wait()

    def run(self):
        """
        thread core function
        :return:
        """
        try:
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, "local udp server starting")
            logger.info("local udp server starting")
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.local_host, self.local_port))
            self.udp_socket.settimeout(10.0)
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, "local udp server started")
            logger.info("local udp server started")
            while self.local_udp_server_alive:
                recv_msg = self.udp_socket.recvfrom(1024)
                recv_msg = recv_msg[0].decode("utf-8")
                if self.verify_contents == recv_msg:
                    self._signalInfo.emit(Constants.SIGNAL_INFORMATION,"local udp server received:" + recv_msg)
                    logger.info("local udp server received:" + recv_msg)
                    self._signalInfo.emit(Constants.SIGNAL_TEST_RESULT, {"result":"success"})
        except socket.timeout as e1:
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION, str(e1))
            self._signalInfo.emit(Constants.SIGNAL_TEST_RESULT, {"result": "fail"})
            logger.error(str(e1))
        except BaseException as e:
            self._signalInfo.emit(Constants.SIGNAL_INFORMATION,str(e))
            logger.error(str(e))

    def stop_thread(self):
        """
        stop socket object and stop the thread
        :return:
        """
        if self.udp_socket:
            self.udp_socket.close()
        self.local_udp_server_alive == False

