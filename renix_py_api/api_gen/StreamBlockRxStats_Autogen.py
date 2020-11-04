"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class StreamBlockRxStats(Result):
    def __init__(self, **kwargs):
        self._StreamBlockID = ''  # Stream Block, not editable
        self._PortID = ''  # Rx Port Name, not editable
        self._RxStreamFrames = 0  # Rx Stream Frames, not editable
        self._RxFrameRate = 0  # Rx Frame Rate (fps), not editable
        self._RxByteRate = 0  # Rx Byte Rate, not editable
        self._RxSeqErr = 0  # Rx Sequence Error, not editable
        self._RxPayloadErr = 0  # Rx Payload Error, not editable
        self._MinLatency = 0  # Min Latency (us), not editable
        self._AvaLatency = 0  # Avg Latency (us), not editable
        self._MaxLatency = 0  # Max Latency (us), not editable
        self._RxBitRate = 0  # Rx Bit Rate (bps), not editable
        self._RxUtil = 0  # Rx Utilization (%), not editable
        self._MinJitter = 0  # Min Jitter (us), not editable
        self._AvaJitter = 0  # Avg Jitter (us), not editable
        self._MaxJitter = 0  # Max Jitter (us), not editable
        self._RxLossStreamFrames = 0  # Realtime Lost Frames, not editable
        self._RxL1Rate = 0  # Rx L1 Rate (bps), not editable
        self._RxAvgRate = 0  # Rx Avg Rate (bps), not editable
        self._RxAvgFps = 0  # Rx Avg Fps, not editable
        self._RxMaxRate = 0  # Rx Max Rate (bps), not editable
        self._RxMaxFps = 0  # Rx Max Fps, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(StreamBlockRxStats, self).__init__(**properties)

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
    def PortID(self):
        """
        get the value of property _PortID
        """
        if self.force_auto_sync:
            self.get('PortID')
        return self._PortID

    @property
    def RxStreamFrames(self):
        """
        get the value of property _RxStreamFrames
        """
        if self.force_auto_sync:
            self.get('RxStreamFrames')
        return self._RxStreamFrames

    @property
    def RxFrameRate(self):
        """
        get the value of property _RxFrameRate
        """
        if self.force_auto_sync:
            self.get('RxFrameRate')
        return self._RxFrameRate

    @property
    def RxByteRate(self):
        """
        get the value of property _RxByteRate
        """
        if self.force_auto_sync:
            self.get('RxByteRate')
        return self._RxByteRate

    @property
    def RxSeqErr(self):
        """
        get the value of property _RxSeqErr
        """
        if self.force_auto_sync:
            self.get('RxSeqErr')
        return self._RxSeqErr

    @property
    def RxPayloadErr(self):
        """
        get the value of property _RxPayloadErr
        """
        if self.force_auto_sync:
            self.get('RxPayloadErr')
        return self._RxPayloadErr

    @property
    def MinLatency(self):
        """
        get the value of property _MinLatency
        """
        if self.force_auto_sync:
            self.get('MinLatency')
        return self._MinLatency

    @property
    def AvaLatency(self):
        """
        get the value of property _AvaLatency
        """
        if self.force_auto_sync:
            self.get('AvaLatency')
        return self._AvaLatency

    @property
    def MaxLatency(self):
        """
        get the value of property _MaxLatency
        """
        if self.force_auto_sync:
            self.get('MaxLatency')
        return self._MaxLatency

    @property
    def RxBitRate(self):
        """
        get the value of property _RxBitRate
        """
        if self.force_auto_sync:
            self.get('RxBitRate')
        return self._RxBitRate

    @property
    def RxUtil(self):
        """
        get the value of property _RxUtil
        """
        if self.force_auto_sync:
            self.get('RxUtil')
        return self._RxUtil

    @property
    def MinJitter(self):
        """
        get the value of property _MinJitter
        """
        if self.force_auto_sync:
            self.get('MinJitter')
        return self._MinJitter

    @property
    def AvaJitter(self):
        """
        get the value of property _AvaJitter
        """
        if self.force_auto_sync:
            self.get('AvaJitter')
        return self._AvaJitter

    @property
    def MaxJitter(self):
        """
        get the value of property _MaxJitter
        """
        if self.force_auto_sync:
            self.get('MaxJitter')
        return self._MaxJitter

    @property
    def RxLossStreamFrames(self):
        """
        get the value of property _RxLossStreamFrames
        """
        if self.force_auto_sync:
            self.get('RxLossStreamFrames')
        return self._RxLossStreamFrames

    @property
    def RxL1Rate(self):
        """
        get the value of property _RxL1Rate
        """
        if self.force_auto_sync:
            self.get('RxL1Rate')
        return self._RxL1Rate

    @property
    def RxAvgRate(self):
        """
        get the value of property _RxAvgRate
        """
        if self.force_auto_sync:
            self.get('RxAvgRate')
        return self._RxAvgRate

    @property
    def RxAvgFps(self):
        """
        get the value of property _RxAvgFps
        """
        if self.force_auto_sync:
            self.get('RxAvgFps')
        return self._RxAvgFps

    @property
    def RxMaxRate(self):
        """
        get the value of property _RxMaxRate
        """
        if self.force_auto_sync:
            self.get('RxMaxRate')
        return self._RxMaxRate

    @property
    def RxMaxFps(self):
        """
        get the value of property _RxMaxFps
        """
        if self.force_auto_sync:
            self.get('RxMaxFps')
        return self._RxMaxFps

    def _set_streamblockid_with_str(self, value):
        self._StreamBlockID = value

    def _set_portid_with_str(self, value):
        self._PortID = value

    def _set_rxstreamframes_with_str(self, value):
        try:
            self._RxStreamFrames = int(value)
        except ValueError:
            self._RxStreamFrames = hex(int(value, 16))

    def _set_rxframerate_with_str(self, value):
        try:
            self._RxFrameRate = int(value)
        except ValueError:
            self._RxFrameRate = hex(int(value, 16))

    def _set_rxbyterate_with_str(self, value):
        try:
            self._RxByteRate = int(value)
        except ValueError:
            self._RxByteRate = hex(int(value, 16))

    def _set_rxseqerr_with_str(self, value):
        try:
            self._RxSeqErr = int(value)
        except ValueError:
            self._RxSeqErr = hex(int(value, 16))

    def _set_rxpayloaderr_with_str(self, value):
        try:
            self._RxPayloadErr = int(value)
        except ValueError:
            self._RxPayloadErr = hex(int(value, 16))

    def _set_minlatency_with_str(self, value):
        self._MinLatency = float(value)

    def _set_avalatency_with_str(self, value):
        self._AvaLatency = float(value)

    def _set_maxlatency_with_str(self, value):
        self._MaxLatency = float(value)

    def _set_rxbitrate_with_str(self, value):
        self._RxBitRate = float(value)

    def _set_rxutil_with_str(self, value):
        self._RxUtil = float(value)

    def _set_minjitter_with_str(self, value):
        self._MinJitter = float(value)

    def _set_avajitter_with_str(self, value):
        self._AvaJitter = float(value)

    def _set_maxjitter_with_str(self, value):
        self._MaxJitter = float(value)

    def _set_rxlossstreamframes_with_str(self, value):
        try:
            self._RxLossStreamFrames = int(value)
        except ValueError:
            self._RxLossStreamFrames = hex(int(value, 16))

    def _set_rxl1rate_with_str(self, value):
        self._RxL1Rate = float(value)

    def _set_rxavgrate_with_str(self, value):
        self._RxAvgRate = float(value)

    def _set_rxavgfps_with_str(self, value):
        try:
            self._RxAvgFps = int(value)
        except ValueError:
            self._RxAvgFps = hex(int(value, 16))

    def _set_rxmaxrate_with_str(self, value):
        self._RxMaxRate = float(value)

    def _set_rxmaxfps_with_str(self, value):
        try:
            self._RxMaxFps = int(value)
        except ValueError:
            self._RxMaxFps = hex(int(value, 16))

