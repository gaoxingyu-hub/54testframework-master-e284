"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ShutdownHardwareCommand(ROMCommand):
    def __init__(self, HardwareList=None, **kwargs):
        self._HardwareList = HardwareList  # Hardware Handles

        properties = kwargs.copy()
        if HardwareList is not None:
            properties['HardwareList'] = HardwareList

        # call base class function, and it will send message to renix server to create a class.
        super(ShutdownHardwareCommand, self).__init__(**properties)

    @property
    def HardwareList(self):
        """
        get the value of property _HardwareList
        """
        return self._HardwareList

    @HardwareList.setter
    def HardwareList(self, value):
        self._HardwareList = value

    def _set_hardwarelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HardwareList = tmp_value.split()

