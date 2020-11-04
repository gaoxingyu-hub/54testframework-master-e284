# -*-coding:utf-8 -*-
# @Time    : 2020/1/30 11:37
# @File    : data_storage.py
# @User    : yangchuan
# @Desc    : test database storage
import os
import frozen_dir
from common.logConfig import Logger
import json
import uuid
import sqlite3
from datetime import datetime
from database.test_results_model import TestResultBase,TestValue,TestParam,TestItem

logger = Logger.module_logger("ThTestResultsStorage")
SETUP_DIR = frozen_dir.app_path()

class ThTestResultsStorage:
    """
     test case result store process:
        (1) generate result json file and write file to disk
        (2) store test case record into sqlite
     demo:
     test package:test_results.py
    """


    @staticmethod
    def check_file_folder(folder_path):
        """
        check the test result storage file path is existed
        :param folder_path: file folder by absolutely file path
        :return: none
        """
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except IOError as e:
            logger.error(str(e))

    @staticmethod
    def save_to_file(test_result,test_result_file_path):
        """

        :param test_result: TestResultBase json model
        :param test_result_file_path: test result json full file path
        :return: none
        """
        try:
            with open(test_result_file_path, 'w', encoding='utf-8') as f:
                json.dump(test_result, f, ensure_ascii=False, indent=4)
        except IOError as e:
            logger.error(str(e))

    @staticmethod
    def generate_test_case_id():
        """
        generate uuid string
        :return: uuid string
        """
        return str(uuid.uuid1())

    @staticmethod
    def save_test_case_record(test_result: TestResultBase, test_result_file_path):
        """
        store the test case result into sqlite records
        :param test_result: test result data model TestResultBase
        :param test_result_file_path:test result json full file path
        :return:
        """
        data_obj_path = os.path.join(
            SETUP_DIR, "data", "test_records.db")
        try:
            conn = sqlite3.connect(data_obj_path)
            c = conn.cursor()
            data = [(test_result.testObjName,test_result.stationName,test_result.stationDrawingNbr,
                     test_result.stationSn,test_result.unitName,test_result.unitDrawingNbr,
                     test_result.unitSn,test_result.dutName,test_result.dutDrawingNbr,
                     test_result.dutSn,test_result.testTime,0,test_result_file_path)]
            c.executemany('insert into test_case_record values(?,?,?,?,?,?,?,?,?,?,?,?,?) ', data)
            conn.commit()

            conn.close()
        except BaseException as e:
            logger.error(str(e))

    @staticmethod
    def test_case_result_storage(test_result):
        """
        test case result store process:
        (1) generate result json file and write file to disk
        (2) store test case record into sqlite
        :param test_result: TestResultBase data object from other modules
        :return: none
        """
        current_datetime_object = datetime.now()
        json_file_folder_path = os.path.join(
            SETUP_DIR, "data", current_datetime_object.strftime("%Y%m%d"))
        random_test_case_id = current_datetime_object.strftime("%Y%m%d-%H%M%S")
        json_file_path = os.path.join(
            SETUP_DIR, "data", current_datetime_object.strftime("%Y%m%d"),random_test_case_id+".json")
        try:
            ThTestResultsStorage.check_file_folder(json_file_folder_path)
            ThTestResultsStorage.save_to_file(test_result.toJSON(),json_file_path)
            ThTestResultsStorage.save_test_case_record(test_result,json_file_path)
        except IOError as e1:
            logger.error(str(e1))
        except BaseException as e:
            logger.error(str(e))


    @staticmethod
    def create_tables():
        """
        create sqlite table for test record storage
        :return: none
        """
        data_obj_path = os.path.join(
            SETUP_DIR, "data", "test_records.db")
        try:
            conn = sqlite3.connect(data_obj_path)
            c = conn.cursor()
            c.execute('''CREATE TABLE test_case_record
                         (testObjName text, 
                         stationName text, 
                         stationDrawingNbr text, 
                         stationSn text, 
                         unitName text,
                         unitDrawingNbr text,
                         unitSn text,
                         dutName text,
                         dutDrawingNbr text,
                         dutSn text, 
                         testTime datetime, 
                         upload integer DEFAULT 0,
                         filePath text
                         )''')
            conn.commit()
            conn.close()
        except BaseException as e:
            logger.error(str(e))







