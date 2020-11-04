"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class CaptureConfig(ROMObject):
    def __init__(self, CaptureMode=None, CacheCapacity=None, FilterMode=None, BufferFullAction=None, StartingFrameIndex=None, AttemptDownloadPacketCount=None, FcsError=None, Ipv4ChecksumError=None, PayloadError=None, EnableRealtimeCapture=None, MaxRealtimeCaptureFrameCount=None, **kwargs):
        self._CaptureState = EnumCaptureState.DISABLED  # Capture State, not editable
        self._CaptureMode = CaptureMode  # Capture Mode
        self._CacheCapacity = CacheCapacity  # Cache Capacity
        self._FilterMode = FilterMode  # Filter Mode
        self._BufferFullAction = BufferFullAction  # Buffer Full Action
        self._ElapsedTime = '00:00:00'  # Capture Elapsed Time, not editable
        self._CapturedPacketCount = 0  # Captured Packet Count, not editable
        self._BufferFull = EnumBuffFullState.NOT_FULL  # Buffer Full, not editable
        self._DownloadedPacketCount = 0  # Downloaded Packet Count, not editable
        self._CurrentDataFile = ''  # Current Capture File Path, not editable
        self._StartingFrameIndex = StartingFrameIndex  # Download Starting Frame Index
        self._AttemptDownloadPacketCount = AttemptDownloadPacketCount  # Stop Download Packet After
        self._FcsError = FcsError  # FCS Error
        self._Ipv4ChecksumError = Ipv4ChecksumError  # IPv4 Checksum Error
        self._PayloadError = PayloadError  # Payload Error
        self._EnableRealtimeCapture = EnableRealtimeCapture  # Enable Real-time Capture
        self._MaxRealtimeCaptureFrameCount = MaxRealtimeCaptureFrameCount  # Max Real-time Capture Frame Count

        properties = kwargs.copy()
        if CaptureMode is not None:
            properties['CaptureMode'] = CaptureMode
        if CacheCapacity is not None:
            properties['CacheCapacity'] = CacheCapacity
        if FilterMode is not None:
            properties['FilterMode'] = FilterMode
        if BufferFullAction is not None:
            properties['BufferFullAction'] = BufferFullAction
        if StartingFrameIndex is not None:
            properties['StartingFrameIndex'] = StartingFrameIndex
        if AttemptDownloadPacketCount is not None:
            properties['AttemptDownloadPacketCount'] = AttemptDownloadPacketCount
        if FcsError is not None:
            properties['FcsError'] = FcsError
        if Ipv4ChecksumError is not None:
            properties['Ipv4ChecksumError'] = Ipv4ChecksumError
        if PayloadError is not None:
            properties['PayloadError'] = PayloadError
        if EnableRealtimeCapture is not None:
            properties['EnableRealtimeCapture'] = EnableRealtimeCapture
        if MaxRealtimeCaptureFrameCount is not None:
            properties['MaxRealtimeCaptureFrameCount'] = MaxRealtimeCaptureFrameCount

        # call base class function, and it will send message to renix server to create a class.
        super(CaptureConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CaptureMode=None, CacheCapacity=None, FilterMode=None, BufferFullAction=None, StartingFrameIndex=None, AttemptDownloadPacketCount=None, FcsError=None, Ipv4ChecksumError=None, PayloadError=None, EnableRealtimeCapture=None, MaxRealtimeCaptureFrameCount=None, **kwargs):
        properties = kwargs.copy()
        if CaptureMode is not None:
            self._CaptureMode = CaptureMode
            properties['CaptureMode'] = CaptureMode
        if CacheCapacity is not None:
            self._CacheCapacity = CacheCapacity
            properties['CacheCapacity'] = CacheCapacity
        if FilterMode is not None:
            self._FilterMode = FilterMode
            properties['FilterMode'] = FilterMode
        if BufferFullAction is not None:
            self._BufferFullAction = BufferFullAction
            properties['BufferFullAction'] = BufferFullAction
        if StartingFrameIndex is not None:
            self._StartingFrameIndex = StartingFrameIndex
            properties['StartingFrameIndex'] = StartingFrameIndex
        if AttemptDownloadPacketCount is not None:
            self._AttemptDownloadPacketCount = AttemptDownloadPacketCount
            properties['AttemptDownloadPacketCount'] = AttemptDownloadPacketCount
        if FcsError is not None:
            self._FcsError = FcsError
            properties['FcsError'] = FcsError
        if Ipv4ChecksumError is not None:
            self._Ipv4ChecksumError = Ipv4ChecksumError
            properties['Ipv4ChecksumError'] = Ipv4ChecksumError
        if PayloadError is not None:
            self._PayloadError = PayloadError
            properties['PayloadError'] = PayloadError
        if EnableRealtimeCapture is not None:
            self._EnableRealtimeCapture = EnableRealtimeCapture
            properties['EnableRealtimeCapture'] = EnableRealtimeCapture
        if MaxRealtimeCaptureFrameCount is not None:
            self._MaxRealtimeCaptureFrameCount = MaxRealtimeCaptureFrameCount
            properties['MaxRealtimeCaptureFrameCount'] = MaxRealtimeCaptureFrameCount

        super(CaptureConfig, self).edit(**properties)

    @property
    def CaptureState(self):
        """
        get the value of property _CaptureState
        """
        if self.force_auto_sync:
            self.get('CaptureState')
        return self._CaptureState

    @property
    def CaptureMode(self):
        """
        get the value of property _CaptureMode
        """
        if self.force_auto_sync:
            self.get('CaptureMode')
        return self._CaptureMode

    @property
    def CacheCapacity(self):
        """
        get the value of property _CacheCapacity
        """
        if self.force_auto_sync:
            self.get('CacheCapacity')
        return self._CacheCapacity

    @property
    def FilterMode(self):
        """
        get the value of property _FilterMode
        """
        if self.force_auto_sync:
            self.get('FilterMode')
        return self._FilterMode

    @property
    def BufferFullAction(self):
        """
        get the value of property _BufferFullAction
        """
        if self.force_auto_sync:
            self.get('BufferFullAction')
        return self._BufferFullAction

    @property
    def ElapsedTime(self):
        """
        get the value of property _ElapsedTime
        """
        if self.force_auto_sync:
            self.get('ElapsedTime')
        return self._ElapsedTime

    @property
    def CapturedPacketCount(self):
        """
        get the value of property _CapturedPacketCount
        """
        if self.force_auto_sync:
            self.get('CapturedPacketCount')
        return self._CapturedPacketCount

    @property
    def BufferFull(self):
        """
        get the value of property _BufferFull
        """
        if self.force_auto_sync:
            self.get('BufferFull')
        return self._BufferFull

    @property
    def DownloadedPacketCount(self):
        """
        get the value of property _DownloadedPacketCount
        """
        if self.force_auto_sync:
            self.get('DownloadedPacketCount')
        return self._DownloadedPacketCount

    @property
    def CurrentDataFile(self):
        """
        get the value of property _CurrentDataFile
        """
        if self.force_auto_sync:
            self.get('CurrentDataFile')
        return self._CurrentDataFile

    @property
    def StartingFrameIndex(self):
        """
        get the value of property _StartingFrameIndex
        """
        if self.force_auto_sync:
            self.get('StartingFrameIndex')
        return self._StartingFrameIndex

    @property
    def AttemptDownloadPacketCount(self):
        """
        get the value of property _AttemptDownloadPacketCount
        """
        if self.force_auto_sync:
            self.get('AttemptDownloadPacketCount')
        return self._AttemptDownloadPacketCount

    @property
    def FcsError(self):
        """
        get the value of property _FcsError
        """
        if self.force_auto_sync:
            self.get('FcsError')
        return self._FcsError

    @property
    def Ipv4ChecksumError(self):
        """
        get the value of property _Ipv4ChecksumError
        """
        if self.force_auto_sync:
            self.get('Ipv4ChecksumError')
        return self._Ipv4ChecksumError

    @property
    def PayloadError(self):
        """
        get the value of property _PayloadError
        """
        if self.force_auto_sync:
            self.get('PayloadError')
        return self._PayloadError

    @property
    def EnableRealtimeCapture(self):
        """
        get the value of property _EnableRealtimeCapture
        """
        if self.force_auto_sync:
            self.get('EnableRealtimeCapture')
        return self._EnableRealtimeCapture

    @property
    def MaxRealtimeCaptureFrameCount(self):
        """
        get the value of property _MaxRealtimeCaptureFrameCount
        """
        if self.force_auto_sync:
            self.get('MaxRealtimeCaptureFrameCount')
        return self._MaxRealtimeCaptureFrameCount

    @CaptureMode.setter
    def CaptureMode(self, value):
        self._CaptureMode = value
        self.edit(CaptureMode=value)

    @CacheCapacity.setter
    def CacheCapacity(self, value):
        self._CacheCapacity = value
        self.edit(CacheCapacity=value)

    @FilterMode.setter
    def FilterMode(self, value):
        self._FilterMode = value
        self.edit(FilterMode=value)

    @BufferFullAction.setter
    def BufferFullAction(self, value):
        self._BufferFullAction = value
        self.edit(BufferFullAction=value)

    @StartingFrameIndex.setter
    def StartingFrameIndex(self, value):
        self._StartingFrameIndex = value
        self.edit(StartingFrameIndex=value)

    @AttemptDownloadPacketCount.setter
    def AttemptDownloadPacketCount(self, value):
        self._AttemptDownloadPacketCount = value
        self.edit(AttemptDownloadPacketCount=value)

    @FcsError.setter
    def FcsError(self, value):
        self._FcsError = value
        self.edit(FcsError=value)

    @Ipv4ChecksumError.setter
    def Ipv4ChecksumError(self, value):
        self._Ipv4ChecksumError = value
        self.edit(Ipv4ChecksumError=value)

    @PayloadError.setter
    def PayloadError(self, value):
        self._PayloadError = value
        self.edit(PayloadError=value)

    @EnableRealtimeCapture.setter
    def EnableRealtimeCapture(self, value):
        self._EnableRealtimeCapture = value
        self.edit(EnableRealtimeCapture=value)

    @MaxRealtimeCaptureFrameCount.setter
    def MaxRealtimeCaptureFrameCount(self, value):
        self._MaxRealtimeCaptureFrameCount = value
        self.edit(MaxRealtimeCaptureFrameCount=value)

    def _set_capturestate_with_str(self, value):
        seperate = value.find(':')
        exec('self._CaptureState = EnumCaptureState.%s' % value[:seperate])

    def _set_capturemode_with_str(self, value):
        seperate = value.find(':')
        exec('self._CaptureMode = EnumCaptureMode.%s' % value[:seperate])

    def _set_cachecapacity_with_str(self, value):
        seperate = value.find(':')
        exec('self._CacheCapacity = EnumCacheCapacity.%s' % value[:seperate])

    def _set_filtermode_with_str(self, value):
        seperate = value.find(':')
        exec('self._FilterMode = EnumFilterMode.%s' % value[:seperate])

    def _set_bufferfullaction_with_str(self, value):
        seperate = value.find(':')
        exec('self._BufferFullAction = EnumBufferFullAction.%s' % value[:seperate])

    def _set_elapsedtime_with_str(self, value):
        self._ElapsedTime = value

    def _set_capturedpacketcount_with_str(self, value):
        try:
            self._CapturedPacketCount = int(value)
        except ValueError:
            self._CapturedPacketCount = hex(int(value, 16))

    def _set_bufferfull_with_str(self, value):
        seperate = value.find(':')
        exec('self._BufferFull = EnumBuffFullState.%s' % value[:seperate])

    def _set_downloadedpacketcount_with_str(self, value):
        try:
            self._DownloadedPacketCount = int(value)
        except ValueError:
            self._DownloadedPacketCount = hex(int(value, 16))

    def _set_currentdatafile_with_str(self, value):
        self._CurrentDataFile = value

    def _set_startingframeindex_with_str(self, value):
        try:
            self._StartingFrameIndex = int(value)
        except ValueError:
            self._StartingFrameIndex = hex(int(value, 16))

    def _set_attemptdownloadpacketcount_with_str(self, value):
        try:
            self._AttemptDownloadPacketCount = int(value)
        except ValueError:
            self._AttemptDownloadPacketCount = hex(int(value, 16))

    def _set_fcserror_with_str(self, value):
        self._FcsError = (value == 'True')

    def _set_ipv4checksumerror_with_str(self, value):
        self._Ipv4ChecksumError = (value == 'True')

    def _set_payloaderror_with_str(self, value):
        self._PayloadError = (value == 'True')

    def _set_enablerealtimecapture_with_str(self, value):
        self._EnableRealtimeCapture = (value == 'True')

    def _set_maxrealtimecaptureframecount_with_str(self, value):
        try:
            self._MaxRealtimeCaptureFrameCount = int(value)
        except ValueError:
            self._MaxRealtimeCaptureFrameCount = hex(int(value, 16))

