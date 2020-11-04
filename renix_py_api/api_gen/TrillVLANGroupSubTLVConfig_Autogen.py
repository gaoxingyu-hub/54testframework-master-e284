"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillVLANGroupSubTLVConfig(ROMObject):
    def __init__(self, PrimaryVLANID=None, SecondaryVLANID=None, **kwargs):
        self._PrimaryVLANID = PrimaryVLANID  # Primary VLAN ID
        self._SecondaryVLANID = SecondaryVLANID  # Secondary VLAN ID

        properties = kwargs.copy()
        if PrimaryVLANID is not None:
            properties['PrimaryVLANID'] = PrimaryVLANID
        if SecondaryVLANID is not None:
            properties['SecondaryVLANID'] = SecondaryVLANID

        # call base class function, and it will send message to renix server to create a class.
        super(TrillVLANGroupSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrimaryVLANID=None, SecondaryVLANID=None, **kwargs):
        properties = kwargs.copy()
        if PrimaryVLANID is not None:
            self._PrimaryVLANID = PrimaryVLANID
            properties['PrimaryVLANID'] = PrimaryVLANID
        if SecondaryVLANID is not None:
            self._SecondaryVLANID = SecondaryVLANID
            properties['SecondaryVLANID'] = SecondaryVLANID

        super(TrillVLANGroupSubTLVConfig, self).edit(**properties)

    @property
    def PrimaryVLANID(self):
        """
        get the value of property _PrimaryVLANID
        """
        if self.force_auto_sync:
            self.get('PrimaryVLANID')
        return self._PrimaryVLANID

    @property
    def SecondaryVLANID(self):
        """
        get the value of property _SecondaryVLANID
        """
        if self.force_auto_sync:
            self.get('SecondaryVLANID')
        return self._SecondaryVLANID

    @PrimaryVLANID.setter
    def PrimaryVLANID(self, value):
        self._PrimaryVLANID = value
        self.edit(PrimaryVLANID=value)

    @SecondaryVLANID.setter
    def SecondaryVLANID(self, value):
        self._SecondaryVLANID = value
        self.edit(SecondaryVLANID=value)

    def _set_primaryvlanid_with_str(self, value):
        try:
            self._PrimaryVLANID = int(value)
        except ValueError:
            self._PrimaryVLANID = hex(int(value, 16))

    def _set_secondaryvlanid_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SecondaryVLANID = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._SecondaryVLANID.append(int(str_value))
            except ValueError:
                self._SecondaryVLANID.append(hex(int(str_value, 16)))

