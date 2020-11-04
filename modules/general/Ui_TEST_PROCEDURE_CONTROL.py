# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\tianheng_projects\54\54TestFramework\ui\TEST_PROCEDURE_CONTROL.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(334, 145)
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
        self.textBrowser_contents = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_contents.setGeometry(QtCore.QRect(10, 10, 300, 61))
        self.textBrowser_contents.setObjectName("textBrowser_contents")
        self.pushButton_control = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_control.setGeometry(QtCore.QRect(120, 80, 91, 31))
        self.pushButton_control.setObjectName("pushButton_control")
        self.pushButton_control.raise_()
        self.textBrowser_contents.raise_()
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_control.setText(_translate("Dialog", "下一步"))
import iconQrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
