"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetConnectedClCommand(ROMCommand):
    def __init__(self, **kwargs):
        self._ClListenPort = None  # Renix Server Listen Port, not editable
        self._TimeStamp = None  # Last Renix connection time, not editable
        self._MaxServiceCount = 2  # Max server count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(GetConnectedClCommand, self).__init__(**properties)

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

    @property
    def MaxServiceCount(self):
        """
        get the value of property _MaxServiceCount
        """
        return self._MaxServiceCount

    def _set_cllistenport_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ClListenPort = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._ClListenPort.append(int(str_value))
            except ValueError:
                self._ClListenPort.append(hex(int(str_value, 16)))

    def _set_timestamp_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TimeStamp = tmp_value.split()

    def _set_maxservicecount_with_str(self, value):
        try:
            self._MaxServiceCount = int(value)
        except ValueError:
            self._MaxServiceCount = hex(int(value, 16))

