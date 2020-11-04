"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Ipv4Route_Autogen import Ipv4Route


@rom_manager.rom
class BgpSummaryIpv4Route(Ipv4Route):
    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

