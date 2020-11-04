"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class DeleteHeaderCommand(ROMCommand):
    def __init__(self, Stream=None, Index=None, HeaderName=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._Index = Index  # Delete Position
        self._HeaderName = HeaderName  # Delete Header Name
        self._HeaderNames = None  # Header Names, not editable

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if Index is not None:
            properties['Index'] = Index
        if HeaderName is not None:
            properties['HeaderName'] = HeaderName

        # call base class function, and it will send message to renix server to create a class.
        super(DeleteHeaderCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def Index(self):
        """
        get the value of property _Index
        """
        return self._Index

    @property
    def HeaderName(self):
        """
        get the value of property _HeaderName
        """
        return self._HeaderName

    @property
    def HeaderNames(self):
        """
        get the value of property _HeaderNames
        """
        return self._HeaderNames

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @Index.setter
    def Index(self, value):
        self._Index = value

    @HeaderName.setter
    def HeaderName(self, value):
        self._HeaderName = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_index_with_str(self, value):
        try:
            self._Index = int(value)
        except ValueError:
            self._Index = hex(int(value, 16))

    def _set_headername_with_str(self, value):
        self._HeaderName = value

    def _set_headernames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HeaderNames = tmp_value.split()

    def _set_output_property(self, value):
        self._set_headernames_with_str(value)

