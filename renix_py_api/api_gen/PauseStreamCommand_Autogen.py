"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class PauseStreamCommand(ROMCommand):
    def __init__(self, StreamList=None, **kwargs):
        self._StreamList = StreamList  # Stream Handles

        properties = kwargs.copy()
        if StreamList is not None:
            properties['StreamList'] = StreamList

        # call base class function, and it will send message to renix server to create a class.
        super(PauseStreamCommand, self).__init__(**properties)

    @property
    def StreamList(self):
        """
        get the value of property _StreamList
        """
        return self._StreamList

    @StreamList.setter
    def StreamList(self, value):
        self._StreamList = value

    def _set_streamlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamList = tmp_value.split()

