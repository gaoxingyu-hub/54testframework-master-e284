"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class CustomResultViewWizardConfig(WizardConfigBase):
    def __init__(self, ViewFolder=None, ViewName=None, DataClassName=None, ColumnNames=None, **kwargs):
        self._ViewFolder = ViewFolder  # Custom Result View Folder
        self._ViewName = ViewName  # Result View Name
        self._DataClassName = DataClassName  # Result Class Name
        self._ColumnNames = ColumnNames  # Column Names
        self._CustomResultViewFile = ''  # Saved Custom Result View File, not editable

        properties = kwargs.copy()
        if ViewFolder is not None:
            properties['ViewFolder'] = ViewFolder
        if ViewName is not None:
            properties['ViewName'] = ViewName
        if DataClassName is not None:
            properties['DataClassName'] = DataClassName
        if ColumnNames is not None:
            properties['ColumnNames'] = ColumnNames

        # call base class function, and it will send message to renix server to create a class.
        super(CustomResultViewWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ViewFolder=None, ViewName=None, DataClassName=None, ColumnNames=None, **kwargs):
        properties = kwargs.copy()
        if ViewFolder is not None:
            self._ViewFolder = ViewFolder
            properties['ViewFolder'] = ViewFolder
        if ViewName is not None:
            self._ViewName = ViewName
            properties['ViewName'] = ViewName
        if DataClassName is not None:
            self._DataClassName = DataClassName
            properties['DataClassName'] = DataClassName
        if ColumnNames is not None:
            self._ColumnNames = ColumnNames
            properties['ColumnNames'] = ColumnNames

        super(CustomResultViewWizardConfig, self).edit(**properties)

    @property
    def ViewFolder(self):
        """
        get the value of property _ViewFolder
        """
        if self.force_auto_sync:
            self.get('ViewFolder')
        return self._ViewFolder

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
    def ColumnNames(self):
        """
        get the value of property _ColumnNames
        """
        if self.force_auto_sync:
            self.get('ColumnNames')
        return self._ColumnNames

    @property
    def CustomResultViewFile(self):
        """
        get the value of property _CustomResultViewFile
        """
        if self.force_auto_sync:
            self.get('CustomResultViewFile')
        return self._CustomResultViewFile

    @ViewFolder.setter
    def ViewFolder(self, value):
        self._ViewFolder = value
        self.edit(ViewFolder=value)

    @ViewName.setter
    def ViewName(self, value):
        self._ViewName = value
        self.edit(ViewName=value)

    @DataClassName.setter
    def DataClassName(self, value):
        self._DataClassName = value
        self.edit(DataClassName=value)

    @ColumnNames.setter
    def ColumnNames(self, value):
        self._ColumnNames = value
        self.edit(ColumnNames=value)

    def _set_viewfolder_with_str(self, value):
        self._ViewFolder = value

    def _set_viewname_with_str(self, value):
        self._ViewName = value

    def _set_dataclassname_with_str(self, value):
        self._DataClassName = value

    def _set_columnnames_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ColumnNames = tmp_value.split()

    def _set_customresultviewfile_with_str(self, value):
        self._CustomResultViewFile = value

