"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ReleasePortCommand(ROMCommand):
    def __init__(self, LocationList=None, ForceRelease=None, **kwargs):
        self._LocationList = LocationList  # Port Location List
        self._ForceRelease = ForceRelease  # Force Release Port

        properties = kwargs.copy()
        if LocationList is not None:
            properties['LocationList'] = LocationList
        if ForceRelease is not None:
            properties['ForceRelease'] = ForceRelease

        # call base class function, and it will send message to renix server to create a class.
        super(ReleasePortCommand, self).__init__(**properties)

    @property
    def LocationList(self):
        """
        get the value of property _LocationList
        """
        return self._LocationList

    @property
    def ForceRelease(self):
        """
        get the value of property _ForceRelease
        """
        return self._ForceRelease

    @LocationList.setter
    def LocationList(self, value):
        self._LocationList = value

    @ForceRelease.setter
    def ForceRelease(self, value):
        self._ForceRelease = value

    def _set_locationlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LocationList = tmp_value.split()

    def _set_forcerelease_with_str(self, value):
        self._ForceRelease = (value == 'True')

