"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dot3ahStartOrgSpecCommand(ROMCommand):
    def __init__(self, Dot3ahConfigs=None, **kwargs):
        self._Dot3ahConfigs = Dot3ahConfigs  # 802.3ah Protocol Configs

        properties = kwargs.copy()
        if Dot3ahConfigs is not None:
            properties['Dot3ahConfigs'] = Dot3ahConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(Dot3ahStartOrgSpecCommand, self).__init__(**properties)

    @property
    def Dot3ahConfigs(self):
        """
        get the value of property _Dot3ahConfigs
        """
        return self._Dot3ahConfigs

    @Dot3ahConfigs.setter
    def Dot3ahConfigs(self, value):
        self._Dot3ahConfigs = value

    def _set_dot3ahconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dot3ahConfigs = tmp_value.split()

