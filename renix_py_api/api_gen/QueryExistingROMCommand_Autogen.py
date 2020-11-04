"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class QueryExistingROMCommand(ROMCommand):
    def __init__(self, ParentHandles=None, ChildType=None, **kwargs):
        self._ParentHandles = ParentHandles  # Parent Handle List
        self._ChildType = ChildType  # Query Type String
        self._QueryResult = False  # Result of query existing rom command, not editable

        properties = kwargs.copy()
        if ParentHandles is not None:
            properties['ParentHandles'] = ParentHandles
        if ChildType is not None:
            properties['ChildType'] = ChildType

        # call base class function, and it will send message to renix server to create a class.
        super(QueryExistingROMCommand, self).__init__(**properties)

    @property
    def ParentHandles(self):
        """
        get the value of property _ParentHandles
        """
        return self._ParentHandles

    @property
    def ChildType(self):
        """
        get the value of property _ChildType
        """
        return self._ChildType

    @property
    def QueryResult(self):
        """
        get the value of property _QueryResult
        """
        return self._QueryResult

    @ParentHandles.setter
    def ParentHandles(self, value):
        self._ParentHandles = value

    @ChildType.setter
    def ChildType(self, value):
        self._ChildType = value

    def _set_parenthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ParentHandles = tmp_value.split()

    def _set_childtype_with_str(self, value):
        self._ChildType = value

    def _set_queryresult_with_str(self, value):
        self._QueryResult = (value == 'True')

    def _set_output_property(self, value):
        self._set_queryresult_with_str(value)

