"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EvpnRouteConfig_Autogen import EvpnRouteConfig


@rom_manager.rom
class EvpnRouteIpPrefixConfig(EvpnRouteConfig):
    def __init__(self, RouteBlockName=None, EviCount=None, RouteNumber=None, NetWorkCount=None, Vni=None, VniStep=None, StartIpv4=None, PrefixLength=None, Ipv4Increment=None, EndIpv4Address=None, GatewayIp=None, EnableIncludeRouterMac=None, RouterMac=None, **kwargs):
        self._RouteBlockName = RouteBlockName  # Route Block Name
        self._EviCount = EviCount  # EVI Count
        self._RouteNumber = RouteNumber  # Number Of Routes
        self._NetWorkCount = NetWorkCount  # NetWork Count
        self._Vni = Vni  # Encapsulation Label
        self._VniStep = VniStep  # Encapsulation Label Step
        self._StartIpv4 = StartIpv4  # Start IPv4 Prefix
        self._PrefixLength = PrefixLength  # IP Prefix Length
        self._Ipv4Increment = Ipv4Increment  # Ipv4 Address Increment
        self._EndIpv4Address = EndIpv4Address  # End Ipv4 Address
        self._GatewayIp = GatewayIp  # Gateway Ip
        self._EnableIncludeRouterMac = EnableIncludeRouterMac  # Include Router Mac
        self._RouterMac = RouterMac  # Router Mac Address

        properties = kwargs.copy()
        if RouteBlockName is not None:
            properties['RouteBlockName'] = RouteBlockName
        if EviCount is not None:
            properties['EviCount'] = EviCount
        if RouteNumber is not None:
            properties['RouteNumber'] = RouteNumber
        if NetWorkCount is not None:
            properties['NetWorkCount'] = NetWorkCount
        if Vni is not None:
            properties['Vni'] = Vni
        if VniStep is not None:
            properties['VniStep'] = VniStep
        if StartIpv4 is not None:
            properties['StartIpv4'] = StartIpv4
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if Ipv4Increment is not None:
            properties['Ipv4Increment'] = Ipv4Increment
        if EndIpv4Address is not None:
            properties['EndIpv4Address'] = EndIpv4Address
        if GatewayIp is not None:
            properties['GatewayIp'] = GatewayIp
        if EnableIncludeRouterMac is not None:
            properties['EnableIncludeRouterMac'] = EnableIncludeRouterMac
        if RouterMac is not None:
            properties['RouterMac'] = RouterMac

        # call base class function, and it will send message to renix server to create a class.
        super(EvpnRouteIpPrefixConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteBlockName=None, EviCount=None, RouteNumber=None, NetWorkCount=None, Vni=None, VniStep=None, StartIpv4=None, PrefixLength=None, Ipv4Increment=None, EndIpv4Address=None, GatewayIp=None, EnableIncludeRouterMac=None, RouterMac=None, **kwargs):
        properties = kwargs.copy()
        if RouteBlockName is not None:
            self._RouteBlockName = RouteBlockName
            properties['RouteBlockName'] = RouteBlockName
        if EviCount is not None:
            self._EviCount = EviCount
            properties['EviCount'] = EviCount
        if RouteNumber is not None:
            self._RouteNumber = RouteNumber
            properties['RouteNumber'] = RouteNumber
        if NetWorkCount is not None:
            self._NetWorkCount = NetWorkCount
            properties['NetWorkCount'] = NetWorkCount
        if Vni is not None:
            self._Vni = Vni
            properties['Vni'] = Vni
        if VniStep is not None:
            self._VniStep = VniStep
            properties['VniStep'] = VniStep
        if StartIpv4 is not None:
            self._StartIpv4 = StartIpv4
            properties['StartIpv4'] = StartIpv4
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if Ipv4Increment is not None:
            self._Ipv4Increment = Ipv4Increment
            properties['Ipv4Increment'] = Ipv4Increment
        if EndIpv4Address is not None:
            self._EndIpv4Address = EndIpv4Address
            properties['EndIpv4Address'] = EndIpv4Address
        if GatewayIp is not None:
            self._GatewayIp = GatewayIp
            properties['GatewayIp'] = GatewayIp
        if EnableIncludeRouterMac is not None:
            self._EnableIncludeRouterMac = EnableIncludeRouterMac
            properties['EnableIncludeRouterMac'] = EnableIncludeRouterMac
        if RouterMac is not None:
            self._RouterMac = RouterMac
            properties['RouterMac'] = RouterMac

        super(EvpnRouteIpPrefixConfig, self).edit(**properties)

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
    def RouteNumber(self):
        """
        get the value of property _RouteNumber
        """
        if self.force_auto_sync:
            self.get('RouteNumber')
        return self._RouteNumber

    @property
    def NetWorkCount(self):
        """
        get the value of property _NetWorkCount
        """
        if self.force_auto_sync:
            self.get('NetWorkCount')
        return self._NetWorkCount

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

    @property
    def StartIpv4(self):
        """
        get the value of property _StartIpv4
        """
        if self.force_auto_sync:
            self.get('StartIpv4')
        return self._StartIpv4

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def Ipv4Increment(self):
        """
        get the value of property _Ipv4Increment
        """
        if self.force_auto_sync:
            self.get('Ipv4Increment')
        return self._Ipv4Increment

    @property
    def EndIpv4Address(self):
        """
        get the value of property _EndIpv4Address
        """
        if self.force_auto_sync:
            self.get('EndIpv4Address')
        return self._EndIpv4Address

    @property
    def GatewayIp(self):
        """
        get the value of property _GatewayIp
        """
        if self.force_auto_sync:
            self.get('GatewayIp')
        return self._GatewayIp

    @property
    def EnableIncludeRouterMac(self):
        """
        get the value of property _EnableIncludeRouterMac
        """
        if self.force_auto_sync:
            self.get('EnableIncludeRouterMac')
        return self._EnableIncludeRouterMac

    @property
    def RouterMac(self):
        """
        get the value of property _RouterMac
        """
        if self.force_auto_sync:
            self.get('RouterMac')
        return self._RouterMac

    @RouteBlockName.setter
    def RouteBlockName(self, value):
        self._RouteBlockName = value
        self.edit(RouteBlockName=value)

    @EviCount.setter
    def EviCount(self, value):
        self._EviCount = value
        self.edit(EviCount=value)

    @RouteNumber.setter
    def RouteNumber(self, value):
        self._RouteNumber = value
        self.edit(RouteNumber=value)

    @NetWorkCount.setter
    def NetWorkCount(self, value):
        self._NetWorkCount = value
        self.edit(NetWorkCount=value)

    @Vni.setter
    def Vni(self, value):
        self._Vni = value
        self.edit(Vni=value)

    @VniStep.setter
    def VniStep(self, value):
        self._VniStep = value
        self.edit(VniStep=value)

    @StartIpv4.setter
    def StartIpv4(self, value):
        self._StartIpv4 = value
        self.edit(StartIpv4=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @Ipv4Increment.setter
    def Ipv4Increment(self, value):
        self._Ipv4Increment = value
        self.edit(Ipv4Increment=value)

    @EndIpv4Address.setter
    def EndIpv4Address(self, value):
        self._EndIpv4Address = value
        self.edit(EndIpv4Address=value)

    @GatewayIp.setter
    def GatewayIp(self, value):
        self._GatewayIp = value
        self.edit(GatewayIp=value)

    @EnableIncludeRouterMac.setter
    def EnableIncludeRouterMac(self, value):
        self._EnableIncludeRouterMac = value
        self.edit(EnableIncludeRouterMac=value)

    @RouterMac.setter
    def RouterMac(self, value):
        self._RouterMac = value
        self.edit(RouterMac=value)

    def _set_routeblockname_with_str(self, value):
        self._RouteBlockName = value

    def _set_evicount_with_str(self, value):
        try:
            self._EviCount = int(value)
        except ValueError:
            self._EviCount = hex(int(value, 16))

    def _set_routenumber_with_str(self, value):
        try:
            self._RouteNumber = int(value)
        except ValueError:
            self._RouteNumber = hex(int(value, 16))

    def _set_networkcount_with_str(self, value):
        try:
            self._NetWorkCount = int(value)
        except ValueError:
            self._NetWorkCount = hex(int(value, 16))

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

    def _set_startipv4_with_str(self, value):
        self._StartIpv4 = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_ipv4increment_with_str(self, value):
        try:
            self._Ipv4Increment = int(value)
        except ValueError:
            self._Ipv4Increment = hex(int(value, 16))

    def _set_endipv4address_with_str(self, value):
        self._EndIpv4Address = value

    def _set_gatewayip_with_str(self, value):
        self._GatewayIp = value

    def _set_enableincluderoutermac_with_str(self, value):
        self._EnableIncludeRouterMac = (value == 'True')

    def _set_routermac_with_str(self, value):
        self._RouterMac = value

