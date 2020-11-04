"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class BgpRouteWizardConfig(WizardConfigBase):
    def __init__(self, BgpRouteType=None, RoutesBlockCount=None, FirstRoute=None, RandomRoute=None, RouteStep=None, LastRoute=None, PrefixLength=None, EndPrefixLength=None, RouteCountPerRoutesBlock=None, UseSessionAddressAsNextHop=None, NextHop=None, NextHopStep=None, LocalPref=None, LocalPrefStep=None, EnableMed=None, MultExitDisc=None, MultExitDiscStep=None, Ipv6RoutesBlockCount=None, FirstIpv6Route=None, RandomIpv6Route=None, Ipv6RouteStep=None, LastIpv6Route=None, Ipv6PrefixLength=None, EndIpv6PrefixLength=None, Ipv6RouteCountPerRoutesBlock=None, Ipv6RouteUseSessionAddressAsNextHop=None, Ipv6NextHop=None, Ipv6NextHopStep=None, LinkLocalNextHop=None, LinkLocalNextHopStep=None, Ipv6RouteLocalPref=None, Ipv6RouteLocalPrefStep=None, Ipv6RouteEnableMed=None, Ipv6RouteMultExitDisc=None, Ipv6RouteMultExitDiscStep=None, **kwargs):
        self._BgpRouteType = BgpRouteType  # BGP Routes Type
        self._RoutesBlockCount = RoutesBlockCount  # Routes Block Count per BGP Block
        self._FirstRoute = FirstRoute  # First IPv4 Route
        self._RandomRoute = RandomRoute  # Enable Random Routes
        self._RouteStep = RouteStep  # IPv4 Route Step
        self._LastRoute = LastRoute  # End IPv4 Route
        self._PrefixLength = PrefixLength  # IPv4 Route Prefix Length
        self._EndPrefixLength = EndPrefixLength  # End IPv4 Route Prefix Length
        self._RouteCountPerRoutesBlock = RouteCountPerRoutesBlock  # Route Count Per Routes Block
        self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop  # Use Session Address as Next Hop
        self._NextHop = NextHop  # Next Hop
        self._NextHopStep = NextHopStep  # Next Hop Step
        self._LocalPref = LocalPref  # Local Preference
        self._LocalPrefStep = LocalPrefStep  # Local Preference Step
        self._EnableMed = EnableMed  # Enable Multi Exit Discriminator
        self._MultExitDisc = MultExitDisc  # Multi Exit Discriminator
        self._MultExitDiscStep = MultExitDiscStep  # Multi Exit Discriminator Step
        self._Ipv6RoutesBlockCount = Ipv6RoutesBlockCount  # Routes Block Count per BGP block
        self._FirstIpv6Route = FirstIpv6Route  # First IPv6 Route
        self._RandomIpv6Route = RandomIpv6Route  # Enable Random IPv6 Routes
        self._Ipv6RouteStep = Ipv6RouteStep  # IPv6 Route Step
        self._LastIpv6Route = LastIpv6Route  # End IPv6 Route
        self._Ipv6PrefixLength = Ipv6PrefixLength  # IPv6 Route Prefix Length
        self._EndIpv6PrefixLength = EndIpv6PrefixLength  # End IPv6 Route Prefix Length
        self._Ipv6RouteCountPerRoutesBlock = Ipv6RouteCountPerRoutesBlock  # IPv6 Route Count Per Routes Block
        self._Ipv6RouteUseSessionAddressAsNextHop = Ipv6RouteUseSessionAddressAsNextHop  # Use Session Address as Next Hop
        self._Ipv6NextHop = Ipv6NextHop  # Next Hop
        self._Ipv6NextHopStep = Ipv6NextHopStep  # Next Hop Step
        self._LinkLocalNextHop = LinkLocalNextHop  # Link Local Next Hop
        self._LinkLocalNextHopStep = LinkLocalNextHopStep  # Link Local Next Hop Step
        self._Ipv6RouteLocalPref = Ipv6RouteLocalPref  # Local Preference
        self._Ipv6RouteLocalPrefStep = Ipv6RouteLocalPrefStep  # Local Preference Step
        self._Ipv6RouteEnableMed = Ipv6RouteEnableMed  # Enable Multi Exit Discriminator
        self._Ipv6RouteMultExitDisc = Ipv6RouteMultExitDisc  # Multi Exit Discriminator
        self._Ipv6RouteMultExitDiscStep = Ipv6RouteMultExitDiscStep  # Multi Exit Discriminator Step

        properties = kwargs.copy()
        if BgpRouteType is not None:
            properties['BgpRouteType'] = BgpRouteType
        if RoutesBlockCount is not None:
            properties['RoutesBlockCount'] = RoutesBlockCount
        if FirstRoute is not None:
            properties['FirstRoute'] = FirstRoute
        if RandomRoute is not None:
            properties['RandomRoute'] = RandomRoute
        if RouteStep is not None:
            properties['RouteStep'] = RouteStep
        if LastRoute is not None:
            properties['LastRoute'] = LastRoute
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if EndPrefixLength is not None:
            properties['EndPrefixLength'] = EndPrefixLength
        if RouteCountPerRoutesBlock is not None:
            properties['RouteCountPerRoutesBlock'] = RouteCountPerRoutesBlock
        if UseSessionAddressAsNextHop is not None:
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if NextHop is not None:
            properties['NextHop'] = NextHop
        if NextHopStep is not None:
            properties['NextHopStep'] = NextHopStep
        if LocalPref is not None:
            properties['LocalPref'] = LocalPref
        if LocalPrefStep is not None:
            properties['LocalPrefStep'] = LocalPrefStep
        if EnableMed is not None:
            properties['EnableMed'] = EnableMed
        if MultExitDisc is not None:
            properties['MultExitDisc'] = MultExitDisc
        if MultExitDiscStep is not None:
            properties['MultExitDiscStep'] = MultExitDiscStep
        if Ipv6RoutesBlockCount is not None:
            properties['Ipv6RoutesBlockCount'] = Ipv6RoutesBlockCount
        if FirstIpv6Route is not None:
            properties['FirstIpv6Route'] = FirstIpv6Route
        if RandomIpv6Route is not None:
            properties['RandomIpv6Route'] = RandomIpv6Route
        if Ipv6RouteStep is not None:
            properties['Ipv6RouteStep'] = Ipv6RouteStep
        if LastIpv6Route is not None:
            properties['LastIpv6Route'] = LastIpv6Route
        if Ipv6PrefixLength is not None:
            properties['Ipv6PrefixLength'] = Ipv6PrefixLength
        if EndIpv6PrefixLength is not None:
            properties['EndIpv6PrefixLength'] = EndIpv6PrefixLength
        if Ipv6RouteCountPerRoutesBlock is not None:
            properties['Ipv6RouteCountPerRoutesBlock'] = Ipv6RouteCountPerRoutesBlock
        if Ipv6RouteUseSessionAddressAsNextHop is not None:
            properties['Ipv6RouteUseSessionAddressAsNextHop'] = Ipv6RouteUseSessionAddressAsNextHop
        if Ipv6NextHop is not None:
            properties['Ipv6NextHop'] = Ipv6NextHop
        if Ipv6NextHopStep is not None:
            properties['Ipv6NextHopStep'] = Ipv6NextHopStep
        if LinkLocalNextHop is not None:
            properties['LinkLocalNextHop'] = LinkLocalNextHop
        if LinkLocalNextHopStep is not None:
            properties['LinkLocalNextHopStep'] = LinkLocalNextHopStep
        if Ipv6RouteLocalPref is not None:
            properties['Ipv6RouteLocalPref'] = Ipv6RouteLocalPref
        if Ipv6RouteLocalPrefStep is not None:
            properties['Ipv6RouteLocalPrefStep'] = Ipv6RouteLocalPrefStep
        if Ipv6RouteEnableMed is not None:
            properties['Ipv6RouteEnableMed'] = Ipv6RouteEnableMed
        if Ipv6RouteMultExitDisc is not None:
            properties['Ipv6RouteMultExitDisc'] = Ipv6RouteMultExitDisc
        if Ipv6RouteMultExitDiscStep is not None:
            properties['Ipv6RouteMultExitDiscStep'] = Ipv6RouteMultExitDiscStep

        # call base class function, and it will send message to renix server to create a class.
        super(BgpRouteWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, BgpRouteType=None, RoutesBlockCount=None, FirstRoute=None, RandomRoute=None, RouteStep=None, LastRoute=None, PrefixLength=None, EndPrefixLength=None, RouteCountPerRoutesBlock=None, UseSessionAddressAsNextHop=None, NextHop=None, NextHopStep=None, LocalPref=None, LocalPrefStep=None, EnableMed=None, MultExitDisc=None, MultExitDiscStep=None, Ipv6RoutesBlockCount=None, FirstIpv6Route=None, RandomIpv6Route=None, Ipv6RouteStep=None, LastIpv6Route=None, Ipv6PrefixLength=None, EndIpv6PrefixLength=None, Ipv6RouteCountPerRoutesBlock=None, Ipv6RouteUseSessionAddressAsNextHop=None, Ipv6NextHop=None, Ipv6NextHopStep=None, LinkLocalNextHop=None, LinkLocalNextHopStep=None, Ipv6RouteLocalPref=None, Ipv6RouteLocalPrefStep=None, Ipv6RouteEnableMed=None, Ipv6RouteMultExitDisc=None, Ipv6RouteMultExitDiscStep=None, **kwargs):
        properties = kwargs.copy()
        if BgpRouteType is not None:
            self._BgpRouteType = BgpRouteType
            properties['BgpRouteType'] = BgpRouteType
        if RoutesBlockCount is not None:
            self._RoutesBlockCount = RoutesBlockCount
            properties['RoutesBlockCount'] = RoutesBlockCount
        if FirstRoute is not None:
            self._FirstRoute = FirstRoute
            properties['FirstRoute'] = FirstRoute
        if RandomRoute is not None:
            self._RandomRoute = RandomRoute
            properties['RandomRoute'] = RandomRoute
        if RouteStep is not None:
            self._RouteStep = RouteStep
            properties['RouteStep'] = RouteStep
        if LastRoute is not None:
            self._LastRoute = LastRoute
            properties['LastRoute'] = LastRoute
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if EndPrefixLength is not None:
            self._EndPrefixLength = EndPrefixLength
            properties['EndPrefixLength'] = EndPrefixLength
        if RouteCountPerRoutesBlock is not None:
            self._RouteCountPerRoutesBlock = RouteCountPerRoutesBlock
            properties['RouteCountPerRoutesBlock'] = RouteCountPerRoutesBlock
        if UseSessionAddressAsNextHop is not None:
            self._UseSessionAddressAsNextHop = UseSessionAddressAsNextHop
            properties['UseSessionAddressAsNextHop'] = UseSessionAddressAsNextHop
        if NextHop is not None:
            self._NextHop = NextHop
            properties['NextHop'] = NextHop
        if NextHopStep is not None:
            self._NextHopStep = NextHopStep
            properties['NextHopStep'] = NextHopStep
        if LocalPref is not None:
            self._LocalPref = LocalPref
            properties['LocalPref'] = LocalPref
        if LocalPrefStep is not None:
            self._LocalPrefStep = LocalPrefStep
            properties['LocalPrefStep'] = LocalPrefStep
        if EnableMed is not None:
            self._EnableMed = EnableMed
            properties['EnableMed'] = EnableMed
        if MultExitDisc is not None:
            self._MultExitDisc = MultExitDisc
            properties['MultExitDisc'] = MultExitDisc
        if MultExitDiscStep is not None:
            self._MultExitDiscStep = MultExitDiscStep
            properties['MultExitDiscStep'] = MultExitDiscStep
        if Ipv6RoutesBlockCount is not None:
            self._Ipv6RoutesBlockCount = Ipv6RoutesBlockCount
            properties['Ipv6RoutesBlockCount'] = Ipv6RoutesBlockCount
        if FirstIpv6Route is not None:
            self._FirstIpv6Route = FirstIpv6Route
            properties['FirstIpv6Route'] = FirstIpv6Route
        if RandomIpv6Route is not None:
            self._RandomIpv6Route = RandomIpv6Route
            properties['RandomIpv6Route'] = RandomIpv6Route
        if Ipv6RouteStep is not None:
            self._Ipv6RouteStep = Ipv6RouteStep
            properties['Ipv6RouteStep'] = Ipv6RouteStep
        if LastIpv6Route is not None:
            self._LastIpv6Route = LastIpv6Route
            properties['LastIpv6Route'] = LastIpv6Route
        if Ipv6PrefixLength is not None:
            self._Ipv6PrefixLength = Ipv6PrefixLength
            properties['Ipv6PrefixLength'] = Ipv6PrefixLength
        if EndIpv6PrefixLength is not None:
            self._EndIpv6PrefixLength = EndIpv6PrefixLength
            properties['EndIpv6PrefixLength'] = EndIpv6PrefixLength
        if Ipv6RouteCountPerRoutesBlock is not None:
            self._Ipv6RouteCountPerRoutesBlock = Ipv6RouteCountPerRoutesBlock
            properties['Ipv6RouteCountPerRoutesBlock'] = Ipv6RouteCountPerRoutesBlock
        if Ipv6RouteUseSessionAddressAsNextHop is not None:
            self._Ipv6RouteUseSessionAddressAsNextHop = Ipv6RouteUseSessionAddressAsNextHop
            properties['Ipv6RouteUseSessionAddressAsNextHop'] = Ipv6RouteUseSessionAddressAsNextHop
        if Ipv6NextHop is not None:
            self._Ipv6NextHop = Ipv6NextHop
            properties['Ipv6NextHop'] = Ipv6NextHop
        if Ipv6NextHopStep is not None:
            self._Ipv6NextHopStep = Ipv6NextHopStep
            properties['Ipv6NextHopStep'] = Ipv6NextHopStep
        if LinkLocalNextHop is not None:
            self._LinkLocalNextHop = LinkLocalNextHop
            properties['LinkLocalNextHop'] = LinkLocalNextHop
        if LinkLocalNextHopStep is not None:
            self._LinkLocalNextHopStep = LinkLocalNextHopStep
            properties['LinkLocalNextHopStep'] = LinkLocalNextHopStep
        if Ipv6RouteLocalPref is not None:
            self._Ipv6RouteLocalPref = Ipv6RouteLocalPref
            properties['Ipv6RouteLocalPref'] = Ipv6RouteLocalPref
        if Ipv6RouteLocalPrefStep is not None:
            self._Ipv6RouteLocalPrefStep = Ipv6RouteLocalPrefStep
            properties['Ipv6RouteLocalPrefStep'] = Ipv6RouteLocalPrefStep
        if Ipv6RouteEnableMed is not None:
            self._Ipv6RouteEnableMed = Ipv6RouteEnableMed
            properties['Ipv6RouteEnableMed'] = Ipv6RouteEnableMed
        if Ipv6RouteMultExitDisc is not None:
            self._Ipv6RouteMultExitDisc = Ipv6RouteMultExitDisc
            properties['Ipv6RouteMultExitDisc'] = Ipv6RouteMultExitDisc
        if Ipv6RouteMultExitDiscStep is not None:
            self._Ipv6RouteMultExitDiscStep = Ipv6RouteMultExitDiscStep
            properties['Ipv6RouteMultExitDiscStep'] = Ipv6RouteMultExitDiscStep

        super(BgpRouteWizardConfig, self).edit(**properties)

    @property
    def BgpRouteType(self):
        """
        get the value of property _BgpRouteType
        """
        if self.force_auto_sync:
            self.get('BgpRouteType')
        return self._BgpRouteType

    @property
    def RoutesBlockCount(self):
        """
        get the value of property _RoutesBlockCount
        """
        if self.force_auto_sync:
            self.get('RoutesBlockCount')
        return self._RoutesBlockCount

    @property
    def FirstRoute(self):
        """
        get the value of property _FirstRoute
        """
        if self.force_auto_sync:
            self.get('FirstRoute')
        return self._FirstRoute

    @property
    def RandomRoute(self):
        """
        get the value of property _RandomRoute
        """
        if self.force_auto_sync:
            self.get('RandomRoute')
        return self._RandomRoute

    @property
    def RouteStep(self):
        """
        get the value of property _RouteStep
        """
        if self.force_auto_sync:
            self.get('RouteStep')
        return self._RouteStep

    @property
    def LastRoute(self):
        """
        get the value of property _LastRoute
        """
        if self.force_auto_sync:
            self.get('LastRoute')
        return self._LastRoute

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def EndPrefixLength(self):
        """
        get the value of property _EndPrefixLength
        """
        if self.force_auto_sync:
            self.get('EndPrefixLength')
        return self._EndPrefixLength

    @property
    def RouteCountPerRoutesBlock(self):
        """
        get the value of property _RouteCountPerRoutesBlock
        """
        if self.force_auto_sync:
            self.get('RouteCountPerRoutesBlock')
        return self._RouteCountPerRoutesBlock

    @property
    def UseSessionAddressAsNextHop(self):
        """
        get the value of property _UseSessionAddressAsNextHop
        """
        if self.force_auto_sync:
            self.get('UseSessionAddressAsNextHop')
        return self._UseSessionAddressAsNextHop

    @property
    def NextHop(self):
        """
        get the value of property _NextHop
        """
        if self.force_auto_sync:
            self.get('NextHop')
        return self._NextHop

    @property
    def NextHopStep(self):
        """
        get the value of property _NextHopStep
        """
        if self.force_auto_sync:
            self.get('NextHopStep')
        return self._NextHopStep

    @property
    def LocalPref(self):
        """
        get the value of property _LocalPref
        """
        if self.force_auto_sync:
            self.get('LocalPref')
        return self._LocalPref

    @property
    def LocalPrefStep(self):
        """
        get the value of property _LocalPrefStep
        """
        if self.force_auto_sync:
            self.get('LocalPrefStep')
        return self._LocalPrefStep

    @property
    def EnableMed(self):
        """
        get the value of property _EnableMed
        """
        if self.force_auto_sync:
            self.get('EnableMed')
        return self._EnableMed

    @property
    def MultExitDisc(self):
        """
        get the value of property _MultExitDisc
        """
        if self.force_auto_sync:
            self.get('MultExitDisc')
        return self._MultExitDisc

    @property
    def MultExitDiscStep(self):
        """
        get the value of property _MultExitDiscStep
        """
        if self.force_auto_sync:
            self.get('MultExitDiscStep')
        return self._MultExitDiscStep

    @property
    def Ipv6RoutesBlockCount(self):
        """
        get the value of property _Ipv6RoutesBlockCount
        """
        if self.force_auto_sync:
            self.get('Ipv6RoutesBlockCount')
        return self._Ipv6RoutesBlockCount

    @property
    def FirstIpv6Route(self):
        """
        get the value of property _FirstIpv6Route
        """
        if self.force_auto_sync:
            self.get('FirstIpv6Route')
        return self._FirstIpv6Route

    @property
    def RandomIpv6Route(self):
        """
        get the value of property _RandomIpv6Route
        """
        if self.force_auto_sync:
            self.get('RandomIpv6Route')
        return self._RandomIpv6Route

    @property
    def Ipv6RouteStep(self):
        """
        get the value of property _Ipv6RouteStep
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteStep')
        return self._Ipv6RouteStep

    @property
    def LastIpv6Route(self):
        """
        get the value of property _LastIpv6Route
        """
        if self.force_auto_sync:
            self.get('LastIpv6Route')
        return self._LastIpv6Route

    @property
    def Ipv6PrefixLength(self):
        """
        get the value of property _Ipv6PrefixLength
        """
        if self.force_auto_sync:
            self.get('Ipv6PrefixLength')
        return self._Ipv6PrefixLength

    @property
    def EndIpv6PrefixLength(self):
        """
        get the value of property _EndIpv6PrefixLength
        """
        if self.force_auto_sync:
            self.get('EndIpv6PrefixLength')
        return self._EndIpv6PrefixLength

    @property
    def Ipv6RouteCountPerRoutesBlock(self):
        """
        get the value of property _Ipv6RouteCountPerRoutesBlock
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteCountPerRoutesBlock')
        return self._Ipv6RouteCountPerRoutesBlock

    @property
    def Ipv6RouteUseSessionAddressAsNextHop(self):
        """
        get the value of property _Ipv6RouteUseSessionAddressAsNextHop
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteUseSessionAddressAsNextHop')
        return self._Ipv6RouteUseSessionAddressAsNextHop

    @property
    def Ipv6NextHop(self):
        """
        get the value of property _Ipv6NextHop
        """
        if self.force_auto_sync:
            self.get('Ipv6NextHop')
        return self._Ipv6NextHop

    @property
    def Ipv6NextHopStep(self):
        """
        get the value of property _Ipv6NextHopStep
        """
        if self.force_auto_sync:
            self.get('Ipv6NextHopStep')
        return self._Ipv6NextHopStep

    @property
    def LinkLocalNextHop(self):
        """
        get the value of property _LinkLocalNextHop
        """
        if self.force_auto_sync:
            self.get('LinkLocalNextHop')
        return self._LinkLocalNextHop

    @property
    def LinkLocalNextHopStep(self):
        """
        get the value of property _LinkLocalNextHopStep
        """
        if self.force_auto_sync:
            self.get('LinkLocalNextHopStep')
        return self._LinkLocalNextHopStep

    @property
    def Ipv6RouteLocalPref(self):
        """
        get the value of property _Ipv6RouteLocalPref
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteLocalPref')
        return self._Ipv6RouteLocalPref

    @property
    def Ipv6RouteLocalPrefStep(self):
        """
        get the value of property _Ipv6RouteLocalPrefStep
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteLocalPrefStep')
        return self._Ipv6RouteLocalPrefStep

    @property
    def Ipv6RouteEnableMed(self):
        """
        get the value of property _Ipv6RouteEnableMed
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteEnableMed')
        return self._Ipv6RouteEnableMed

    @property
    def Ipv6RouteMultExitDisc(self):
        """
        get the value of property _Ipv6RouteMultExitDisc
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteMultExitDisc')
        return self._Ipv6RouteMultExitDisc

    @property
    def Ipv6RouteMultExitDiscStep(self):
        """
        get the value of property _Ipv6RouteMultExitDiscStep
        """
        if self.force_auto_sync:
            self.get('Ipv6RouteMultExitDiscStep')
        return self._Ipv6RouteMultExitDiscStep

    @BgpRouteType.setter
    def BgpRouteType(self, value):
        self._BgpRouteType = value
        self.edit(BgpRouteType=value)

    @RoutesBlockCount.setter
    def RoutesBlockCount(self, value):
        self._RoutesBlockCount = value
        self.edit(RoutesBlockCount=value)

    @FirstRoute.setter
    def FirstRoute(self, value):
        self._FirstRoute = value
        self.edit(FirstRoute=value)

    @RandomRoute.setter
    def RandomRoute(self, value):
        self._RandomRoute = value
        self.edit(RandomRoute=value)

    @RouteStep.setter
    def RouteStep(self, value):
        self._RouteStep = value
        self.edit(RouteStep=value)

    @LastRoute.setter
    def LastRoute(self, value):
        self._LastRoute = value
        self.edit(LastRoute=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @EndPrefixLength.setter
    def EndPrefixLength(self, value):
        self._EndPrefixLength = value
        self.edit(EndPrefixLength=value)

    @RouteCountPerRoutesBlock.setter
    def RouteCountPerRoutesBlock(self, value):
        self._RouteCountPerRoutesBlock = value
        self.edit(RouteCountPerRoutesBlock=value)

    @UseSessionAddressAsNextHop.setter
    def UseSessionAddressAsNextHop(self, value):
        self._UseSessionAddressAsNextHop = value
        self.edit(UseSessionAddressAsNextHop=value)

    @NextHop.setter
    def NextHop(self, value):
        self._NextHop = value
        self.edit(NextHop=value)

    @NextHopStep.setter
    def NextHopStep(self, value):
        self._NextHopStep = value
        self.edit(NextHopStep=value)

    @LocalPref.setter
    def LocalPref(self, value):
        self._LocalPref = value
        self.edit(LocalPref=value)

    @LocalPrefStep.setter
    def LocalPrefStep(self, value):
        self._LocalPrefStep = value
        self.edit(LocalPrefStep=value)

    @EnableMed.setter
    def EnableMed(self, value):
        self._EnableMed = value
        self.edit(EnableMed=value)

    @MultExitDisc.setter
    def MultExitDisc(self, value):
        self._MultExitDisc = value
        self.edit(MultExitDisc=value)

    @MultExitDiscStep.setter
    def MultExitDiscStep(self, value):
        self._MultExitDiscStep = value
        self.edit(MultExitDiscStep=value)

    @Ipv6RoutesBlockCount.setter
    def Ipv6RoutesBlockCount(self, value):
        self._Ipv6RoutesBlockCount = value
        self.edit(Ipv6RoutesBlockCount=value)

    @FirstIpv6Route.setter
    def FirstIpv6Route(self, value):
        self._FirstIpv6Route = value
        self.edit(FirstIpv6Route=value)

    @RandomIpv6Route.setter
    def RandomIpv6Route(self, value):
        self._RandomIpv6Route = value
        self.edit(RandomIpv6Route=value)

    @Ipv6RouteStep.setter
    def Ipv6RouteStep(self, value):
        self._Ipv6RouteStep = value
        self.edit(Ipv6RouteStep=value)

    @LastIpv6Route.setter
    def LastIpv6Route(self, value):
        self._LastIpv6Route = value
        self.edit(LastIpv6Route=value)

    @Ipv6PrefixLength.setter
    def Ipv6PrefixLength(self, value):
        self._Ipv6PrefixLength = value
        self.edit(Ipv6PrefixLength=value)

    @EndIpv6PrefixLength.setter
    def EndIpv6PrefixLength(self, value):
        self._EndIpv6PrefixLength = value
        self.edit(EndIpv6PrefixLength=value)

    @Ipv6RouteCountPerRoutesBlock.setter
    def Ipv6RouteCountPerRoutesBlock(self, value):
        self._Ipv6RouteCountPerRoutesBlock = value
        self.edit(Ipv6RouteCountPerRoutesBlock=value)

    @Ipv6RouteUseSessionAddressAsNextHop.setter
    def Ipv6RouteUseSessionAddressAsNextHop(self, value):
        self._Ipv6RouteUseSessionAddressAsNextHop = value
        self.edit(Ipv6RouteUseSessionAddressAsNextHop=value)

    @Ipv6NextHop.setter
    def Ipv6NextHop(self, value):
        self._Ipv6NextHop = value
        self.edit(Ipv6NextHop=value)

    @Ipv6NextHopStep.setter
    def Ipv6NextHopStep(self, value):
        self._Ipv6NextHopStep = value
        self.edit(Ipv6NextHopStep=value)

    @LinkLocalNextHop.setter
    def LinkLocalNextHop(self, value):
        self._LinkLocalNextHop = value
        self.edit(LinkLocalNextHop=value)

    @LinkLocalNextHopStep.setter
    def LinkLocalNextHopStep(self, value):
        self._LinkLocalNextHopStep = value
        self.edit(LinkLocalNextHopStep=value)

    @Ipv6RouteLocalPref.setter
    def Ipv6RouteLocalPref(self, value):
        self._Ipv6RouteLocalPref = value
        self.edit(Ipv6RouteLocalPref=value)

    @Ipv6RouteLocalPrefStep.setter
    def Ipv6RouteLocalPrefStep(self, value):
        self._Ipv6RouteLocalPrefStep = value
        self.edit(Ipv6RouteLocalPrefStep=value)

    @Ipv6RouteEnableMed.setter
    def Ipv6RouteEnableMed(self, value):
        self._Ipv6RouteEnableMed = value
        self.edit(Ipv6RouteEnableMed=value)

    @Ipv6RouteMultExitDisc.setter
    def Ipv6RouteMultExitDisc(self, value):
        self._Ipv6RouteMultExitDisc = value
        self.edit(Ipv6RouteMultExitDisc=value)

    @Ipv6RouteMultExitDiscStep.setter
    def Ipv6RouteMultExitDiscStep(self, value):
        self._Ipv6RouteMultExitDiscStep = value
        self.edit(Ipv6RouteMultExitDiscStep=value)

    def _set_bgproutetype_with_str(self, value):
        seperate = value.find(':')
        exec('self._BgpRouteType = EnumBgpWizardRouteType.%s' % value[:seperate])

    def _set_routesblockcount_with_str(self, value):
        try:
            self._RoutesBlockCount = int(value)
        except ValueError:
            self._RoutesBlockCount = hex(int(value, 16))

    def _set_firstroute_with_str(self, value):
        self._FirstRoute = value

    def _set_randomroute_with_str(self, value):
        self._RandomRoute = (value == 'True')

    def _set_routestep_with_str(self, value):
        try:
            self._RouteStep = int(value)
        except ValueError:
            self._RouteStep = hex(int(value, 16))

    def _set_lastroute_with_str(self, value):
        self._LastRoute = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_endprefixlength_with_str(self, value):
        try:
            self._EndPrefixLength = int(value)
        except ValueError:
            self._EndPrefixLength = hex(int(value, 16))

    def _set_routecountperroutesblock_with_str(self, value):
        try:
            self._RouteCountPerRoutesBlock = int(value)
        except ValueError:
            self._RouteCountPerRoutesBlock = hex(int(value, 16))

    def _set_usesessionaddressasnexthop_with_str(self, value):
        self._UseSessionAddressAsNextHop = (value == 'True')

    def _set_nexthop_with_str(self, value):
        self._NextHop = value

    def _set_nexthopstep_with_str(self, value):
        self._NextHopStep = value

    def _set_localpref_with_str(self, value):
        try:
            self._LocalPref = int(value)
        except ValueError:
            self._LocalPref = hex(int(value, 16))

    def _set_localprefstep_with_str(self, value):
        try:
            self._LocalPrefStep = int(value)
        except ValueError:
            self._LocalPrefStep = hex(int(value, 16))

    def _set_enablemed_with_str(self, value):
        self._EnableMed = (value == 'True')

    def _set_multexitdisc_with_str(self, value):
        try:
            self._MultExitDisc = int(value)
        except ValueError:
            self._MultExitDisc = hex(int(value, 16))

    def _set_multexitdiscstep_with_str(self, value):
        try:
            self._MultExitDiscStep = int(value)
        except ValueError:
            self._MultExitDiscStep = hex(int(value, 16))

    def _set_ipv6routesblockcount_with_str(self, value):
        try:
            self._Ipv6RoutesBlockCount = int(value)
        except ValueError:
            self._Ipv6RoutesBlockCount = hex(int(value, 16))

    def _set_firstipv6route_with_str(self, value):
        self._FirstIpv6Route = value

    def _set_randomipv6route_with_str(self, value):
        self._RandomIpv6Route = (value == 'True')

    def _set_ipv6routestep_with_str(self, value):
        try:
            self._Ipv6RouteStep = int(value)
        except ValueError:
            self._Ipv6RouteStep = hex(int(value, 16))

    def _set_lastipv6route_with_str(self, value):
        self._LastIpv6Route = value

    def _set_ipv6prefixlength_with_str(self, value):
        try:
            self._Ipv6PrefixLength = int(value)
        except ValueError:
            self._Ipv6PrefixLength = hex(int(value, 16))

    def _set_endipv6prefixlength_with_str(self, value):
        try:
            self._EndIpv6PrefixLength = int(value)
        except ValueError:
            self._EndIpv6PrefixLength = hex(int(value, 16))

    def _set_ipv6routecountperroutesblock_with_str(self, value):
        try:
            self._Ipv6RouteCountPerRoutesBlock = int(value)
        except ValueError:
            self._Ipv6RouteCountPerRoutesBlock = hex(int(value, 16))

    def _set_ipv6routeusesessionaddressasnexthop_with_str(self, value):
        self._Ipv6RouteUseSessionAddressAsNextHop = (value == 'True')

    def _set_ipv6nexthop_with_str(self, value):
        self._Ipv6NextHop = value

    def _set_ipv6nexthopstep_with_str(self, value):
        self._Ipv6NextHopStep = value

    def _set_linklocalnexthop_with_str(self, value):
        self._LinkLocalNextHop = value

    def _set_linklocalnexthopstep_with_str(self, value):
        self._LinkLocalNextHopStep = value

    def _set_ipv6routelocalpref_with_str(self, value):
        try:
            self._Ipv6RouteLocalPref = int(value)
        except ValueError:
            self._Ipv6RouteLocalPref = hex(int(value, 16))

    def _set_ipv6routelocalprefstep_with_str(self, value):
        try:
            self._Ipv6RouteLocalPrefStep = int(value)
        except ValueError:
            self._Ipv6RouteLocalPrefStep = hex(int(value, 16))

    def _set_ipv6routeenablemed_with_str(self, value):
        self._Ipv6RouteEnableMed = (value == 'True')

    def _set_ipv6routemultexitdisc_with_str(self, value):
        try:
            self._Ipv6RouteMultExitDisc = int(value)
        except ValueError:
            self._Ipv6RouteMultExitDisc = hex(int(value, 16))

    def _set_ipv6routemultexitdiscstep_with_str(self, value):
        try:
            self._Ipv6RouteMultExitDiscStep = int(value)
        except ValueError:
            self._Ipv6RouteMultExitDiscStep = hex(int(value, 16))

