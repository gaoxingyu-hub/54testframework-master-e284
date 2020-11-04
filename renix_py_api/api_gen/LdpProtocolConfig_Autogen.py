"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .L23ProtocolConfig_Autogen import L23ProtocolConfig


@rom_manager.rom
class LdpProtocolConfig(L23ProtocolConfig):
    def __init__(self, RouterId=None, HelloType=None, TransportMode=None, EgressLabel=None, MinLabel=None, LabelSpaceId=None, HelloInterval=None, HelloHoldTime=None, KeepAliveInterval=None, KeepAliveHoldTime=None, **kwargs):
        self._RouterId = RouterId  # Router ID
        self._State = EnumLdpState.NOT_STARTED  # LDP State, not editable
        self._HelloType = HelloType  # Hello Type
        self._TransportMode = TransportMode  # Transport Mode
        self._EgressLabel = EgressLabel  # Egress Label
        self._MinLabel = MinLabel  # Min Label
        self._LabelSpaceId = LabelSpaceId  # Label Space ID
        self._HelloInterval = HelloInterval  # Hello Interval (sec)
        self._HelloHoldTime = HelloHoldTime  # Hello HoldTime (sec)
        self._KeepAliveInterval = KeepAliveInterval  # Keep Alive Interval (sec)
        self._KeepAliveHoldTime = KeepAliveHoldTime  # Keep Alive HoldTime (sec)

        properties = kwargs.copy()
        if RouterId is not None:
            properties['RouterId'] = RouterId
        if HelloType is not None:
            properties['HelloType'] = HelloType
        if TransportMode is not None:
            properties['TransportMode'] = TransportMode
        if EgressLabel is not None:
            properties['EgressLabel'] = EgressLabel
        if MinLabel is not None:
            properties['MinLabel'] = MinLabel
        if LabelSpaceId is not None:
            properties['LabelSpaceId'] = LabelSpaceId
        if HelloInterval is not None:
            properties['HelloInterval'] = HelloInterval
        if HelloHoldTime is not None:
            properties['HelloHoldTime'] = HelloHoldTime
        if KeepAliveInterval is not None:
            properties['KeepAliveInterval'] = KeepAliveInterval
        if KeepAliveHoldTime is not None:
            properties['KeepAliveHoldTime'] = KeepAliveHoldTime

        # call base class function, and it will send message to renix server to create a class.
        super(LdpProtocolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouterId=None, HelloType=None, TransportMode=None, EgressLabel=None, MinLabel=None, LabelSpaceId=None, HelloInterval=None, HelloHoldTime=None, KeepAliveInterval=None, KeepAliveHoldTime=None, **kwargs):
        properties = kwargs.copy()
        if RouterId is not None:
            self._RouterId = RouterId
            properties['RouterId'] = RouterId
        if HelloType is not None:
            self._HelloType = HelloType
            properties['HelloType'] = HelloType
        if TransportMode is not None:
            self._TransportMode = TransportMode
            properties['TransportMode'] = TransportMode
        if EgressLabel is not None:
            self._EgressLabel = EgressLabel
            properties['EgressLabel'] = EgressLabel
        if MinLabel is not None:
            self._MinLabel = MinLabel
            properties['MinLabel'] = MinLabel
        if LabelSpaceId is not None:
            self._LabelSpaceId = LabelSpaceId
            properties['LabelSpaceId'] = LabelSpaceId
        if HelloInterval is not None:
            self._HelloInterval = HelloInterval
            properties['HelloInterval'] = HelloInterval
        if HelloHoldTime is not None:
            self._HelloHoldTime = HelloHoldTime
            properties['HelloHoldTime'] = HelloHoldTime
        if KeepAliveInterval is not None:
            self._KeepAliveInterval = KeepAliveInterval
            properties['KeepAliveInterval'] = KeepAliveInterval
        if KeepAliveHoldTime is not None:
            self._KeepAliveHoldTime = KeepAliveHoldTime
            properties['KeepAliveHoldTime'] = KeepAliveHoldTime

        super(LdpProtocolConfig, self).edit(**properties)

    @property
    def RouterId(self):
        """
        get the value of property _RouterId
        """
        if self.force_auto_sync:
            self.get('RouterId')
        return self._RouterId

    @property
    def State(self):
        """
        get the value of property _State
        """
        if self.force_auto_sync:
            self.get('State')
        return self._State

    @property
    def HelloType(self):
        """
        get the value of property _HelloType
        """
        if self.force_auto_sync:
            self.get('HelloType')
        return self._HelloType

    @property
    def TransportMode(self):
        """
        get the value of property _TransportMode
        """
        if self.force_auto_sync:
            self.get('TransportMode')
        return self._TransportMode

    @property
    def EgressLabel(self):
        """
        get the value of property _EgressLabel
        """
        if self.force_auto_sync:
            self.get('EgressLabel')
        return self._EgressLabel

    @property
    def MinLabel(self):
        """
        get the value of property _MinLabel
        """
        if self.force_auto_sync:
            self.get('MinLabel')
        return self._MinLabel

    @property
    def LabelSpaceId(self):
        """
        get the value of property _LabelSpaceId
        """
        if self.force_auto_sync:
            self.get('LabelSpaceId')
        return self._LabelSpaceId

    @property
    def HelloInterval(self):
        """
        get the value of property _HelloInterval
        """
        if self.force_auto_sync:
            self.get('HelloInterval')
        return self._HelloInterval

    @property
    def HelloHoldTime(self):
        """
        get the value of property _HelloHoldTime
        """
        if self.force_auto_sync:
            self.get('HelloHoldTime')
        return self._HelloHoldTime

    @property
    def KeepAliveInterval(self):
        """
        get the value of property _KeepAliveInterval
        """
        if self.force_auto_sync:
            self.get('KeepAliveInterval')
        return self._KeepAliveInterval

    @property
    def KeepAliveHoldTime(self):
        """
        get the value of property _KeepAliveHoldTime
        """
        if self.force_auto_sync:
            self.get('KeepAliveHoldTime')
        return self._KeepAliveHoldTime

    @RouterId.setter
    def RouterId(self, value):
        self._RouterId = value
        self.edit(RouterId=value)

    @HelloType.setter
    def HelloType(self, value):
        self._HelloType = value
        self.edit(HelloType=value)

    @TransportMode.setter
    def TransportMode(self, value):
        self._TransportMode = value
        self.edit(TransportMode=value)

    @EgressLabel.setter
    def EgressLabel(self, value):
        self._EgressLabel = value
        self.edit(EgressLabel=value)

    @MinLabel.setter
    def MinLabel(self, value):
        self._MinLabel = value
        self.edit(MinLabel=value)

    @LabelSpaceId.setter
    def LabelSpaceId(self, value):
        self._LabelSpaceId = value
        self.edit(LabelSpaceId=value)

    @HelloInterval.setter
    def HelloInterval(self, value):
        self._HelloInterval = value
        self.edit(HelloInterval=value)

    @HelloHoldTime.setter
    def HelloHoldTime(self, value):
        self._HelloHoldTime = value
        self.edit(HelloHoldTime=value)

    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value):
        self._KeepAliveInterval = value
        self.edit(KeepAliveInterval=value)

    @KeepAliveHoldTime.setter
    def KeepAliveHoldTime(self, value):
        self._KeepAliveHoldTime = value
        self.edit(KeepAliveHoldTime=value)

    def _set_routerid_with_str(self, value):
        self._RouterId = value

    def _set_state_with_str(self, value):
        seperate = value.find(':')
        exec('self._State = EnumLdpState.%s' % value[:seperate])

    def _set_hellotype_with_str(self, value):
        seperate = value.find(':')
        exec('self._HelloType = EnumHelloType.%s' % value[:seperate])

    def _set_transportmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._TransportMode = EnumTransportMode.%s' % value[:seperate])

    def _set_egresslabel_with_str(self, value):
        seperate = value.find(':')
        exec('self._EgressLabel = EnumEgressLabel.%s' % value[:seperate])

    def _set_minlabel_with_str(self, value):
        try:
            self._MinLabel = int(value)
        except ValueError:
            self._MinLabel = hex(int(value, 16))

    def _set_labelspaceid_with_str(self, value):
        try:
            self._LabelSpaceId = int(value)
        except ValueError:
            self._LabelSpaceId = hex(int(value, 16))

    def _set_hellointerval_with_str(self, value):
        try:
            self._HelloInterval = int(value)
        except ValueError:
            self._HelloInterval = hex(int(value, 16))

    def _set_helloholdtime_with_str(self, value):
        try:
            self._HelloHoldTime = int(value)
        except ValueError:
            self._HelloHoldTime = hex(int(value, 16))

    def _set_keepaliveinterval_with_str(self, value):
        try:
            self._KeepAliveInterval = int(value)
        except ValueError:
            self._KeepAliveInterval = hex(int(value, 16))

    def _set_keepaliveholdtime_with_str(self, value):
        try:
            self._KeepAliveHoldTime = int(value)
        except ValueError:
            self._KeepAliveHoldTime = hex(int(value, 16))

