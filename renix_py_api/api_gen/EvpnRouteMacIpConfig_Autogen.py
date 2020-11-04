"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .EvpnRouteConfig_Autogen import EvpnRouteConfig


@rom_manager.rom
class EvpnRouteMacIpConfig(EvpnRouteConfig):
    def __init__(self, RouteBlockName=None, RouteNumber=None, NetWorkCount=None, StartMacAddress=None, MacPrefixLength=None, MacIncrement=None, EndMacAddress=None, EviCount=None, AssociatedIpType=None, Vni=None, VniStep=None, StartIpv4Address=None, Ipv4PrefixLength=None, Ipv4Increment=None, EndIpv4Address=None, EnableLabel2=None, L3Vni=None, L3VniStep=None, EnableIncludeRouterMac=None, RouterMac=None, EnableIncludeDefaultGateway=None, **kwargs):
        self._RouteBlockName = RouteBlockName  # Route Block Name
        self._RouteNumber = RouteNumber  # Number Of Routes
        self._NetWorkCount = NetWorkCount  # NetWork Count
        self._StartMacAddress = StartMacAddress  # Start Mac Address
        self._MacPrefixLength = MacPrefixLength  # Mac Prefix Length
        self._MacIncrement = MacIncrement  # Mac Address Increment
        self._EndMacAddress = EndMacAddress  # End Mac Address
        self._EviCount = EviCount  # EVI Count
        self._AssociatedIpType = AssociatedIpType  # Associated Ip
        self._Vni = Vni  # Encapsulation Label
        self._VniStep = VniStep  # Encapsulation Label Step
        self._StartIpv4Address = StartIpv4Address  # Start Ipv4 Address
        self._Ipv4PrefixLength = Ipv4PrefixLength  # IP Prefix Length
        self._Ipv4Increment = Ipv4Increment  # Ipv4 Address Increment
        self._EndIpv4Address = EndIpv4Address  # End Ipv4 Address
        self._EnableLabel2 = EnableLabel2  # MPLS Label2
        self._L3Vni = L3Vni  # Encapsulation Label2
        self._L3VniStep = L3VniStep  # Encapsulation Label2 Step
        self._EnableIncludeRouterMac = EnableIncludeRouterMac  # Include Router
        self._RouterMac = RouterMac  # Router Mac Address
        self._EnableIncludeDefaultGateway = EnableIncludeDefaultGateway  # Include Default Gateway

        properties = kwargs.copy()
        if RouteBlockName is not None:
            properties['RouteBlockName'] = RouteBlockName
        if RouteNumber is not None:
            properties['RouteNumber'] = RouteNumber
        if NetWorkCount is not None:
            properties['NetWorkCount'] = NetWorkCount
        if StartMacAddress is not None:
            properties['StartMacAddress'] = StartMacAddress
        if MacPrefixLength is not None:
            properties['MacPrefixLength'] = MacPrefixLength
        if MacIncrement is not None:
            properties['MacIncrement'] = MacIncrement
        if EndMacAddress is not None:
            properties['EndMacAddress'] = EndMacAddress
        if EviCount is not None:
            properties['EviCount'] = EviCount
        if AssociatedIpType is not None:
            properties['AssociatedIpType'] = AssociatedIpType
        if Vni is not None:
            properties['Vni'] = Vni
        if VniStep is not None:
            properties['VniStep'] = VniStep
        if StartIpv4Address is not None:
            properties['StartIpv4Address'] = StartIpv4Address
        if Ipv4PrefixLength is not None:
            properties['Ipv4PrefixLength'] = Ipv4PrefixLength
        if Ipv4Increment is not None:
            properties['Ipv4Increment'] = Ipv4Increment
        if EndIpv4Address is not None:
            properties['EndIpv4Address'] = EndIpv4Address
        if EnableLabel2 is not None:
            properties['EnableLabel2'] = EnableLabel2
        if L3Vni is not None:
            properties['L3Vni'] = L3Vni
        if L3VniStep is not None:
            properties['L3VniStep'] = L3VniStep
        if EnableIncludeRouterMac is not None:
            properties['EnableIncludeRouterMac'] = EnableIncludeRouterMac
        if RouterMac is not None:
            properties['RouterMac'] = RouterMac
        if EnableIncludeDefaultGateway is not None:
            properties['EnableIncludeDefaultGateway'] = EnableIncludeDefaultGateway

        # call base class function, and it will send message to renix server to create a class.
        super(EvpnRouteMacIpConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteBlockName=None, RouteNumber=None, NetWorkCount=None, StartMacAddress=None, MacPrefixLength=None, MacIncrement=None, EndMacAddress=None, EviCount=None, AssociatedIpType=None, Vni=None, VniStep=None, StartIpv4Address=None, Ipv4PrefixLength=None, Ipv4Increment=None, EndIpv4Address=None, EnableLabel2=None, L3Vni=None, L3VniStep=None, EnableIncludeRouterMac=None, RouterMac=None, EnableIncludeDefaultGateway=None, **kwargs):
        properties = kwargs.copy()
        if RouteBlockName is not None:
            self._RouteBlockName = RouteBlockName
            properties['RouteBlockName'] = RouteBlockName
        if RouteNumber is not None:
            self._RouteNumber = RouteNumber
            properties['RouteNumber'] = RouteNumber
        if NetWorkCount is not None:
            self._NetWorkCount = NetWorkCount
            properties['NetWorkCount'] = NetWorkCount
        if StartMacAddress is not None:
            self._StartMacAddress = StartMacAddress
            properties['StartMacAddress'] = StartMacAddress
        if MacPrefixLength is not None:
            self._MacPrefixLength = MacPrefixLength
            properties['MacPrefixLength'] = MacPrefixLength
        if MacIncrement is not None:
            self._MacIncrement = MacIncrement
            properties['MacIncrement'] = MacIncrement
        if EndMacAddress is not None:
            self._EndMacAddress = EndMacAddress
            properties['EndMacAddress'] = EndMacAddress
        if EviCount is not None:
            self._EviCount = EviCount
            properties['EviCount'] = EviCount
        if AssociatedIpType is not None:
            self._AssociatedIpType = AssociatedIpType
            properties['AssociatedIpType'] = AssociatedIpType
        if Vni is not None:
            self._Vni = Vni
            properties['Vni'] = Vni
        if VniStep is not None:
            self._VniStep = VniStep
            properties['VniStep'] = VniStep
        if StartIpv4Address is not None:
            self._StartIpv4Address = StartIpv4Address
            properties['StartIpv4Address'] = StartIpv4Address
        if Ipv4PrefixLength is not None:
            self._Ipv4PrefixLength = Ipv4PrefixLength
            properties['Ipv4PrefixLength'] = Ipv4PrefixLength
        if Ipv4Increment is not None:
            self._Ipv4Increment = Ipv4Increment
            properties['Ipv4Increment'] = Ipv4Increment
        if EndIpv4Address is not None:
            self._EndIpv4Address = EndIpv4Address
            properties['EndIpv4Address'] = EndIpv4Address
        if EnableLabel2 is not None:
            self._EnableLabel2 = EnableLabel2
            properties['EnableLabel2'] = EnableLabel2
        if L3Vni is not None:
            self._L3Vni = L3Vni
            properties['L3Vni'] = L3Vni
        if L3VniStep is not None:
            self._L3VniStep = L3VniStep
            properties['L3VniStep'] = L3VniStep
        if EnableIncludeRouterMac is not None:
            self._EnableIncludeRouterMac = EnableIncludeRouterMac
            properties['EnableIncludeRouterMac'] = EnableIncludeRouterMac
        if RouterMac is not None:
            self._RouterMac = RouterMac
            properties['RouterMac'] = RouterMac
        if EnableIncludeDefaultGateway is not None:
            self._EnableIncludeDefaultGateway = EnableIncludeDefaultGateway
            properties['EnableIncludeDefaultGateway'] = EnableIncludeDefaultGateway

        super(EvpnRouteMacIpConfig, self).edit(**properties)

    @property
    def RouteBlockName(self):
        """
        get the value of property _RouteBlockName
        """
        if self.force_auto_sync:
            self.get('RouteBlockName')
        return self._RouteBlockName

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
    def StartMacAddress(self):
        """
        get the value of property _StartMacAddress
        """
        if self.force_auto_sync:
            self.get('StartMacAddress')
        return self._StartMacAddress

    @property
    def MacPrefixLength(self):
        """
        get the value of property _MacPrefixLength
        """
        if self.force_auto_sync:
            self.get('MacPrefixLength')
        return self._MacPrefixLength

    @property
    def MacIncrement(self):
        """
        get the value of property _MacIncrement
        """
        if self.force_auto_sync:
            self.get('MacIncrement')
        return self._MacIncrement

    @property
    def EndMacAddress(self):
        """
        get the value of property _EndMacAddress
        """
        if self.force_auto_sync:
            self.get('EndMacAddress')
        return self._EndMacAddress

    @property
    def EviCount(self):
        """
        get the value of property _EviCount
        """
        if self.force_auto_sync:
            self.get('EviCount')
        return self._EviCount

    @property
    def AssociatedIpType(self):
        """
        get the value of property _AssociatedIpType
        """
        if self.force_auto_sync:
            self.get('AssociatedIpType')
        return self._AssociatedIpType

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
    def StartIpv4Address(self):
        """
        get the value of property _StartIpv4Address
        """
        if self.force_auto_sync:
            self.get('StartIpv4Address')
        return self._StartIpv4Address

    @property
    def Ipv4PrefixLength(self):
        """
        get the value of property _Ipv4PrefixLength
        """
        if self.force_auto_sync:
            self.get('Ipv4PrefixLength')
        return self._Ipv4PrefixLength

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
    def EnableLabel2(self):
        """
        get the value of property _EnableLabel2
        """
        if self.force_auto_sync:
            self.get('EnableLabel2')
        return self._EnableLabel2

    @property
    def L3Vni(self):
        """
        get the value of property _L3Vni
        """
        if self.force_auto_sync:
            self.get('L3Vni')
        return self._L3Vni

    @property
    def L3VniStep(self):
        """
        get the value of property _L3VniStep
        """
        if self.force_auto_sync:
            self.get('L3VniStep')
        return self._L3VniStep

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

    @property
    def EnableIncludeDefaultGateway(self):
        """
        get the value of property _EnableIncludeDefaultGateway
        """
        if self.force_auto_sync:
            self.get('EnableIncludeDefaultGateway')
        return self._EnableIncludeDefaultGateway

    @RouteBlockName.setter
    def RouteBlockName(self, value):
        self._RouteBlockName = value
        self.edit(RouteBlockName=value)

    @RouteNumber.setter
    def RouteNumber(self, value):
        self._RouteNumber = value
        self.edit(RouteNumber=value)

    @NetWorkCount.setter
    def NetWorkCount(self, value):
        self._NetWorkCount = value
        self.edit(NetWorkCount=value)

    @StartMacAddress.setter
    def StartMacAddress(self, value):
        self._StartMacAddress = value
        self.edit(StartMacAddress=value)

    @MacPrefixLength.setter
    def MacPrefixLength(self, value):
        self._MacPrefixLength = value
        self.edit(MacPrefixLength=value)

    @MacIncrement.setter
    def MacIncrement(self, value):
        self._MacIncrement = value
        self.edit(MacIncrement=value)

    @EndMacAddress.setter
    def EndMacAddress(self, value):
        self._EndMacAddress = value
        self.edit(EndMacAddress=value)

    @EviCount.setter
    def EviCount(self, value):
        self._EviCount = value
        self.edit(EviCount=value)

    @AssociatedIpType.setter
    def AssociatedIpType(self, value):
        self._AssociatedIpType = value
        self.edit(AssociatedIpType=value)

    @Vni.setter
    def Vni(self, value):
        self._Vni = value
        self.edit(Vni=value)

    @VniStep.setter
    def VniStep(self, value):
        self._VniStep = value
        self.edit(VniStep=value)

    @StartIpv4Address.setter
    def StartIpv4Address(self, value):
        self._StartIpv4Address = value
        self.edit(StartIpv4Address=value)

    @Ipv4PrefixLength.setter
    def Ipv4PrefixLength(self, value):
        self._Ipv4PrefixLength = value
        self.edit(Ipv4PrefixLength=value)

    @Ipv4Increment.setter
    def Ipv4Increment(self, value):
        self._Ipv4Increment = value
        self.edit(Ipv4Increment=value)

    @EndIpv4Address.setter
    def EndIpv4Address(self, value):
        self._EndIpv4Address = value
        self.edit(EndIpv4Address=value)

    @EnableLabel2.setter
    def EnableLabel2(self, value):
        self._EnableLabel2 = value
        self.edit(EnableLabel2=value)

    @L3Vni.setter
    def L3Vni(self, value):
        self._L3Vni = value
        self.edit(L3Vni=value)

    @L3VniStep.setter
    def L3VniStep(self, value):
        self._L3VniStep = value
        self.edit(L3VniStep=value)

    @EnableIncludeRouterMac.setter
    def EnableIncludeRouterMac(self, value):
        self._EnableIncludeRouterMac = value
        self.edit(EnableIncludeRouterMac=value)

    @RouterMac.setter
    def RouterMac(self, value):
        self._RouterMac = value
        self.edit(RouterMac=value)

    @EnableIncludeDefaultGateway.setter
    def EnableIncludeDefaultGateway(self, value):
        self._EnableIncludeDefaultGateway = value
        self.edit(EnableIncludeDefaultGateway=value)

    def _set_routeblockname_with_str(self, value):
        self._RouteBlockName = value

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

    def _set_startmacaddress_with_str(self, value):
        self._StartMacAddress = value

    def _set_macprefixlength_with_str(self, value):
        try:
            self._MacPrefixLength = int(value)
        except ValueError:
            self._MacPrefixLength = hex(int(value, 16))

    def _set_macincrement_with_str(self, value):
        try:
            self._MacIncrement = int(value)
        except ValueError:
            self._MacIncrement = hex(int(value, 16))

    def _set_endmacaddress_with_str(self, value):
        self._EndMacAddress = value

    def _set_evicount_with_str(self, value):
        try:
            self._EviCount = int(value)
        except ValueError:
            self._EviCount = hex(int(value, 16))

    def _set_associatediptype_with_str(self, value):
        seperate = value.find(':')
        exec('self._AssociatedIpType = EnumAssociatedIpType.%s' % value[:seperate])

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

    def _set_startipv4address_with_str(self, value):
        self._StartIpv4Address = value

    def _set_ipv4prefixlength_with_str(self, value):
        try:
            self._Ipv4PrefixLength = int(value)
        except ValueError:
            self._Ipv4PrefixLength = hex(int(value, 16))

    def _set_ipv4increment_with_str(self, value):
        try:
            self._Ipv4Increment = int(value)
        except ValueError:
            self._Ipv4Increment = hex(int(value, 16))

    def _set_endipv4address_with_str(self, value):
        self._EndIpv4Address = value

    def _set_enablelabel2_with_str(self, value):
        self._EnableLabel2 = (value == 'True')

    def _set_l3vni_with_str(self, value):
        try:
            self._L3Vni = int(value)
        except ValueError:
            self._L3Vni = hex(int(value, 16))

    def _set_l3vnistep_with_str(self, value):
        try:
            self._L3VniStep = int(value)
        except ValueError:
            self._L3VniStep = hex(int(value, 16))

    def _set_enableincluderoutermac_with_str(self, value):
        self._EnableIncludeRouterMac = (value == 'True')

    def _set_routermac_with_str(self, value):
        self._RouterMac = value

    def _set_enableincludedefaultgateway_with_str(self, value):
        self._EnableIncludeDefaultGateway = (value == 'True')

