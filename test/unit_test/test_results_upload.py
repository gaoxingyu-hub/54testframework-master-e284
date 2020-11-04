# -*-coding:utf-8 -*-

# @Time    : 2020/2/5 13:46
# @File    : test_results_upload.py
# @User    : yangchuan
# @Desc    : 
from database.data_upload_task import TaskDataResultUpload
import json
import os

import frozen_dir

SETUP_DIR = frozen_dir.app_path()

if __name__ == '__main__':
    full_config_file = os.path.join(SETUP_DIR, "data", "example.json")
    with open(full_config_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        upload = TaskDataResultUpload("http://uop.ch722-9.com/api/LK-0508101/LK101/tdapi/insertJson", data)
        upload.start()
        upload.wait(5000)
        print(upload.get_result())
