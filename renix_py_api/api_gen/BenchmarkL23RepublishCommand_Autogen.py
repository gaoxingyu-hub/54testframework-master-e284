"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BenchmarkL23RepublishCommand(ROMCommand):
    def __init__(self, CommandHandle=None, **kwargs):
        self._CommandHandle = CommandHandle  # Engine Command Handle

        properties = kwargs.copy()
        if CommandHandle is not None:
            properties['CommandHandle'] = CommandHandle

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkL23RepublishCommand, self).__init__(**properties)

    @property
    def CommandHandle(self):
        """
        get the value of property _CommandHandle
        """
        return self._CommandHandle

    @CommandHandle.setter
    def CommandHandle(self, value):
        self._CommandHandle = value

    def _set_commandhandle_with_str(self, value):
        self._CommandHandle = value

