# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\sourcecode\54\Eric6WorkSpace\testInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 528)
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
        self.testexecute_page1_label_2 = QtWidgets.QLabel(Dialog)
        self.testexecute_page1_label_2.setGeometry(QtCore.QRect(20, 10, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.testexecute_page1_label_2.setFont(font)
        self.testexecute_page1_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.testexecute_page1_label_2.setObjectName("testexecute_page1_label_2")
        self.groupBox_9 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 40, 341, 141))
        self.groupBox_9.setFlat(False)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label = QtWidgets.QLabel(self.groupBox_9)
        self.label.setObjectName("label")
        self.gridLayout_28.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_main_name = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_main_name.setObjectName("lineEdit_main_name")
        self.gridLayout_28.addWidget(self.lineEdit_main_name, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setObjectName("label_2")
        self.gridLayout_28.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_main_tuhao = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_main_tuhao.setObjectName("lineEdit_main_tuhao")
        self.gridLayout_28.addWidget(self.lineEdit_main_tuhao, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.label_3.setObjectName("label_3")
        self.gridLayout_28.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_main_serialno = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_main_serialno.setObjectName("lineEdit_main_serialno")
        self.gridLayout_28.addWidget(self.lineEdit_main_serialno, 2, 1, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 190, 341, 141))
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_4 = QtWidgets.QLabel(self.groupBox_10)
        self.label_4.setObjectName("label_4")
        self.gridLayout_29.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_branch_name = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_branch_name.setObjectName("lineEdit_branch_name")
        self.gridLayout_29.addWidget(self.lineEdit_branch_name, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_10)
        self.label_5.setObjectName("label_5")
        self.gridLayout_29.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_branch_tuhao = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_branch_tuhao.setObjectName("lineEdit_branch_tuhao")
        self.gridLayout_29.addWidget(self.lineEdit_branch_tuhao, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_10)
        self.label_6.setObjectName("label_6")
        self.gridLayout_29.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_branch_serialno = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_branch_serialno.setObjectName("lineEdit_branch_serialno")
        self.gridLayout_29.addWidget(self.lineEdit_branch_serialno, 2, 1, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 340, 341, 141))
        self.groupBox_11.setFlat(False)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_7 = QtWidgets.QLabel(self.groupBox_11)
        self.label_7.setObjectName("label_7")
        self.gridLayout_30.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_dut_name = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_dut_name.setObjectName("lineEdit_dut_name")
        self.gridLayout_30.addWidget(self.lineEdit_dut_name, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_11)
        self.label_8.setObjectName("label_8")
        self.gridLayout_30.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_dut_tuhao = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_dut_tuhao.setObjectName("lineEdit_dut_tuhao")
        self.gridLayout_30.addWidget(self.lineEdit_dut_tuhao, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_11)
        self.label_9.setObjectName("label_9")
        self.gridLayout_30.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_dut_serialno = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_dut_serialno.setObjectName("lineEdit_dut_serialno")
        self.gridLayout_30.addWidget(self.lineEdit_dut_serialno, 2, 1, 1, 1)
        self.pushButton_verify = QtWidgets.QPushButton(Dialog)
        self.pushButton_verify.setGeometry(QtCore.QRect(270, 490, 93, 28))
        self.pushButton_verify.setObjectName("pushButton_verify")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "测试参数"))
        self.testexecute_page1_label_2.setText(_translate("Dialog", "测试基础信息"))
        self.groupBox_9.setTitle(_translate("Dialog", "所属整机"))
        self.label.setText(_translate("Dialog", "名称："))
        self.label_2.setText(_translate("Dialog", "图号："))
        self.label_3.setText(_translate("Dialog", "序列号："))
        self.groupBox_10.setTitle(_translate("Dialog", "所属分机"))
        self.label_4.setText(_translate("Dialog", "名称："))
        self.label_5.setText(_translate("Dialog", "图号："))
        self.label_6.setText(_translate("Dialog", "序列号："))
        self.groupBox_11.setTitle(_translate("Dialog", "被测件"))
        self.label_7.setText(_translate("Dialog", "名称："))
        self.label_8.setText(_translate("Dialog", "图号："))
        self.label_9.setText(_translate("Dialog", "序列号："))
        self.pushButton_verify.setText(_translate("Dialog", "确认运行"))

