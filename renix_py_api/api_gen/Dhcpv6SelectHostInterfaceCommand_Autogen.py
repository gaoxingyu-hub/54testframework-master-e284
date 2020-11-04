"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dhcpv6SelectHostInterfaceCommand(ROMCommand):
    def __init__(self, Dhcpv6Clients=None, InterfaceHandles=None, **kwargs):
        self._Dhcpv6Clients = Dhcpv6Clients  # Dhcpv6 Protocol Configs
        self._InterfaceHandles = InterfaceHandles  # Interfaces

        properties = kwargs.copy()
        if Dhcpv6Clients is not None:
            properties['Dhcpv6Clients'] = Dhcpv6Clients
        if InterfaceHandles is not None:
            properties['InterfaceHandles'] = InterfaceHandles

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6SelectHostInterfaceCommand, self).__init__(**properties)

    @property
    def Dhcpv6Clients(self):
        """
        get the value of property _Dhcpv6Clients
        """
        return self._Dhcpv6Clients

    @property
    def InterfaceHandles(self):
        """
        get the value of property _InterfaceHandles
        """
        return self._InterfaceHandles

    @Dhcpv6Clients.setter
    def Dhcpv6Clients(self, value):
        self._Dhcpv6Clients = value

    @InterfaceHandles.setter
    def InterfaceHandles(self, value):
        self._InterfaceHandles = value

    def _set_dhcpv6clients_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dhcpv6Clients = tmp_value.split()

    def _set_interfacehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceHandles = tmp_value.split()

