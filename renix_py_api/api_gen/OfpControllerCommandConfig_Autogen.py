"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OfpControllerCommandConfig(ROMObject):
    def __init__(self, CmdType=None, EnableBarrier=None, StrictMatch=None, Flags=None, ControllerMaxLength=None, TableID=None, OutGroup=None, OutPort=None, DesiredRole=None, GenerationID=None, PacketData=None, LoopCount=None, ThinkDuration=None, **kwargs):
        self._CmdType = CmdType  # Command Type
        self._EnableBarrier = EnableBarrier  # Enable Barrier
        self._StrictMatch = StrictMatch  # Match Strictly
        self._Flags = Flags  # Flags
        self._ControllerMaxLength = ControllerMaxLength  # Controller Max Length
        self._TableID = TableID  # Table ID
        self._OutGroup = OutGroup  # Out Group
        self._OutPort = OutPort  # Out Port
        self._DesiredRole = DesiredRole  # Desired Role
        self._GenerationID = GenerationID  # Generation ID
        self._PacketData = PacketData  # Packet Data (hex)
        self._LoopCount = LoopCount  # Loop Count
        self._ThinkDuration = ThinkDuration  # Duration (ms)

        properties = kwargs.copy()
        if CmdType is not None:
            properties['CmdType'] = CmdType
        if EnableBarrier is not None:
            properties['EnableBarrier'] = EnableBarrier
        if StrictMatch is not None:
            properties['StrictMatch'] = StrictMatch
        if Flags is not None:
            properties['Flags'] = Flags
        if ControllerMaxLength is not None:
            properties['ControllerMaxLength'] = ControllerMaxLength
        if TableID is not None:
            properties['TableID'] = TableID
        if OutGroup is not None:
            properties['OutGroup'] = OutGroup
        if OutPort is not None:
            properties['OutPort'] = OutPort
        if DesiredRole is not None:
            properties['DesiredRole'] = DesiredRole
        if GenerationID is not None:
            properties['GenerationID'] = GenerationID
        if PacketData is not None:
            properties['PacketData'] = PacketData
        if LoopCount is not None:
            properties['LoopCount'] = LoopCount
        if ThinkDuration is not None:
            properties['ThinkDuration'] = ThinkDuration

        # call base class function, and it will send message to renix server to create a class.
        super(OfpControllerCommandConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CmdType=None, EnableBarrier=None, StrictMatch=None, Flags=None, ControllerMaxLength=None, TableID=None, OutGroup=None, OutPort=None, DesiredRole=None, GenerationID=None, PacketData=None, LoopCount=None, ThinkDuration=None, **kwargs):
        properties = kwargs.copy()
        if CmdType is not None:
            self._CmdType = CmdType
            properties['CmdType'] = CmdType
        if EnableBarrier is not None:
            self._EnableBarrier = EnableBarrier
            properties['EnableBarrier'] = EnableBarrier
        if StrictMatch is not None:
            self._StrictMatch = StrictMatch
            properties['StrictMatch'] = StrictMatch
        if Flags is not None:
            self._Flags = Flags
            properties['Flags'] = Flags
        if ControllerMaxLength is not None:
            self._ControllerMaxLength = ControllerMaxLength
            properties['ControllerMaxLength'] = ControllerMaxLength
        if TableID is not None:
            self._TableID = TableID
            properties['TableID'] = TableID
        if OutGroup is not None:
            self._OutGroup = OutGroup
            properties['OutGroup'] = OutGroup
        if OutPort is not None:
            self._OutPort = OutPort
            properties['OutPort'] = OutPort
        if DesiredRole is not None:
            self._DesiredRole = DesiredRole
            properties['DesiredRole'] = DesiredRole
        if GenerationID is not None:
            self._GenerationID = GenerationID
            properties['GenerationID'] = GenerationID
        if PacketData is not None:
            self._PacketData = PacketData
            properties['PacketData'] = PacketData
        if LoopCount is not None:
            self._LoopCount = LoopCount
            properties['LoopCount'] = LoopCount
        if ThinkDuration is not None:
            self._ThinkDuration = ThinkDuration
            properties['ThinkDuration'] = ThinkDuration

        super(OfpControllerCommandConfig, self).edit(**properties)

    @property
    def CmdType(self):
        """
        get the value of property _CmdType
        """
        if self.force_auto_sync:
            self.get('CmdType')
        return self._CmdType

    @property
    def EnableBarrier(self):
        """
        get the value of property _EnableBarrier
        """
        if self.force_auto_sync:
            self.get('EnableBarrier')
        return self._EnableBarrier

    @property
    def StrictMatch(self):
        """
        get the value of property _StrictMatch
        """
        if self.force_auto_sync:
            self.get('StrictMatch')
        return self._StrictMatch

    @property
    def Flags(self):
        """
        get the value of property _Flags
        """
        if self.force_auto_sync:
            self.get('Flags')
        return self._Flags

    @property
    def ControllerMaxLength(self):
        """
        get the value of property _ControllerMaxLength
        """
        if self.force_auto_sync:
            self.get('ControllerMaxLength')
        return self._ControllerMaxLength

    @property
    def TableID(self):
        """
        get the value of property _TableID
        """
        if self.force_auto_sync:
            self.get('TableID')
        return self._TableID

    @property
    def OutGroup(self):
        """
        get the value of property _OutGroup
        """
        if self.force_auto_sync:
            self.get('OutGroup')
        return self._OutGroup

    @property
    def OutPort(self):
        """
        get the value of property _OutPort
        """
        if self.force_auto_sync:
            self.get('OutPort')
        return self._OutPort

    @property
    def DesiredRole(self):
        """
        get the value of property _DesiredRole
        """
        if self.force_auto_sync:
            self.get('DesiredRole')
        return self._DesiredRole

    @property
    def GenerationID(self):
        """
        get the value of property _GenerationID
        """
        if self.force_auto_sync:
            self.get('GenerationID')
        return self._GenerationID

    @property
    def PacketData(self):
        """
        get the value of property _PacketData
        """
        if self.force_auto_sync:
            self.get('PacketData')
        return self._PacketData

    @property
    def LoopCount(self):
        """
        get the value of property _LoopCount
        """
        if self.force_auto_sync:
            self.get('LoopCount')
        return self._LoopCount

    @property
    def ThinkDuration(self):
        """
        get the value of property _ThinkDuration
        """
        if self.force_auto_sync:
            self.get('ThinkDuration')
        return self._ThinkDuration

    @CmdType.setter
    def CmdType(self, value):
        self._CmdType = value
        self.edit(CmdType=value)

    @EnableBarrier.setter
    def EnableBarrier(self, value):
        self._EnableBarrier = value
        self.edit(EnableBarrier=value)

    @StrictMatch.setter
    def StrictMatch(self, value):
        self._StrictMatch = value
        self.edit(StrictMatch=value)

    @Flags.setter
    def Flags(self, value):
        self._Flags = value
        self.edit(Flags=value)

    @ControllerMaxLength.setter
    def ControllerMaxLength(self, value):
        self._ControllerMaxLength = value
        self.edit(ControllerMaxLength=value)

    @TableID.setter
    def TableID(self, value):
        self._TableID = value
        self.edit(TableID=value)

    @OutGroup.setter
    def OutGroup(self, value):
        self._OutGroup = value
        self.edit(OutGroup=value)

    @OutPort.setter
    def OutPort(self, value):
        self._OutPort = value
        self.edit(OutPort=value)

    @DesiredRole.setter
    def DesiredRole(self, value):
        self._DesiredRole = value
        self.edit(DesiredRole=value)

    @GenerationID.setter
    def GenerationID(self, value):
        self._GenerationID = value
        self.edit(GenerationID=value)

    @PacketData.setter
    def PacketData(self, value):
        self._PacketData = value
        self.edit(PacketData=value)

    @LoopCount.setter
    def LoopCount(self, value):
        self._LoopCount = value
        self.edit(LoopCount=value)

    @ThinkDuration.setter
    def ThinkDuration(self, value):
        self._ThinkDuration = value
        self.edit(ThinkDuration=value)

    def _set_cmdtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._CmdType = EnumOfpCmdType.%s' % value[:seperate])

    def _set_enablebarrier_with_str(self, value):
        self._EnableBarrier = (value == 'True')

    def _set_strictmatch_with_str(self, value):
        self._StrictMatch = (value == 'True')

    def _set_flags_with_str(self, value):
        try:
            self._Flags = int(value)
        except ValueError:
            self._Flags = hex(int(value, 16))

    def _set_controllermaxlength_with_str(self, value):
        try:
            self._ControllerMaxLength = int(value)
        except ValueError:
            self._ControllerMaxLength = hex(int(value, 16))

    def _set_tableid_with_str(self, value):
        try:
            self._TableID = int(value)
        except ValueError:
            self._TableID = hex(int(value, 16))

    def _set_outgroup_with_str(self, value):
        try:
            self._OutGroup = int(value)
        except ValueError:
            self._OutGroup = hex(int(value, 16))

    def _set_outport_with_str(self, value):
        try:
            self._OutPort = int(value)
        except ValueError:
            self._OutPort = hex(int(value, 16))

    def _set_desiredrole_with_str(self, value):
        seperate = value.find(':')
        exec('self._DesiredRole = EnumOfpRole.%s' % value[:seperate])

    def _set_generationid_with_str(self, value):
        try:
            self._GenerationID = int(value)
        except ValueError:
            self._GenerationID = hex(int(value, 16))

    def _set_packetdata_with_str(self, value):
        self._PacketData = value

    def _set_loopcount_with_str(self, value):
        try:
            self._LoopCount = int(value)
        except ValueError:
            self._LoopCount = hex(int(value, 16))

    def _set_thinkduration_with_str(self, value):
        try:
            self._ThinkDuration = int(value)
        except ValueError:
            self._ThinkDuration = hex(int(value, 16))

