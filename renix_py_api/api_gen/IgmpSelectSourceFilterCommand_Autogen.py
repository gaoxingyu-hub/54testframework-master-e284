"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IgmpSelectSourceFilterCommand(ROMCommand):
    def __init__(self, IgmpMemberships=None, IgmpSourceFilter=None, **kwargs):
        self._IgmpMemberships = IgmpMemberships  # Memberships
        self._IgmpSourceFilter = IgmpSourceFilter  # Interfaces

        properties = kwargs.copy()
        if IgmpMemberships is not None:
            properties['IgmpMemberships'] = IgmpMemberships
        if IgmpSourceFilter is not None:
            properties['IgmpSourceFilter'] = IgmpSourceFilter

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpSelectSourceFilterCommand, self).__init__(**properties)

    @property
    def IgmpMemberships(self):
        """
        get the value of property _IgmpMemberships
        """
        return self._IgmpMemberships

    @property
    def IgmpSourceFilter(self):
        """
        get the value of property _IgmpSourceFilter
        """
        return self._IgmpSourceFilter

    @IgmpMemberships.setter
    def IgmpMemberships(self, value):
        self._IgmpMemberships = value

    @IgmpSourceFilter.setter
    def IgmpSourceFilter(self, value):
        self._IgmpSourceFilter = value

    def _set_igmpmemberships_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpMemberships = tmp_value.split()

    def _set_igmpsourcefilter_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpSourceFilter = tmp_value.split()

