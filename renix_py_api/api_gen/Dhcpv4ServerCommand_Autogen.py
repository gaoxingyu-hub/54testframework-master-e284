"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dhcpv4ServerCommand(ROMCommand):
    def __init__(self, Dhcpv4Servers=None, **kwargs):
        self._Dhcpv4Servers = Dhcpv4Servers  # DHCPv4 Server Protocol Configs

        properties = kwargs.copy()
        if Dhcpv4Servers is not None:
            properties['Dhcpv4Servers'] = Dhcpv4Servers

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerCommand, self).__init__(**properties)

    @property
    def Dhcpv4Servers(self):
        """
        get the value of property _Dhcpv4Servers
        """
        return self._Dhcpv4Servers

    @Dhcpv4Servers.setter
    def Dhcpv4Servers(self, value):
        self._Dhcpv4Servers = value

    def _set_dhcpv4servers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dhcpv4Servers = tmp_value.split()

