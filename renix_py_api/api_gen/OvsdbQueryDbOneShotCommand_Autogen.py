"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .OvsdbQueryDbCommand_Autogen import OvsdbQueryDbCommand


@rom_manager.rom
class OvsdbQueryDbOneShotCommand(OvsdbQueryDbCommand):
    def __init__(self, OvsdbHandles=None, **kwargs):
        self._OvsdbHandles = OvsdbHandles  # OVSDB Protocol Config

        properties = kwargs.copy()
        if OvsdbHandles is not None:
            properties['OvsdbHandles'] = OvsdbHandles

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbQueryDbOneShotCommand, self).__init__(**properties)

    @property
    def OvsdbHandles(self):
        """
        get the value of property _OvsdbHandles
        """
        return self._OvsdbHandles

    @OvsdbHandles.setter
    def OvsdbHandles(self, value):
        self._OvsdbHandles = value

    def _set_ovsdbhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OvsdbHandles = tmp_value.split()

