# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\control_device\COM_CONTROL_DEVICE_EXECUTE3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.verticalLayout.addWidget(self.textBrowser_contents)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.testexecute_page3_label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page3_label_3.setFont(font)
        self.testexecute_page3_label_3.setObjectName("testexecute_page3_label_3")
        self.gridLayout_4.addWidget(self.testexecute_page3_label_3, 0, 0, 1, 1)
        self.listWidget_com = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_com.setObjectName("listWidget_com")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_com.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_com.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_com.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_com.addItem(item)
        self.gridLayout_4.addWidget(self.listWidget_com, 1, 0, 1, 1)
        self.testexecute_page4_label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page4_label_10.setFont(font)
        self.testexecute_page4_label_10.setObjectName("testexecute_page4_label_10")
        self.gridLayout_4.addWidget(self.testexecute_page4_label_10, 2, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.testexecute_page4_label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page4_label_6.setFont(font)
        self.testexecute_page4_label_6.setObjectName("testexecute_page4_label_6")
        self.gridLayout_11.addWidget(self.testexecute_page4_label_6, 0, 0, 1, 1)
        self.lineEdit_local_ip = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.lineEdit_local_ip.setFont(font)
        self.lineEdit_local_ip.setObjectName("lineEdit_local_ip")
        self.gridLayout_11.addWidget(self.lineEdit_local_ip, 0, 1, 1, 1)
        self.testexecute_page4_label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page4_label_7.setFont(font)
        self.testexecute_page4_label_7.setObjectName("testexecute_page4_label_7")
        self.gridLayout_11.addWidget(self.testexecute_page4_label_7, 0, 2, 1, 1)
        self.lineEdit_local_port = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.lineEdit_local_port.setFont(font)
        self.lineEdit_local_port.setObjectName("lineEdit_local_port")
        self.gridLayout_11.addWidget(self.lineEdit_local_port, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_11, 3, 0, 1, 1)
        self.pushButton_test = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_test.setObjectName("pushButton_test")
        self.gridLayout_4.addWidget(self.pushButton_test, 3, 1, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.testexecute_page4_label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page4_label_8.setFont(font)
        self.testexecute_page4_label_8.setObjectName("testexecute_page4_label_8")
        self.gridLayout_12.addWidget(self.testexecute_page4_label_8, 0, 0, 1, 1)
        self.lineEdit_remote_ip = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.lineEdit_remote_ip.setFont(font)
        self.lineEdit_remote_ip.setObjectName("lineEdit_remote_ip")
        self.gridLayout_12.addWidget(self.lineEdit_remote_ip, 0, 1, 1, 1)
        self.testexecute_page4_label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page4_label_9.setFont(font)
        self.testexecute_page4_label_9.setObjectName("testexecute_page4_label_9")
        self.gridLayout_12.addWidget(self.testexecute_page4_label_9, 0, 2, 1, 1)
        self.lineEdit_remote_port = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.lineEdit_remote_port.setFont(font)
        self.lineEdit_remote_port.setObjectName("lineEdit_remote_port")
        self.gridLayout_12.addWidget(self.lineEdit_remote_port, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_12, 4, 0, 1, 1)
        self.pushButton_remote_link = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_remote_link.setObjectName("pushButton_remote_link")
        self.gridLayout_4.addWidget(self.pushButton_remote_link, 4, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_3.addWidget(self.textBrowser_log, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 5, 0, 1, 2)
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
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "协议转换与控制测试：COM5-COM8"))
        self.testexecute_page3_label_3.setText(_translate("Dialog", "测试端口"))
        __sortingEnabled = self.listWidget_com.isSortingEnabled()
        self.listWidget_com.setSortingEnabled(False)
        item = self.listWidget_com.item(0)
        item.setText(_translate("Dialog", "COM5"))
        item = self.listWidget_com.item(1)
        item.setText(_translate("Dialog", "COM6"))
        item = self.listWidget_com.item(2)
        item.setText(_translate("Dialog", "COM7"))
        item = self.listWidget_com.item(3)
        item.setText(_translate("Dialog", "COM8"))
        self.listWidget_com.setSortingEnabled(__sortingEnabled)
        self.testexecute_page4_label_10.setText(_translate("Dialog", "测试配置"))
        self.testexecute_page4_label_6.setText(_translate("Dialog", "本地IP"))
        self.testexecute_page4_label_7.setText(_translate("Dialog", "端口"))
        self.pushButton_test.setText(_translate("Dialog", "测试"))
        self.testexecute_page4_label_8.setText(_translate("Dialog", "远程IP"))
        self.testexecute_page4_label_9.setText(_translate("Dialog", "端口"))
        self.pushButton_remote_link.setText(_translate("Dialog", "连接"))
        self.groupBox_3.setTitle(_translate("Dialog", "测试日志"))
        self.pushButton_next.setText(_translate("Dialog", "下一步"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
