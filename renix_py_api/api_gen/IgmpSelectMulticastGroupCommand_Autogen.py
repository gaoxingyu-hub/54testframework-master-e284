"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IgmpSelectMulticastGroupCommand(ROMCommand):
    def __init__(self, IgmpMemberships=None, IgmpMulticastGroup=None, **kwargs):
        self._IgmpMemberships = IgmpMemberships  # Memberships
        self._IgmpMulticastGroup = IgmpMulticastGroup  # Multi-cast Group

        properties = kwargs.copy()
        if IgmpMemberships is not None:
            properties['IgmpMemberships'] = IgmpMemberships
        if IgmpMulticastGroup is not None:
            properties['IgmpMulticastGroup'] = IgmpMulticastGroup

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpSelectMulticastGroupCommand, self).__init__(**properties)

    @property
    def IgmpMemberships(self):
        """
        get the value of property _IgmpMemberships
        """
        return self._IgmpMemberships

    @property
    def IgmpMulticastGroup(self):
        """
        get the value of property _IgmpMulticastGroup
        """
        return self._IgmpMulticastGroup

    @IgmpMemberships.setter
    def IgmpMemberships(self, value):
        self._IgmpMemberships = value

    @IgmpMulticastGroup.setter
    def IgmpMulticastGroup(self, value):
        self._IgmpMulticastGroup = value

    def _set_igmpmemberships_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpMemberships = tmp_value.split()

    def _set_igmpmulticastgroup_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IgmpMulticastGroup = tmp_value.split()

