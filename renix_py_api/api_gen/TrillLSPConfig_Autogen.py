"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillLSPConfig(ROMObject):
    def __init__(self, SystemID=None, HostName=None, PseudonodeID=None, Lifetime=None, SequenceNumber=None, AttachedBitSet=None, OverloadBitSet=None, MinimumAcceptableMTU=None, **kwargs):
        self._SystemID = SystemID  # System ID
        self._HostName = HostName  # Host Name
        self._PseudonodeID = PseudonodeID  # Pseudonode ID
        self._Lifetime = Lifetime  # Lifetime (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._AttachedBitSet = AttachedBitSet  # Attached Bit Set
        self._OverloadBitSet = OverloadBitSet  # Overload Bit Set
        self._MinimumAcceptableMTU = MinimumAcceptableMTU  # Maximum Acceptable MTU

        properties = kwargs.copy()
        if SystemID is not None:
            properties['SystemID'] = SystemID
        if HostName is not None:
            properties['HostName'] = HostName
        if PseudonodeID is not None:
            properties['PseudonodeID'] = PseudonodeID
        if Lifetime is not None:
            properties['Lifetime'] = Lifetime
        if SequenceNumber is not None:
            properties['SequenceNumber'] = SequenceNumber
        if AttachedBitSet is not None:
            properties['AttachedBitSet'] = AttachedBitSet
        if OverloadBitSet is not None:
            properties['OverloadBitSet'] = OverloadBitSet
        if MinimumAcceptableMTU is not None:
            properties['MinimumAcceptableMTU'] = MinimumAcceptableMTU

        # call base class function, and it will send message to renix server to create a class.
        super(TrillLSPConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SystemID=None, HostName=None, PseudonodeID=None, Lifetime=None, SequenceNumber=None, AttachedBitSet=None, OverloadBitSet=None, MinimumAcceptableMTU=None, **kwargs):
        properties = kwargs.copy()
        if SystemID is not None:
            self._SystemID = SystemID
            properties['SystemID'] = SystemID
        if HostName is not None:
            self._HostName = HostName
            properties['HostName'] = HostName
        if PseudonodeID is not None:
            self._PseudonodeID = PseudonodeID
            properties['PseudonodeID'] = PseudonodeID
        if Lifetime is not None:
            self._Lifetime = Lifetime
            properties['Lifetime'] = Lifetime
        if SequenceNumber is not None:
            self._SequenceNumber = SequenceNumber
            properties['SequenceNumber'] = SequenceNumber
        if AttachedBitSet is not None:
            self._AttachedBitSet = AttachedBitSet
            properties['AttachedBitSet'] = AttachedBitSet
        if OverloadBitSet is not None:
            self._OverloadBitSet = OverloadBitSet
            properties['OverloadBitSet'] = OverloadBitSet
        if MinimumAcceptableMTU is not None:
            self._MinimumAcceptableMTU = MinimumAcceptableMTU
            properties['MinimumAcceptableMTU'] = MinimumAcceptableMTU

        super(TrillLSPConfig, self).edit(**properties)

    @property
    def SystemID(self):
        """
        get the value of property _SystemID
        """
        if self.force_auto_sync:
            self.get('SystemID')
        return self._SystemID

    @property
    def HostName(self):
        """
        get the value of property _HostName
        """
        if self.force_auto_sync:
            self.get('HostName')
        return self._HostName

    @property
    def PseudonodeID(self):
        """
        get the value of property _PseudonodeID
        """
        if self.force_auto_sync:
            self.get('PseudonodeID')
        return self._PseudonodeID

    @property
    def Lifetime(self):
        """
        get the value of property _Lifetime
        """
        if self.force_auto_sync:
            self.get('Lifetime')
        return self._Lifetime

    @property
    def SequenceNumber(self):
        """
        get the value of property _SequenceNumber
        """
        if self.force_auto_sync:
            self.get('SequenceNumber')
        return self._SequenceNumber

    @property
    def AttachedBitSet(self):
        """
        get the value of property _AttachedBitSet
        """
        if self.force_auto_sync:
            self.get('AttachedBitSet')
        return self._AttachedBitSet

    @property
    def OverloadBitSet(self):
        """
        get the value of property _OverloadBitSet
        """
        if self.force_auto_sync:
            self.get('OverloadBitSet')
        return self._OverloadBitSet

    @property
    def MinimumAcceptableMTU(self):
        """
        get the value of property _MinimumAcceptableMTU
        """
        if self.force_auto_sync:
            self.get('MinimumAcceptableMTU')
        return self._MinimumAcceptableMTU

    @SystemID.setter
    def SystemID(self, value):
        self._SystemID = value
        self.edit(SystemID=value)

    @HostName.setter
    def HostName(self, value):
        self._HostName = value
        self.edit(HostName=value)

    @PseudonodeID.setter
    def PseudonodeID(self, value):
        self._PseudonodeID = value
        self.edit(PseudonodeID=value)

    @Lifetime.setter
    def Lifetime(self, value):
        self._Lifetime = value
        self.edit(Lifetime=value)

    @SequenceNumber.setter
    def SequenceNumber(self, value):
        self._SequenceNumber = value
        self.edit(SequenceNumber=value)

    @AttachedBitSet.setter
    def AttachedBitSet(self, value):
        self._AttachedBitSet = value
        self.edit(AttachedBitSet=value)

    @OverloadBitSet.setter
    def OverloadBitSet(self, value):
        self._OverloadBitSet = value
        self.edit(OverloadBitSet=value)

    @MinimumAcceptableMTU.setter
    def MinimumAcceptableMTU(self, value):
        self._MinimumAcceptableMTU = value
        self.edit(MinimumAcceptableMTU=value)

    def _set_systemid_with_str(self, value):
        self._SystemID = value

    def _set_hostname_with_str(self, value):
        self._HostName = value

    def _set_pseudonodeid_with_str(self, value):
        try:
            self._PseudonodeID = int(value)
        except ValueError:
            self._PseudonodeID = hex(int(value, 16))

    def _set_lifetime_with_str(self, value):
        try:
            self._Lifetime = int(value)
        except ValueError:
            self._Lifetime = hex(int(value, 16))

    def _set_sequencenumber_with_str(self, value):
        try:
            self._SequenceNumber = int(value)
        except ValueError:
            self._SequenceNumber = hex(int(value, 16))

    def _set_attachedbitset_with_str(self, value):
        self._AttachedBitSet = (value == 'True')

    def _set_overloadbitset_with_str(self, value):
        self._OverloadBitSet = (value == 'True')

    def _set_minimumacceptablemtu_with_str(self, value):
        try:
            self._MinimumAcceptableMTU = int(value)
        except ValueError:
            self._MinimumAcceptableMTU = hex(int(value, 16))

