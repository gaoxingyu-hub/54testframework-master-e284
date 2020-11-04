# -*-coding:utf-8 -*-

# @Time    : 2020/2/2 10:56
# @File    : network_tools.py
# @User    : yangchuan
# @Desc    : network test methods
from pythonping import ping
from common.logConfig import Logger
from common.data_checker import ThDataChecker

logger = Logger.module_logger("ThNetWordTestCase")
class ThNetworkTestCase:

    def __init__(self):
        pass

    @staticmethod
    def ping(ip,timeout,packet_counts):
        """
        ping the specific ip address
        :param ip: ip address with string format
        :param timeout: ping timeout seconds
        :param packet_counts: send packet counts
        :return: bool,responseList object
        """
        try:
            if not ThDataChecker.is_ip(ip):
                return False,None
            result = ping(ip, verbose=False,timeout=timeout,count=packet_counts)
            return result.success(),result
        except BaseException as e:
            logger.error(str(e))
        return False,None


