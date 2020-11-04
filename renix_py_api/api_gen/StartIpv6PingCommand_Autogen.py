"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PingCommand_Autogen import PingCommand


@rom_manager.rom
class StartIpv6PingCommand(PingCommand):
    def __init__(self, CustomIP=None, **kwargs):
        self._CustomIP = CustomIP  # Custom IP

        properties = kwargs.copy()
        if CustomIP is not None:
            properties['CustomIP'] = CustomIP

        # call base class function, and it will send message to renix server to create a class.
        super(StartIpv6PingCommand, self).__init__(**properties)

    @property
    def CustomIP(self):
        """
        get the value of property _CustomIP
        """
        return self._CustomIP

    @CustomIP.setter
    def CustomIP(self, value):
        self._CustomIP = value

    def _set_customip_with_str(self, value):
        self._CustomIP = value

