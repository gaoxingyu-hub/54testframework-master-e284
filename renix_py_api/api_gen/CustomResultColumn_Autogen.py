"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class CustomResultColumn(ROMObject):
    def __init__(self, ViewName=None, DataClassName=None, GroupName=None, ColumnName=None, Formula=None, IsBool=None, **kwargs):
        self._ViewName = ViewName  # View Name
        self._DataClassName = DataClassName  # Data Class Name
        self._GroupName = GroupName  # Group Name
        self._ColumnName = ColumnName  # Column Name
        self._Formula = Formula  # Formula
        self._IsBool = IsBool  # Is Relation

        properties = kwargs.copy()
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if DataClassName is not None:
            properties['DataClassName'] = DataClassName
        if GroupName is not None:
            properties['GroupName'] = GroupName
        if ColumnName is not None:
            properties['ColumnName'] = ColumnName
        if Formula is not None:
            properties['Formula'] = Formula
        if IsBool is not None:
            properties['IsBool'] = IsBool

        # call base class function, and it will send message to renix server to create a class.
        super(CustomResultColumn, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ViewName=None, DataClassName=None, GroupName=None, ColumnName=None, Formula=None, IsBool=None, **kwargs):
        properties = kwargs.copy()
        if ViewName is not None:
            self._ViewName = ViewName
            properties['ViewName'] = ViewName
        if DataClassName is not None:
            self._DataClassName = DataClassName
            properties['DataClassName'] = DataClassName
        if GroupName is not None:
            self._GroupName = GroupName
            properties['GroupName'] = GroupName
        if ColumnName is not None:
            self._ColumnName = ColumnName
            properties['ColumnName'] = ColumnName
        if Formula is not None:
            self._Formula = Formula
            properties['Formula'] = Formula
        if IsBool is not None:
            self._IsBool = IsBool
            properties['IsBool'] = IsBool

        super(CustomResultColumn, self).edit(**properties)

    @property
    def ViewName(self):
        """
        get the value of property _ViewName
        """
        if self.force_auto_sync:
            self.get('ViewName')
        return self._ViewName

    @property
    def DataClassName(self):
        """
        get the value of property _DataClassName
        """
        if self.force_auto_sync:
            self.get('DataClassName')
        return self._DataClassName

    @property
    def GroupName(self):
        """
        get the value of property _GroupName
        """
        if self.force_auto_sync:
            self.get('GroupName')
        return self._GroupName

    @property
    def ColumnName(self):
        """
        get the value of property _ColumnName
        """
        if self.force_auto_sync:
            self.get('ColumnName')
        return self._ColumnName

    @property
    def Formula(self):
        """
        get the value of property _Formula
        """
        if self.force_auto_sync:
            self.get('Formula')
        return self._Formula

    @property
    def IsBool(self):
        """
        get the value of property _IsBool
        """
        if self.force_auto_sync:
            self.get('IsBool')
        return self._IsBool

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value
        self.edit(ViewName=value)

    @DataClassName.setter
    def DataClassName(self, value):
        self._DataClassName = value
        self.edit(DataClassName=value)

    @GroupName.setter
    def GroupName(self, value):
        self._GroupName = value
        self.edit(GroupName=value)

    @ColumnName.setter
    def ColumnName(self, value):
        self._ColumnName = value
        self.edit(ColumnName=value)

    @Formula.setter
    def Formula(self, value):
        self._Formula = value
        self.edit(Formula=value)

    @IsBool.setter
    def IsBool(self, value):
        self._IsBool = value
        self.edit(IsBool=value)

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_dataclassname_with_str(self, value):
        self._DataClassName = value

    def _set_groupname_with_str(self, value):
        self._GroupName = value

    def _set_columnname_with_str(self, value):
        self._ColumnName = value

    def _set_formula_with_str(self, value):
        self._Formula = value

    def _set_isbool_with_str(self, value):
        self._IsBool = (value == 'True')

