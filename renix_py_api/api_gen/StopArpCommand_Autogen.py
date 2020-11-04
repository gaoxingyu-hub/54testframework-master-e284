"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StopArpCommand(ROMCommand):
    def __init__(self, InterfaceConfigs=None, **kwargs):
        self._InterfaceConfigs = InterfaceConfigs  # Interfaces

        properties = kwargs.copy()
        if InterfaceConfigs is not None:
            properties['InterfaceConfigs'] = InterfaceConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(StopArpCommand, self).__init__(**properties)

    @property
    def InterfaceConfigs(self):
        """
        get the value of property _InterfaceConfigs
        """
        return self._InterfaceConfigs

    @InterfaceConfigs.setter
    def InterfaceConfigs(self, value):
        self._InterfaceConfigs = value

    def _set_interfaceconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InterfaceConfigs = tmp_value.split()

