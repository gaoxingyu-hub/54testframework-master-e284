"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PppoeConnectCommand(ROMCommand):
    def __init__(self, PppoeBlockHandles=None, **kwargs):
        self._PppoeBlockHandles = PppoeBlockHandles  # PPPoE Protocol Configs

        properties = kwargs.copy()
        if PppoeBlockHandles is not None:
            properties['PppoeBlockHandles'] = PppoeBlockHandles

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeConnectCommand, self).__init__(**properties)

    @property
    def PppoeBlockHandles(self):
        """
        get the value of property _PppoeBlockHandles
        """
        return self._PppoeBlockHandles

    @PppoeBlockHandles.setter
    def PppoeBlockHandles(self, value):
        self._PppoeBlockHandles = value

    def _set_pppoeblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PppoeBlockHandles = tmp_value.split()

