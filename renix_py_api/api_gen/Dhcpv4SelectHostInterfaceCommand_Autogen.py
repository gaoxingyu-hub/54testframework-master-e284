"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dhcpv4SelectHostInterfaceCommand(ROMCommand):
    def __init__(self, Dhcpv4Clients=None, InterfaceHandles=None, **kwargs):
        self._Dhcpv4Clients = Dhcpv4Clients  # Dhcpv4 Protocol Configs
        self._InterfaceHandles = InterfaceHandles  # Interfaces

        properties = kwargs.copy()
        if Dhcpv4Clients is not None:
            properties['Dhcpv4Clients'] = Dhcpv4Clients
        if InterfaceHandles is not None:
            properties['InterfaceHandles'] = InterfaceHandles

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4SelectHostInterfaceCommand, self).__init__(**properties)

    @property
    def Dhcpv4Clients(self):
        """
        get the value of property _Dhcpv4Clients
        """
        return self._Dhcpv4Clients

    @property
    def InterfaceHandles(self):
        """
        get the value of property _InterfaceHandles
        """
        return self._InterfaceHandles

    @Dhcpv4Clients.setter
    def Dhcpv4Clients(self, value):
        self._Dhcpv4Clients = value

    @InterfaceHandles.setter
    def InterfaceHandles(self, value):
        self._InterfaceHandles = value

    def _set_dhcpv4clients_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dhcpv4Clients = tmp_value.split()

    def _set_interfacehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceHandles = tmp_value.split()

