from PyQt5 import QtWidgets,QtCore
import sys,getopt
import frozen_dir
from common.info import SystemLanguage,MainWindowConstants
import os
import argparse
SETUP_DIR = frozen_dir.app_path()

if __name__ == '__main__':


    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "lang=", "station=", "category=", "stationName=", "categoryName="])
        print(opts)
        for o, a in opts:
            if "lang" in o:
                if a == "en":
                    SystemLanguage.LANGUAGE = SystemLanguage.en_US
                elif a == "zh-CN":
                    SystemLanguage.LANGUAGE = SystemLanguage.ZH_CN
                elif a == "fr":
                    SystemLanguage.LANGUAGE = SystemLanguage.fr_FR
    except getopt.GetoptError:
        print("Get unrecognized parameters")
        # sys.exit(2)

    main_window_constant = globals()['MainWindowConstants']
    main_window_constant.set_language(main_window_constant, lang=SystemLanguage.LANGUAGE)
    # globals()['MainWindowConstants'].set_language(lang = SystemLanguage.LANGUAGE)
    from MainWindow import MainWindow
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
