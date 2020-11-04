"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class OvsdbQueryDbCommand(ROMCommand):
    def __init__(self, OvsdbContents=None, OvsdbDatabaseType=None, OvsdbTableType=None, **kwargs):
        self._OvsdbContents = OvsdbContents  # 
        self._OvsdbDatabaseType = OvsdbDatabaseType  # Data Base Type
        self._OvsdbTableType = OvsdbTableType  # Table Type

        properties = kwargs.copy()
        if OvsdbContents is not None:
            properties['OvsdbContents'] = OvsdbContents
        if OvsdbDatabaseType is not None:
            properties['OvsdbDatabaseType'] = OvsdbDatabaseType
        if OvsdbTableType is not None:
            properties['OvsdbTableType'] = OvsdbTableType

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbQueryDbCommand, self).__init__(**properties)

    @property
    def OvsdbContents(self):
        """
        get the value of property _OvsdbContents
        """
        return self._OvsdbContents

    @property
    def OvsdbDatabaseType(self):
        """
        get the value of property _OvsdbDatabaseType
        """
        return self._OvsdbDatabaseType

    @property
    def OvsdbTableType(self):
        """
        get the value of property _OvsdbTableType
        """
        return self._OvsdbTableType

    @OvsdbContents.setter
    def OvsdbContents(self, value):
        self._OvsdbContents = value

    @OvsdbDatabaseType.setter
    def OvsdbDatabaseType(self, value):
        self._OvsdbDatabaseType = value

    @OvsdbTableType.setter
    def OvsdbTableType(self, value):
        self._OvsdbTableType = value

    def _set_ovsdbcontents_with_str(self, value):
        self._OvsdbContents = value

    def _set_ovsdbdatabasetype_with_str(self, value):
        self._OvsdbDatabaseType = value

    def _set_ovsdbtabletype_with_str(self, value):
        self._OvsdbTableType = value

