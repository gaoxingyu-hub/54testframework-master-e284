"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetOMInfoCommand(ROMCommand):
    def __init__(self, PortHandle=None, **kwargs):
        self._PortHandle = PortHandle  # Port Handles

        properties = kwargs.copy()
        if PortHandle is not None:
            properties['PortHandle'] = PortHandle

        # call base class function, and it will send message to renix server to create a class.
        super(GetOMInfoCommand, self).__init__(**properties)

    @property
    def PortHandle(self):
        """
        get the value of property _PortHandle
        """
        return self._PortHandle

    @PortHandle.setter
    def PortHandle(self, value):
        self._PortHandle = value

    def _set_porthandle_with_str(self, value):
        self._PortHandle = value

