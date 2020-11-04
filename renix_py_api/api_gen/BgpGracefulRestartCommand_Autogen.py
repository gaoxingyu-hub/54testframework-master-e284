"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BgpGracefulRestartCommand(ROMCommand):
    def __init__(self, BgpSessionBlockHandles=None, **kwargs):
        self._BgpSessionBlockHandles = BgpSessionBlockHandles  # BGP Protocol Configs

        properties = kwargs.copy()
        if BgpSessionBlockHandles is not None:
            properties['BgpSessionBlockHandles'] = BgpSessionBlockHandles

        # call base class function, and it will send message to renix server to create a class.
        super(BgpGracefulRestartCommand, self).__init__(**properties)

    @property
    def BgpSessionBlockHandles(self):
        """
        get the value of property _BgpSessionBlockHandles
        """
        return self._BgpSessionBlockHandles

    @BgpSessionBlockHandles.setter
    def BgpSessionBlockHandles(self, value):
        self._BgpSessionBlockHandles = value

    def _set_bgpsessionblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BgpSessionBlockHandles = tmp_value.split()

