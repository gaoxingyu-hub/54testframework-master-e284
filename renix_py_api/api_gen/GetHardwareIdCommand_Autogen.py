"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetHardwareIdCommand(ROMCommand):
    def __init__(self, Chassis=None, FilePath=None, **kwargs):
        self._Chassis = Chassis  # Chassis Handle
        self._FilePath = FilePath  # File Path

        properties = kwargs.copy()
        if Chassis is not None:
            properties['Chassis'] = Chassis
        if FilePath is not None:
            properties['FilePath'] = FilePath

        # call base class function, and it will send message to renix server to create a class.
        super(GetHardwareIdCommand, self).__init__(**properties)

    @property
    def Chassis(self):
        """
        get the value of property _Chassis
        """
        return self._Chassis

    @property
    def FilePath(self):
        """
        get the value of property _FilePath
        """
        return self._FilePath

    @Chassis.setter
    def Chassis(self, value):
        self._Chassis = value

    @FilePath.setter
    def FilePath(self, value):
        self._FilePath = value

    def _set_chassis_with_str(self, value):
        self._Chassis = value

    def _set_filepath_with_str(self, value):
        self._FilePath = value

