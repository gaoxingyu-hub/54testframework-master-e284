#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 18:55
# @Author  : chuan.yang
# @File    : data_checker.py
# @Desc    : check database format is correct
import re

class ThDataChecker:
    """
    static class methods for general purpose database process
    """
    @classmethod
    def is_ip(self,inputs):
        """
        check string is valid ip address string
        :param inputs: string
        :return:  bool true or false
        """
        format = '((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))'
        pattern = re.match(format, inputs)
        if pattern is not None:
            return True
        else:
            return False