"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class TrafficItemGroup(ROMObject):
    def __init__(self, GroupName=None, **kwargs):
        self._GroupName = GroupName  # Group Name

        properties = kwargs.copy()
        if GroupName is not None:
            properties['GroupName'] = GroupName

        # call base class function, and it will send message to renix server to create a class.
        super(TrafficItemGroup, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, GroupName=None, **kwargs):
        properties = kwargs.copy()
        if GroupName is not None:
            self._GroupName = GroupName
            properties['GroupName'] = GroupName

        super(TrafficItemGroup, self).edit(**properties)

    @property
    def GroupName(self):
        """
        get the value of property _GroupName
        """
        if self.force_auto_sync:
            self.get('GroupName')
        return self._GroupName

    @GroupName.setter
    def GroupName(self, value):
        self._GroupName = value
        self.edit(GroupName=value)

    def _set_groupname_with_str(self, value):
        self._GroupName = value

