"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PimCommand_Autogen import PimCommand


@rom_manager.rom
class PimStartBootStrapCommand(PimCommand):
    def __init__(self, PimConfigs=None, **kwargs):
        self._PimConfigs = PimConfigs  # Pim Protocol Configs

        properties = kwargs.copy()
        if PimConfigs is not None:
            properties['PimConfigs'] = PimConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(PimStartBootStrapCommand, self).__init__(**properties)

    @property
    def PimConfigs(self):
        """
        get the value of property _PimConfigs
        """
        return self._PimConfigs

    @PimConfigs.setter
    def PimConfigs(self, value):
        self._PimConfigs = value

    def _set_pimconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PimConfigs = tmp_value.split()

