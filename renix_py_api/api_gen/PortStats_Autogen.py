"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PortStats(Result):
    def __init__(self, **kwargs):
        self._PortID = ''  # Port Name, not editable
        self._TxSignatureStreamFrames = 0  # Tx Stream Frames, not editable
        self._RxSignatureStreamFrames = 0  # Rx Signature Stream Frames, not editable
        self._TxTotalFrames = 0  # Tx Total Frames, not editable
        self._RxTotalFrames = 0  # Rx Total Frames, not editable
        self._TxFrameRate = 0  # Tx Frame Rate (fps), not editable
        self._RxFrameRate = 0  # Rx Frame Rate (fps), not editable
        self._TxL1Rate = 0  # Tx L1 Rate (bps), not editable
        self._RxL1Rate = 0  # Rx L1 Rate (bps), not editable
        self._TxUtil = 0  # Tx Utilization (%), not editable
        self._RxUtil = 0  # Rx Utilization (%), not editable
        self._TxByteRate = 0  # Tx Byte Rate, not editable
        self._RxByteRate = 0  # Rx Byte Rate, not editable
        self._TxBitRate = 0  # Tx Bit Rate (bps), not editable
        self._RxBitRate = 0  # Rx Bit Rate (bps), not editable
        self._TxTotalBytes = 0  # Tx Total Bytes, not editable
        self._RxTotalBytes = 0  # Rx Total Bytes, not editable
        self._RxFilterFrames = 0  # Rx Filter Frames, not editable
        self._RxFilterRate = 0  # Rx Filter Rate, not editable
        self._RxFCSErr = 0  # Rx FCS Error, not editable
        self._RxIpv4ChecksumError = 0  # Rx IPv4 Checksum Error, not editable
        self._RxTcpChecksumError = 0  # Rx TCP Checksum Error, not editable
        self._RxUdpChecksumError = 0  # Rx UDP Checksum Error, not editable
        self._RxPauseFrames = 0  # Rx Pause Frames, not editable
        self._RxUnderSizeFrames = 0  # Rx Undersize Frames, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PortStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PortID(self):
        """
        get the value of property _PortID
        """
        if self.force_auto_sync:
            self.get('PortID')
        return self._PortID

    @property
    def TxSignatureStreamFrames(self):
        """
        get the value of property _TxSignatureStreamFrames
        """
        if self.force_auto_sync:
            self.get('TxSignatureStreamFrames')
        return self._TxSignatureStreamFrames

    @property
    def RxSignatureStreamFrames(self):
        """
        get the value of property _RxSignatureStreamFrames
        """
        if self.force_auto_sync:
            self.get('RxSignatureStreamFrames')
        return self._RxSignatureStreamFrames

    @property
    def TxTotalFrames(self):
        """
        get the value of property _TxTotalFrames
        """
        if self.force_auto_sync:
            self.get('TxTotalFrames')
        return self._TxTotalFrames

    @property
    def RxTotalFrames(self):
        """
        get the value of property _RxTotalFrames
        """
        if self.force_auto_sync:
            self.get('RxTotalFrames')
        return self._RxTotalFrames

    @property
    def TxFrameRate(self):
        """
        get the value of property _TxFrameRate
        """
        if self.force_auto_sync:
            self.get('TxFrameRate')
        return self._TxFrameRate

    @property
    def RxFrameRate(self):
        """
        get the value of property _RxFrameRate
        """
        if self.force_auto_sync:
            self.get('RxFrameRate')
        return self._RxFrameRate

    @property
    def TxL1Rate(self):
        """
        get the value of property _TxL1Rate
        """
        if self.force_auto_sync:
            self.get('TxL1Rate')
        return self._TxL1Rate

    @property
    def RxL1Rate(self):
        """
        get the value of property _RxL1Rate
        """
        if self.force_auto_sync:
            self.get('RxL1Rate')
        return self._RxL1Rate

    @property
    def TxUtil(self):
        """
        get the value of property _TxUtil
        """
        if self.force_auto_sync:
            self.get('TxUtil')
        return self._TxUtil

    @property
    def RxUtil(self):
        """
        get the value of property _RxUtil
        """
        if self.force_auto_sync:
            self.get('RxUtil')
        return self._RxUtil

    @property
    def TxByteRate(self):
        """
        get the value of property _TxByteRate
        """
        if self.force_auto_sync:
            self.get('TxByteRate')
        return self._TxByteRate

    @property
    def RxByteRate(self):
        """
        get the value of property _RxByteRate
        """
        if self.force_auto_sync:
            self.get('RxByteRate')
        return self._RxByteRate

    @property
    def TxBitRate(self):
        """
        get the value of property _TxBitRate
        """
        if self.force_auto_sync:
            self.get('TxBitRate')
        return self._TxBitRate

    @property
    def RxBitRate(self):
        """
        get the value of property _RxBitRate
        """
        if self.force_auto_sync:
            self.get('RxBitRate')
        return self._RxBitRate

    @property
    def TxTotalBytes(self):
        """
        get the value of property _TxTotalBytes
        """
        if self.force_auto_sync:
            self.get('TxTotalBytes')
        return self._TxTotalBytes

    @property
    def RxTotalBytes(self):
        """
        get the value of property _RxTotalBytes
        """
        if self.force_auto_sync:
            self.get('RxTotalBytes')
        return self._RxTotalBytes

    @property
    def RxFilterFrames(self):
        """
        get the value of property _RxFilterFrames
        """
        if self.force_auto_sync:
            self.get('RxFilterFrames')
        return self._RxFilterFrames

    @property
    def RxFilterRate(self):
        """
        get the value of property _RxFilterRate
        """
        if self.force_auto_sync:
            self.get('RxFilterRate')
        return self._RxFilterRate

    @property
    def RxFCSErr(self):
        """
        get the value of property _RxFCSErr
        """
        if self.force_auto_sync:
            self.get('RxFCSErr')
        return self._RxFCSErr

    @property
    def RxIpv4ChecksumError(self):
        """
        get the value of property _RxIpv4ChecksumError
        """
        if self.force_auto_sync:
            self.get('RxIpv4ChecksumError')
        return self._RxIpv4ChecksumError

    @property
    def RxTcpChecksumError(self):
        """
        get the value of property _RxTcpChecksumError
        """
        if self.force_auto_sync:
            self.get('RxTcpChecksumError')
        return self._RxTcpChecksumError

    @property
    def RxUdpChecksumError(self):
        """
        get the value of property _RxUdpChecksumError
        """
        if self.force_auto_sync:
            self.get('RxUdpChecksumError')
        return self._RxUdpChecksumError

    @property
    def RxPauseFrames(self):
        """
        get the value of property _RxPauseFrames
        """
        if self.force_auto_sync:
            self.get('RxPauseFrames')
        return self._RxPauseFrames

    @property
    def RxUnderSizeFrames(self):
        """
        get the value of property _RxUnderSizeFrames
        """
        if self.force_auto_sync:
            self.get('RxUnderSizeFrames')
        return self._RxUnderSizeFrames

    def _set_portid_with_str(self, value):
        self._PortID = value

    def _set_txsignaturestreamframes_with_str(self, value):
        try:
            self._TxSignatureStreamFrames = int(value)
        except ValueError:
            self._TxSignatureStreamFrames = hex(int(value, 16))

    def _set_rxsignaturestreamframes_with_str(self, value):
        try:
            self._RxSignatureStreamFrames = int(value)
        except ValueError:
            self._RxSignatureStreamFrames = hex(int(value, 16))

    def _set_txtotalframes_with_str(self, value):
        try:
            self._TxTotalFrames = int(value)
        except ValueError:
            self._TxTotalFrames = hex(int(value, 16))

    def _set_rxtotalframes_with_str(self, value):
        try:
            self._RxTotalFrames = int(value)
        except ValueError:
            self._RxTotalFrames = hex(int(value, 16))

    def _set_txframerate_with_str(self, value):
        try:
            self._TxFrameRate = int(value)
        except ValueError:
            self._TxFrameRate = hex(int(value, 16))

    def _set_rxframerate_with_str(self, value):
        try:
            self._RxFrameRate = int(value)
        except ValueError:
            self._RxFrameRate = hex(int(value, 16))

    def _set_txl1rate_with_str(self, value):
        self._TxL1Rate = float(value)

    def _set_rxl1rate_with_str(self, value):
        self._RxL1Rate = float(value)

    def _set_txutil_with_str(self, value):
        self._TxUtil = float(value)

    def _set_rxutil_with_str(self, value):
        self._RxUtil = float(value)

    def _set_txbyterate_with_str(self, value):
        try:
            self._TxByteRate = int(value)
        except ValueError:
            self._TxByteRate = hex(int(value, 16))

    def _set_rxbyterate_with_str(self, value):
        try:
            self._RxByteRate = int(value)
        except ValueError:
            self._RxByteRate = hex(int(value, 16))

    def _set_txbitrate_with_str(self, value):
        self._TxBitRate = float(value)

    def _set_rxbitrate_with_str(self, value):
        self._RxBitRate = float(value)

    def _set_txtotalbytes_with_str(self, value):
        try:
            self._TxTotalBytes = int(value)
        except ValueError:
            self._TxTotalBytes = hex(int(value, 16))

    def _set_rxtotalbytes_with_str(self, value):
        try:
            self._RxTotalBytes = int(value)
        except ValueError:
            self._RxTotalBytes = hex(int(value, 16))

    def _set_rxfilterframes_with_str(self, value):
        try:
            self._RxFilterFrames = int(value)
        except ValueError:
            self._RxFilterFrames = hex(int(value, 16))

    def _set_rxfilterrate_with_str(self, value):
        try:
            self._RxFilterRate = int(value)
        except ValueError:
            self._RxFilterRate = hex(int(value, 16))

    def _set_rxfcserr_with_str(self, value):
        try:
            self._RxFCSErr = int(value)
        except ValueError:
            self._RxFCSErr = hex(int(value, 16))

    def _set_rxipv4checksumerror_with_str(self, value):
        try:
            self._RxIpv4ChecksumError = int(value)
        except ValueError:
            self._RxIpv4ChecksumError = hex(int(value, 16))

    def _set_rxtcpchecksumerror_with_str(self, value):
        try:
            self._RxTcpChecksumError = int(value)
        except ValueError:
            self._RxTcpChecksumError = hex(int(value, 16))

    def _set_rxudpchecksumerror_with_str(self, value):
        try:
            self._RxUdpChecksumError = int(value)
        except ValueError:
            self._RxUdpChecksumError = hex(int(value, 16))

    def _set_rxpauseframes_with_str(self, value):
        try:
            self._RxPauseFrames = int(value)
        except ValueError:
            self._RxPauseFrames = hex(int(value, 16))

    def _set_rxundersizeframes_with_str(self, value):
        try:
            self._RxUnderSizeFrames = int(value)
        except ValueError:
            self._RxUnderSizeFrames = hex(int(value, 16))

