import os
from pathlib import Path
import json

from PyQt5.QtWidgets import QMessageBox, QWidget

from common.logConfig import Logger
import frozen_dir

logger = Logger.module_logger("baseconfig")
SETUP_DIR = frozen_dir.app_path()
class BaseConfig:
    """
    parent class
    load the config file into object
    """
    def __init__(self,file_name):
        self.config_directory = "conf"
        self.full_config_file = os.path.join(SETUP_DIR, self.config_directory,file_name)
        return

    def read_config(self):
        """
        read config json format file info database object
        :return: json database object
        """
        try:
            data = None
            with open(self.full_config_file,encoding='utf-8') as json_file:
                data = json.load(json_file)
        except IOError as e:
            logger.error(str(e))
            # QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No)
            return
        except BaseException as e1:
            logger.error(str(e1))
            # QMessageBox.warning(QWidget, "标题", "警告框消息正文", QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Yes)
            return
        return data

class TestModuleConfig(BaseConfig):
    """
    child class for module test log file read
    """
    def __init__(self,file_name):
        super(TestModuleConfig,self).__init__(file_name)
        self.title = ""
        self.module_name = ""
        self.steps = None
        self.disassemble = None
        self.testprepare = None
        self.testexecute = None
        self.get_test_parameters()
        return

    def get_test_parameters(self):
        """
        read the module test log file into database object
        :return: database dict object
        """
        try:
            config_obj = self.read_config()
            self.title = config_obj["title"]
            self.module_name = config_obj["module_name"]
            self.steps = config_obj["steps"]
            self.disassemble = config_obj["disassemble"]
            self.testprepare = config_obj["testprepare"]
            self.testexecute = config_obj["testexecute"]
        except BaseException as e:
            logger.error(str(e))
        return config_obj

class SystemConfig(BaseConfig):
    """
    child class for software system config file
    """
    def __init__(self,file_name='system.json'):
        super(SystemConfig,self).__init__(file_name)
        config_obj = self.get_system_parameters()
        self.step2name = config_obj["step2name"]
        self.menu = config_obj["menu"]
        self.menu2module = config_obj["menu2module"]
        self.menuindex2module = config_obj["menuindex2module"]
        return

    def get_system_parameters(self):
        """
        read the system config log file into database object
        :return: database dict object
        """
        try:
            config_obj = self.read_config()
        except BaseException as e:
            logger.error(str(e))
        return config_obj

class TestModuleConfigNew(BaseConfig):
    """
        child class for module test log file read
        latest version
    """
    def __init__(self,file_name):
        super(TestModuleConfigNew,self).__init__(file_name)
        self.title = ""
        self.module_name = ""
        self.test_case = None
        self.test_source = None
        self.test_case_detail = None
        self.get_test_parameters()

        return

    def get_test_parameters(self):
        try:
            config_obj = self.read_config()
            self.title = config_obj["title"]
            self.module_name = config_obj["module_name"]
            self.test_case = config_obj["test_case"]
            self.test_case_detail = config_obj["test_case_detail"]
            self.test_source = config_obj["test_source"]
        except BaseException as e:
            logger.error(str(e))
        return config_obj


class EcomNs1TestModuleConfig(BaseConfig):
    """
    Ecom ns 1 switcher test case parameters
    """
    def __init__(self,file_name):
        super(EcomNs1TestModuleConfig,self).__init__(file_name)
        self.steps = None
        self.get_test_parameters()

    def get_test_parameters(self):
        """
        read the module test log file into database object
        :return: database dict object
        """
        try:
            config_obj = self.read_config()
            self.steps = config_obj["steps"]
        except BaseException as e:
            logger.error(str(e))
        return config_obj

class EcomNs2TestModuleConfig(BaseConfig):
    """
    Ecom ns 1 switcher test case parameters
    """
    def __init__(self,file_name):
        super(EcomNs2TestModuleConfig,self).__init__(file_name)
        self.steps = None
        self.get_test_parameters()

    def get_test_parameters(self):
        """
        read the module test log file into database object
        :return: database dict object
        """
        try:
            config_obj = self.read_config()
            self.steps = config_obj["steps"]
        except BaseException as e:
            logger.error(str(e))
        return config_obj


class RouterLanTestModuleConfig(BaseConfig):
    """
    Router config module
    """
    def __init__(self, file_name):
        super(RouterLanTestModuleConfig, self).__init__(file_name)
        self.steps = None
        self.get_test_parameters()

    def get_test_parameters(self):
        try:
            config_obj = self.read_config()
            self.steps = config_obj["steps"]
        except BaseException as e:
            logger.error(str(e))
        return config_obj
