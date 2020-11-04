"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StpCommand(ROMCommand):
    def __init__(self, ObjectList=None, **kwargs):
        self._ObjectList = ObjectList  # Object List

        properties = kwargs.copy()
        if ObjectList is not None:
            properties['ObjectList'] = ObjectList

        # call base class function, and it will send message to renix server to create a class.
        super(StpCommand, self).__init__(**properties)

    @property
    def ObjectList(self):
        """
        get the value of property _ObjectList
        """
        return self._ObjectList

    @ObjectList.setter
    def ObjectList(self, value):
        self._ObjectList = value

    def _set_objectlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ObjectList = tmp_value.split()

