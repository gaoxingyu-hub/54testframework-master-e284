# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\sdsl\SDSL_COM.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from constant_trans import TransConstants


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
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox_com = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_com.setObjectName("comboBox_com")
        self.gridLayout_3.addWidget(self.comboBox_com, 0, 1, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout_3.addWidget(self.pushButton_send, 0, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser_tips = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_tips.setObjectName("textBrowser_tips")
        self.gridLayout_5.addWidget(self.textBrowser_tips, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_6.addWidget(self.textBrowser_log, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 4)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "COM"))
        self.pushButton_send.setText(_translate("Dialog", TransConstants.send))
        self.groupBox_2.setTitle(_translate("Dialog", TransConstants.tip_info))
        self.pushButton_next.setText(_translate("Dialog", TransConstants.next))
        self.groupBox_3.setTitle(_translate("Dialog", TransConstants.log))
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
