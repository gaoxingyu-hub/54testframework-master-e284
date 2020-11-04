# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\vhf_radio\VHF_Test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 600)
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
"margin-top:10px;\n"
"border-width:0;\n"
"border-style:outset;\n"
"background-color:#E3EAF4;\n"
"}\n"
"QGraphicsView{\n"
"background-color:#E3EAF4;\n"
"border-width:0;\n"
"border-style:outset;\n"
"}\n"
"QGroupBox{\n"
"padding-top:30px;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_freq_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg.setMinimumSize(QtCore.QSize(0, 26))
        self.lineEdit_freq_sg.setObjectName("lineEdit_freq_sg")
        self.gridLayout.addWidget(self.lineEdit_freq_sg, 1, 1, 1, 1)
        self.comboBox_sg_freq = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_sg_freq.setMinimumSize(QtCore.QSize(0, 26))
        self.comboBox_sg_freq.setObjectName("comboBox_sg_freq")
        self.comboBox_sg_freq.addItem("")
        self.gridLayout.addWidget(self.comboBox_sg_freq, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.lineEdit_power_sg = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_power_sg.sizePolicy().hasHeightForWidth())
        self.lineEdit_power_sg.setSizePolicy(sizePolicy)
        self.lineEdit_power_sg.setObjectName("lineEdit_power_sg")
        self.gridLayout.addWidget(self.lineEdit_power_sg, 1, 4, 1, 1)
        self.comboBox_sg_power = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_sg_power.sizePolicy().hasHeightForWidth())
        self.comboBox_sg_power.setSizePolicy(sizePolicy)
        self.comboBox_sg_power.setObjectName("comboBox_sg_power")
        self.comboBox_sg_power.addItem("")
        self.gridLayout.addWidget(self.comboBox_sg_power, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_freq_sg_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg_2.setMinimumSize(QtCore.QSize(0, 26))
        self.lineEdit_freq_sg_2.setObjectName("lineEdit_freq_sg_2")
        self.gridLayout.addWidget(self.lineEdit_freq_sg_2, 2, 1, 1, 1)
        self.comboBox_sg_freq_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_sg_freq_2.setMinimumSize(QtCore.QSize(0, 26))
        self.comboBox_sg_freq_2.setObjectName("comboBox_sg_freq_2")
        self.comboBox_sg_freq_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_sg_freq_2, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.lineEdit_power_sg_2 = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_power_sg_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_power_sg_2.setSizePolicy(sizePolicy)
        self.lineEdit_power_sg_2.setObjectName("lineEdit_power_sg_2")
        self.gridLayout.addWidget(self.lineEdit_power_sg_2, 2, 4, 1, 1)
        self.comboBox_sg_power_2 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_sg_power_2.sizePolicy().hasHeightForWidth())
        self.comboBox_sg_power_2.setSizePolicy(sizePolicy)
        self.comboBox_sg_power_2.setObjectName("comboBox_sg_power_2")
        self.comboBox_sg_power_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_sg_power_2, 2, 5, 1, 1)
        self.comboBox_sg_addr = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_sg_addr.setMinimumSize(QtCore.QSize(0, 26))
        self.comboBox_sg_addr.setObjectName("comboBox_sg_addr")
        self.comboBox_sg_addr.addItem("")
        self.gridLayout.addWidget(self.comboBox_sg_addr, 0, 1, 1, 1)
        self.lineEdit_addr_sg = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_addr_sg.sizePolicy().hasHeightForWidth())
        self.lineEdit_addr_sg.setSizePolicy(sizePolicy)
        self.lineEdit_addr_sg.setObjectName("lineEdit_addr_sg")
        self.gridLayout.addWidget(self.lineEdit_addr_sg, 0, 2, 1, 4)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 133, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout_5.addWidget(self.pushButton_next, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton_excute = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_excute.setObjectName("pushButton_excute")
        self.gridLayout_5.addWidget(self.pushButton_excute, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "信号源"))
        self.label_5.setText(_translate("Dialog", "地址"))
        self.label.setText(_translate("Dialog", "频率"))
        self.comboBox_sg_freq.setItemText(0, _translate("Dialog", "MHz"))
        self.label_2.setText(_translate("Dialog", "功率"))
        self.comboBox_sg_power.setItemText(0, _translate("Dialog", "dBm"))
        self.label_3.setText(_translate("Dialog", "调制"))
        self.comboBox_sg_freq_2.setItemText(0, _translate("Dialog", "kHz"))
        self.label_4.setText(_translate("Dialog", "频偏"))
        self.comboBox_sg_power_2.setItemText(0, _translate("Dialog", "kHz"))
        self.comboBox_sg_addr.setItemText(0, _translate("Dialog", "LAN"))
        self.groupBox_3.setTitle(_translate("Dialog", "测试结果"))
        self.comboBox.setItemText(0, _translate("Dialog", "正常"))
        self.comboBox.setItemText(1, _translate("Dialog", "异常"))
        self.groupBox_4.setTitle(_translate("Dialog", "操作面板"))
        self.pushButton_next.setText(_translate("Dialog", "下一步"))
        self.pushButton_excute.setText(_translate("Dialog", "执行"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
