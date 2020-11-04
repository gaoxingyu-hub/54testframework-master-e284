"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class InsertHeaderCommand(ROMCommand):
    def __init__(self, Stream=None, HeaderType=None, Index=None, LowerHeader=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._HeaderType = HeaderType  # Header Type
        self._Index = Index  # Insert Position
        self._LowerHeader = LowerHeader  # Lower Header Name
        self._HeaderNames = None  # Header Names, not editable

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if HeaderType is not None:
            properties['HeaderType'] = HeaderType
        if Index is not None:
            properties['Index'] = Index
        if LowerHeader is not None:
            properties['LowerHeader'] = LowerHeader

        # call base class function, and it will send message to renix server to create a class.
        super(InsertHeaderCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def HeaderType(self):
        """
        get the value of property _HeaderType
        """
        return self._HeaderType

    @property
    def Index(self):
        """
        get the value of property _Index
        """
        return self._Index

    @property
    def LowerHeader(self):
        """
        get the value of property _LowerHeader
        """
        return self._LowerHeader

    @property
    def HeaderNames(self):
        """
        get the value of property _HeaderNames
        """
        return self._HeaderNames

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @HeaderType.setter
    def HeaderType(self, value):
        self._HeaderType = value

    @Index.setter
    def Index(self, value):
        self._Index = value

    @LowerHeader.setter
    def LowerHeader(self, value):
        self._LowerHeader = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_headertype_with_str(self, value):
        self._HeaderType = value

    def _set_index_with_str(self, value):
        try:
            self._Index = int(value)
        except ValueError:
            self._Index = hex(int(value, 16))

    def _set_lowerheader_with_str(self, value):
        self._LowerHeader = value

    def _set_headernames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._HeaderNames = tmp_value.split()

    def _set_output_property(self, value):
        self._set_headernames_with_str(value)

