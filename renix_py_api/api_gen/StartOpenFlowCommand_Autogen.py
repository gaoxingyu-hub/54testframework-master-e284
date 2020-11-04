"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartOpenFlowCommand(ROMCommand):
    def __init__(self, OpenFlowConfigs=None, **kwargs):
        self._OpenFlowConfigs = OpenFlowConfigs  # OpenFlow Handle List

        properties = kwargs.copy()
        if OpenFlowConfigs is not None:
            properties['OpenFlowConfigs'] = OpenFlowConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(StartOpenFlowCommand, self).__init__(**properties)

    @property
    def OpenFlowConfigs(self):
        """
        get the value of property _OpenFlowConfigs
        """
        return self._OpenFlowConfigs

    @OpenFlowConfigs.setter
    def OpenFlowConfigs(self, value):
        self._OpenFlowConfigs = value

    def _set_openflowconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._OpenFlowConfigs = tmp_value.split()

