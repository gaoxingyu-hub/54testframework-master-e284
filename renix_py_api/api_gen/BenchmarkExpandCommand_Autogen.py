"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BenchmarkExpandCommand(ROMCommand):
    def __init__(self, ConfigHandle=None, **kwargs):
        self._ConfigHandle = ConfigHandle  # Config Handle

        properties = kwargs.copy()
        if ConfigHandle is not None:
            properties['ConfigHandle'] = ConfigHandle

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkExpandCommand, self).__init__(**properties)

    @property
    def ConfigHandle(self):
        """
        get the value of property _ConfigHandle
        """
        return self._ConfigHandle

    @ConfigHandle.setter
    def ConfigHandle(self, value):
        self._ConfigHandle = value

    def _set_confighandle_with_str(self, value):
        self._ConfigHandle = value

