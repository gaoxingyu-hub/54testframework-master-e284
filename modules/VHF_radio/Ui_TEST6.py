# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_TEST6.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modules.VHF_radio.VHF_radio_CONSTANT import ModuleConstants


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
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setGeometry(QtCore.QRect(11, 1, 560, 211))
        self.textBrowser_contents.setStyleSheet("QTextBrowser{\n"
"border-width:0;\n"
"border-style:outset;\n"
"background-color:#E3EAF4;}")
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 240, 541, 261))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_1.setGeometry(QtCore.QRect(70, 20, 260, 20))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 260, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 260, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 180, 260, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 260, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 180, 40, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(370, 180, 45, 20))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 140, 40, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(370, 140, 45, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 100, 40, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 100, 45, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 60, 45, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(330, 20, 40, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_1.setGeometry(QtCore.QRect(370, 20, 45, 20))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setGeometry(QtCore.QRect(250, 530, 120, 40))
        self.pushButton_next.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_next.setObjectName("pushButton_next")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog",ModuleConstants.shiliangxinhaofashengqi))
        self.label_1.setText(_translate("Dialog",ModuleConstants.frequence))
        self.label_2.setText(_translate("Dialog", ModuleConstants.tiaozhi_fangshi))
        self.label_3.setText(_translate("Dialog", ModuleConstants.tiaozhi_xinhao))
        self.label_5.setText(_translate("Dialog",  ModuleConstants.xinhao_fudu))
        self.label_4.setText(_translate("Dialog",ModuleConstants.pinpian))
        self.comboBox_5.setItemText(0, _translate("Dialog", "dBm"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "kHz"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "kHz"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "FM"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "AM"))
        self.comboBox_1.setItemText(0, _translate("Dialog", "MHz"))
        self.pushButton_next.setText(_translate("Dialog", ModuleConstants.next))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
