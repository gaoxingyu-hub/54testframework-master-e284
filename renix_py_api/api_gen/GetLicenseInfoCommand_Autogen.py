"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class GetLicenseInfoCommand(ROMCommand):
    def __init__(self, Chassis=None, Option=None, **kwargs):
        self._Chassis = Chassis  # Chassis Handle
        self._Option = Option  # Command Option
        self._InfoList = None  # License Information List, not editable

        properties = kwargs.copy()
        if Chassis is not None:
            properties['Chassis'] = Chassis
        if Option is not None:
            properties['Option'] = Option

        # call base class function, and it will send message to renix server to create a class.
        super(GetLicenseInfoCommand, self).__init__(**properties)

    @property
    def Chassis(self):
        """
        get the value of property _Chassis
        """
        return self._Chassis

    @property
    def Option(self):
        """
        get the value of property _Option
        """
        return self._Option

    @property
    def InfoList(self):
        """
        get the value of property _InfoList
        """
        return self._InfoList

    @Chassis.setter
    def Chassis(self, value):
        self._Chassis = value

    @Option.setter
    def Option(self, value):
        self._Option = value

    def _set_chassis_with_str(self, value):
        self._Chassis = value

    def _set_option_with_str(self, value):
        seperate = value.find(':')
        exec('self._Option = EnumOption.%s' % value[:seperate])

    def _set_infolist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._InfoList = tmp_value.split()

    def _set_output_property(self, value):
        self._set_infolist_with_str(value)

