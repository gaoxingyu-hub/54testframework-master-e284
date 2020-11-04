"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ConfigureClockSyncCommand(ROMCommand):
    def __init__(self, ChassisHandles=None, **kwargs):
        self._ChassisHandles = ChassisHandles  # Chassis Handles

        properties = kwargs.copy()
        if ChassisHandles is not None:
            properties['ChassisHandles'] = ChassisHandles

        # call base class function, and it will send message to renix server to create a class.
        super(ConfigureClockSyncCommand, self).__init__(**properties)

    @property
    def ChassisHandles(self):
        """
        get the value of property _ChassisHandles
        """
        return self._ChassisHandles

    @ChassisHandles.setter
    def ChassisHandles(self, value):
        self._ChassisHandles = value

    def _set_chassishandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChassisHandles = tmp_value.split()

