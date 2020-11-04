"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrillGroupMacAddressSubTLVConfig(ROMObject):
    def __init__(self, TopologyID=None, VLANID=None, **kwargs):
        self._TopologyID = TopologyID  # Topology ID
        self._VLANID = VLANID  # VLAN ID

        properties = kwargs.copy()
        if TopologyID is not None:
            properties['TopologyID'] = TopologyID
        if VLANID is not None:
            properties['VLANID'] = VLANID

        # call base class function, and it will send message to renix server to create a class.
        super(TrillGroupMacAddressSubTLVConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TopologyID=None, VLANID=None, **kwargs):
        properties = kwargs.copy()
        if TopologyID is not None:
            self._TopologyID = TopologyID
            properties['TopologyID'] = TopologyID
        if VLANID is not None:
            self._VLANID = VLANID
            properties['VLANID'] = VLANID

        super(TrillGroupMacAddressSubTLVConfig, self).edit(**properties)

    @property
    def TopologyID(self):
        """
        get the value of property _TopologyID
        """
        if self.force_auto_sync:
            self.get('TopologyID')
        return self._TopologyID

    @property
    def VLANID(self):
        """
        get the value of property _VLANID
        """
        if self.force_auto_sync:
            self.get('VLANID')
        return self._VLANID

    @TopologyID.setter
    def TopologyID(self, value):
        self._TopologyID = value
        self.edit(TopologyID=value)

    @VLANID.setter
    def VLANID(self, value):
        self._VLANID = value
        self.edit(VLANID=value)

    def _set_topologyid_with_str(self, value):
        try:
            self._TopologyID = int(value)
        except ValueError:
            self._TopologyID = hex(int(value, 16))

    def _set_vlanid_with_str(self, value):
        try:
            self._VLANID = int(value)
        except ValueError:
            self._VLANID = hex(int(value, 16))

