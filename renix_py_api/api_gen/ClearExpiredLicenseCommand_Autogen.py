"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ClearExpiredLicenseCommand(ROMCommand):
    def __init__(self, ChassisList=None, **kwargs):
        self._ChassisList = ChassisList  # Chassis Handles

        properties = kwargs.copy()
        if ChassisList is not None:
            properties['ChassisList'] = ChassisList

        # call base class function, and it will send message to renix server to create a class.
        super(ClearExpiredLicenseCommand, self).__init__(**properties)

    @property
    def ChassisList(self):
        """
        get the value of property _ChassisList
        """
        return self._ChassisList

    @ChassisList.setter
    def ChassisList(self, value):
        self._ChassisList = value

    def _set_chassislist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ChassisList = tmp_value.split()

