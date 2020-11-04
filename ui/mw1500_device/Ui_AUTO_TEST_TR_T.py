# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\mw1500_device\AUTO_TEST_TR_T.ui'
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_freq_H = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_freq_H.setObjectName("comboBox_freq_H")
        self.comboBox_freq_H.addItem("")
        self.comboBox_freq_H.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_freq_H)
        self.lineEdit_freq_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_freq_sg.sizePolicy().hasHeightForWidth())
        self.lineEdit_freq_sg.setSizePolicy(sizePolicy)
        self.lineEdit_freq_sg.setFrame(False)
        self.lineEdit_freq_sg.setDragEnabled(False)
        self.lineEdit_freq_sg.setReadOnly(True)
        self.lineEdit_freq_sg.setObjectName("lineEdit_freq_sg")
        self.horizontalLayout_2.addWidget(self.lineEdit_freq_sg)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_freq_M = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_freq_M.setObjectName("comboBox_freq_M")
        self.comboBox_freq_M.addItem("")
        self.comboBox_freq_M.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_freq_M)
        self.lineEdit_freq_sg_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_freq_sg_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_freq_sg_2.setSizePolicy(sizePolicy)
        self.lineEdit_freq_sg_2.setFrame(False)
        self.lineEdit_freq_sg_2.setDragEnabled(False)
        self.lineEdit_freq_sg_2.setReadOnly(True)
        self.lineEdit_freq_sg_2.setObjectName("lineEdit_freq_sg_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_freq_sg_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_freq_L = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_freq_L.setObjectName("comboBox_freq_L")
        self.comboBox_freq_L.addItem("")
        self.comboBox_freq_L.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_freq_L)
        self.lineEdit_freq_sg_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_freq_sg_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_freq_sg_3.setSizePolicy(sizePolicy)
        self.lineEdit_freq_sg_3.setFrame(False)
        self.lineEdit_freq_sg_3.setDragEnabled(False)
        self.lineEdit_freq_sg_3.setReadOnly(True)
        self.lineEdit_freq_sg_3.setObjectName("lineEdit_freq_sg_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_freq_sg_3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 2, 2)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(2, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_next.setText(_translate("Dialog", "下一步"))
        self.groupBox_2.setTitle(_translate("Dialog", "测试频率"))
        self.label.setText(_translate("Dialog", "高频点"))
        self.comboBox_freq_H.setItemText(0, _translate("Dialog", "1750"))
        self.comboBox_freq_H.setItemText(1, _translate("Dialog", "1850"))
        self.lineEdit_freq_sg.setText(_translate("Dialog", "MHz"))
        self.label_2.setText(_translate("Dialog", "中频点"))
        self.comboBox_freq_M.setItemText(0, _translate("Dialog", "1550"))
        self.comboBox_freq_M.setItemText(1, _translate("Dialog", "1650"))
        self.lineEdit_freq_sg_2.setText(_translate("Dialog", "MHz"))
        self.label_3.setText(_translate("Dialog", "低频点"))
        self.comboBox_freq_L.setItemText(0, _translate("Dialog", "1350"))
        self.comboBox_freq_L.setItemText(1, _translate("Dialog", "1450"))
        self.lineEdit_freq_sg_3.setText(_translate("Dialog", "MHz"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
