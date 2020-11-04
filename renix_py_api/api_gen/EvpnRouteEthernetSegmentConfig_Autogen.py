"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EvpnRouteConfig_Autogen import EvpnRouteConfig


@rom_manager.rom
class EvpnRouteEthernetSegmentConfig(EvpnRouteConfig):
    def __init__(self, RouteBlockName=None, EviCount=None, EsImportRoute=None, **kwargs):
        self._RouteBlockName = RouteBlockName  # Route Block Name
        self._EviCount = EviCount  # EVI Count
        self._EsImportRoute = EsImportRoute  # Es-Import Route Target

        properties = kwargs.copy()
        if RouteBlockName is not None:
            properties['RouteBlockName'] = RouteBlockName
        if EviCount is not None:
            properties['EviCount'] = EviCount
        if EsImportRoute is not None:
            properties['EsImportRoute'] = EsImportRoute

        # call base class function, and it will send message to renix server to create a class.
        super(EvpnRouteEthernetSegmentConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteBlockName=None, EviCount=None, EsImportRoute=None, **kwargs):
        properties = kwargs.copy()
        if RouteBlockName is not None:
            self._RouteBlockName = RouteBlockName
            properties['RouteBlockName'] = RouteBlockName
        if EviCount is not None:
            self._EviCount = EviCount
            properties['EviCount'] = EviCount
        if EsImportRoute is not None:
            self._EsImportRoute = EsImportRoute
            properties['EsImportRoute'] = EsImportRoute

        super(EvpnRouteEthernetSegmentConfig, self).edit(**properties)

    @property
    def RouteBlockName(self):
        """
        get the value of property _RouteBlockName
        """
        if self.force_auto_sync:
            self.get('RouteBlockName')
        return self._RouteBlockName

    @property
    def EviCount(self):
        """
        get the value of property _EviCount
        """
        if self.force_auto_sync:
            self.get('EviCount')
        return self._EviCount

    @property
    def EsImportRoute(self):
        """
        get the value of property _EsImportRoute
        """
        if self.force_auto_sync:
            self.get('EsImportRoute')
        return self._EsImportRoute

    @RouteBlockName.setter
    def RouteBlockName(self, value):
        self._RouteBlockName = value
        self.edit(RouteBlockName=value)

    @EviCount.setter
    def EviCount(self, value):
        self._EviCount = value
        self.edit(EviCount=value)

    @EsImportRoute.setter
    def EsImportRoute(self, value):
        self._EsImportRoute = value
        self.edit(EsImportRoute=value)

    def _set_routeblockname_with_str(self, value):
        self._RouteBlockName = value

    def _set_evicount_with_str(self, value):
        try:
            self._EviCount = int(value)
        except ValueError:
            self._EviCount = hex(int(value, 16))

    def _set_esimportroute_with_str(self, value):
        self._EsImportRoute = value

