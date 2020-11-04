"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Ospfv3GraceRestartCommand(ROMCommand):
    def __init__(self, Ospfv3Configs=None, **kwargs):
        self._Ospfv3Configs = Ospfv3Configs  # OSPFv3 Protocol Configs

        properties = kwargs.copy()
        if Ospfv3Configs is not None:
            properties['Ospfv3Configs'] = Ospfv3Configs

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3GraceRestartCommand, self).__init__(**properties)

    @property
    def Ospfv3Configs(self):
        """
        get the value of property _Ospfv3Configs
        """
        return self._Ospfv3Configs

    @Ospfv3Configs.setter
    def Ospfv3Configs(self, value):
        self._Ospfv3Configs = value

    def _set_ospfv3configs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ospfv3Configs = tmp_value.split()

