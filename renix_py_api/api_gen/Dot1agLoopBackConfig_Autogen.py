"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Dot1agCommandConfig_Autogen import Dot1agCommandConfig


@rom_manager.rom
class Dot1agLoopBackConfig(Dot1agCommandConfig):
    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

