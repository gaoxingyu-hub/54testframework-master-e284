"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StopIpv6PingCommand(ROMCommand):
    def __init__(self, InterfaceHandle=None, **kwargs):
        self._InterfaceHandle = InterfaceHandle  # Ping Interface

        properties = kwargs.copy()
        if InterfaceHandle is not None:
            properties['InterfaceHandle'] = InterfaceHandle

        # call base class function, and it will send message to renix server to create a class.
        super(StopIpv6PingCommand, self).__init__(**properties)

    @property
    def InterfaceHandle(self):
        """
        get the value of property _InterfaceHandle
        """
        return self._InterfaceHandle

    @InterfaceHandle.setter
    def InterfaceHandle(self, value):
        self._InterfaceHandle = value

    def _set_interfacehandle_with_str(self, value):
        self._InterfaceHandle = value

