"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class TrillStopCommand(ROMCommand):
    def __init__(self, TrillProtocolConfigs=None, **kwargs):
        self._TrillProtocolConfigs = TrillProtocolConfigs  # TRILL Protocol Configs

        properties = kwargs.copy()
        if TrillProtocolConfigs is not None:
            properties['TrillProtocolConfigs'] = TrillProtocolConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(TrillStopCommand, self).__init__(**properties)

    @property
    def TrillProtocolConfigs(self):
        """
        get the value of property _TrillProtocolConfigs
        """
        return self._TrillProtocolConfigs

    @TrillProtocolConfigs.setter
    def TrillProtocolConfigs(self, value):
        self._TrillProtocolConfigs = value

    def _set_trillprotocolconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._TrillProtocolConfigs = tmp_value.split()

