"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dhcpv6ServerCommand(ROMCommand):
    def __init__(self, Dhcpv6Servers=None, **kwargs):
        self._Dhcpv6Servers = Dhcpv6Servers  # DHCPv6/PD Server Protocol Configs

        properties = kwargs.copy()
        if Dhcpv6Servers is not None:
            properties['Dhcpv6Servers'] = Dhcpv6Servers

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ServerCommand, self).__init__(**properties)

    @property
    def Dhcpv6Servers(self):
        """
        get the value of property _Dhcpv6Servers
        """
        return self._Dhcpv6Servers

    @Dhcpv6Servers.setter
    def Dhcpv6Servers(self, value):
        self._Dhcpv6Servers = value

    def _set_dhcpv6servers_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dhcpv6Servers = tmp_value.split()

