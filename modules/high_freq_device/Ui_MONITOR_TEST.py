# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\autoTest\54testframework\ui\MONITOR_TEST.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_v2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v2.setObjectName("checkBox_v2")
        self.gridLayout_2.addWidget(self.checkBox_v2, 0, 0, 1, 1)
        self.checkBox_v3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v3.setObjectName("checkBox_v3")
        self.gridLayout_2.addWidget(self.checkBox_v3, 0, 1, 1, 1)
        self.checkBox_v4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v4.setObjectName("checkBox_v4")
        self.gridLayout_2.addWidget(self.checkBox_v4, 0, 2, 1, 1)
        self.checkBox_v5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v5.setObjectName("checkBox_v5")
        self.gridLayout_2.addWidget(self.checkBox_v5, 0, 3, 1, 1)
        self.checkBox_v6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v6.setObjectName("checkBox_v6")
        self.gridLayout_2.addWidget(self.checkBox_v6, 1, 0, 1, 1)
        self.checkBox_v8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v8.setObjectName("checkBox_v8")
        self.gridLayout_2.addWidget(self.checkBox_v8, 1, 1, 1, 1)
        self.checkBox_v9 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v9.setObjectName("checkBox_v9")
        self.gridLayout_2.addWidget(self.checkBox_v9, 1, 2, 1, 1)
        self.checkBox_v10 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v10.setObjectName("checkBox_v10")
        self.gridLayout_2.addWidget(self.checkBox_v10, 1, 3, 1, 1)
        self.checkBox_v11 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v11.setObjectName("checkBox_v11")
        self.gridLayout_2.addWidget(self.checkBox_v11, 2, 0, 1, 1)
        self.checkBox_v12 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v12.setObjectName("checkBox_v12")
        self.gridLayout_2.addWidget(self.checkBox_v12, 2, 1, 1, 1)
        self.checkBox_v13 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_v13.setObjectName("checkBox_v13")
        self.gridLayout_2.addWidget(self.checkBox_v13, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if SystemLanguage.LANGUAGE == SystemLanguage.fr_FR:
            self.checkBox_v2.setText(_translate("Dialog", "Le voyant V2 s’allume."))
            self.checkBox_v3.setText(_translate("Dialog", "Le voyant V3 clignote"))
            self.checkBox_v4.setText(_translate("Dialog", "Le voyant V4 clignote"))
            self.checkBox_v5.setText(_translate("Dialog", "Le voyant V5 clignote"))
            self.checkBox_v6.setText(_translate("Dialog", "Le voyant V6 clignote"))
            self.checkBox_v8.setText(_translate("Dialog", "Le voyant V8 s’allume."))
            self.checkBox_v9.setText(_translate("Dialog", "Le voyant V9 s’allume."))
            self.checkBox_v10.setText(_translate("Dialog", "Le voyant V10 s’allume."))
            self.checkBox_v11.setText(_translate("Dialog", "Le voyant V11 s’allume."))
            self.checkBox_v12.setText(_translate("Dialog", "Le voyant V12 clignote"))
            self.checkBox_v13.setText(_translate("Dialog", "Le voyant V13 clignote"))
            self.pushButton_next.setText(_translate("Dialog", "Étape suivante"))
        else:
            self.checkBox_v2.setText(_translate("Dialog", "V2指示灯亮起"))
            self.checkBox_v3.setText(_translate("Dialog", "V3指示灯闪烁"))
            self.checkBox_v4.setText(_translate("Dialog", "V4指示灯闪烁"))
            self.checkBox_v5.setText(_translate("Dialog", "V5指示灯闪烁"))
            self.checkBox_v6.setText(_translate("Dialog", "V6指示灯闪烁"))
            self.checkBox_v8.setText(_translate("Dialog", "V8指示灯亮起"))
            self.checkBox_v9.setText(_translate("Dialog", "V9指示灯亮起"))
            self.checkBox_v10.setText(_translate("Dialog", "V10指示灯亮起"))
            self.checkBox_v11.setText(_translate("Dialog", "V11指示灯亮起"))
            self.checkBox_v12.setText(_translate("Dialog", "V12指示灯闪烁"))
            self.checkBox_v13.setText(_translate("Dialog", "V13指示灯闪烁"))
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
