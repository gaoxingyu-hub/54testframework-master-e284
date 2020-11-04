"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Dot1agStopLoopBackCommand(ROMCommand):
    def __init__(self, Dot1agConfigs=None, **kwargs):
        self._Dot1agConfigs = Dot1agConfigs  # 802.1ag Protocol Configs

        properties = kwargs.copy()
        if Dot1agConfigs is not None:
            properties['Dot1agConfigs'] = Dot1agConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(Dot1agStopLoopBackCommand, self).__init__(**properties)

    @property
    def Dot1agConfigs(self):
        """
        get the value of property _Dot1agConfigs
        """
        return self._Dot1agConfigs

    @Dot1agConfigs.setter
    def Dot1agConfigs(self, value):
        self._Dot1agConfigs = value

    def _set_dot1agconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Dot1agConfigs = tmp_value.split()

