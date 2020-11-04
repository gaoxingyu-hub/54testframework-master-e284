"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PppoeChangeModeCommand(ROMCommand):
    def __init__(self, PppoeBlockHandles=None, EmulationMode=None, **kwargs):
        self._PppoeBlockHandles = PppoeBlockHandles  # PPPoE Protocol Configs
        self._EmulationMode = EmulationMode  # Emulation Mode

        properties = kwargs.copy()
        if PppoeBlockHandles is not None:
            properties['PppoeBlockHandles'] = PppoeBlockHandles
        if EmulationMode is not None:
            properties['EmulationMode'] = EmulationMode

        # call base class function, and it will send message to renix server to create a class.
        super(PppoeChangeModeCommand, self).__init__(**properties)

    @property
    def PppoeBlockHandles(self):
        """
        get the value of property _PppoeBlockHandles
        """
        return self._PppoeBlockHandles

    @property
    def EmulationMode(self):
        """
        get the value of property _EmulationMode
        """
        return self._EmulationMode

    @PppoeBlockHandles.setter
    def PppoeBlockHandles(self, value):
        self._PppoeBlockHandles = value

    @EmulationMode.setter
    def EmulationMode(self, value):
        self._EmulationMode = value

    def _set_pppoeblockhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PppoeBlockHandles = tmp_value.split()

    def _set_emulationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._EmulationMode = EnumPppoeMode.%s' % value[:seperate])

