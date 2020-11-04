"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class MldSendReportCommand(ROMCommand):
    def __init__(self, MldConfigs=None, **kwargs):
        self._MldConfigs = MldConfigs  # MLD Protocol Configs

        properties = kwargs.copy()
        if MldConfigs is not None:
            properties['MldConfigs'] = MldConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(MldSendReportCommand, self).__init__(**properties)

    @property
    def MldConfigs(self):
        """
        get the value of property _MldConfigs
        """
        return self._MldConfigs

    @MldConfigs.setter
    def MldConfigs(self, value):
        self._MldConfigs = value

    def _set_mldconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldConfigs = tmp_value.split()

