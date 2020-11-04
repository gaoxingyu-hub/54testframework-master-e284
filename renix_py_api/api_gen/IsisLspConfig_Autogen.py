"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class IsisLspConfig(ROMObject):
    def __init__(self, SystemId=None, Level=None, PseudonodeId=None, TeRouterId=None, SequenceNumber=None, RemainingLifeTime=None, Checksum=None, AttachedBit=None, OverloadBit=None, **kwargs):
        self._SystemId = SystemId  # System ID
        self._Level = Level  # Level
        self._PseudonodeId = PseudonodeId  # Pseudonode ID
        self._TeRouterId = TeRouterId  # TE Router ID
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._RemainingLifeTime = RemainingLifeTime  # Remaining LifeTime
        self._Checksum = Checksum  # Checksum Correct
        self._AttachedBit = AttachedBit  # Attached Bit
        self._OverloadBit = OverloadBit  # Overload Bit

        properties = kwargs.copy()
        if SystemId is not None:
            properties['SystemId'] = SystemId
        if Level is not None:
            properties['Level'] = Level
        if PseudonodeId is not None:
            properties['PseudonodeId'] = PseudonodeId
        if TeRouterId is not None:
            properties['TeRouterId'] = TeRouterId
        if SequenceNumber is not None:
            properties['SequenceNumber'] = SequenceNumber
        if RemainingLifeTime is not None:
            properties['RemainingLifeTime'] = RemainingLifeTime
        if Checksum is not None:
            properties['Checksum'] = Checksum
        if AttachedBit is not None:
            properties['AttachedBit'] = AttachedBit
        if OverloadBit is not None:
            properties['OverloadBit'] = OverloadBit

        # call base class function, and it will send message to renix server to create a class.
        super(IsisLspConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SystemId=None, Level=None, PseudonodeId=None, TeRouterId=None, SequenceNumber=None, RemainingLifeTime=None, Checksum=None, AttachedBit=None, OverloadBit=None, **kwargs):
        properties = kwargs.copy()
        if SystemId is not None:
            self._SystemId = SystemId
            properties['SystemId'] = SystemId
        if Level is not None:
            self._Level = Level
            properties['Level'] = Level
        if PseudonodeId is not None:
            self._PseudonodeId = PseudonodeId
            properties['PseudonodeId'] = PseudonodeId
        if TeRouterId is not None:
            self._TeRouterId = TeRouterId
            properties['TeRouterId'] = TeRouterId
        if SequenceNumber is not None:
            self._SequenceNumber = SequenceNumber
            properties['SequenceNumber'] = SequenceNumber
        if RemainingLifeTime is not None:
            self._RemainingLifeTime = RemainingLifeTime
            properties['RemainingLifeTime'] = RemainingLifeTime
        if Checksum is not None:
            self._Checksum = Checksum
            properties['Checksum'] = Checksum
        if AttachedBit is not None:
            self._AttachedBit = AttachedBit
            properties['AttachedBit'] = AttachedBit
        if OverloadBit is not None:
            self._OverloadBit = OverloadBit
            properties['OverloadBit'] = OverloadBit

        super(IsisLspConfig, self).edit(**properties)

    @property
    def SystemId(self):
        """
        get the value of property _SystemId
        """
        if self.force_auto_sync:
            self.get('SystemId')
        return self._SystemId

    @property
    def Level(self):
        """
        get the value of property _Level
        """
        if self.force_auto_sync:
            self.get('Level')
        return self._Level

    @property
    def PseudonodeId(self):
        """
        get the value of property _PseudonodeId
        """
        if self.force_auto_sync:
            self.get('PseudonodeId')
        return self._PseudonodeId

    @property
    def TeRouterId(self):
        """
        get the value of property _TeRouterId
        """
        if self.force_auto_sync:
            self.get('TeRouterId')
        return self._TeRouterId

    @property
    def SequenceNumber(self):
        """
        get the value of property _SequenceNumber
        """
        if self.force_auto_sync:
            self.get('SequenceNumber')
        return self._SequenceNumber

    @property
    def RemainingLifeTime(self):
        """
        get the value of property _RemainingLifeTime
        """
        if self.force_auto_sync:
            self.get('RemainingLifeTime')
        return self._RemainingLifeTime

    @property
    def Checksum(self):
        """
        get the value of property _Checksum
        """
        if self.force_auto_sync:
            self.get('Checksum')
        return self._Checksum

    @property
    def AttachedBit(self):
        """
        get the value of property _AttachedBit
        """
        if self.force_auto_sync:
            self.get('AttachedBit')
        return self._AttachedBit

    @property
    def OverloadBit(self):
        """
        get the value of property _OverloadBit
        """
        if self.force_auto_sync:
            self.get('OverloadBit')
        return self._OverloadBit

    @SystemId.setter
    def SystemId(self, value):
        self._SystemId = value
        self.edit(SystemId=value)

    @Level.setter
    def Level(self, value):
        self._Level = value
        self.edit(Level=value)

    @PseudonodeId.setter
    def PseudonodeId(self, value):
        self._PseudonodeId = value
        self.edit(PseudonodeId=value)

    @TeRouterId.setter
    def TeRouterId(self, value):
        self._TeRouterId = value
        self.edit(TeRouterId=value)

    @SequenceNumber.setter
    def SequenceNumber(self, value):
        self._SequenceNumber = value
        self.edit(SequenceNumber=value)

    @RemainingLifeTime.setter
    def RemainingLifeTime(self, value):
        self._RemainingLifeTime = value
        self.edit(RemainingLifeTime=value)

    @Checksum.setter
    def Checksum(self, value):
        self._Checksum = value
        self.edit(Checksum=value)

    @AttachedBit.setter
    def AttachedBit(self, value):
        self._AttachedBit = value
        self.edit(AttachedBit=value)

    @OverloadBit.setter
    def OverloadBit(self, value):
        self._OverloadBit = value
        self.edit(OverloadBit=value)

    def _set_systemid_with_str(self, value):
        self._SystemId = value

    def _set_level_with_str(self, value):
        seperate = value.find(':')
        exec('self._Level = EnumInterSystemLevel.%s' % value[:seperate])

    def _set_pseudonodeid_with_str(self, value):
        try:
            self._PseudonodeId = int(value)
        except ValueError:
            self._PseudonodeId = hex(int(value, 16))

    def _set_terouterid_with_str(self, value):
        self._TeRouterId = value

    def _set_sequencenumber_with_str(self, value):
        try:
            self._SequenceNumber = int(value)
        except ValueError:
            self._SequenceNumber = hex(int(value, 16))

    def _set_remaininglifetime_with_str(self, value):
        try:
            self._RemainingLifeTime = int(value)
        except ValueError:
            self._RemainingLifeTime = hex(int(value, 16))

    def _set_checksum_with_str(self, value):
        self._Checksum = (value == 'True')

    def _set_attachedbit_with_str(self, value):
        self._AttachedBit = (value == 'True')

    def _set_overloadbit_with_str(self, value):
        self._OverloadBit = (value == 'True')

