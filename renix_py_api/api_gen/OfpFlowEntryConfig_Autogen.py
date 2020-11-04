"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpFlowEntryConfig(ROMObject):
    def __init__(self, Priority=None, IdleTimeout=None, HardTimeout=None, Cookie=None, Flags=None, PacketInAction=None, FlowStreamMatch=None, InPort=None, OutPort=None, **kwargs):
        self._Priority = Priority  # Priority
        self._IdleTimeout = IdleTimeout  # Idle Timeout (sec)
        self._HardTimeout = HardTimeout  # Hard Timeout (sec)
        self._Cookie = Cookie  # Cookie
        self._Flags = swap_int_to_enum_flag(Flags, EnumOfpFlowFlags)  # Flags
        self._PacketInAction = PacketInAction  # PacketIn Action
        self._FlowStreamMatch = FlowStreamMatch  # Flow Match
        self._InPort = InPort  # Ingress Port ID
        self._OutPort = OutPort  # Output Port ID

        properties = kwargs.copy()
        if Priority is not None:
            properties['Priority'] = Priority
        if IdleTimeout is not None:
            properties['IdleTimeout'] = IdleTimeout
        if HardTimeout is not None:
            properties['HardTimeout'] = HardTimeout
        if Cookie is not None:
            properties['Cookie'] = Cookie
        if Flags is not None:
            if isinstance(Flags, Flag):
                properties['Flags'] = Flags.value
            else:
                properties['Flags'] = Flags
        if PacketInAction is not None:
            properties['PacketInAction'] = PacketInAction
        if FlowStreamMatch is not None:
            properties['FlowStreamMatch'] = FlowStreamMatch
        if InPort is not None:
            properties['InPort'] = InPort
        if OutPort is not None:
            properties['OutPort'] = OutPort

        # call base class function, and it will send message to renix server to create a class.
        super(OfpFlowEntryConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Priority=None, IdleTimeout=None, HardTimeout=None, Cookie=None, Flags=None, PacketInAction=None, FlowStreamMatch=None, InPort=None, OutPort=None, **kwargs):
        properties = kwargs.copy()
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if IdleTimeout is not None:
            self._IdleTimeout = IdleTimeout
            properties['IdleTimeout'] = IdleTimeout
        if HardTimeout is not None:
            self._HardTimeout = HardTimeout
            properties['HardTimeout'] = HardTimeout
        if Cookie is not None:
            self._Cookie = Cookie
            properties['Cookie'] = Cookie
        if Flags is not None:
            self._Flags = swap_int_to_enum_flag(Flags, EnumOfpFlowFlags)
            if isinstance(Flags, Flag):
                properties['Flags'] = Flags.value
            else:
                properties['Flags'] = Flags
        if PacketInAction is not None:
            self._PacketInAction = PacketInAction
            properties['PacketInAction'] = PacketInAction
        if FlowStreamMatch is not None:
            self._FlowStreamMatch = FlowStreamMatch
            properties['FlowStreamMatch'] = FlowStreamMatch
        if InPort is not None:
            self._InPort = InPort
            properties['InPort'] = InPort
        if OutPort is not None:
            self._OutPort = OutPort
            properties['OutPort'] = OutPort

        super(OfpFlowEntryConfig, self).edit(**properties)

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def IdleTimeout(self):
        """
        get the value of property _IdleTimeout
        """
        if self.force_auto_sync:
            self.get('IdleTimeout')
        return self._IdleTimeout

    @property
    def HardTimeout(self):
        """
        get the value of property _HardTimeout
        """
        if self.force_auto_sync:
            self.get('HardTimeout')
        return self._HardTimeout

    @property
    def Cookie(self):
        """
        get the value of property _Cookie
        """
        if self.force_auto_sync:
            self.get('Cookie')
        return self._Cookie

    @property
    def Flags(self):
        """
        get the value of property _Flags
        """
        if self.force_auto_sync:
            self.get('Flags')
        return self._Flags

    @property
    def PacketInAction(self):
        """
        get the value of property _PacketInAction
        """
        if self.force_auto_sync:
            self.get('PacketInAction')
        return self._PacketInAction

    @property
    def FlowStreamMatch(self):
        """
        get the value of property _FlowStreamMatch
        """
        if self.force_auto_sync:
            self.get('FlowStreamMatch')
        return self._FlowStreamMatch

    @property
    def InPort(self):
        """
        get the value of property _InPort
        """
        if self.force_auto_sync:
            self.get('InPort')
        return self._InPort

    @property
    def OutPort(self):
        """
        get the value of property _OutPort
        """
        if self.force_auto_sync:
            self.get('OutPort')
        return self._OutPort

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @IdleTimeout.setter
    def IdleTimeout(self, value):
        self._IdleTimeout = value
        self.edit(IdleTimeout=value)

    @HardTimeout.setter
    def HardTimeout(self, value):
        self._HardTimeout = value
        self.edit(HardTimeout=value)

    @Cookie.setter
    def Cookie(self, value):
        self._Cookie = value
        self.edit(Cookie=value)

    @Flags.setter
    def Flags(self, value):
        self._Flags = swap_int_to_enum_flag(value, EnumOfpFlowFlags)
        if isinstance(value, Flag):
            self.edit(Flags=value.value)
        else:
            self.edit(Flags=value)

    @PacketInAction.setter
    def PacketInAction(self, value):
        self._PacketInAction = value
        self.edit(PacketInAction=value)

    @FlowStreamMatch.setter
    def FlowStreamMatch(self, value):
        self._FlowStreamMatch = value
        self.edit(FlowStreamMatch=value)

    @InPort.setter
    def InPort(self, value):
        self._InPort = value
        self.edit(InPort=value)

    @OutPort.setter
    def OutPort(self, value):
        self._OutPort = value
        self.edit(OutPort=value)

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_idletimeout_with_str(self, value):
        try:
            self._IdleTimeout = int(value)
        except ValueError:
            self._IdleTimeout = hex(int(value, 16))

    def _set_hardtimeout_with_str(self, value):
        try:
            self._HardTimeout = int(value)
        except ValueError:
            self._HardTimeout = hex(int(value, 16))

    def _set_cookie_with_str(self, value):
        try:
            self._Cookie = int(value)
        except ValueError:
            self._Cookie = hex(int(value, 16))

    def _set_flags_with_str(self, value):
        seperate = value.find(':')
        self._Flags = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOfpFlowFlags)

    def _set_packetinaction_with_str(self, value):
        seperate = value.find(':')
        exec('self._PacketInAction = EnumOfpPacketInAction.%s' % value[:seperate])

    def _set_flowstreammatch_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FlowStreamMatch = tmp_value.split()

    def _set_inport_with_str(self, value):
        try:
            self._InPort = int(value)
        except ValueError:
            self._InPort = hex(int(value, 16))

    def _set_outport_with_str(self, value):
        try:
            self._OutPort = int(value)
        except ValueError:
            self._OutPort = hex(int(value, 16))

