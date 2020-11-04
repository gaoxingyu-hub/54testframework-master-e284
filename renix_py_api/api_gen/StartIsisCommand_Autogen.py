"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartIsisCommand(ROMCommand):
    def __init__(self, IsisConfigs=None, **kwargs):
        self._IsisConfigs = IsisConfigs  # IS-IS Protocol Configs

        properties = kwargs.copy()
        if IsisConfigs is not None:
            properties['IsisConfigs'] = IsisConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(StartIsisCommand, self).__init__(**properties)

    @property
    def IsisConfigs(self):
        """
        get the value of property _IsisConfigs
        """
        return self._IsisConfigs

    @IsisConfigs.setter
    def IsisConfigs(self, value):
        self._IsisConfigs = value

    def _set_isisconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IsisConfigs = tmp_value.split()

