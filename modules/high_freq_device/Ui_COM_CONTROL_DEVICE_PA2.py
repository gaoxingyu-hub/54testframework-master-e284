# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tianheng_projects\54\54TestFramework\ui\COM_CONTROL_DEVICE_PA2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(980, 980)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QTextBrower{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QStackedWidget{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:12px;\n"
"font-family:Microsoft YaHei;\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QPushButton{         /*按钮自适应拉伸背景*/\n"
"border-width: 2px 15px 2px 15px;\n"
"background-color:#2884D8;\n"
"color: #FFFFFF;\n"
"font-size:12px;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font-size:12px;\n"
"font-family:Microsoft YaHei;\n"
"border:1px solid rgb(0, 0, 0); \n"
"}")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_4 = QtWidgets.QSplitter(Dialog)
        self.splitter_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.groupBox_test_results = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test_results.setGeometry(QtCore.QRect(10, 440, 961, 521))
        self.groupBox_test_results.setTitle("")
        self.groupBox_test_results.setObjectName("groupBox_test_results")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_test_results)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget_test_results = QtWidgets.QTableWidget(self.groupBox_test_results)
        self.tableWidget_test_results.setObjectName("tableWidget_test_results")
        self.tableWidget_test_results.setColumnCount(0)
        self.tableWidget_test_results.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_test_results, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 146, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_start.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"")
        self.pushButton_start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon/start1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_restart = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_restart.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.pushButton_restart.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon/restart1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_restart.setIcon(icon1)
        self.pushButton_restart.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.gridLayout.addWidget(self.pushButton_restart, 0, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_close.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.pushButton_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icon/close1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 961, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_test_modules = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_test_modules.setObjectName("groupBox_test_modules")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_test_modules)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_test_modules)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_test_duration = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setKerning(False)
        self.label_test_duration.setFont(font)
        self.label_test_duration.setTextFormat(QtCore.Qt.PlainText)
        self.label_test_duration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_test_duration.setObjectName("label_test_duration")
        self.gridLayout_2.addWidget(self.label_test_duration, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_test_modules)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.gridLayout_3.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_test_modules)
        self.groupBox_test_resource = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_test_resource.setObjectName("groupBox_test_resource")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_test_resource)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_test_resource = QtWidgets.QTableWidget(self.groupBox_test_resource)
        self.tableWidget_test_resource.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget_test_resource.setObjectName("tableWidget_test_resource")
        self.tableWidget_test_resource.setColumnCount(5)
        self.tableWidget_test_resource.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 4, item)
        self.tableWidget_test_resource.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_test_resource.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout_5.addWidget(self.tableWidget_test_resource, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_test_resource)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_test_modules.setTitle(_translate("Dialog", "测试项目"))
        self.label_test_duration.setText(_translate("Dialog", "00:00:00"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "协议控制和转换模块"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_test_resource.setTitle(_translate("Dialog", "测试资源"))
        item = self.tableWidget_test_resource.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "名称"))
        item = self.tableWidget_test_resource.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "类型"))
        item = self.tableWidget_test_resource.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "编号/型号"))
        item = self.tableWidget_test_resource.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "数量"))
        __sortingEnabled = self.tableWidget_test_resource.isSortingEnabled()
        self.tableWidget_test_resource.setSortingEnabled(False)
        item = self.tableWidget_test_resource.item(0, 0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(0, 1)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(0, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(0, 3)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(0, 4)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(1, 0)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 3)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 4)
        item.setText(_translate("Dialog", "2"))
        self.tableWidget_test_resource.setSortingEnabled(__sortingEnabled)
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
