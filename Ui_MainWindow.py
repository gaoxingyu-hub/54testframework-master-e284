# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from constant_trans import TransConstants


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QDialog{\n"
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
"QTreeView::branch:has-siblings:adjoins-item {\n"
"border-image: url(imgs/common/more.png);\n"
"}\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"border-image: url(imgs/common/end.png)\n"
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
"background-color:#2784D6;\n"
"}\n"
)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxMenu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxMenu.setStyleSheet("background-color:#E3EAF4;\n"
"color:#666666")
        self.groupBoxMenu.setObjectName("groupBoxMenu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxMenu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBoxMenu)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setAutoScroll(False)
        self.treeWidget.setIconSize(QtCore.QSize(0, 0))
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBoxMenu)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:#E3EAF4;\n"
"color:#666666")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setStyleSheet("background-color:#172545;\n"
"height:30px;\n"
"border:None;\n"
"padding:1px;\n"
"font-size:14px;\n"
"font-family:Microsoft YaHei;\n"
"color: #FFFFFF;")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.toolBar.addAction(self.action_about)
        self.toolBar.addAction(self.action_help)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle( TransConstants.main_fkj)
        self.groupBoxMenu.setTitle( TransConstants.main_test_module)
        self.treeWidget.headerItem().setText(0, "1")
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0,  TransConstants.main_tongxin)
        self.treeWidget.topLevelItem(0).child(0).setText(0,  TransConstants.main_sanshe)
        self.treeWidget.topLevelItem(0).child(1).setText(0,  TransConstants.main_mw1500)
        self.treeWidget.topLevelItem(0).child(2).setText(0,  TransConstants.main_ecom1)
        self.treeWidget.topLevelItem(0).child(3).setText(0,  TransConstants.main_ecom2)
        self.treeWidget.topLevelItem(0).child(4).setText(0,  TransConstants.main_vhf)
        self.treeWidget.topLevelItem(0).child(5).setText(0,  TransConstants.main_zizuwang)
        self.treeWidget.topLevelItem(0).child(6).setText(0,  TransConstants.main_sdsl)
        self.treeWidget.topLevelItem(0).child(7).setText(0,  TransConstants.main_ip)
        self.treeWidget.topLevelItem(0).child(8).setText(0,  TransConstants.main_tongxin_control)
        self.treeWidget.topLevelItem(0).child(9).setText(0,  TransConstants.router)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle( TransConstants.TESTTABLE_ITEM)
        self.toolBar.setWindowTitle( "toolBar")
        self.action_about.setText( TransConstants.about)
        self.action_about.setToolTip( "<html><head/><body><p><img src=\":/newPrefix/icon/start1.ico\"/></p></body></html>")
        self.action_help.setText( TransConstants.t_help)
        self.action_help.setToolTip( "<html><head/><body><p><img src=\":/newPrefix/icon/start1.ico\"/></p></body></html>")
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
