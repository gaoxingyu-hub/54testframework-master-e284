"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class LdpAdvertiseLspCommand(ROMCommand):
    def __init__(self, LspConfigs=None, **kwargs):
        self._LspConfigs = LspConfigs  # LSP Handle List

        properties = kwargs.copy()
        if LspConfigs is not None:
            properties['LspConfigs'] = LspConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(LdpAdvertiseLspCommand, self).__init__(**properties)

    @property
    def LspConfigs(self):
        """
        get the value of property _LspConfigs
        """
        return self._LspConfigs

    @LspConfigs.setter
    def LspConfigs(self, value):
        self._LspConfigs = value

    def _set_lspconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LspConfigs = tmp_value.split()

