"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BgpRoutePoolBaseConfig_Autogen import BgpRoutePoolBaseConfig


@rom_manager.rom
class BgpIpv6RoutepoolConfig(BgpRoutePoolBaseConfig):
    def __init__(self, FirstIpv6Route=None, RandomIpv6Route=None, Ipv6RouteStep=None, RouteStep=None, LastIpv6Route=None, PrefixLength=None, EndPrefixLength=None, NextHop=None, NextHopStep=None, EnableLinkLocalNextHop=None, LinkLocalNextHop=None, LinkLocalNextHopStep=None, **kwargs):
        self._FirstIpv6Route = FirstIpv6Route  # First IPv6 Route
        self._RandomIpv6Route = RandomIpv6Route  # Enable Random IPv6 Routes
        self._Ipv6RouteStep = Ipv6RouteStep  # IPv6 Route Step
        self._RouteStep = RouteStep  # IPv6 Route Step
        self._LastIpv6Route = LastIpv6Route  # End IPv6 Route
        self._PrefixLength = PrefixLength  # IPv6 Route Prefix Length
        self._EndPrefixLength = EndPrefixLength  # End IPv6 Route Prefix Length
        self._NextHop = NextHop  # Next Hop
        self._NextHopStep = NextHopStep  # Next Hop Step
        self._EnableLinkLocalNextHop = EnableLinkLocalNextHop  # Enable Link Local Next Hop
        self._LinkLocalNextHop = LinkLocalNextHop  # Link Local Next Hop
        self._LinkLocalNextHopStep = LinkLocalNextHopStep  # Link Local Next Hop Step

        properties = kwargs.copy()
        if FirstIpv6Route is not None:
            properties['FirstIpv6Route'] = FirstIpv6Route
        if RandomIpv6Route is not None:
            properties['RandomIpv6Route'] = RandomIpv6Route
        if Ipv6RouteStep is not None:
            properties['Ipv6RouteStep'] = Ipv6RouteStep
        if RouteStep is not None:
            properties['RouteStep'] = RouteStep
        if LastIpv6Route is not None:
            properties['LastIpv6Route'] = LastIpv6Route
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if EndPrefixLength is not None:
            properties['EndPrefixLength'] = EndPrefixLength
        if NextHop is not None:
            properties['NextHop'] = NextHop
        if NextHopStep is not None:
            properties['NextHopStep'] = NextHopStep
        if EnableLinkLocalNextHop is not None:
            properties['EnableLinkLocalNextHop'] = EnableLinkLocalNextHop
        if LinkLocalNextHop is not None:
            properties['LinkLocalNextHop'] = LinkLocalNextHop
        if LinkLocalNextHopStep is not None:
            properties['LinkLocalNextHopStep'] = LinkLocalNextHopStep

        # call base class function, and it will send message to renix server to create a class.
        super(BgpIpv6RoutepoolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FirstIpv6Route=None, RandomIpv6Route=None, Ipv6RouteStep=None, RouteStep=None, LastIpv6Route=None, PrefixLength=None, EndPrefixLength=None, NextHop=None, NextHopStep=None, EnableLinkLocalNextHop=None, LinkLocalNextHop=None, LinkLocalNextHopStep=None, **kwargs):
        properties = kwargs.copy()
        if FirstIpv6Route is not None:
            self._FirstIpv6Route = FirstIpv6Route
            properties['FirstIpv6Route'] = FirstIpv6Route
        if RandomIpv6Route is not None:
            self._RandomIpv6Route = RandomIpv6Route
            properties['RandomIpv6Route'] = RandomIpv6Route
        if Ipv6RouteStep is not None:
            self._Ipv6RouteStep = Ipv6RouteStep
            properties['Ipv6RouteStep'] = Ipv6RouteStep
        if RouteStep is not None:
            self._RouteStep = RouteStep
            properties['RouteStep'] = RouteStep
        if LastIpv6Route is not None:
            self._LastIpv6Route = LastIpv6Route
            properties['LastIpv6Route'] = LastIpv6Route
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if EndPrefixLength is not None:
            self._EndPrefixLength = EndPrefixLength
            properties['EndPrefixLength'] = EndPrefixLength
        if NextHop is not None:
            self._NextHop = NextHop
            properties['NextHop'] = NextHop
        if NextHopStep is not None:
            self._NextHopStep = NextHopStep
            properties['NextHopStep'] = NextHopStep
        if EnableLinkLocalNextHop is not None:
            self._EnableLinkLocalNextHop = EnableLinkLocalNextHop
            properties['EnableLinkLocalNextHop'] = EnableLinkLocalNextHop
        if LinkLocalNextHop is not None:
            self._LinkLocalNextHop = LinkLocalNextHop
            properties['LinkLocalNextHop'] = LinkLocalNextHop
        if LinkLocalNextHopStep is not None:
            self._LinkLocalNextHopStep = LinkLocalNextHopStep
            properties['LinkLocalNextHopStep'] = LinkLocalNextHopStep

        super(BgpIpv6RoutepoolConfig, self).edit(**properties)

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
    def RouteStep(self):
        """
        get the value of property _RouteStep
        """
        if self.force_auto_sync:
            self.get('RouteStep')
        return self._RouteStep

    @property
    def LastIpv6Route(self):
        """
        get the value of property _LastIpv6Route
        """
        if self.force_auto_sync:
            self.get('LastIpv6Route')
        return self._LastIpv6Route

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
    def EnableLinkLocalNextHop(self):
        """
        get the value of property _EnableLinkLocalNextHop
        """
        if self.force_auto_sync:
            self.get('EnableLinkLocalNextHop')
        return self._EnableLinkLocalNextHop

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

    @RouteStep.setter
    def RouteStep(self, value):
        self._RouteStep = value
        self.edit(RouteStep=value)

    @LastIpv6Route.setter
    def LastIpv6Route(self, value):
        self._LastIpv6Route = value
        self.edit(LastIpv6Route=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @EndPrefixLength.setter
    def EndPrefixLength(self, value):
        self._EndPrefixLength = value
        self.edit(EndPrefixLength=value)

    @NextHop.setter
    def NextHop(self, value):
        self._NextHop = value
        self.edit(NextHop=value)

    @NextHopStep.setter
    def NextHopStep(self, value):
        self._NextHopStep = value
        self.edit(NextHopStep=value)

    @EnableLinkLocalNextHop.setter
    def EnableLinkLocalNextHop(self, value):
        self._EnableLinkLocalNextHop = value
        self.edit(EnableLinkLocalNextHop=value)

    @LinkLocalNextHop.setter
    def LinkLocalNextHop(self, value):
        self._LinkLocalNextHop = value
        self.edit(LinkLocalNextHop=value)

    @LinkLocalNextHopStep.setter
    def LinkLocalNextHopStep(self, value):
        self._LinkLocalNextHopStep = value
        self.edit(LinkLocalNextHopStep=value)

    def _set_firstipv6route_with_str(self, value):
        self._FirstIpv6Route = value

    def _set_randomipv6route_with_str(self, value):
        self._RandomIpv6Route = (value == 'True')

    def _set_ipv6routestep_with_str(self, value):
        try:
            self._Ipv6RouteStep = int(value)
        except ValueError:
            self._Ipv6RouteStep = hex(int(value, 16))

    def _set_routestep_with_str(self, value):
        self._RouteStep = value

    def _set_lastipv6route_with_str(self, value):
        self._LastIpv6Route = value

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

    def _set_nexthop_with_str(self, value):
        self._NextHop = value

    def _set_nexthopstep_with_str(self, value):
        self._NextHopStep = value

    def _set_enablelinklocalnexthop_with_str(self, value):
        self._EnableLinkLocalNextHop = (value == 'True')

    def _set_linklocalnexthop_with_str(self, value):
        self._LinkLocalNextHop = value

    def _set_linklocalnexthopstep_with_str(self, value):
        self._LinkLocalNextHopStep = value

