"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class MldSelectMulticastGroupCommand(ROMCommand):
    def __init__(self, MldMemberships=None, MldMulticastGroup=None, **kwargs):
        self._MldMemberships = MldMemberships  # Memberships
        self._MldMulticastGroup = MldMulticastGroup  # Multi-cast Group

        properties = kwargs.copy()
        if MldMemberships is not None:
            properties['MldMemberships'] = MldMemberships
        if MldMulticastGroup is not None:
            properties['MldMulticastGroup'] = MldMulticastGroup

        # call base class function, and it will send message to renix server to create a class.
        super(MldSelectMulticastGroupCommand, self).__init__(**properties)

    @property
    def MldMemberships(self):
        """
        get the value of property _MldMemberships
        """
        return self._MldMemberships

    @property
    def MldMulticastGroup(self):
        """
        get the value of property _MldMulticastGroup
        """
        return self._MldMulticastGroup

    @MldMemberships.setter
    def MldMemberships(self, value):
        self._MldMemberships = value

    @MldMulticastGroup.setter
    def MldMulticastGroup(self, value):
        self._MldMulticastGroup = value

    def _set_mldmemberships_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldMemberships = tmp_value.split()

    def _set_mldmulticastgroup_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._MldMulticastGroup = tmp_value.split()

