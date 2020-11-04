"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateStreamCommand(ROMCommand):
    def __init__(self, VtepConfigs=None, **kwargs):
        self._VtepConfigs = VtepConfigs  # VTEP Handles

        properties = kwargs.copy()
        if VtepConfigs is not None:
            properties['VtepConfigs'] = VtepConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(CreateStreamCommand, self).__init__(**properties)

    @property
    def VtepConfigs(self):
        """
        get the value of property _VtepConfigs
        """
        return self._VtepConfigs

    @VtepConfigs.setter
    def VtepConfigs(self, value):
        self._VtepConfigs = value

    def _set_vtepconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VtepConfigs = tmp_value.split()

