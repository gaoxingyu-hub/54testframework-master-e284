# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work\AutoTest\54testframework\ui\AUTO_TEST.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_freq_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_freq_sg.setObjectName("lineEdit_freq_sg")
        self.gridLayout_3.addWidget(self.lineEdit_freq_sg, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_power = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_power.setObjectName("lineEdit_power")
        self.gridLayout_3.addWidget(self.lineEdit_power, 2, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 2, 2, 1, 1)
        self.lineEdit_addr_sg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_addr_sg.setObjectName("lineEdit_addr_sg")
        self.gridLayout_3.addWidget(self.lineEdit_addr_sg, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.label_img = QtWidgets.QLabel(self.groupBox)
        self.label_img.setText("")
        self.label_img.setScaledContents(False)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.gridLayout_5.addWidget(self.label_img, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 3, 1, 1)
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.gridLayout_5.addWidget(self.textBrowser_contents, 0, 0, 1, 5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_rbw = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_rbw.setObjectName("lineEdit_rbw")
        self.gridLayout_4.addWidget(self.lineEdit_rbw, 3, 1, 1, 2)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 3, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_3, 2, 3, 1, 1)
        self.lineEdit_freq_sa = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_freq_sa.setObjectName("lineEdit_freq_sa")
        self.gridLayout_4.addWidget(self.lineEdit_freq_sa, 2, 1, 1, 2)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_6, 1, 3, 1, 1)
        self.lineEdit_addr_sa = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_addr_sa.setObjectName("lineEdit_addr_sa")
        self.gridLayout_4.addWidget(self.lineEdit_addr_sa, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 2, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 3, 0, 1, 5)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.groupBox_2.setTitle(_translate("Dialog", "Source de signal"))
            self.comboBox_5.setItemText(0, _translate("Dialog", "LAN"))
            self.label.setText(_translate("Dialog", "Fréquence"))
            self.comboBox.setItemText(0, _translate("Dialog", "MHz"))
            self.label_2.setText(_translate("Dialog", "Puissance"))
            self.comboBox_2.setItemText(0, _translate("Dialog", "dBm"))
            self.label_5.setText(_translate("Dialog", "addr"))
            self.groupBox_3.setTitle(_translate("Dialog", "Spectographe"))
            self.label_3.setText(_translate("Dialog", "Fréquence"))
            self.label_4.setText(_translate("Dialog", "Span"))
            self.comboBox_4.setItemText(0, _translate("Dialog", "MHz"))
            self.comboBox_3.setItemText(0, _translate("Dialog", "MHz"))
            self.comboBox_6.setItemText(0, _translate("Dialog", "LAN"))
            self.label_6.setText(_translate("Dialog", "addr"))
            self.pushButton_next.setText(_translate("Dialog", "Étape suivante"))
        else:
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.groupBox_2.setTitle(_translate("Dialog", "信号源"))
            self.comboBox_5.setItemText(0, _translate("Dialog", "LAN"))
            self.label.setText(_translate("Dialog", "频率"))
            self.comboBox.setItemText(0, _translate("Dialog", "MHz"))
            self.label_2.setText(_translate("Dialog", "功率"))
            self.comboBox_2.setItemText(0, _translate("Dialog", "dBm"))
            self.label_5.setText(_translate("Dialog", "addr"))
            self.groupBox_3.setTitle(_translate("Dialog", "频谱仪"))
            self.label_3.setText(_translate("Dialog", "频率"))
            self.label_4.setText(_translate("Dialog", "Span"))
            self.comboBox_4.setItemText(0, _translate("Dialog", "MHz"))
            self.comboBox_3.setItemText(0, _translate("Dialog", "MHz"))
            self.comboBox_6.setItemText(0, _translate("Dialog", "LAN"))
            self.label_6.setText(_translate("Dialog", "addr"))
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

