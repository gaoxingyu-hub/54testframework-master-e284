"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillEnabledVLANsSubTLVConfig(ROMObject):
    def __init__(self, ListOfEnabledVLANID=None, **kwargs):
        self._ListOfEnabledVLANID = ListOfEnabledVLANID  # List of Enabled VLAN ID

        properties = kwargs.copy()
        if ListOfEnabledVLANID is not None:
            properties['ListOfEnabledVLANID'] = ListOfEnabledVLANID

        # call base class function, and it will send message to renix server to create a class.
        super(TrillEnabledVLANsSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ListOfEnabledVLANID=None, **kwargs):
        properties = kwargs.copy()
        if ListOfEnabledVLANID is not None:
            self._ListOfEnabledVLANID = ListOfEnabledVLANID
            properties['ListOfEnabledVLANID'] = ListOfEnabledVLANID

        super(TrillEnabledVLANsSubTLVConfig, self).edit(**properties)

    @property
    def ListOfEnabledVLANID(self):
        """
        get the value of property _ListOfEnabledVLANID
        """
        if self.force_auto_sync:
            self.get('ListOfEnabledVLANID')
        return self._ListOfEnabledVLANID

    @ListOfEnabledVLANID.setter
    def ListOfEnabledVLANID(self, value):
        self._ListOfEnabledVLANID = value
        self.edit(ListOfEnabledVLANID=value)

    def _set_listofenabledvlanid_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ListOfEnabledVLANID = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._ListOfEnabledVLANID.append(int(str_value))
            except ValueError:
                self._ListOfEnabledVLANID.append(hex(int(str_value, 16)))

