"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .CreateResultViewCommand_Autogen import CreateResultViewCommand


@rom_manager.rom
class CreateCustomResultViewCommand(CreateResultViewCommand):
    def __init__(self, ViewName=None, ColumnNames=None, **kwargs):
        self._ViewName = ViewName  # Result View Name
        self._ColumnNames = ColumnNames  # Column Names

        properties = kwargs.copy()
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if ColumnNames is not None:
            properties['ColumnNames'] = ColumnNames

        # call base class function, and it will send message to renix server to create a class.
        super(CreateCustomResultViewCommand, self).__init__(**properties)

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        return self._ViewName

    @property
    def ColumnNames(self):
        """
        get the value of property _ColumnNames
        """
        return self._ColumnNames

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value

    @ColumnNames.setter
    def ColumnNames(self, value):
        self._ColumnNames = value

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_columnnames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ColumnNames = tmp_value.split()

