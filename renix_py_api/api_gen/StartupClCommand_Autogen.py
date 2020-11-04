"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartupClCommand(ROMCommand):
    def __init__(self, **kwargs):
        self._ClListenPort = 9001  # Renix Server Listen Port, not editable
        self._TimeStamp = ''  # Renix start time, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(StartupClCommand, self).__init__(**properties)

    @property
    def ClListenPort(self):
        """
        get the value of property _ClListenPort
        """
        return self._ClListenPort

    @property
    def TimeStamp(self):
        """
        get the value of property _TimeStamp
        """
        return self._TimeStamp

    def _set_cllistenport_with_str(self, value):
        try:
            self._ClListenPort = int(value)
        except ValueError:
            self._ClListenPort = hex(int(value, 16))

    def _set_timestamp_with_str(self, value):
        self._TimeStamp = value

