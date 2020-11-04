"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StatsSimpleFilterApplyCommand(ROMCommand):
    def __init__(self, HandleList=None, **kwargs):
        self._HandleList = HandleList  # Port or SysEntry Handles or null

        properties = kwargs.copy()
        if HandleList is not None:
            properties['HandleList'] = HandleList

        # call base class function, and it will send message to renix server to create a class.
        super(StatsSimpleFilterApplyCommand, self).__init__(**properties)

    @property
    def HandleList(self):
        """
        get the value of property _HandleList
        """
        return self._HandleList

    @HandleList.setter
    def HandleList(self, value):
        self._HandleList = value

    def _set_handlelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HandleList = tmp_value.split()

