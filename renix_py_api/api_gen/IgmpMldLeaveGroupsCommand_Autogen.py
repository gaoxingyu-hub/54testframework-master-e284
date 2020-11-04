"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class IgmpMldLeaveGroupsCommand(ROMCommand):
    def __init__(self, BlockList=None, **kwargs):
        self._BlockList = BlockList  # Block List

        properties = kwargs.copy()
        if BlockList is not None:
            properties['BlockList'] = BlockList

        # call base class function, and it will send message to renix server to create a class.
        super(IgmpMldLeaveGroupsCommand, self).__init__(**properties)

    @property
    def BlockList(self):
        """
        get the value of property _BlockList
        """
        return self._BlockList

    @BlockList.setter
    def BlockList(self, value):
        self._BlockList = value

    def _set_blocklist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._BlockList = tmp_value.split()

