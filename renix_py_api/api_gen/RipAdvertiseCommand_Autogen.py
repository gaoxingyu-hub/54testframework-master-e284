"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class RipAdvertiseCommand(ROMCommand):
    def __init__(self, RipConfigs=None, **kwargs):
        self._RipConfigs = RipConfigs  # RIP Protocol Configs

        properties = kwargs.copy()
        if RipConfigs is not None:
            properties['RipConfigs'] = RipConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(RipAdvertiseCommand, self).__init__(**properties)

    @property
    def RipConfigs(self):
        """
        get the value of property _RipConfigs
        """
        return self._RipConfigs

    @RipConfigs.setter
    def RipConfigs(self, value):
        self._RipConfigs = value

    def _set_ripconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._RipConfigs = tmp_value.split()

