"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillCapabilityTLVConfig(ROMObject):
    def __init__(self, RouterID=None, SBit=None, DBit=None, **kwargs):
        self._CapabilitySubTLV = ''  # Capability Sub-TLV, not editable
        self._RouterID = RouterID  # Router ID
        self._SBit = SBit  # S bit (bit 0)
        self._DBit = DBit  # D bit (bit 1)

        properties = kwargs.copy()
        if RouterID is not None:
            properties['RouterID'] = RouterID
        if SBit is not None:
            properties['SBit'] = SBit
        if DBit is not None:
            properties['DBit'] = DBit

        # call base class function, and it will send message to renix server to create a class.
        super(TrillCapabilityTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouterID=None, SBit=None, DBit=None, **kwargs):
        properties = kwargs.copy()
        if RouterID is not None:
            self._RouterID = RouterID
            properties['RouterID'] = RouterID
        if SBit is not None:
            self._SBit = SBit
            properties['SBit'] = SBit
        if DBit is not None:
            self._DBit = DBit
            properties['DBit'] = DBit

        super(TrillCapabilityTLVConfig, self).edit(**properties)

    @property
    def CapabilitySubTLV(self):
        """
        get the value of property _CapabilitySubTLV
        """
        if self.force_auto_sync:
            self.get('CapabilitySubTLV')
        return self._CapabilitySubTLV

    @property
    def RouterID(self):
        """
        get the value of property _RouterID
        """
        if self.force_auto_sync:
            self.get('RouterID')
        return self._RouterID

    @property
    def SBit(self):
        """
        get the value of property _SBit
        """
        if self.force_auto_sync:
            self.get('SBit')
        return self._SBit

    @property
    def DBit(self):
        """
        get the value of property _DBit
        """
        if self.force_auto_sync:
            self.get('DBit')
        return self._DBit

    @RouterID.setter
    def RouterID(self, value):
        self._RouterID = value
        self.edit(RouterID=value)

    @SBit.setter
    def SBit(self, value):
        self._SBit = value
        self.edit(SBit=value)

    @DBit.setter
    def DBit(self, value):
        self._DBit = value
        self.edit(DBit=value)

    def _set_capabilitysubtlv_with_str(self, value):
        self._CapabilitySubTLV = value

    def _set_routerid_with_str(self, value):
        self._RouterID = value

    def _set_sbit_with_str(self, value):
        self._SBit = (value == 'True')

    def _set_dbit_with_str(self, value):
        self._DBit = (value == 'True')

