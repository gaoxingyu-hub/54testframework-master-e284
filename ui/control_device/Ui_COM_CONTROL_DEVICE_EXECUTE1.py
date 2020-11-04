# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\control_device\COM_CONTROL_DEVICE_EXECUTE1.ui'
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.verticalLayout.addWidget(self.textBrowser_contents)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.gridLayout_3.addWidget(self.textBrowser_log, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 2, 4, 1)
        self.listWidget_lan = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_lan.setObjectName("listWidget_lan")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_lan.addItem(item)
        self.gridLayout_4.addWidget(self.listWidget_lan, 1, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.gridLayout_4.addWidget(self.lineEdit_ip, 3, 0, 1, 1)
        self.pushButton_execute = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.gridLayout_4.addWidget(self.pushButton_execute, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
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
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "网络协议转换板测试"))
        self.label_3.setText(_translate("Dialog", "测试端口"))
        self.groupBox_3.setTitle(_translate("Dialog", "测试日志"))
        __sortingEnabled = self.listWidget_lan.isSortingEnabled()
        self.listWidget_lan.setSortingEnabled(False)
        item = self.listWidget_lan.item(0)
        item.setText(_translate("Dialog", "LAN2"))
        item = self.listWidget_lan.item(1)
        item.setText(_translate("Dialog", "LAN3"))
        item = self.listWidget_lan.item(2)
        item.setText(_translate("Dialog", "LAN4"))
        item = self.listWidget_lan.item(3)
        item.setText(_translate("Dialog", "LAN5"))
        item = self.listWidget_lan.item(4)
        item.setText(_translate("Dialog", "LAN6"))
        item = self.listWidget_lan.item(5)
        item.setText(_translate("Dialog", "LAN7"))
        item = self.listWidget_lan.item(6)
        item.setText(_translate("Dialog", "LAN8"))
        self.listWidget_lan.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Dialog", "测试IP地址"))
        self.lineEdit_ip.setText(_translate("Dialog", "192.168.1.200"))
        self.pushButton_execute.setText(_translate("Dialog", "测试"))
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
