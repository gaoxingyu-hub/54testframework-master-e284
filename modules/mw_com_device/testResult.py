#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/22 16:53
# @Author  : chuan.yang
# @File    : testResult.py
# @Desc    :
from dataclasses import dataclass,asdict

@dataclass()
class TestDataProtocolTransferBoard:
    lan2: str
    lan3: str
    lan3: str
    lan4: str
    lan5: str
    lan6: str
    lan7: str
    lan8: str

    def __init__(self):
        pass

    def to_list(self):
        return asdict(self)

@dataclass()
class TestDataProtocolTransferAndControl1:
    com1: str
    com2: str
    com3: str
    com4: str

    def __init__(self):
        pass

    def to_list(self):
        return asdict(self)

@dataclass()
class TestDataProtocolTransferAndControl2:
    com5: str
    com6: str
    com7: str
    com8: str

    def __init__(self):
        pass

    def to_list(self):
        return asdict(self)

@dataclass()
class TestDataProtocolTransferAndControl3:
    com9: str

    def __init__(self):
        pass

    def to_list(self):
        return asdict(self)
