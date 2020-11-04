"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SysEntry(ROMObject):
    def __init__(self, TestCaseName=None, EnableDebug=None, ProductNameSuffix=None, **kwargs):
        self._Version = '3.0.0.999999'  # Version, not editable
        self._VersionType = ''  # Version, not editable
        self._TestCaseName = TestCaseName  # Test Case Name
        self._EnableDebug = EnableDebug  # Enable Debug
        self._ProductNameSuffix = ProductNameSuffix  # Product Name Suffix

        properties = kwargs.copy()
        if TestCaseName is not None:
            properties['TestCaseName'] = TestCaseName
        if EnableDebug is not None:
            properties['EnableDebug'] = EnableDebug
        if ProductNameSuffix is not None:
            properties['ProductNameSuffix'] = ProductNameSuffix

        # call base class function, and it will send message to renix server to create a class.
        super(SysEntry, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, TestCaseName=None, EnableDebug=None, ProductNameSuffix=None, **kwargs):
        properties = kwargs.copy()
        if TestCaseName is not None:
            self._TestCaseName = TestCaseName
            properties['TestCaseName'] = TestCaseName
        if EnableDebug is not None:
            self._EnableDebug = EnableDebug
            properties['EnableDebug'] = EnableDebug
        if ProductNameSuffix is not None:
            self._ProductNameSuffix = ProductNameSuffix
            properties['ProductNameSuffix'] = ProductNameSuffix

        super(SysEntry, self).edit(**properties)

    @property
    def Version(self):
        """
        get the value of property _Version
        """
        if self.force_auto_sync:
            self.get('Version')
        return self._Version

    @property
    def VersionType(self):
        """
        get the value of property _VersionType
        """
        if self.force_auto_sync:
            self.get('VersionType')
        return self._VersionType

    @property
    def TestCaseName(self):
        """
        get the value of property _TestCaseName
        """
        if self.force_auto_sync:
            self.get('TestCaseName')
        return self._TestCaseName

    @property
    def EnableDebug(self):
        """
        get the value of property _EnableDebug
        """
        if self.force_auto_sync:
            self.get('EnableDebug')
        return self._EnableDebug

    @property
    def ProductNameSuffix(self):
        """
        get the value of property _ProductNameSuffix
        """
        if self.force_auto_sync:
            self.get('ProductNameSuffix')
        return self._ProductNameSuffix

    @TestCaseName.setter
    def TestCaseName(self, value):
        self._TestCaseName = value
        self.edit(TestCaseName=value)

    @EnableDebug.setter
    def EnableDebug(self, value):
        self._EnableDebug = value
        self.edit(EnableDebug=value)

    @ProductNameSuffix.setter
    def ProductNameSuffix(self, value):
        self._ProductNameSuffix = value
        self.edit(ProductNameSuffix=value)

    def _set_version_with_str(self, value):
        self._Version = value

    def _set_versiontype_with_str(self, value):
        self._VersionType = value

    def _set_testcasename_with_str(self, value):
        self._TestCaseName = value

    def _set_enabledebug_with_str(self, value):
        self._EnableDebug = (value == 'True')

    def _set_productnamesuffix_with_str(self, value):
        self._ProductNameSuffix = value

