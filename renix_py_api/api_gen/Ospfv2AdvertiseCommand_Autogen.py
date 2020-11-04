"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class Ospfv2AdvertiseCommand(ROMCommand):
    def __init__(self, Ospfv2LsaConfigs=None, **kwargs):
        self._Ospfv2LsaConfigs = Ospfv2LsaConfigs  # OSPFv2 LSA Configs

        properties = kwargs.copy()
        if Ospfv2LsaConfigs is not None:
            properties['Ospfv2LsaConfigs'] = Ospfv2LsaConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2AdvertiseCommand, self).__init__(**properties)

    @property
    def Ospfv2LsaConfigs(self):
        """
        get the value of property _Ospfv2LsaConfigs
        """
        return self._Ospfv2LsaConfigs

    @Ospfv2LsaConfigs.setter
    def Ospfv2LsaConfigs(self, value):
        self._Ospfv2LsaConfigs = value

    def _set_ospfv2lsaconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Ospfv2LsaConfigs = tmp_value.split()

