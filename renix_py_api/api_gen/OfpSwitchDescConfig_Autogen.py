"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OfpRoleDescConfig_Autogen import OfpRoleDescConfig


@rom_manager.rom
class OfpSwitchDescConfig(OfpRoleDescConfig):
    def __init__(self, DPID=None, **kwargs):
        self._DPID = DPID  # DPID

        properties = kwargs.copy()
        if DPID is not None:
            properties['DPID'] = DPID

        # call base class function, and it will send message to renix server to create a class.
        super(OfpSwitchDescConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DPID=None, **kwargs):
        properties = kwargs.copy()
        if DPID is not None:
            self._DPID = DPID
            properties['DPID'] = DPID

        super(OfpSwitchDescConfig, self).edit(**properties)

    @property
    def DPID(self):
        """
        get the value of property _DPID
        """
        if self.force_auto_sync:
            self.get('DPID')
        return self._DPID

    @DPID.setter
    def DPID(self, value):
        self._DPID = value
        self.edit(DPID=value)

    def _set_dpid_with_str(self, value):
        try:
            self._DPID = int(value)
        except ValueError:
            self._DPID = hex(int(value, 16))

