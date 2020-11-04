"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class LdpTerminateCommand(ROMCommand):
    def __init__(self, LdpConfigs=None, **kwargs):
        self._LdpConfigs = LdpConfigs  # LDP Protocol Configs

        properties = kwargs.copy()
        if LdpConfigs is not None:
            properties['LdpConfigs'] = LdpConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(LdpTerminateCommand, self).__init__(**properties)

    @property
    def LdpConfigs(self):
        """
        get the value of property _LdpConfigs
        """
        return self._LdpConfigs

    @LdpConfigs.setter
    def LdpConfigs(self, value):
        self._LdpConfigs = value

    def _set_ldpconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LdpConfigs = tmp_value.split()

