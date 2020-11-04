"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class StreamPortConfig(ROMObject):
    def __init__(self, TransmitMode=None, GenerateError=None, LoadProfileType=None, IgnoreLinkState=None, TimeStampPosTx=None, TimeStampPosRx=None, LatencyCompensationTx=None, LatencyCompensationRx=None, **kwargs):
        self._TransmitMode = TransmitMode  # Transmit Mode
        self._GenerateError = GenerateError  # Error Generation
        self._LoadProfileType = LoadProfileType  # Load Profile Type
        self._IgnoreLinkState = IgnoreLinkState  # Ignore Link State
        self._TimeStampPosTx = TimeStampPosTx  # Time Stamp Position Tx
        self._TimeStampPosRx = TimeStampPosRx  # Time Stamp Position Rx
        self._LatencyCompensationTx = LatencyCompensationTx  # Latency Compensation Tx
        self._LatencyCompensationRx = LatencyCompensationRx  # Latency Compensation Rx

        properties = kwargs.copy()
        if TransmitMode is not None:
            properties['TransmitMode'] = TransmitMode
        if GenerateError is not None:
            properties['GenerateError'] = GenerateError
        if LoadProfileType is not None:
            properties['LoadProfileType'] = LoadProfileType
        if IgnoreLinkState is not None:
            properties['IgnoreLinkState'] = IgnoreLinkState
        if TimeStampPosTx is not None:
            properties['TimeStampPosTx'] = TimeStampPosTx
        if TimeStampPosRx is not None:
            properties['TimeStampPosRx'] = TimeStampPosRx
        if LatencyCompensationTx is not None:
            properties['LatencyCompensationTx'] = LatencyCompensationTx
        if LatencyCompensationRx is not None:
            properties['LatencyCompensationRx'] = LatencyCompensationRx

        # call base class function, and it will send message to renix server to create a class.
        super(StreamPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TransmitMode=None, GenerateError=None, LoadProfileType=None, IgnoreLinkState=None, TimeStampPosTx=None, TimeStampPosRx=None, LatencyCompensationTx=None, LatencyCompensationRx=None, **kwargs):
        properties = kwargs.copy()
        if TransmitMode is not None:
            self._TransmitMode = TransmitMode
            properties['TransmitMode'] = TransmitMode
        if GenerateError is not None:
            self._GenerateError = GenerateError
            properties['GenerateError'] = GenerateError
        if LoadProfileType is not None:
            self._LoadProfileType = LoadProfileType
            properties['LoadProfileType'] = LoadProfileType
        if IgnoreLinkState is not None:
            self._IgnoreLinkState = IgnoreLinkState
            properties['IgnoreLinkState'] = IgnoreLinkState
        if TimeStampPosTx is not None:
            self._TimeStampPosTx = TimeStampPosTx
            properties['TimeStampPosTx'] = TimeStampPosTx
        if TimeStampPosRx is not None:
            self._TimeStampPosRx = TimeStampPosRx
            properties['TimeStampPosRx'] = TimeStampPosRx
        if LatencyCompensationTx is not None:
            self._LatencyCompensationTx = LatencyCompensationTx
            properties['LatencyCompensationTx'] = LatencyCompensationTx
        if LatencyCompensationRx is not None:
            self._LatencyCompensationRx = LatencyCompensationRx
            properties['LatencyCompensationRx'] = LatencyCompensationRx

        super(StreamPortConfig, self).edit(**properties)

    @property
    def TransmitMode(self):
        """
        get the value of property _TransmitMode
        """
        if self.force_auto_sync:
            self.get('TransmitMode')
        return self._TransmitMode

    @property
    def GenerateError(self):
        """
        get the value of property _GenerateError
        """
        if self.force_auto_sync:
            self.get('GenerateError')
        return self._GenerateError

    @property
    def LoadProfileType(self):
        """
        get the value of property _LoadProfileType
        """
        if self.force_auto_sync:
            self.get('LoadProfileType')
        return self._LoadProfileType

    @property
    def IgnoreLinkState(self):
        """
        get the value of property _IgnoreLinkState
        """
        if self.force_auto_sync:
            self.get('IgnoreLinkState')
        return self._IgnoreLinkState

    @property
    def TimeStampPosTx(self):
        """
        get the value of property _TimeStampPosTx
        """
        if self.force_auto_sync:
            self.get('TimeStampPosTx')
        return self._TimeStampPosTx

    @property
    def TimeStampPosRx(self):
        """
        get the value of property _TimeStampPosRx
        """
        if self.force_auto_sync:
            self.get('TimeStampPosRx')
        return self._TimeStampPosRx

    @property
    def LatencyCompensationTx(self):
        """
        get the value of property _LatencyCompensationTx
        """
        if self.force_auto_sync:
            self.get('LatencyCompensationTx')
        return self._LatencyCompensationTx

    @property
    def LatencyCompensationRx(self):
        """
        get the value of property _LatencyCompensationRx
        """
        if self.force_auto_sync:
            self.get('LatencyCompensationRx')
        return self._LatencyCompensationRx

    @TransmitMode.setter
    def TransmitMode(self, value):
        self._TransmitMode = value
        self.edit(TransmitMode=value)

    @GenerateError.setter
    def GenerateError(self, value):
        self._GenerateError = value
        self.edit(GenerateError=value)

    @LoadProfileType.setter
    def LoadProfileType(self, value):
        self._LoadProfileType = value
        self.edit(LoadProfileType=value)

    @IgnoreLinkState.setter
    def IgnoreLinkState(self, value):
        self._IgnoreLinkState = value
        self.edit(IgnoreLinkState=value)

    @TimeStampPosTx.setter
    def TimeStampPosTx(self, value):
        self._TimeStampPosTx = value
        self.edit(TimeStampPosTx=value)

    @TimeStampPosRx.setter
    def TimeStampPosRx(self, value):
        self._TimeStampPosRx = value
        self.edit(TimeStampPosRx=value)

    @LatencyCompensationTx.setter
    def LatencyCompensationTx(self, value):
        self._LatencyCompensationTx = value
        self.edit(LatencyCompensationTx=value)

    @LatencyCompensationRx.setter
    def LatencyCompensationRx(self, value):
        self._LatencyCompensationRx = value
        self.edit(LatencyCompensationRx=value)

    def _set_transmitmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransmitMode = EnumTransmitMode.%s' % value[:seperate])

    def _set_generateerror_with_str(self, value):
        seperate = value.find(':')
        exec('self._GenerateError = EnumErrorGen.%s' % value[:seperate])

    def _set_loadprofiletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LoadProfileType = EnumLoadProfileType.%s' % value[:seperate])

    def _set_ignorelinkstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._IgnoreLinkState = EnumIgnoreLinkState.%s' % value[:seperate])

    def _set_timestamppostx_with_str(self, value):
        seperate = value.find(':')
        exec('self._TimeStampPosTx = EnumTimeStampPos.%s' % value[:seperate])

    def _set_timestampposrx_with_str(self, value):
        seperate = value.find(':')
        exec('self._TimeStampPosRx = EnumTimeStampPos.%s' % value[:seperate])

    def _set_latencycompensationtx_with_str(self, value):
        try:
            self._LatencyCompensationTx = int(value)
        except ValueError:
            self._LatencyCompensationTx = hex(int(value, 16))

    def _set_latencycompensationrx_with_str(self, value):
        try:
            self._LatencyCompensationRx = int(value)
        except ValueError:
            self._LatencyCompensationRx = hex(int(value, 16))

