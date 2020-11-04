"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BfdCommand_Autogen import BfdCommand


@rom_manager.rom
class BfdResumePDUsCommand(BfdCommand):
    def __init__(self, BfdProtocolConfigs=None, **kwargs):
        self._BfdProtocolConfigs = BfdProtocolConfigs  # BFD Protocol Configs

        properties = kwargs.copy()
        if BfdProtocolConfigs is not None:
            properties['BfdProtocolConfigs'] = BfdProtocolConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(BfdResumePDUsCommand, self).__init__(**properties)

    @property
    def BfdProtocolConfigs(self):
        """
        get the value of property _BfdProtocolConfigs
        """
        return self._BfdProtocolConfigs

    @BfdProtocolConfigs.setter
    def BfdProtocolConfigs(self, value):
        self._BfdProtocolConfigs = value

    def _set_bfdprotocolconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BfdProtocolConfigs = tmp_value.split()

