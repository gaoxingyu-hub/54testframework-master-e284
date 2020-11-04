# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\ecom-ns-2\ECOM_NS2_Ping.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from common.info import SystemLanguage


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("\n"
"QWidget{\n"
"background-color:#E3EAF4;\n"
"}\n"
"QLineEdit{\n"
"background-color:#E3EAF4;\n"
"}\n"
"QDialog{\n"
"background-color:#E3EAF4;\n"
"margin-top:10px;\n"
"}\n"
"QLabel{\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"background-color:#E3EAF4;\n"
"}\n"
"QGroupBox{\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color:#E3EAF4;\n"
"}\n"
"QPushButton{\n"
"background-color:#2884D8;\n"
"color: #FFFFFF;\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"QTextBrowser{\n"
"border-width:0;\n"
"border-style:outset;\n"
"background-color:#E3EAF4;\n"
"}\n"
"QGraphicsView{\n"
"background-color:#E3EAF4;\n"
"border-width:0;\n"
"border-style:outset;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_ip_address = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ip_address.setObjectName("lineEdit_ip_address")
        self.gridLayout_3.addWidget(self.lineEdit_ip_address, 0, 1, 1, 1)
        self.pushButton_ping = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ping.setObjectName("pushButton_ping")
        self.gridLayout_3.addWidget(self.pushButton_ping, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_tips = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_tips.setObjectName("textBrowser_tips")
        self.gridLayout_5.addWidget(self.textBrowser_tips, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_6.addWidget(self.textBrowser_log, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
            self.label_3.setText(_translate("Dialog", "Adresse IP"))
            self.pushButton_ping.setText(_translate("Dialog", "ping"))
            self.groupBox_2.setTitle(_translate("Dialog", "Information de remarque"))
            self.pushButton_next.setText(_translate("Dialog", "Étape suivante"))
            self.groupBox_3.setTitle(_translate("Dialog", "Journal"))
        else:
            self.label_3.setText(_translate("Dialog", "IP地址"))
            self.pushButton_ping.setText(_translate("Dialog", "ping"))
            self.groupBox_2.setTitle(_translate("Dialog", "提示信息"))
            self.pushButton_next.setText(_translate("Dialog", "下一步"))
            self.groupBox_3.setTitle(_translate("Dialog", "日志"))
        self.textBrowser_log.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
