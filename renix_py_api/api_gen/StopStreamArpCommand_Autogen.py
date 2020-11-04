"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StopStreamArpCommand(ROMCommand):
    def __init__(self, StreamHandles=None, **kwargs):
        self._StreamHandles = StreamHandles  # Stream Handles

        properties = kwargs.copy()
        if StreamHandles is not None:
            properties['StreamHandles'] = StreamHandles

        # call base class function, and it will send message to renix server to create a class.
        super(StopStreamArpCommand, self).__init__(**properties)

    @property
    def StreamHandles(self):
        """
        get the value of property _StreamHandles
        """
        return self._StreamHandles

    @StreamHandles.setter
    def StreamHandles(self, value):
        self._StreamHandles = value

    def _set_streamhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamHandles = tmp_value.split()

