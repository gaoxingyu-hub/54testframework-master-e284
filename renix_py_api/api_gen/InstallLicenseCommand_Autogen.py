"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class InstallLicenseCommand(ROMCommand):
    def __init__(self, Chassis=None, LicenseFile=None, **kwargs):
        self._Chassis = Chassis  # Chassis Handle
        self._LicenseFile = LicenseFile  # License File

        properties = kwargs.copy()
        if Chassis is not None:
            properties['Chassis'] = Chassis
        if LicenseFile is not None:
            properties['LicenseFile'] = LicenseFile

        # call base class function, and it will send message to renix server to create a class.
        super(InstallLicenseCommand, self).__init__(**properties)

    @property
    def Chassis(self):
        """
        get the value of property _Chassis
        """
        return self._Chassis

    @property
    def LicenseFile(self):
        """
        get the value of property _LicenseFile
        """
        return self._LicenseFile

    @Chassis.setter
    def Chassis(self, value):
        self._Chassis = value

    @LicenseFile.setter
    def LicenseFile(self, value):
        self._LicenseFile = value

    def _set_chassis_with_str(self, value):
        self._Chassis = value

    def _set_licensefile_with_str(self, value):
        self._LicenseFile = value

