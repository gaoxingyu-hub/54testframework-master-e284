# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\router\Router.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(980, 980)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:#E3EAF4;\n"
"margin-top:10px;\n"
"}\n"
"\n"
"QTextBrower{\n"
"background-color:#E3EAF4;\n"
"border-width:0;border-style:outset\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:#E3EAF4;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#E3EAF4;\n"
"}\n"
"\n"
"QStackedWidget{\n"
"background-color:#E3EAF4;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"background-color:#E3EAF4;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"border:1px solid rgb(0, 0, 0);\n"
"background-color:#E3EAF4;\n"
"}\n"
"\n"
"\n"
"QToolBar{\n"
"background-color:#D5D5D5;\n"
"height:30px;\n"
"border:None;\n"
"padding:1px;\n"
"}\n"
"/****QTreeWidget****/\n"
"QTreeWidget{\n"
"background-color:#E3EAF4;\n"
"padding-top:20px;\n"
"padding-left:10px;\n"
"margin-top:20px;\n"
"}\n"
"QTreeView::item{\n"
"font: 14px;\n"
"}\n"
"QTreeView::item:selected{\n"
"selection-color: #1F95FF;\n"
"}\n"
"QTreeView::item:hover{\n"
"background-color:#D0DAE5;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"border-image: none;\n"
"image: url(imgs/common/plus.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"border-image: none;\n"
"image: url(imgs/common/Minus.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(imgs/common/tree.png);\n"
"}\n"
"QTableWidget{\n"
"outline: none;\n"
"selection-color:#666666;\n"
"alternate-background-color:#F9FAFC;\n"
"}\n"
"QTableCornerButton::section{\n"
"background: #EDF2F8;\n"
"}\n"
"QTableWidget::item{\n"
"font-size:14px;\n"
"line-height:30px;\n"
"border:1px solid #D2D2D2;\n"
"}\n"
"\n"
"QTableWidget::item:hover{\n"
"background-color:#EAF7FF;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"color: #666666;\n"
"text-align:center;\n"
"font: 14px Arial;\n"
"border:1px solid #D2D2D2;\n"
"background: #F9FBFD;\n"
"width: 40px;\n"
"height:30px;\n"
"alternate-background-color:#F9FAFC;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"color: #666666;\n"
"font: 14px Microsoft YaHei;\n"
"padding: 0px 1px 0 1px;\n"
"text-align:center;\n"
"border:1px solid #D2D2D2;\n"
"background: #EDF2F8;\n"
"height: 30px;\n"
"alternate-background-color:#F9FAFC;\n"
"}\n"
"QScrollBar:vertical{\n"
"border: 5px solid #D5D5D5;\n"
"}\n"
"/****QPushButton****/\n"
"QPushButton{\n"
"width:32px;\n"
"height:32px;\n"
"background-color:#F4F4F3;\n"
"color: #FFFFFF;\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#2784D6;\n"
"cursor:pointer;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#2784D6;\n"
"}\n"
"QTreeWidget::indicator:checked {\n"
"    image: url(imgs/common/checked.png);\n"
"}\n"
"QTreeWidget::indicator:unchecked {\n"
"    image: url(imgs/common/check.png);\n"
"}\n"
"")
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_start.setStyleSheet("")
        self.pushButton_start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon/start.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setAutoFillBackground(False)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon/cancel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 0, 2, 1, 1)
        self.pushButton_restart = QtWidgets.QPushButton(Dialog)
        self.pushButton_restart.setStyleSheet("")
        self.pushButton_restart.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/stop.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_restart.setIcon(icon2)
        self.pushButton_restart.setIconSize(QtCore.QSize(32, 31))
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.gridLayout.addWidget(self.pushButton_restart, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(808, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_test_modules = QtWidgets.QGroupBox(Dialog)
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
        self.groupBox_test_resource = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test_resource.setObjectName("groupBox_test_resource")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_test_resource)
        self.gridLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_test_resource = QtWidgets.QTableWidget(self.groupBox_test_resource)
        self.tableWidget_test_resource.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget_test_resource.setAlternatingRowColors(True)
        self.tableWidget_test_resource.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_test_resource.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_test_resource.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_test_resource.setShowGrid(False)
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
        self.tableWidget_test_resource.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_test_resource.setItem(1, 4, item)
        self.tableWidget_test_resource.horizontalHeader().setVisible(True)
        self.tableWidget_test_resource.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_test_resource.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_test_resource.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_test_resource.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_test_resource.verticalHeader().setVisible(False)
        self.tableWidget_test_resource.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_test_resource.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_test_resource.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_test_resource.verticalHeader().setStretchLastSection(False)
        self.gridLayout_5.addWidget(self.tableWidget_test_resource, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_test_resource)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_test_results = QtWidgets.QGroupBox(Dialog)
        self.groupBox_test_results.setTitle("")
        self.groupBox_test_results.setObjectName("groupBox_test_results")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_test_results)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_test_results)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_test_results)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_test_modules.setTitle(_translate("Dialog", "测试项目"))
        self.label_test_duration.setText(_translate("Dialog", "00:00:00"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "路由器"))
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
        item = self.tableWidget_test_resource.item(0, 1)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(0, 2)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(0, 3)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(0, 4)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_test_resource.item(1, 1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 3)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_test_resource.item(1, 4)
        item.setText(_translate("Dialog", "2"))
        self.tableWidget_test_resource.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "测试项目"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "测试结果"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "测试结论"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "路由器模块测试"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
