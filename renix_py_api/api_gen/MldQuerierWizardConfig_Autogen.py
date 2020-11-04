"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class MldQuerierWizardConfig(ProtocolWizardConfig):
    def __init__(self, Version=None, **kwargs):
        self._Version = Version  # Version

        properties = kwargs.copy()
        if Version is not None:
            properties['Version'] = Version

        # call base class function, and it will send message to renix server to create a class.
        super(MldQuerierWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Version=None, **kwargs):
        properties = kwargs.copy()
        if Version is not None:
            self._Version = Version
            properties['Version'] = Version

        super(MldQuerierWizardConfig, self).edit(**properties)

    @property
    def Version(self):
        """
        get the value of property _Version
        """
        if self.force_auto_sync:
            self.get('Version')
        return self._Version

    @Version.setter
    def Version(self, value):
        self._Version = value
        self.edit(Version=value)

    def _set_version_with_str(self, value):
        seperate = value.find(':')
        exec('self._Version = EnumMldQuerierVersion.%s' % value[:seperate])

