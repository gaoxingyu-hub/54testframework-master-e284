"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillGroupMacRecordConfig(ROMObject):
    def __init__(self, GroupMacAddress=None, SourceMACAddressList=None, **kwargs):
        self._GroupMacAddress = GroupMacAddress  # Group Mac Address
        self._SourceMACAddressList = SourceMACAddressList  # Source Mac Address

        properties = kwargs.copy()
        if GroupMacAddress is not None:
            properties['GroupMacAddress'] = GroupMacAddress
        if SourceMACAddressList is not None:
            properties['SourceMACAddressList'] = SourceMACAddressList

        # call base class function, and it will send message to renix server to create a class.
        super(TrillGroupMacRecordConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, GroupMacAddress=None, SourceMACAddressList=None, **kwargs):
        properties = kwargs.copy()
        if GroupMacAddress is not None:
            self._GroupMacAddress = GroupMacAddress
            properties['GroupMacAddress'] = GroupMacAddress
        if SourceMACAddressList is not None:
            self._SourceMACAddressList = SourceMACAddressList
            properties['SourceMACAddressList'] = SourceMACAddressList

        super(TrillGroupMacRecordConfig, self).edit(**properties)

    @property
    def GroupMacAddress(self):
        """
        get the value of property _GroupMacAddress
        """
        if self.force_auto_sync:
            self.get('GroupMacAddress')
        return self._GroupMacAddress

    @property
    def SourceMACAddressList(self):
        """
        get the value of property _SourceMACAddressList
        """
        if self.force_auto_sync:
            self.get('SourceMACAddressList')
        return self._SourceMACAddressList

    @GroupMacAddress.setter
    def GroupMacAddress(self, value):
        self._GroupMacAddress = value
        self.edit(GroupMacAddress=value)

    @SourceMACAddressList.setter
    def SourceMACAddressList(self, value):
        self._SourceMACAddressList = value
        self.edit(SourceMACAddressList=value)

    def _set_groupmacaddress_with_str(self, value):
        self._GroupMacAddress = value

    def _set_sourcemacaddresslist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._SourceMACAddressList = tmp_value.split()

