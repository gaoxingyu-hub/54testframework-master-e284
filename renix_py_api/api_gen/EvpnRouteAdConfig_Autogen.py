"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EvpnRouteConfig_Autogen import EvpnRouteConfig


@rom_manager.rom
class EvpnRouteAdConfig(EvpnRouteConfig):
    def __init__(self, RouteBlockName=None, AdRouteType=None, ActiveStandbyMode=None, EviCount=None, Vni=None, VniStep=None, **kwargs):
        self._RouteBlockName = RouteBlockName  # Route Block Name
        self._AdRouteType = AdRouteType  # AD Route Type
        self._ActiveStandbyMode = ActiveStandbyMode  # Active-Standby Mode
        self._EviCount = EviCount  # EVI Count
        self._Vni = Vni  # Encapsulation Label
        self._VniStep = VniStep  # Encapsulation Label Step

        properties = kwargs.copy()
        if RouteBlockName is not None:
            properties['RouteBlockName'] = RouteBlockName
        if AdRouteType is not None:
            properties['AdRouteType'] = AdRouteType
        if ActiveStandbyMode is not None:
            properties['ActiveStandbyMode'] = ActiveStandbyMode
        if EviCount is not None:
            properties['EviCount'] = EviCount
        if Vni is not None:
            properties['Vni'] = Vni
        if VniStep is not None:
            properties['VniStep'] = VniStep

        # call base class function, and it will send message to renix server to create a class.
        super(EvpnRouteAdConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteBlockName=None, AdRouteType=None, ActiveStandbyMode=None, EviCount=None, Vni=None, VniStep=None, **kwargs):
        properties = kwargs.copy()
        if RouteBlockName is not None:
            self._RouteBlockName = RouteBlockName
            properties['RouteBlockName'] = RouteBlockName
        if AdRouteType is not None:
            self._AdRouteType = AdRouteType
            properties['AdRouteType'] = AdRouteType
        if ActiveStandbyMode is not None:
            self._ActiveStandbyMode = ActiveStandbyMode
            properties['ActiveStandbyMode'] = ActiveStandbyMode
        if EviCount is not None:
            self._EviCount = EviCount
            properties['EviCount'] = EviCount
        if Vni is not None:
            self._Vni = Vni
            properties['Vni'] = Vni
        if VniStep is not None:
            self._VniStep = VniStep
            properties['VniStep'] = VniStep

        super(EvpnRouteAdConfig, self).edit(**properties)

    @property
    def RouteBlockName(self):
        """
        get the value of property _RouteBlockName
        """
        if self.force_auto_sync:
            self.get('RouteBlockName')
        return self._RouteBlockName

    @property
    def AdRouteType(self):
        """
        get the value of property _AdRouteType
        """
        if self.force_auto_sync:
            self.get('AdRouteType')
        return self._AdRouteType

    @property
    def ActiveStandbyMode(self):
        """
        get the value of property _ActiveStandbyMode
        """
        if self.force_auto_sync:
            self.get('ActiveStandbyMode')
        return self._ActiveStandbyMode

    @property
    def EviCount(self):
        """
        get the value of property _EviCount
        """
        if self.force_auto_sync:
            self.get('EviCount')
        return self._EviCount

    @property
    def Vni(self):
        """
        get the value of property _Vni
        """
        if self.force_auto_sync:
            self.get('Vni')
        return self._Vni

    @property
    def VniStep(self):
        """
        get the value of property _VniStep
        """
        if self.force_auto_sync:
            self.get('VniStep')
        return self._VniStep

    @RouteBlockName.setter
    def RouteBlockName(self, value):
        self._RouteBlockName = value
        self.edit(RouteBlockName=value)

    @AdRouteType.setter
    def AdRouteType(self, value):
        self._AdRouteType = value
        self.edit(AdRouteType=value)

    @ActiveStandbyMode.setter
    def ActiveStandbyMode(self, value):
        self._ActiveStandbyMode = value
        self.edit(ActiveStandbyMode=value)

    @EviCount.setter
    def EviCount(self, value):
        self._EviCount = value
        self.edit(EviCount=value)

    @Vni.setter
    def Vni(self, value):
        self._Vni = value
        self.edit(Vni=value)

    @VniStep.setter
    def VniStep(self, value):
        self._VniStep = value
        self.edit(VniStep=value)

    def _set_routeblockname_with_str(self, value):
        self._RouteBlockName = value

    def _set_adroutetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AdRouteType = EnumAdRouteType.%s' % value[:seperate])

    def _set_activestandbymode_with_str(self, value):
        seperate = value.find(':')
        exec('self._ActiveStandbyMode = EnumActiveStandbyType.%s' % value[:seperate])

    def _set_evicount_with_str(self, value):
        try:
            self._EviCount = int(value)
        except ValueError:
            self._EviCount = hex(int(value, 16))

    def _set_vni_with_str(self, value):
        try:
            self._Vni = int(value)
        except ValueError:
            self._Vni = hex(int(value, 16))

    def _set_vnistep_with_str(self, value):
        try:
            self._VniStep = int(value)
        except ValueError:
            self._VniStep = hex(int(value, 16))

