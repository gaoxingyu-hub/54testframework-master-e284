"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class OfpCreateFlowTableWizard(WizardConfigBase):
    def __init__(self, StreamTemplateHanles=None, SwitchHandles=None, ControllerHandle=None, FlowTableType=None, FlowMatch=None, FlowActionType=None, HardTimeOut=None, IdleTimeOut=None, Cookie=None, CookieMask=None, Priority=None, Flags=None, InPort=None, OutPort=None, **kwargs):
        self._StreamTemplateHanles = StreamTemplateHanles  # Stream Handles
        self._SwitchHandles = SwitchHandles  # Switch Handles
        self._ControllerHandle = ControllerHandle  # ControllerHandle
        self._FlowTableType = FlowTableType  # Tree
        self._FlowMatch = FlowMatch  # Flow Match
        self._FlowActionType = FlowActionType  # Action
        self._HardTimeOut = HardTimeOut  # Max time before discarding
        self._IdleTimeOut = IdleTimeOut  # Idle time before discarding
        self._Cookie = Cookie  # Cookie
        self._CookieMask = CookieMask  # Cookie Mask
        self._Priority = Priority  # Priority
        self._Flags = swap_int_to_enum_flag(Flags, EnumOfpFlowFlags)  # Flags
        self._InPort = InPort  # Ingress Port ID
        self._OutPort = OutPort  # Output Port ID

        properties = kwargs.copy()
        if StreamTemplateHanles is not None:
            properties['StreamTemplateHanles'] = StreamTemplateHanles
        if SwitchHandles is not None:
            properties['SwitchHandles'] = SwitchHandles
        if ControllerHandle is not None:
            properties['ControllerHandle'] = ControllerHandle
        if FlowTableType is not None:
            properties['FlowTableType'] = FlowTableType
        if FlowMatch is not None:
            properties['FlowMatch'] = FlowMatch
        if FlowActionType is not None:
            properties['FlowActionType'] = FlowActionType
        if HardTimeOut is not None:
            properties['HardTimeOut'] = HardTimeOut
        if IdleTimeOut is not None:
            properties['IdleTimeOut'] = IdleTimeOut
        if Cookie is not None:
            properties['Cookie'] = Cookie
        if CookieMask is not None:
            properties['CookieMask'] = CookieMask
        if Priority is not None:
            properties['Priority'] = Priority
        if Flags is not None:
            if isinstance(Flags, Flag):
                properties['Flags'] = Flags.value
            else:
                properties['Flags'] = Flags
        if InPort is not None:
            properties['InPort'] = InPort
        if OutPort is not None:
            properties['OutPort'] = OutPort

        # call base class function, and it will send message to renix server to create a class.
        super(OfpCreateFlowTableWizard, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StreamTemplateHanles=None, SwitchHandles=None, ControllerHandle=None, FlowTableType=None, FlowMatch=None, FlowActionType=None, HardTimeOut=None, IdleTimeOut=None, Cookie=None, CookieMask=None, Priority=None, Flags=None, InPort=None, OutPort=None, **kwargs):
        properties = kwargs.copy()
        if StreamTemplateHanles is not None:
            self._StreamTemplateHanles = StreamTemplateHanles
            properties['StreamTemplateHanles'] = StreamTemplateHanles
        if SwitchHandles is not None:
            self._SwitchHandles = SwitchHandles
            properties['SwitchHandles'] = SwitchHandles
        if ControllerHandle is not None:
            self._ControllerHandle = ControllerHandle
            properties['ControllerHandle'] = ControllerHandle
        if FlowTableType is not None:
            self._FlowTableType = FlowTableType
            properties['FlowTableType'] = FlowTableType
        if FlowMatch is not None:
            self._FlowMatch = FlowMatch
            properties['FlowMatch'] = FlowMatch
        if FlowActionType is not None:
            self._FlowActionType = FlowActionType
            properties['FlowActionType'] = FlowActionType
        if HardTimeOut is not None:
            self._HardTimeOut = HardTimeOut
            properties['HardTimeOut'] = HardTimeOut
        if IdleTimeOut is not None:
            self._IdleTimeOut = IdleTimeOut
            properties['IdleTimeOut'] = IdleTimeOut
        if Cookie is not None:
            self._Cookie = Cookie
            properties['Cookie'] = Cookie
        if CookieMask is not None:
            self._CookieMask = CookieMask
            properties['CookieMask'] = CookieMask
        if Priority is not None:
            self._Priority = Priority
            properties['Priority'] = Priority
        if Flags is not None:
            self._Flags = swap_int_to_enum_flag(Flags, EnumOfpFlowFlags)
            if isinstance(Flags, Flag):
                properties['Flags'] = Flags.value
            else:
                properties['Flags'] = Flags
        if InPort is not None:
            self._InPort = InPort
            properties['InPort'] = InPort
        if OutPort is not None:
            self._OutPort = OutPort
            properties['OutPort'] = OutPort

        super(OfpCreateFlowTableWizard, self).edit(**properties)

    @property
    def StreamTemplateHanles(self):
        """
        get the value of property _StreamTemplateHanles
        """
        if self.force_auto_sync:
            self.get('StreamTemplateHanles')
        return self._StreamTemplateHanles

    @property
    def SwitchHandles(self):
        """
        get the value of property _SwitchHandles
        """
        if self.force_auto_sync:
            self.get('SwitchHandles')
        return self._SwitchHandles

    @property
    def ControllerHandle(self):
        """
        get the value of property _ControllerHandle
        """
        if self.force_auto_sync:
            self.get('ControllerHandle')
        return self._ControllerHandle

    @property
    def FlowTableType(self):
        """
        get the value of property _FlowTableType
        """
        if self.force_auto_sync:
            self.get('FlowTableType')
        return self._FlowTableType

    @property
    def FlowMatch(self):
        """
        get the value of property _FlowMatch
        """
        if self.force_auto_sync:
            self.get('FlowMatch')
        return self._FlowMatch

    @property
    def FlowActionType(self):
        """
        get the value of property _FlowActionType
        """
        if self.force_auto_sync:
            self.get('FlowActionType')
        return self._FlowActionType

    @property
    def HardTimeOut(self):
        """
        get the value of property _HardTimeOut
        """
        if self.force_auto_sync:
            self.get('HardTimeOut')
        return self._HardTimeOut

    @property
    def IdleTimeOut(self):
        """
        get the value of property _IdleTimeOut
        """
        if self.force_auto_sync:
            self.get('IdleTimeOut')
        return self._IdleTimeOut

    @property
    def Cookie(self):
        """
        get the value of property _Cookie
        """
        if self.force_auto_sync:
            self.get('Cookie')
        return self._Cookie

    @property
    def CookieMask(self):
        """
        get the value of property _CookieMask
        """
        if self.force_auto_sync:
            self.get('CookieMask')
        return self._CookieMask

    @property
    def Priority(self):
        """
        get the value of property _Priority
        """
        if self.force_auto_sync:
            self.get('Priority')
        return self._Priority

    @property
    def Flags(self):
        """
        get the value of property _Flags
        """
        if self.force_auto_sync:
            self.get('Flags')
        return self._Flags

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

    @StreamTemplateHanles.setter
    def StreamTemplateHanles(self, value):
        self._StreamTemplateHanles = value
        self.edit(StreamTemplateHanles=value)

    @SwitchHandles.setter
    def SwitchHandles(self, value):
        self._SwitchHandles = value
        self.edit(SwitchHandles=value)

    @ControllerHandle.setter
    def ControllerHandle(self, value):
        self._ControllerHandle = value
        self.edit(ControllerHandle=value)

    @FlowTableType.setter
    def FlowTableType(self, value):
        self._FlowTableType = value
        self.edit(FlowTableType=value)

    @FlowMatch.setter
    def FlowMatch(self, value):
        self._FlowMatch = value
        self.edit(FlowMatch=value)

    @FlowActionType.setter
    def FlowActionType(self, value):
        self._FlowActionType = value
        self.edit(FlowActionType=value)

    @HardTimeOut.setter
    def HardTimeOut(self, value):
        self._HardTimeOut = value
        self.edit(HardTimeOut=value)

    @IdleTimeOut.setter
    def IdleTimeOut(self, value):
        self._IdleTimeOut = value
        self.edit(IdleTimeOut=value)

    @Cookie.setter
    def Cookie(self, value):
        self._Cookie = value
        self.edit(Cookie=value)

    @CookieMask.setter
    def CookieMask(self, value):
        self._CookieMask = value
        self.edit(CookieMask=value)

    @Priority.setter
    def Priority(self, value):
        self._Priority = value
        self.edit(Priority=value)

    @Flags.setter
    def Flags(self, value):
        self._Flags = swap_int_to_enum_flag(value, EnumOfpFlowFlags)
        if isinstance(value, Flag):
            self.edit(Flags=value.value)
        else:
            self.edit(Flags=value)

    @InPort.setter
    def InPort(self, value):
        self._InPort = value
        self.edit(InPort=value)

    @OutPort.setter
    def OutPort(self, value):
        self._OutPort = value
        self.edit(OutPort=value)

    def _set_streamtemplatehanles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHanles = tmp_value.split()

    def _set_switchhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SwitchHandles = tmp_value.split()

    def _set_controllerhandle_with_str(self, value):
        self._ControllerHandle = value

    def _set_flowtabletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FlowTableType = EnumFlowTableType.%s' % value[:seperate])

    def _set_flowmatch_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FlowMatch = tmp_value.split()

    def _set_flowactiontype_with_str(self, value):
        seperate = value.find(':')
        exec('self._FlowActionType = EnumFlowActionType.%s' % value[:seperate])

    def _set_hardtimeout_with_str(self, value):
        try:
            self._HardTimeOut = int(value)
        except ValueError:
            self._HardTimeOut = hex(int(value, 16))

    def _set_idletimeout_with_str(self, value):
        try:
            self._IdleTimeOut = int(value)
        except ValueError:
            self._IdleTimeOut = hex(int(value, 16))

    def _set_cookie_with_str(self, value):
        try:
            self._Cookie = int(value)
        except ValueError:
            self._Cookie = hex(int(value, 16))

    def _set_cookiemask_with_str(self, value):
        try:
            self._CookieMask = int(value)
        except ValueError:
            self._CookieMask = hex(int(value, 16))

    def _set_priority_with_str(self, value):
        try:
            self._Priority = int(value)
        except ValueError:
            self._Priority = hex(int(value, 16))

    def _set_flags_with_str(self, value):
        seperate = value.find(':')
        self._Flags = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOfpFlowFlags)

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

