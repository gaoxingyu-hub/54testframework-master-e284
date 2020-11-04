"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Ospfv3WithdrawCommand(ROMCommand):
    def __init__(self, Ospfv3LsaConfigs=None, **kwargs):
        self._Ospfv3LsaConfigs = Ospfv3LsaConfigs  # OSPFv3 LSA Configs

        properties = kwargs.copy()
        if Ospfv3LsaConfigs is not None:
            properties['Ospfv3LsaConfigs'] = Ospfv3LsaConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3WithdrawCommand, self).__init__(**properties)

    @property
    def Ospfv3LsaConfigs(self):
        """
        get the value of property _Ospfv3LsaConfigs
        """
        return self._Ospfv3LsaConfigs

    @Ospfv3LsaConfigs.setter
    def Ospfv3LsaConfigs(self, value):
        self._Ospfv3LsaConfigs = value

    def _set_ospfv3lsaconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ospfv3LsaConfigs = tmp_value.split()

