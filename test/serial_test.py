#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 12:09
# @Author  : chuan.yang
# @File    : serial_test.py
# @Desc    :
from common.serial_port_utility import ThSerialPortUtility

if __name__ == '__main__':
    re = ThSerialPortUtility.list_ports()
    print(re)