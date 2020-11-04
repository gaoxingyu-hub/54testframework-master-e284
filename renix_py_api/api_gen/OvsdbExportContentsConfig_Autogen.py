"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OvsdbExportContentsConfig(ROMObject):
    def __init__(self, OvsdbDatabaseType=None, OvsdbTableType=None, OvsdbExportFilePrefix=None, OvsdbSaveAsArchive=None, OvsdbExportPath=None, **kwargs):
        self._OvsdbDatabaseType = OvsdbDatabaseType  # Data Base Type
        self._OvsdbTableType = OvsdbTableType  # Table Type
        self._OvsdbExportFilePrefix = OvsdbExportFilePrefix  # Export File Prefix
        self._OvsdbSaveAsArchive = OvsdbSaveAsArchive  # Save As Archive
        self._OvsdbExportPath = OvsdbExportPath  # Export Path

        properties = kwargs.copy()
        if OvsdbDatabaseType is not None:
            properties['OvsdbDatabaseType'] = OvsdbDatabaseType
        if OvsdbTableType is not None:
            properties['OvsdbTableType'] = OvsdbTableType
        if OvsdbExportFilePrefix is not None:
            properties['OvsdbExportFilePrefix'] = OvsdbExportFilePrefix
        if OvsdbSaveAsArchive is not None:
            properties['OvsdbSaveAsArchive'] = OvsdbSaveAsArchive
        if OvsdbExportPath is not None:
            properties['OvsdbExportPath'] = OvsdbExportPath

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbExportContentsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OvsdbDatabaseType=None, OvsdbTableType=None, OvsdbExportFilePrefix=None, OvsdbSaveAsArchive=None, OvsdbExportPath=None, **kwargs):
        properties = kwargs.copy()
        if OvsdbDatabaseType is not None:
            self._OvsdbDatabaseType = OvsdbDatabaseType
            properties['OvsdbDatabaseType'] = OvsdbDatabaseType
        if OvsdbTableType is not None:
            self._OvsdbTableType = OvsdbTableType
            properties['OvsdbTableType'] = OvsdbTableType
        if OvsdbExportFilePrefix is not None:
            self._OvsdbExportFilePrefix = OvsdbExportFilePrefix
            properties['OvsdbExportFilePrefix'] = OvsdbExportFilePrefix
        if OvsdbSaveAsArchive is not None:
            self._OvsdbSaveAsArchive = OvsdbSaveAsArchive
            properties['OvsdbSaveAsArchive'] = OvsdbSaveAsArchive
        if OvsdbExportPath is not None:
            self._OvsdbExportPath = OvsdbExportPath
            properties['OvsdbExportPath'] = OvsdbExportPath

        super(OvsdbExportContentsConfig, self).edit(**properties)

    @property
    def OvsdbDatabaseType(self):
        """
        get the value of property _OvsdbDatabaseType
        """
        if self.force_auto_sync:
            self.get('OvsdbDatabaseType')
        return self._OvsdbDatabaseType

    @property
    def OvsdbTableType(self):
        """
        get the value of property _OvsdbTableType
        """
        if self.force_auto_sync:
            self.get('OvsdbTableType')
        return self._OvsdbTableType

    @property
    def OvsdbExportFilePrefix(self):
        """
        get the value of property _OvsdbExportFilePrefix
        """
        if self.force_auto_sync:
            self.get('OvsdbExportFilePrefix')
        return self._OvsdbExportFilePrefix

    @property
    def OvsdbSaveAsArchive(self):
        """
        get the value of property _OvsdbSaveAsArchive
        """
        if self.force_auto_sync:
            self.get('OvsdbSaveAsArchive')
        return self._OvsdbSaveAsArchive

    @property
    def OvsdbExportPath(self):
        """
        get the value of property _OvsdbExportPath
        """
        if self.force_auto_sync:
            self.get('OvsdbExportPath')
        return self._OvsdbExportPath

    @OvsdbDatabaseType.setter
    def OvsdbDatabaseType(self, value):
        self._OvsdbDatabaseType = value
        self.edit(OvsdbDatabaseType=value)

    @OvsdbTableType.setter
    def OvsdbTableType(self, value):
        self._OvsdbTableType = value
        self.edit(OvsdbTableType=value)

    @OvsdbExportFilePrefix.setter
    def OvsdbExportFilePrefix(self, value):
        self._OvsdbExportFilePrefix = value
        self.edit(OvsdbExportFilePrefix=value)

    @OvsdbSaveAsArchive.setter
    def OvsdbSaveAsArchive(self, value):
        self._OvsdbSaveAsArchive = value
        self.edit(OvsdbSaveAsArchive=value)

    @OvsdbExportPath.setter
    def OvsdbExportPath(self, value):
        self._OvsdbExportPath = value
        self.edit(OvsdbExportPath=value)

    def _set_ovsdbdatabasetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbDatabaseType = EnumDatabaseType.%s' % value[:seperate])

    def _set_ovsdbtabletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbTableType = EnumTableType.%s' % value[:seperate])

    def _set_ovsdbexportfileprefix_with_str(self, value):
        self._OvsdbExportFilePrefix = value

    def _set_ovsdbsaveasarchive_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbSaveAsArchive = EnumArchive.%s' % value[:seperate])

    def _set_ovsdbexportpath_with_str(self, value):
        self._OvsdbExportPath = value

