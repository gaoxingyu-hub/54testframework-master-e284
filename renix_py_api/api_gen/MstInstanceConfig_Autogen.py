"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BaseMstInstanceConfig_Autogen import BaseMstInstanceConfig


@rom_manager.rom
class MstInstanceConfig(BaseMstInstanceConfig):
    def __init__(self, BridgePriority=None, PortPriority=None, VlanIds=None, **kwargs):
        self._BridgePriority = BridgePriority  # Bridge Priority
        self._PortPriority = PortPriority  # Port Priority
        self._VlanIds = VlanIds  # VLAN IDs

        properties = kwargs.copy()
        if BridgePriority is not None:
            properties['BridgePriority'] = BridgePriority
        if PortPriority is not None:
            properties['PortPriority'] = PortPriority
        if VlanIds is not None:
            properties['VlanIds'] = VlanIds

        # call base class function, and it will send message to renix server to create a class.
        super(MstInstanceConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, BridgePriority=None, PortPriority=None, VlanIds=None, **kwargs):
        properties = kwargs.copy()
        if BridgePriority is not None:
            self._BridgePriority = BridgePriority
            properties['BridgePriority'] = BridgePriority
        if PortPriority is not None:
            self._PortPriority = PortPriority
            properties['PortPriority'] = PortPriority
        if VlanIds is not None:
            self._VlanIds = VlanIds
            properties['VlanIds'] = VlanIds

        super(MstInstanceConfig, self).edit(**properties)

    @property
    def BridgePriority(self):
        """
        get the value of property _BridgePriority
        """
        if self.force_auto_sync:
            self.get('BridgePriority')
        return self._BridgePriority

    @property
    def PortPriority(self):
        """
        get the value of property _PortPriority
        """
        if self.force_auto_sync:
            self.get('PortPriority')
        return self._PortPriority

    @property
    def VlanIds(self):
        """
        get the value of property _VlanIds
        """
        if self.force_auto_sync:
            self.get('VlanIds')
        return self._VlanIds

    @BridgePriority.setter
    def BridgePriority(self, value):
        self._BridgePriority = value
        self.edit(BridgePriority=value)

    @PortPriority.setter
    def PortPriority(self, value):
        self._PortPriority = value
        self.edit(PortPriority=value)

    @VlanIds.setter
    def VlanIds(self, value):
        self._VlanIds = value
        self.edit(VlanIds=value)

    def _set_bridgepriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._BridgePriority = EnumRootPriority.%s' % value[:seperate])

    def _set_portpriority_with_str(self, value):
        seperate = value.find(':')
        exec('self._PortPriority = EnumPortPriority.%s' % value[:seperate])

    def _set_vlanids_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VlanIds = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._VlanIds.append(int(str_value))
            except ValueError:
                self._VlanIds.append(hex(int(str_value, 16)))

