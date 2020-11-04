"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class StreamTxStats(Result):
    def __init__(self, **kwargs):
        self._StreamBlockID = ''  # Stream Block, not editable
        self._StreamID = 0  # Stream ID, not editable
        self._PortID = ''  # Tx Port Name, not editable
        self._TxStreamFrames = 0  # Tx Stream Frames, not editable
        self._TxFrameRate = 0  # Tx Frame Rate (fps), not editable
        self._TxByteRate = 0  # Tx Byte Rate, not editable
        self._TxBitRate = 0  # Tx Bit Rate (bps), not editable
        self._TxL1Rate = 0  # Tx L1 Rate (bps), not editable
        self._TxUtil = 0  # Tx Utilization (%), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(StreamTxStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def StreamBlockID(self):
        """
        get the value of property _StreamBlockID
        """
        if self.force_auto_sync:
            self.get('StreamBlockID')
        return self._StreamBlockID

    @property
    def StreamID(self):
        """
        get the value of property _StreamID
        """
        if self.force_auto_sync:
            self.get('StreamID')
        return self._StreamID

    @property
    def PortID(self):
        """
        get the value of property _PortID
        """
        if self.force_auto_sync:
            self.get('PortID')
        return self._PortID

    @property
    def TxStreamFrames(self):
        """
        get the value of property _TxStreamFrames
        """
        if self.force_auto_sync:
            self.get('TxStreamFrames')
        return self._TxStreamFrames

    @property
    def TxFrameRate(self):
        """
        get the value of property _TxFrameRate
        """
        if self.force_auto_sync:
            self.get('TxFrameRate')
        return self._TxFrameRate

    @property
    def TxByteRate(self):
        """
        get the value of property _TxByteRate
        """
        if self.force_auto_sync:
            self.get('TxByteRate')
        return self._TxByteRate

    @property
    def TxBitRate(self):
        """
        get the value of property _TxBitRate
        """
        if self.force_auto_sync:
            self.get('TxBitRate')
        return self._TxBitRate

    @property
    def TxL1Rate(self):
        """
        get the value of property _TxL1Rate
        """
        if self.force_auto_sync:
            self.get('TxL1Rate')
        return self._TxL1Rate

    @property
    def TxUtil(self):
        """
        get the value of property _TxUtil
        """
        if self.force_auto_sync:
            self.get('TxUtil')
        return self._TxUtil

    def _set_streamblockid_with_str(self, value):
        self._StreamBlockID = value

    def _set_streamid_with_str(self, value):
        try:
            self._StreamID = int(value)
        except ValueError:
            self._StreamID = hex(int(value, 16))

    def _set_portid_with_str(self, value):
        self._PortID = value

    def _set_txstreamframes_with_str(self, value):
        try:
            self._TxStreamFrames = int(value)
        except ValueError:
            self._TxStreamFrames = hex(int(value, 16))

    def _set_txframerate_with_str(self, value):
        try:
            self._TxFrameRate = int(value)
        except ValueError:
            self._TxFrameRate = hex(int(value, 16))

    def _set_txbyterate_with_str(self, value):
        try:
            self._TxByteRate = int(value)
        except ValueError:
            self._TxByteRate = hex(int(value, 16))

    def _set_txbitrate_with_str(self, value):
        self._TxBitRate = float(value)

    def _set_txl1rate_with_str(self, value):
        self._TxL1Rate = float(value)

    def _set_txutil_with_str(self, value):
        self._TxUtil = float(value)

