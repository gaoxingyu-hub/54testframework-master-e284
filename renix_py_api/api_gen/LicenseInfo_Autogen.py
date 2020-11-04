"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class LicenseInfo(ROMObject):
    def __init__(self, **kwargs):
        self._Info = ''  # License Information, not editable
        self._LicenseFileName = ''  # License File Name, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(LicenseInfo, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(LicenseInfo, self).edit(**properties)

    @property
    def Info(self):
        """
        get the value of property _Info
        """
        if self.force_auto_sync:
            self.get('Info')
        return self._Info

    @property
    def LicenseFileName(self):
        """
        get the value of property _LicenseFileName
        """
        if self.force_auto_sync:
            self.get('LicenseFileName')
        return self._LicenseFileName

    def _set_info_with_str(self, value):
        self._Info = value

    def _set_licensefilename_with_str(self, value):
        self._LicenseFileName = value

