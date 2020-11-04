# -*- coding: utf-8 -*-

"""
Module implementing DialogSdslCom.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from .Ui_SDSL_COM import Ui_Dialog
from common.logConfig import Logger
from common.serial_port_utility import ThSerialPortUtility
from .SDSL_CONSTANT import ModuleConstants
import serial
import serial.threaded
import time
from common.info import Constants

logger = Logger.module_logger("sdsl com test")
class DialogSdslCom(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    _signalFinish = pyqtSignal(str, object)
    test_result = {}

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DialogSdslCom, self).__init__(parent)
        self.setupUi(self)
        self.flag = 1
        self.get_ports()
        #7E 06 00 25 2B 81H
        self.cmds = [126, 6, 0, 37, 42, 129]
        #7E 19 00 95 53 44 53 4C 20 20 20 20 20 20 34 00 33 03 3D 57 01 01 01 A5 81
        self.verify_cmds = [126,25,0,149,83,68,83,76,32,32,32,32,32,32,52,0,51,3,61,87,1,1,1,165,129]

    
    @pyqtSlot()
    def on_pushButton_send_clicked(self):
        """
        Slot documentation goes here.
        """
        com = self.comboBox_com.currentText()
        if com:
            try:
                com_obj = serial.Serial(port=com, baudrate=115200,
                                        bytesize=8, parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE, timeout=3)
                with serial.threaded.ReaderThread(com_obj, TestFramedPacket) as protocol:
                    protocol.send_packet(self.cmds)
                    time.sleep(1)
                    if protocol.received_packets:
                        pass
            except serial.SerialTimeoutException as e:
                QMessageBox.show(ModuleConstants.QMESSAGEBOX_WARN,
                                 ModuleConstants.QMESSAGEBOX_WARN_COM_CONNECT_FAIL)
                logger.error(str(e))
        else:
            QMessageBox.show(ModuleConstants.QMESSAGEBOX_WARN,
                             ModuleConstants.QMESSAGEBOX_WARN_COM_CONNECT_FAIL)
            logger.error(ModuleConstants.QMESSAGEBOX_WARN_COM_CONNECT_FAIL)

    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        self._signalFinish.emit(Constants.SIGNAL_TEST_RESULT, {self.windowTitle(): Constants.RESULT_SUCCESS})
        self._signalFinish.emit(self.windowTitle(), self.test_result)
        self.accept()
        self.close()

    def set_contents(self,title,contents,img_file_path):
        try:
            self.setWindowTitle(title)
            self.textBrowser_tips.setText(contents)
        except BaseException as e:
            logger.error(str(e))

    def get_ports(self):
        self.ports = ThSerialPortUtility.list_ports()
        self.comboBox_com.clear()
        for item in self.ports:
            self.comboBox_com.addItem(item)


class TestFramedPacket(serial.threaded.FramedPacket):
    def __init__(self):
        super(TestFramedPacket, self).__init__()
        self.received_packets = []

    def handle_packet(self, packet):
        self.received_packets.clear()
        self.received_packets.append(packet)

    def send_packet(self, packet):
        self.transport.write(packet)