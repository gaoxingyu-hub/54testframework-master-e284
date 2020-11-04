"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class EncodeStreamCommand(ROMCommand):
    def __init__(self, Stream=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._Data = ''  # Stream Hex String Data, not editable

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream

        # call base class function, and it will send message to renix server to create a class.
        super(EncodeStreamCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def Data(self):
        """
        get the value of property _Data
        """
        return self._Data

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_data_with_str(self, value):
        self._Data = value

    def _set_output_property(self, value):
        self._set_data_with_str(value)

