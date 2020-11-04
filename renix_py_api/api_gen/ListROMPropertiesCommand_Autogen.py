"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ListROMPropertiesCommand(ROMCommand):
    def __init__(self, ROMName=None, GetDetail=None, **kwargs):
        self._ROMName = ROMName  # ROM Name
        self._GetDetail = GetDetail  # List ROM Property detail
        self._Properties = None  # ROM Properties, not editable
        self._Detail = ''  # ROM Property Detail Information, not editable

        properties = kwargs.copy()
        if ROMName is not None:
            properties['ROMName'] = ROMName
        if GetDetail is not None:
            properties['GetDetail'] = GetDetail

        # call base class function, and it will send message to renix server to create a class.
        super(ListROMPropertiesCommand, self).__init__(**properties)

    @property
    def ROMName(self):
        """
        get the value of property _ROMName
        """
        return self._ROMName

    @property
    def GetDetail(self):
        """
        get the value of property _GetDetail
        """
        return self._GetDetail

    @property
    def Properties(self):
        """
        get the value of property _Properties
        """
        return self._Properties

    @property
    def Detail(self):
        """
        get the value of property _Detail
        """
        return self._Detail

    @ROMName.setter
    def ROMName(self, value):
        self._ROMName = value

    @GetDetail.setter
    def GetDetail(self, value):
        self._GetDetail = value

    def _set_romname_with_str(self, value):
        self._ROMName = value

    def _set_getdetail_with_str(self, value):
        self._GetDetail = (value == 'True')

    def _set_properties_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Properties = tmp_value.split()

    def _set_detail_with_str(self, value):
        self._Detail = value

