"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LicenseFeatureInfo(ROMObject):
    def __init__(self, **kwargs):
        self._FeatureName = ''  # Feature Name, not editable
        self._ExpireDate = ''  # Expiration Date, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(LicenseFeatureInfo, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(LicenseFeatureInfo, self).edit(**properties)

    @property
    def FeatureName(self):
        """
        get the value of property _FeatureName
        """
        if self.force_auto_sync:
            self.get('FeatureName')
        return self._FeatureName

    @property
    def ExpireDate(self):
        """
        get the value of property _ExpireDate
        """
        if self.force_auto_sync:
            self.get('ExpireDate')
        return self._ExpireDate

    def _set_featurename_with_str(self, value):
        self._FeatureName = value

    def _set_expiredate_with_str(self, value):
        self._ExpireDate = value

