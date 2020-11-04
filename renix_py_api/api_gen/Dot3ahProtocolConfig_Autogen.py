"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class Dot3ahProtocolConfig(L23ProtocolConfig):
    def __init__(self, MaxPduSize=None, TransmitType=None, LoopBackRespTime=None, EnableLinkFault=None, EnableDyingGasp=None, EnableCriticalEvent=None, EnableLoopBackResp=None, EnableVarResp=None, VarReqPeriod=None, **kwargs):
        self._State = EnumDot3ahLocalState.DISABLED  # State, not editable
        self._MaxPduSize = MaxPduSize  # Max PDU Size
        self._TransmitType = TransmitType  # Transmit Type
        self._LoopBackRespTime = LoopBackRespTime  # Loopback Response Time (sec)
        self._EnableLinkFault = EnableLinkFault  # Enable Link Fault
        self._EnableDyingGasp = EnableDyingGasp  # Enable Dying Gasp
        self._EnableCriticalEvent = EnableCriticalEvent  # Enable Critical Event
        self._EnableLoopBackResp = EnableLoopBackResp  # Enable Loopback Response
        self._EnableVarResp = EnableVarResp  # Enable Variable Response
        self._VarReqPeriod = VarReqPeriod  # Variable Request Period (sec)

        properties = kwargs.copy()
        if MaxPduSize is not None:
            properties['MaxPduSize'] = MaxPduSize
        if TransmitType is not None:
            properties['TransmitType'] = TransmitType
        if LoopBackRespTime is not None:
            properties['LoopBackRespTime'] = LoopBackRespTime
        if EnableLinkFault is not None:
            properties['EnableLinkFault'] = EnableLinkFault
        if EnableDyingGasp is not None:
            properties['EnableDyingGasp'] = EnableDyingGasp
        if EnableCriticalEvent is not None:
            properties['EnableCriticalEvent'] = EnableCriticalEvent
        if EnableLoopBackResp is not None:
            properties['EnableLoopBackResp'] = EnableLoopBackResp
        if EnableVarResp is not None:
            properties['EnableVarResp'] = EnableVarResp
        if VarReqPeriod is not None:
            properties['VarReqPeriod'] = VarReqPeriod

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MaxPduSize=None, TransmitType=None, LoopBackRespTime=None, EnableLinkFault=None, EnableDyingGasp=None, EnableCriticalEvent=None, EnableLoopBackResp=None, EnableVarResp=None, VarReqPeriod=None, **kwargs):
        properties = kwargs.copy()
        if MaxPduSize is not None:
            self._MaxPduSize = MaxPduSize
            properties['MaxPduSize'] = MaxPduSize
        if TransmitType is not None:
            self._TransmitType = TransmitType
            properties['TransmitType'] = TransmitType
        if LoopBackRespTime is not None:
            self._LoopBackRespTime = LoopBackRespTime
            properties['LoopBackRespTime'] = LoopBackRespTime
        if EnableLinkFault is not None:
            self._EnableLinkFault = EnableLinkFault
            properties['EnableLinkFault'] = EnableLinkFault
        if EnableDyingGasp is not None:
            self._EnableDyingGasp = EnableDyingGasp
            properties['EnableDyingGasp'] = EnableDyingGasp
        if EnableCriticalEvent is not None:
            self._EnableCriticalEvent = EnableCriticalEvent
            properties['EnableCriticalEvent'] = EnableCriticalEvent
        if EnableLoopBackResp is not None:
            self._EnableLoopBackResp = EnableLoopBackResp
            properties['EnableLoopBackResp'] = EnableLoopBackResp
        if EnableVarResp is not None:
            self._EnableVarResp = EnableVarResp
            properties['EnableVarResp'] = EnableVarResp
        if VarReqPeriod is not None:
            self._VarReqPeriod = VarReqPeriod
            properties['VarReqPeriod'] = VarReqPeriod

        super(Dot3ahProtocolConfig, self).edit(**properties)

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def MaxPduSize(self):
        """
        get the value of property _MaxPduSize
        """
        if self.force_auto_sync:
            self.get('MaxPduSize')
        return self._MaxPduSize

    @property
    def TransmitType(self):
        """
        get the value of property _TransmitType
        """
        if self.force_auto_sync:
            self.get('TransmitType')
        return self._TransmitType

    @property
    def LoopBackRespTime(self):
        """
        get the value of property _LoopBackRespTime
        """
        if self.force_auto_sync:
            self.get('LoopBackRespTime')
        return self._LoopBackRespTime

    @property
    def EnableLinkFault(self):
        """
        get the value of property _EnableLinkFault
        """
        if self.force_auto_sync:
            self.get('EnableLinkFault')
        return self._EnableLinkFault

    @property
    def EnableDyingGasp(self):
        """
        get the value of property _EnableDyingGasp
        """
        if self.force_auto_sync:
            self.get('EnableDyingGasp')
        return self._EnableDyingGasp

    @property
    def EnableCriticalEvent(self):
        """
        get the value of property _EnableCriticalEvent
        """
        if self.force_auto_sync:
            self.get('EnableCriticalEvent')
        return self._EnableCriticalEvent

    @property
    def EnableLoopBackResp(self):
        """
        get the value of property _EnableLoopBackResp
        """
        if self.force_auto_sync:
            self.get('EnableLoopBackResp')
        return self._EnableLoopBackResp

    @property
    def EnableVarResp(self):
        """
        get the value of property _EnableVarResp
        """
        if self.force_auto_sync:
            self.get('EnableVarResp')
        return self._EnableVarResp

    @property
    def VarReqPeriod(self):
        """
        get the value of property _VarReqPeriod
        """
        if self.force_auto_sync:
            self.get('VarReqPeriod')
        return self._VarReqPeriod

    @MaxPduSize.setter
    def MaxPduSize(self, value):
        self._MaxPduSize = value
        self.edit(MaxPduSize=value)

    @TransmitType.setter
    def TransmitType(self, value):
        self._TransmitType = value
        self.edit(TransmitType=value)

    @LoopBackRespTime.setter
    def LoopBackRespTime(self, value):
        self._LoopBackRespTime = value
        self.edit(LoopBackRespTime=value)

    @EnableLinkFault.setter
    def EnableLinkFault(self, value):
        self._EnableLinkFault = value
        self.edit(EnableLinkFault=value)

    @EnableDyingGasp.setter
    def EnableDyingGasp(self, value):
        self._EnableDyingGasp = value
        self.edit(EnableDyingGasp=value)

    @EnableCriticalEvent.setter
    def EnableCriticalEvent(self, value):
        self._EnableCriticalEvent = value
        self.edit(EnableCriticalEvent=value)

    @EnableLoopBackResp.setter
    def EnableLoopBackResp(self, value):
        self._EnableLoopBackResp = value
        self.edit(EnableLoopBackResp=value)

    @EnableVarResp.setter
    def EnableVarResp(self, value):
        self._EnableVarResp = value
        self.edit(EnableVarResp=value)

    @VarReqPeriod.setter
    def VarReqPeriod(self, value):
        self._VarReqPeriod = value
        self.edit(VarReqPeriod=value)

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumDot3ahLocalState.%s' % value[:seperate])

    def _set_maxpdusize_with_str(self, value):
        try:
            self._MaxPduSize = int(value)
        except ValueError:
            self._MaxPduSize = hex(int(value, 16))

    def _set_transmittype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransmitType = EnumTransmitType.%s' % value[:seperate])

    def _set_loopbackresptime_with_str(self, value):
        try:
            self._LoopBackRespTime = int(value)
        except ValueError:
            self._LoopBackRespTime = hex(int(value, 16))

    def _set_enablelinkfault_with_str(self, value):
        self._EnableLinkFault = (value == 'True')

    def _set_enabledyinggasp_with_str(self, value):
        self._EnableDyingGasp = (value == 'True')

    def _set_enablecriticalevent_with_str(self, value):
        self._EnableCriticalEvent = (value == 'True')

    def _set_enableloopbackresp_with_str(self, value):
        self._EnableLoopBackResp = (value == 'True')

    def _set_enablevarresp_with_str(self, value):
        self._EnableVarResp = (value == 'True')

    def _set_varreqperiod_with_str(self, value):
        try:
            self._VarReqPeriod = int(value)
        except ValueError:
            self._VarReqPeriod = hex(int(value, 16))

