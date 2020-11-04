# -*-coding:utf-8 -*-
import os
import frozen_dir
from common.logConfig import Logger

logger = Logger.module_logger("LoadQssStyleLogger")


SETUP_DIR = frozen_dir.app_path()


# 加载qss类
class LoadQSS:
    def __init__(self):
        super().__init__()

    @staticmethod
    def load():
        """
        load qss style file
        :param self:
        :return: qss
        """
        config_file_path = os.path.join(
            SETUP_DIR, "qss", "style.qss")
        try:
            with open(config_file_path, 'r') as f:
                style = f.readlines()
                style = ''.join(style).strip('\n')
            return style
        except IOError as err:
            logger.error("load QSS Error"+str(err))
