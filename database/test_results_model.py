#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 15:01
# @Author  : chuan.yang
# @File    : TestResults.py
# @Desc    : test result models
import json

class TestValue:
    """
    test value item
    """

    def __init__(self):
        self.value: str = ""
        self.isNormal: int = 0


class BaseTestParam:
    """
    parent class:test parameter
    """

    def __init__(self):
        self.name: str = ""
        self.isIsolateObj: int = 0


class TestParam(BaseTestParam):
    """
    child class: test parameter
    """

    def __init__(self):
        self.unit: str = ""
        self.criterions: str = ""
        self.onlyConclusion: int = 0
        self.testValues: TestValue = []


class TestItem:
    """
    test item
    """

    def __init__(self):
        self.name: str = ""
        self.testParams: BaseTestParam = []


class TestResultBase:
    """
    test result standard database format
    example:
    temp = TestResultBase()
    temp.dutDrawingNbr = "1"
    temp.stationName = "2"
    temp.stationDrawingNbr = "3"
    temp.stationSn = "4"
    temp.unitName = "5"
    temp.unitDrawingNbr = "6"
    temp.unitSn = "7"
    temp.dutName = "8"
    temp.dutDrawingNbr = "9"
    temp.dutSn = "10"
    temp.testTime = "11"


    testvalue1 = TestValue()
    testvalue1.value = "12300"
    testvalue1.isNormal = 1

    testpara = TestParam()
    testpara.name = "通信功能"
    testpara.isIsolateObj = 0
    testpara.onlyConclusion = 1
    testpara.testValues.append(testvalue1)

    testitem = TestItem()
    testitem.name = "通信控制"
    testitem.testParams.append(testpara)
    temp.testItems.append(testitem)
    """

    def __init__(self):
        self.testObjName: str = ""
        self.stationName: str = ""
        self.stationDrawingNbr: str = ""
        self.stationSn: str = ""
        self.unitName: str = ""
        self.unitDrawingNbr: str = ""
        self.unitSn: str = ""
        self.dutName: str = ""
        self.dutDrawingNbr: str = ""
        self.dutSn: str = ""
        self.testTime: str = ""
        self.testItems: TestItem = []

    def toJSON(self):
        """
        transfer model to json format
        :return: json format
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if __name__ == '__main__':
    temp = TestResultBase()
    temp.testObjName = "1"
    temp.stationName = "2"
    temp.stationDrawingNbr = "3"
    temp.stationSn = "4"
    temp.unitName = "5"
    temp.unitDrawingNbr = "6"
    temp.unitSn = "7"
    temp.dutName = "8"
    temp.dutDrawingNbr = "9"
    temp.dutSn = "10"
    temp.testTime = "2020-02-01 15:00:00"

    testvalue1 = TestValue()
    testvalue1.value = "12300"
    testvalue1.isNormal = 1

    testpara = TestParam()
    testpara.name = "通信功能"
    testpara.isIsolateObj = 0
    testpara.onlyConclusion = 1
    testpara.testValues.append(testvalue1)

    testitem = TestItem()
    testitem.name = "通信控制"
    testitem.testParams.append(testpara)
    temp.testItems.append(testitem)
    print(temp.toJSON())


