# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_TEST1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from modules.mw1500_device.mw1500_constant import ModuleConstants


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("QDialog{\n"
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
"height:32px;\n"
"background-color:#2884D8;\n"
"color: #FFFFFF;\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"}")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 582, 582))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setGeometry(QtCore.QRect(11, 1, 560, 69))
        self.textBrowser_contents.setStyleSheet("QTextBrowser{\n"
"border-width:0;\n"
"border-style:outset;\n"
"background-color:#E3EAF4;}")
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(33, 300, 512, 60))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"border-width:0;\n"
"border-style:outset;\n"
"background-color:#E3EAF4;}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 540, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setGeometry(QtCore.QRect(190, 540, 75, 30))
        self.pushButton_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_img = QtWidgets.QLabel(self.groupBox)
        self.label_img.setGeometry(QtCore.QRect(10, 120, 560, 311))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(30, 460, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_1.setGeometry(QtCore.QRect(100, 460, 100, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_1.setGeometry(QtCore.QRect(210, 460, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 460, 60, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 460, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 460, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", ModuleConstants.anormal))
        self.pushButton_1.setText(_translate("Dialog", ModuleConstants.normal))
        self.label_1.setText(_translate("Dialog", ModuleConstants.send_frequence))
        self.comboBox_1.setItemText(0, _translate("Dialog", "MHz"))
        self.label_2.setText(_translate("Dialog", ModuleConstants.recivice_frequence))
        self.comboBox_2.setItemText(0, _translate("Dialog", "MHz"))
