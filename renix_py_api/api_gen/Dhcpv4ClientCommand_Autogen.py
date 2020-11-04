"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dhcpv4ClientCommand(ROMCommand):
    def __init__(self, Dhcpv4Clients=None, **kwargs):
        self._Dhcpv4Clients = Dhcpv4Clients  # DHCPv4 Client Protocol Configs

        properties = kwargs.copy()
        if Dhcpv4Clients is not None:
            properties['Dhcpv4Clients'] = Dhcpv4Clients

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ClientCommand, self).__init__(**properties)

    @property
    def Dhcpv4Clients(self):
        """
        get the value of property _Dhcpv4Clients
        """
        return self._Dhcpv4Clients

    @Dhcpv4Clients.setter
    def Dhcpv4Clients(self, value):
        self._Dhcpv4Clients = value

    def _set_dhcpv4clients_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dhcpv4Clients = tmp_value.split()

