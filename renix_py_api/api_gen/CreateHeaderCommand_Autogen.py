"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class CreateHeaderCommand(ROMCommand):
    def __init__(self, Stream=None, HeaderTypes=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._HeaderTypes = HeaderTypes  # Header Types
        self._HeaderNames = None  # Header Names, not editable

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if HeaderTypes is not None:
            properties['HeaderTypes'] = HeaderTypes

        # call base class function, and it will send message to renix server to create a class.
        super(CreateHeaderCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def HeaderTypes(self):
        """
        get the value of property _HeaderTypes
        """
        return self._HeaderTypes

    @property
    def HeaderNames(self):
        """
        get the value of property _HeaderNames
        """
        return self._HeaderNames

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @HeaderTypes.setter
    def HeaderTypes(self, value):
        self._HeaderTypes = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_headertypes_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HeaderTypes = tmp_value.split()

    def _set_headernames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HeaderNames = tmp_value.split()

    def _set_output_property(self, value):
        self._set_headernames_with_str(value)

