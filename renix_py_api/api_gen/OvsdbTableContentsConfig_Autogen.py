"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class OvsdbTableContentsConfig(ROMObject):
    def __init__(self, OvsdbRefreshWay=None, OvsdbTimer=None, OvsdbContents=None, OvsdbDatabaseType=None, OvsdbTableType=None, **kwargs):
        self._OvsdbRefreshWay = OvsdbRefreshWay  # 
        self._OvsdbTimer = OvsdbTimer  # 
        self._OvsdbContents = OvsdbContents  # 
        self._OvsdbDatabaseType = OvsdbDatabaseType  # Data Base Type
        self._OvsdbTableType = OvsdbTableType  # Table Type
        self._OvsdbState = EnumRefreshState.IDLE  # Refresh State, not editable

        properties = kwargs.copy()
        if OvsdbRefreshWay is not None:
            properties['OvsdbRefreshWay'] = OvsdbRefreshWay
        if OvsdbTimer is not None:
            properties['OvsdbTimer'] = OvsdbTimer
        if OvsdbContents is not None:
            properties['OvsdbContents'] = OvsdbContents
        if OvsdbDatabaseType is not None:
            properties['OvsdbDatabaseType'] = OvsdbDatabaseType
        if OvsdbTableType is not None:
            properties['OvsdbTableType'] = OvsdbTableType

        # call base class function, and it will send message to renix server to create a class.
        super(OvsdbTableContentsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, OvsdbRefreshWay=None, OvsdbTimer=None, OvsdbContents=None, OvsdbDatabaseType=None, OvsdbTableType=None, **kwargs):
        properties = kwargs.copy()
        if OvsdbRefreshWay is not None:
            self._OvsdbRefreshWay = OvsdbRefreshWay
            properties['OvsdbRefreshWay'] = OvsdbRefreshWay
        if OvsdbTimer is not None:
            self._OvsdbTimer = OvsdbTimer
            properties['OvsdbTimer'] = OvsdbTimer
        if OvsdbContents is not None:
            self._OvsdbContents = OvsdbContents
            properties['OvsdbContents'] = OvsdbContents
        if OvsdbDatabaseType is not None:
            self._OvsdbDatabaseType = OvsdbDatabaseType
            properties['OvsdbDatabaseType'] = OvsdbDatabaseType
        if OvsdbTableType is not None:
            self._OvsdbTableType = OvsdbTableType
            properties['OvsdbTableType'] = OvsdbTableType

        super(OvsdbTableContentsConfig, self).edit(**properties)

    @property
    def OvsdbRefreshWay(self):
        """
        get the value of property _OvsdbRefreshWay
        """
        if self.force_auto_sync:
            self.get('OvsdbRefreshWay')
        return self._OvsdbRefreshWay

    @property
    def OvsdbTimer(self):
        """
        get the value of property _OvsdbTimer
        """
        if self.force_auto_sync:
            self.get('OvsdbTimer')
        return self._OvsdbTimer

    @property
    def OvsdbContents(self):
        """
        get the value of property _OvsdbContents
        """
        if self.force_auto_sync:
            self.get('OvsdbContents')
        return self._OvsdbContents

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
    def OvsdbState(self):
        """
        get the value of property _OvsdbState
        """
        if self.force_auto_sync:
            self.get('OvsdbState')
        return self._OvsdbState

    @OvsdbRefreshWay.setter
    def OvsdbRefreshWay(self, value):
        self._OvsdbRefreshWay = value
        self.edit(OvsdbRefreshWay=value)

    @OvsdbTimer.setter
    def OvsdbTimer(self, value):
        self._OvsdbTimer = value
        self.edit(OvsdbTimer=value)

    @OvsdbContents.setter
    def OvsdbContents(self, value):
        self._OvsdbContents = value
        self.edit(OvsdbContents=value)

    @OvsdbDatabaseType.setter
    def OvsdbDatabaseType(self, value):
        self._OvsdbDatabaseType = value
        self.edit(OvsdbDatabaseType=value)

    @OvsdbTableType.setter
    def OvsdbTableType(self, value):
        self._OvsdbTableType = value
        self.edit(OvsdbTableType=value)

    def _set_ovsdbrefreshway_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbRefreshWay = EnumRefreshWay.%s' % value[:seperate])

    def _set_ovsdbtimer_with_str(self, value):
        try:
            self._OvsdbTimer = int(value)
        except ValueError:
            self._OvsdbTimer = hex(int(value, 16))

    def _set_ovsdbcontents_with_str(self, value):
        self._OvsdbContents = value

    def _set_ovsdbdatabasetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbDatabaseType = EnumDatabaseType.%s' % value[:seperate])

    def _set_ovsdbtabletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbTableType = EnumTableType.%s' % value[:seperate])

    def _set_ovsdbstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._OvsdbState = EnumRefreshState.%s' % value[:seperate])

