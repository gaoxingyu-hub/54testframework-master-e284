"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IgmpSendLeaveCommand(ROMCommand):
    def __init__(self, IgmpConfigs=None, **kwargs):
        self._IgmpConfigs = IgmpConfigs  # IGMP Protocol Configs

        properties = kwargs.copy()
        if IgmpConfigs is not None:
            properties['IgmpConfigs'] = IgmpConfigs

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpSendLeaveCommand, self).__init__(**properties)

    @property
    def IgmpConfigs(self):
        """
        get the value of property _IgmpConfigs
        """
        return self._IgmpConfigs

    @IgmpConfigs.setter
    def IgmpConfigs(self, value):
        self._IgmpConfigs = value

    def _set_igmpconfigs_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpConfigs = tmp_value.split()

