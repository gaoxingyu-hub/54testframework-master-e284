"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartVSwitchCommand(ROMCommand):
    def __init__(self, VSwitchConfigs=None, **kwargs):
        self._VSwitchConfigs = VSwitchConfigs  # Virtual Switch Handle List

        properties = kwargs.copy()
        if VSwitchConfigs is not None:
            properties['VSwitchConfigs'] = VSwitchConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(StartVSwitchCommand, self).__init__(**properties)

    @property
    def VSwitchConfigs(self):
        """
        get the value of property _VSwitchConfigs
        """
        return self._VSwitchConfigs

    @VSwitchConfigs.setter
    def VSwitchConfigs(self, value):
        self._VSwitchConfigs = value

    def _set_vswitchconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._VSwitchConfigs = tmp_value.split()

