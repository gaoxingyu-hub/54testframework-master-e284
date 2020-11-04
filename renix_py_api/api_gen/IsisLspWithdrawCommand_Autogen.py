"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IsisLspWithdrawCommand(ROMCommand):
    def __init__(self, IsisLspConfigs=None, **kwargs):
        self._IsisLspConfigs = IsisLspConfigs  # IS-IS LSP Configs

        properties = kwargs.copy()
        if IsisLspConfigs is not None:
            properties['IsisLspConfigs'] = IsisLspConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(IsisLspWithdrawCommand, self).__init__(**properties)

    @property
    def IsisLspConfigs(self):
        """
        get the value of property _IsisLspConfigs
        """
        return self._IsisLspConfigs

    @IsisLspConfigs.setter
    def IsisLspConfigs(self, value):
        self._IsisLspConfigs = value

    def _set_isislspconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IsisLspConfigs = tmp_value.split()

