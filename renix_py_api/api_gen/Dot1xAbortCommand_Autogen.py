"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dot1xAbortCommand(ROMCommand):
    def __init__(self, Dot1xConfigs=None, **kwargs):
        self._Dot1xConfigs = Dot1xConfigs  # 802.1x Client Protocol Configs

        properties = kwargs.copy()
        if Dot1xConfigs is not None:
            properties['Dot1xConfigs'] = Dot1xConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1xAbortCommand, self).__init__(**properties)

    @property
    def Dot1xConfigs(self):
        """
        get the value of property _Dot1xConfigs
        """
        return self._Dot1xConfigs

    @Dot1xConfigs.setter
    def Dot1xConfigs(self, value):
        self._Dot1xConfigs = value

    def _set_dot1xconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dot1xConfigs = tmp_value.split()

