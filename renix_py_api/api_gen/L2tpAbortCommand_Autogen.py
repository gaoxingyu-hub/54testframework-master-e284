"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class L2tpAbortCommand(ROMCommand):
    def __init__(self, L2tpBlockHandles=None, **kwargs):
        self._L2tpBlockHandles = L2tpBlockHandles  # L2TP Block Protocol Configs

        properties = kwargs.copy()
        if L2tpBlockHandles is not None:
            properties['L2tpBlockHandles'] = L2tpBlockHandles

        # call base class function, and it will send message to renix server to create a class.
        super(L2tpAbortCommand, self).__init__(**properties)

    @property
    def L2tpBlockHandles(self):
        """
        get the value of property _L2tpBlockHandles
        """
        return self._L2tpBlockHandles

    @L2tpBlockHandles.setter
    def L2tpBlockHandles(self, value):
        self._L2tpBlockHandles = value

    def _set_l2tpblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._L2tpBlockHandles = tmp_value.split()

