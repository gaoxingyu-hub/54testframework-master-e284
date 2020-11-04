"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class UpdateCustomResultColumnCommand(ROMCommand):
    def __init__(self, CustomResultColumnHandle=None, ViewName=None, GroupName=None, DataClassName=None, ColumnName=None, IsBool=None, Formula=None, **kwargs):
        self._CustomResultColumnHandle = CustomResultColumnHandle  # Custom Result Column
        self._ViewName = ViewName  # View Name
        self._GroupName = GroupName  # Group Name
        self._DataClassName = DataClassName  # Data Class Name
        self._ColumnName = ColumnName  # Column Name
        self._IsBool = IsBool  # Is Relation
        self._Formula = Formula  # Formula

        properties = kwargs.copy()
        if CustomResultColumnHandle is not None:
            properties['CustomResultColumnHandle'] = CustomResultColumnHandle
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if GroupName is not None:
            properties['GroupName'] = GroupName
        if DataClassName is not None:
            properties['DataClassName'] = DataClassName
        if ColumnName is not None:
            properties['ColumnName'] = ColumnName
        if IsBool is not None:
            properties['IsBool'] = IsBool
        if Formula is not None:
            properties['Formula'] = Formula

        # call base class function, and it will send message to renix server to create a class.
        super(UpdateCustomResultColumnCommand, self).__init__(**properties)

    @property
    def CustomResultColumnHandle(self):
        """
        get the value of property _CustomResultColumnHandle
        """
        return self._CustomResultColumnHandle

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        return self._ViewName

    @property
    def GroupName(self):
        """
        get the value of property _GroupName
        """
        return self._GroupName

    @property
    def DataClassName(self):
        """
        get the value of property _DataClassName
        """
        return self._DataClassName

    @property
    def ColumnName(self):
        """
        get the value of property _ColumnName
        """
        return self._ColumnName

    @property
    def IsBool(self):
        """
        get the value of property _IsBool
        """
        return self._IsBool

    @property
    def Formula(self):
        """
        get the value of property _Formula
        """
        return self._Formula

    @CustomResultColumnHandle.setter
    def CustomResultColumnHandle(self, value):
        self._CustomResultColumnHandle = value

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value

    @GroupName.setter
    def GroupName(self, value):
        self._GroupName = value

    @DataClassName.setter
    def DataClassName(self, value):
        self._DataClassName = value

    @ColumnName.setter
    def ColumnName(self, value):
        self._ColumnName = value

    @IsBool.setter
    def IsBool(self, value):
        self._IsBool = value

    @Formula.setter
    def Formula(self, value):
        self._Formula = value

    def _set_customresultcolumnhandle_with_str(self, value):
        self._CustomResultColumnHandle = value

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_groupname_with_str(self, value):
        self._GroupName = value

    def _set_dataclassname_with_str(self, value):
        self._DataClassName = value

    def _set_columnname_with_str(self, value):
        self._ColumnName = value

    def _set_isbool_with_str(self, value):
        self._IsBool = (value == 'True')

    def _set_formula_with_str(self, value):
        self._Formula = value

