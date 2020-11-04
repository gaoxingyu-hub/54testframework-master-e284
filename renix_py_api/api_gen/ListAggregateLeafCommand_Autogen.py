"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ListAggregateLeafCommand(ROMCommand):
    def __init__(self, Stream=None, ParentName=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._ParentName = ParentName  # Parent Name
        self._Leaves = None  # Header Names, not editable

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if ParentName is not None:
            properties['ParentName'] = ParentName

        # call base class function, and it will send message to renix server to create a class.
        super(ListAggregateLeafCommand, self).__init__(**properties)

    @property
    def Stream(self):
        """
        get the value of property _Stream
        """
        return self._Stream

    @property
    def ParentName(self):
        """
        get the value of property _ParentName
        """
        return self._ParentName

    @property
    def Leaves(self):
        """
        get the value of property _Leaves
        """
        return self._Leaves

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @ParentName.setter
    def ParentName(self, value):
        self._ParentName = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_parentname_with_str(self, value):
        self._ParentName = value

    def _set_leaves_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._Leaves = tmp_value.split()

    def _set_output_property(self, value):
        self._set_leaves_with_str(value)

