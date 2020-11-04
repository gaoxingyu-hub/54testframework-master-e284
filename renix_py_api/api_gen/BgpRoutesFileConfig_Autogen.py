"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class BgpRoutesFileConfig(ROMObject):
    def __init__(self, RoutesFileType=None, UseSessionAddressAsNextHop=None, MaxImportedRoutes=None, RoutesFilePath=None, **kwargs):
        self._RoutesFileType = RoutesFileType  # BGP RouteTable File Type
        self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop  # Use Session Address as NextHop
        self._MaxImportedRoutes = MaxImportedRoutes  # Max Imported Routes Count
        self._RoutesFilePath = RoutesFilePath  # BGP RouteTable File Path
        self._ParsingStatus = EnumBgpRoutesFileParsingStatus.NONE  # Parsing Status, not editable
        self._ParseRoutesCount = 0  # Parse Routes Count, not editable
        self._ImportedRouteBlockCount = 0  # Imported Route Blocks, not editable

        properties = kwargs.copy()
        if RoutesFileType is not None:
            properties['RoutesFileType'] = RoutesFileType
        if UseSessionAddressAsNextHop is not None:
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if MaxImportedRoutes is not None:
            properties['MaxImportedRoutes'] = MaxImportedRoutes
        if RoutesFilePath is not None:
            properties['RoutesFilePath'] = RoutesFilePath

        # call base class function, and it will send message to renix server to create a class.
        super(BgpRoutesFileConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RoutesFileType=None, UseSessionAddressAsNextHop=None, MaxImportedRoutes=None, RoutesFilePath=None, **kwargs):
        properties = kwargs.copy()
        if RoutesFileType is not None:
            self._RoutesFileType = RoutesFileType
            properties['RoutesFileType'] = RoutesFileType
        if UseSessionAddressAsNextHop is not None:
            self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if MaxImportedRoutes is not None:
            self._MaxImportedRoutes = MaxImportedRoutes
            properties['MaxImportedRoutes'] = MaxImportedRoutes
        if RoutesFilePath is not None:
            self._RoutesFilePath = RoutesFilePath
            properties['RoutesFilePath'] = RoutesFilePath

        super(BgpRoutesFileConfig, self).edit(**properties)

    @property
    def RoutesFileType(self):
        """
        get the value of property _RoutesFileType
        """
        if self.force_auto_sync:
            self.get('RoutesFileType')
        return self._RoutesFileType

    @property
    def UseSessionAddressAsNextHop(self):
        """
        get the value of property _UseSessionAddressAsNextHop
        """
        if self.force_auto_sync:
            self.get('UseSessionAddressAsNextHop')
        return self._UseSessionAddressAsNextHop

    @property
    def MaxImportedRoutes(self):
        """
        get the value of property _MaxImportedRoutes
        """
        if self.force_auto_sync:
            self.get('MaxImportedRoutes')
        return self._MaxImportedRoutes

    @property
    def RoutesFilePath(self):
        """
        get the value of property _RoutesFilePath
        """
        if self.force_auto_sync:
            self.get('RoutesFilePath')
        return self._RoutesFilePath

    @property
    def ParsingStatus(self):
        """
        get the value of property _ParsingStatus
        """
        if self.force_auto_sync:
            self.get('ParsingStatus')
        return self._ParsingStatus

    @property
    def ParseRoutesCount(self):
        """
        get the value of property _ParseRoutesCount
        """
        if self.force_auto_sync:
            self.get('ParseRoutesCount')
        return self._ParseRoutesCount

    @property
    def ImportedRouteBlockCount(self):
        """
        get the value of property _ImportedRouteBlockCount
        """
        if self.force_auto_sync:
            self.get('ImportedRouteBlockCount')
        return self._ImportedRouteBlockCount

    @RoutesFileType.setter
    def RoutesFileType(self, value):
        self._RoutesFileType = value
        self.edit(RoutesFileType=value)

    @UseSessionAddressAsNextHop.setter
    def UseSessionAddressAsNextHop(self, value):
        self._UseSessionAddressAsNextHop = value
        self.edit(UseSessionAddressAsNextHop=value)

    @MaxImportedRoutes.setter
    def MaxImportedRoutes(self, value):
        self._MaxImportedRoutes = value
        self.edit(MaxImportedRoutes=value)

    @RoutesFilePath.setter
    def RoutesFilePath(self, value):
        self._RoutesFilePath = value
        self.edit(RoutesFilePath=value)

    def _set_routesfiletype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RoutesFileType = EnumBgpRoutesFileType.%s' % value[:seperate])

    def _set_usesessionaddressasnexthop_with_str(self, value):
        self._UseSessionAddressAsNextHop = (value == 'True')

    def _set_maximportedroutes_with_str(self, value):
        try:
            self._MaxImportedRoutes = int(value)
        except ValueError:
            self._MaxImportedRoutes = hex(int(value, 16))

    def _set_routesfilepath_with_str(self, value):
        self._RoutesFilePath = value

    def _set_parsingstatus_with_str(self, value):
        seperate = value.find(':')
        exec('self._ParsingStatus = EnumBgpRoutesFileParsingStatus.%s' % value[:seperate])

    def _set_parseroutescount_with_str(self, value):
        try:
            self._ParseRoutesCount = int(value)
        except ValueError:
            self._ParseRoutesCount = hex(int(value, 16))

    def _set_importedrouteblockcount_with_str(self, value):
        try:
            self._ImportedRouteBlockCount = int(value)
        except ValueError:
            self._ImportedRouteBlockCount = hex(int(value, 16))

