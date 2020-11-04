"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PingCommand_Autogen import PingCommand


@rom_manager.rom
class VxlanPingCommand(PingCommand):
    def __init__(self, InterfaceHandles=None, **kwargs):
        self._InterfaceHandles = InterfaceHandles  # Ping Interface

        properties = kwargs.copy()
        if InterfaceHandles is not None:
            properties['InterfaceHandles'] = InterfaceHandles

        # call base class function, and it will send message to renix server to create a class.
        super(VxlanPingCommand, self).__init__(**properties)

    @property
    def InterfaceHandles(self):
        """
        get the value of property _InterfaceHandles
        """
        return self._InterfaceHandles

    @InterfaceHandles.setter
    def InterfaceHandles(self, value):
        self._InterfaceHandles = value

    def _set_interfacehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceHandles = tmp_value.split()

