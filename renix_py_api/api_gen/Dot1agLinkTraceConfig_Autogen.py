"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Dot1agCommandConfig_Autogen import Dot1agCommandConfig


@rom_manager.rom
class Dot1agLinkTraceConfig(Dot1agCommandConfig):
    def __init__(self, InitTtl=None, **kwargs):
        self._InitTtl = InitTtl  # Initial TTL

        properties = kwargs.copy()
        if InitTtl is not None:
            properties['InitTtl'] = InitTtl

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agLinkTraceConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, InitTtl=None, **kwargs):
        properties = kwargs.copy()
        if InitTtl is not None:
            self._InitTtl = InitTtl
            properties['InitTtl'] = InitTtl

        super(Dot1agLinkTraceConfig, self).edit(**properties)

    @property
    def InitTtl(self):
        """
        get the value of property _InitTtl
        """
        if self.force_auto_sync:
            self.get('InitTtl')
        return self._InitTtl

    @InitTtl.setter
    def InitTtl(self, value):
        self._InitTtl = value
        self.edit(InitTtl=value)

    def _set_initttl_with_str(self, value):
        try:
            self._InitTtl = int(value)
        except ValueError:
            self._InitTtl = hex(int(value, 16))

