"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetLicenseFeatureInfoCommand(ROMCommand):
    def __init__(self, Chassis=None, **kwargs):
        self._Chassis = Chassis  # Chassis Handle
        self._FeatureInfoList = None  # License Feature Information List, not editable

        properties = kwargs.copy()
        if Chassis is not None:
            properties['Chassis'] = Chassis

        # call base class function, and it will send message to renix server to create a class.
        super(GetLicenseFeatureInfoCommand, self).__init__(**properties)

    @property
    def Chassis(self):
        """
        get the value of property _Chassis
        """
        return self._Chassis

    @property
    def FeatureInfoList(self):
        """
        get the value of property _FeatureInfoList
        """
        return self._FeatureInfoList

    @Chassis.setter
    def Chassis(self, value):
        self._Chassis = value

    def _set_chassis_with_str(self, value):
        self._Chassis = value

    def _set_featureinfolist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._FeatureInfoList = tmp_value.split()

    def _set_output_property(self, value):
        self._set_featureinfolist_with_str(value)

