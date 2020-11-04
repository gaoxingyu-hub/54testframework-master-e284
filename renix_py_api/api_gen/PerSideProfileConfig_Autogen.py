"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .StaticLoadProfileConfig_Autogen import StaticLoadProfileConfig


@rom_manager.rom
class PerSideProfileConfig(StaticLoadProfileConfig):
    def __init__(self, ProfileName=None, **kwargs):
        self._ProfileSide = EnumProfileSide.DOWN_STREAM  # Side, not editable
        self._ProfileName = ProfileName  # Side

        properties = kwargs.copy()
        if ProfileName is not None:
            properties['ProfileName'] = ProfileName

        # call base class function, and it will send message to renix server to create a class.
        super(PerSideProfileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ProfileName=None, **kwargs):
        properties = kwargs.copy()
        if ProfileName is not None:
            self._ProfileName = ProfileName
            properties['ProfileName'] = ProfileName

        super(PerSideProfileConfig, self).edit(**properties)

    @property
    def ProfileSide(self):
        """
        get the value of property _ProfileSide
        """
        if self.force_auto_sync:
            self.get('ProfileSide')
        return self._ProfileSide

    @property
    def ProfileName(self):
        """
        get the value of property _ProfileName
        """
        if self.force_auto_sync:
            self.get('ProfileName')
        return self._ProfileName

    @ProfileName.setter
    def ProfileName(self, value):
        self._ProfileName = value
        self.edit(ProfileName=value)

    def _set_profileside_with_str(self, value):
        seperate = value.find(':')
        exec('self._ProfileSide = EnumProfileSide.%s' % value[:seperate])

    def _set_profilename_with_str(self, value):
        self._ProfileName = value

