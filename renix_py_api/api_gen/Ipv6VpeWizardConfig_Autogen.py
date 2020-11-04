"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .MplsL3VpnWizardConfig_Autogen import MplsL3VpnWizardConfig


@rom_manager.rom
class Ipv6VpeWizardConfig(MplsL3VpnWizardConfig):
    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

