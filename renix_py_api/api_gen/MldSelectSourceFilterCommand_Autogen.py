"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class MldSelectSourceFilterCommand(ROMCommand):
    def __init__(self, MldMemberships=None, MldSourceFilter=None, **kwargs):
        self._MldMemberships = MldMemberships  # Memberships
        self._MldSourceFilter = MldSourceFilter  # Interfaces

        properties = kwargs.copy()
        if MldMemberships is not None:
            properties['MldMemberships'] = MldMemberships
        if MldSourceFilter is not None:
            properties['MldSourceFilter'] = MldSourceFilter

        # call base class function, and it will send message to renix server to create a class.
        super(MldSelectSourceFilterCommand, self).__init__(**properties)

    @property
    def MldMemberships(self):
        """
        get the value of property _MldMemberships
        """
        return self._MldMemberships

    @property
    def MldSourceFilter(self):
        """
        get the value of property _MldSourceFilter
        """
        return self._MldSourceFilter

    @MldMemberships.setter
    def MldMemberships(self, value):
        self._MldMemberships = value

    @MldSourceFilter.setter
    def MldSourceFilter(self, value):
        self._MldSourceFilter = value

    def _set_mldmemberships_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldMemberships = tmp_value.split()

    def _set_mldsourcefilter_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldSourceFilter = tmp_value.split()

