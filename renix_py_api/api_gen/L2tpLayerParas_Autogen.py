"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .NetworkLayerParas_Autogen import NetworkLayerParas


@rom_manager.rom
class L2tpLayerParas(NetworkLayerParas):
    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

