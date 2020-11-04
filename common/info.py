#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 18:39
# @Author  : chuan.yang
# @File    : tips.py
# @Desc    : 提示信息常量


class Constants:
    SIGNAL_TEST_RESULT = "signal_test_result"
    SIGNAL_INFORMATION = "signal_information"
    SIGNAL_NEXT = "next"
    SIGNAL_FINISH = "finish"
    SIGNAL_CASE_FINISH = "case_finish"
    SIGNAL_CLOSE = "close"
    RESULT_SUCCESS = "success"
    RESULT_FAIL = "fail"
    NETWORK_PORT_TEST_NORMAL = "normal"
    NETWORK_PORT_TEST_ABNORMAL = "abnormal"


class TestParameters:
    FRAME_LOSS_TEST_PACKET_LENGTH = 128
    FRAME_LOSS_TEST_PACKET_RATE = 100
    FRAME_LOSS_TEST_TIME_SECS = 10

class SystemLanguage:
    ZH_CN ="zh_CN"
    en_US = "en_US"
    fr_FR = "fr_FR"
    LANGUAGE = ZH_CN


class MainWindowConstants:
    QMESSAGEBOX_WARN = "警告"
    QMESSAGEBOX_WARN_CLOSE_CURRENT_MODULE = "请关闭当前测试项目"
    QMESSAGEBOX_WARN_MODULE_NOT_EXISTED = "测试模块不存在"
    CONTENTS_TEST_CASE = "测试项目"

    def set_language(self, lang):
        if SystemLanguage.fr_FR == lang:
            self.QMESSAGEBOX_WARN = "Alerte"
            self.QMESSAGEBOX_WARN_CLOSE_CURRENT_MODULE = "Veuillez désactiver le test actuel"
            self.QMESSAGEBOX_WARN_MODULE_NOT_EXISTED = "Le module d 'essai n' existe pas."
            self.CONTENTS_TEST_CASE = "Elément de test"
        else:
            self.QMESSAGEBOX_WARN = "警告"
            self.QMESSAGEBOX_WARN_CLOSE_CURRENT_MODULE = "请关闭当前测试项目"
            self.QMESSAGEBOX_WARN_MODULE_NOT_EXISTED = "测试模块不存在"
            self.CONTENTS_TEST_CASE = "测试项目"

class ThCommonNoticeInfo:
    """
    software common notice information text
    """
    START_TEST = "开始测试"
    FINISH_TEST = "测试结束"
    TEST_SUCCESS = "测试成功"
    TEST_FAIL = "测试失败"
    DUT = "测试对象"
    UDP_SERVER_IS_RUNNING = "本地Udp Server已启动"
    WARN = "警告"
    ILLEGAL_IP_ADDRESS = "不合法IP地址"

    def set_language(self, lang):
        if SystemLanguage.fr_FR == lang:
            self.START_TEST = "Commencez le test."
            self.FINISH_TEST = "Test terminé."
            self.TEST_SUCCESS = "Test réussi"
            self.TEST_FAIL = "Test raté"
            self.DUT = "Objet de test"
            self.UDP_SERVER_IS_RUNNING = "本地Udp Server已启动"
            self.WARN = "Alerte"
            self.ILLEGAL_IP_ADDRESS = "Adresse IP illégale"
        else:
            self.START_TEST = "开始测试"
            self.FINISH_TEST = "测试结束"
            self.TEST_SUCCESS = "测试成功"
            self.TEST_FAIL = "测试失败"
            self.DUT = "测试对象"
            self.UDP_SERVER_IS_RUNNING = "本地Udp Server已启动"
            self.WARN = "警告"
            self.ILLEGAL_IP_ADDRESS = "不合法IP地址"