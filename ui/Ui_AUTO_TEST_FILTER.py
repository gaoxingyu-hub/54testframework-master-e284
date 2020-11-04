# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\AUTO_TEST_FILTER.ui'
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
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_bw_na = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_bw_na.setObjectName("lineEdit_bw_na")
        self.gridLayout_5.addWidget(self.lineEdit_bw_na, 1, 1, 1, 1)
        self.comboBox_sa_bw = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_sa_bw.setObjectName("comboBox_sa_bw")
        self.comboBox_sa_bw.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_sa_bw, 1, 2, 1, 1)
        self.lineEdit_freq_na = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_freq_na.setObjectName("lineEdit_freq_na")
        self.gridLayout_5.addWidget(self.lineEdit_freq_na, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.comboBox_na_freq = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_na_freq.setObjectName("comboBox_na_freq")
        self.comboBox_na_freq.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_na_freq, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 2, 2)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_next.setText(_translate("Dialog", "下一步"))
        self.groupBox_4.setTitle(_translate("Dialog", "矢量网络分析仪"))
        self.label_7.setText(_translate("Dialog", "频率"))
        self.comboBox_sa_bw.setItemText(0, _translate("Dialog", "MHz"))
        self.label_8.setText(_translate("Dialog", "带宽"))
        self.comboBox_na_freq.setItemText(0, _translate("Dialog", "MHz"))
import iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
