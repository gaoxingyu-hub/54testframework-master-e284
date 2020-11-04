"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class InsertNodeToASetCommand(ROMCommand):
    def __init__(self, Stream=None, ParentName=None, NodeName=None, NodeCount=None, **kwargs):
        self._Stream = Stream  # Stream Handle
        self._ParentName = ParentName  # Parent Name
        self._NodeName = NodeName  # will Insert Node Name
        self._NodeCount = NodeCount  # Count you will insert the input node

        properties = kwargs.copy()
        if Stream is not None:
            properties['Stream'] = Stream
        if ParentName is not None:
            properties['ParentName'] = ParentName
        if NodeName is not None:
            properties['NodeName'] = NodeName
        if NodeCount is not None:
            properties['NodeCount'] = NodeCount

        # call base class function, and it will send message to renix server to create a class.
        super(InsertNodeToASetCommand, self).__init__(**properties)

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
    def NodeName(self):
        """
        get the value of property _NodeName
        """
        return self._NodeName

    @property
    def NodeCount(self):
        """
        get the value of property _NodeCount
        """
        return self._NodeCount

    @Stream.setter
    def Stream(self, value):
        self._Stream = value

    @ParentName.setter
    def ParentName(self, value):
        self._ParentName = value

    @NodeName.setter
    def NodeName(self, value):
        self._NodeName = value

    @NodeCount.setter
    def NodeCount(self, value):
        self._NodeCount = value

    def _set_stream_with_str(self, value):
        self._Stream = value

    def _set_parentname_with_str(self, value):
        self._ParentName = value

    def _set_nodename_with_str(self, value):
        self._NodeName = value

    def _set_nodecount_with_str(self, value):
        try:
            self._NodeCount = int(value)
        except ValueError:
            self._NodeCount = hex(int(value, 16))

