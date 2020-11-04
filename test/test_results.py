# -*-coding:utf-8 -*-

# @Time    : 2020/1/31 14:19
# @File    : test_results.py
# @User    : yangchuan
# @Desc    :
# from database.test_results import TestResultBase,TestValue,TestParam,TestItem
from database.data_storage import ThTestResultsStorage
from renix_py_api import renix
for i in range(5):
    print("-----%d-----" %i)
    for j in range(5):
        if j > 3:
            break
        print(j)

# if __name__ == '__main__':
    # ThTestResultsStorage.create_tables()
    # temp = TestResultBase()
    # temp.testObjName = "1"
    # temp.stationName = "2"
    # temp.stationDrawingNbr = "3"
    # temp.stationSn = "4"
    # temp.unitName = "5"
    # temp.unitDrawingNbr = "6"
    # temp.unitSn = "7"
    # temp.dutName = "8"
    # temp.dutDrawingNbr = "9"
    # temp.dutSn = "10"
    # temp.testTime = "2020-01-31 12:00:00"
    #
    # testvalue1 = TestValue()
    # testvalue1.value = "12300"
    # testvalue1.isNormal = 1
    #
    # testpara = TestParam()
    # testpara.name = "通信功能"
    # testpara.isIsolateObj = 0
    # testpara.onlyConclusion = 1
    # testpara.testValues.append(testvalue1)
    #
    # testitem = TestItem()
    # testitem.name = "通信控制"
    # testitem.testParams.append(testpara)
    # temp.testItems.append(testitem)
    #
    # test_data = temp.toJSON()
    # # print(temp.dutDrawingNbr)
    # ThTestResultsStorage.test_case_result_storage(temp)
    # ThTestResultsStorage.save_test_case_record(test_data)
#     renix.initialize()
#     print("1")
#     renix.shutdown()

