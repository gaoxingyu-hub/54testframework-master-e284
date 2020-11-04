"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Ospfv2GraceRestartCommand(ROMCommand):
    def __init__(self, Ospfv2Configs=None, **kwargs):
        self._Ospfv2Configs = Ospfv2Configs  # OSPFv2 Protocol Configs

        properties = kwargs.copy()
        if Ospfv2Configs is not None:
            properties['Ospfv2Configs'] = Ospfv2Configs

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2GraceRestartCommand, self).__init__(**properties)

    @property
    def Ospfv2Configs(self):
        """
        get the value of property _Ospfv2Configs
        """
        return self._Ospfv2Configs

    @Ospfv2Configs.setter
    def Ospfv2Configs(self, value):
        self._Ospfv2Configs = value

    def _set_ospfv2configs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ospfv2Configs = tmp_value.split()

