"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class L47VirtualProfile(ROMObject):
    def __init__(self, ProfileType=None, ProfileHandle=None, **kwargs):
        self._ProfileType = ProfileType  # Profile Type
        self._ProfileHandle = ProfileHandle  # Profile

        properties = kwargs.copy()
        if ProfileType is not None:
            properties['ProfileType'] = ProfileType
        if ProfileHandle is not None:
            properties['ProfileHandle'] = ProfileHandle

        # call base class function, and it will send message to renix server to create a class.
        super(L47VirtualProfile, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ProfileType=None, ProfileHandle=None, **kwargs):
        properties = kwargs.copy()
        if ProfileType is not None:
            self._ProfileType = ProfileType
            properties['ProfileType'] = ProfileType
        if ProfileHandle is not None:
            self._ProfileHandle = ProfileHandle
            properties['ProfileHandle'] = ProfileHandle

        super(L47VirtualProfile, self).edit(**properties)

    @property
    def ProfileType(self):
        """
        get the value of property _ProfileType
        """
        if self.force_auto_sync:
            self.get('ProfileType')
        return self._ProfileType

    @property
    def ProfileHandle(self):
        """
        get the value of property _ProfileHandle
        """
        if self.force_auto_sync:
            self.get('ProfileHandle')
        return self._ProfileHandle

    @ProfileType.setter
    def ProfileType(self, value):
        self._ProfileType = value
        self.edit(ProfileType=value)

    @ProfileHandle.setter
    def ProfileHandle(self, value):
        self._ProfileHandle = value
        self.edit(ProfileHandle=value)

    def _set_profiletype_with_str(self, value):
        self._ProfileType = value

    def _set_profilehandle_with_str(self, value):
        self._ProfileHandle = value

