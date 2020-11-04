# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\code\54testframework\ui\high_freq\AUTO_TEST_PA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from common.info import SystemLanguage


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
        self.lineEdit_freq_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg.setObjectName("lineEdit_freq_sg")
        self.gridLayout_3.addWidget(self.lineEdit_freq_sg, 0, 1, 1, 1)
        self.comboBox_sg_power = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_sg_power.setObjectName("comboBox_sg_power")
        self.comboBox_sg_power.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_sg_power, 1, 2, 1, 1)
        self.comboBox_sg_freq = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_sg_freq.setObjectName("comboBox_sg_freq")
        self.comboBox_sg_freq.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_sg_freq, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_power_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_power_sg.setObjectName("lineEdit_power_sg")
        self.gridLayout_3.addWidget(self.lineEdit_power_sg, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_freq_sa = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_freq_sa.setObjectName("lineEdit_freq_sa")
        self.gridLayout_5.addWidget(self.lineEdit_freq_sa, 0, 1, 1, 1)
        self.comboBox_sa_freq = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_sa_freq.setObjectName("comboBox_sa_freq")
        self.comboBox_sa_freq.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_sa_freq, 0, 2, 1, 1)
        self.lineEdit_bw_sa = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_bw_sa.setObjectName("lineEdit_bw_sa")
        self.gridLayout_5.addWidget(self.lineEdit_bw_sa, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox_sa_bw = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_sa_bw.setObjectName("comboBox_sa_bw")
        self.comboBox_sa_bw.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_sa_bw, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
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
        if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
            self.pushButton_next.setText(_translate("Dialog", "Étape suivante"))
            self.groupBox_2.setTitle(_translate("Dialog", "Source de signal"))
            self.comboBox_sg_power.setItemText(0, _translate("Dialog", "dBm"))
            self.comboBox_sg_freq.setItemText(0, _translate("Dialog", "MHz"))
            self.label_2.setText(_translate("Dialog", "Puissance"))
            self.label.setText(_translate("Dialog", "Fréquence"))
            self.groupBox_4.setTitle(_translate("Dialog", "Spectographe "))
            self.comboBox_sa_freq.setItemText(0, _translate("Dialog", "MHz"))
            self.label_7.setText(_translate("Dialog", "Fréquence"))
            self.comboBox_sa_bw.setItemText(0, _translate("Dialog", "MHz"))
            self.label_8.setText(_translate("Dialog", "Largeur de bande"))
        else:
            self.pushButton_next.setText(_translate("Dialog", "下一步"))
            self.groupBox_2.setTitle(_translate("Dialog", "信号源"))
            self.comboBox_sg_power.setItemText(0, _translate("Dialog", "dBm"))
            self.comboBox_sg_freq.setItemText(0, _translate("Dialog", "MHz"))
            self.label_2.setText(_translate("Dialog", "功率"))
            self.label.setText(_translate("Dialog", "频率"))
            self.groupBox_4.setTitle(_translate("Dialog", "频谱仪"))
            self.comboBox_sa_freq.setItemText(0, _translate("Dialog", "MHz"))
            self.label_7.setText(_translate("Dialog", "频率"))
            self.comboBox_sa_bw.setItemText(0, _translate("Dialog", "MHz"))
            self.label_8.setText(_translate("Dialog", "带宽"))
import res.iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
