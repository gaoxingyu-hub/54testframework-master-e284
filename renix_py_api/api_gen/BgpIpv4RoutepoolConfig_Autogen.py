"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .BgpRoutePoolBaseConfig_Autogen import BgpRoutePoolBaseConfig


@rom_manager.rom
class BgpIpv4RoutepoolConfig(BgpRoutePoolBaseConfig):
    def __init__(self, FirstRoute=None, RandomRoute=None, RouteStep=None, Ipv4RouteStep=None, LastRoute=None, PrefixLength=None, EndPrefixLength=None, NextHop=None, NextHopStep=None, **kwargs):
        self._FirstRoute = FirstRoute  # First IPv4 Route
        self._RandomRoute = RandomRoute  # Enable Random Routes
        self._RouteStep = RouteStep  # IPv4 Route Step
        self._Ipv4RouteStep = Ipv4RouteStep  # IPv4 Route Step
        self._LastRoute = LastRoute  # End IPv4 Route
        self._PrefixLength = PrefixLength  # IPv4 Route Prefix Length
        self._EndPrefixLength = EndPrefixLength  # End IPv4 Route Prefix Length
        self._NextHop = NextHop  # Next Hop
        self._NextHopStep = NextHopStep  # Next Hop Step

        properties = kwargs.copy()
        if FirstRoute is not None:
            properties['FirstRoute'] = FirstRoute
        if RandomRoute is not None:
            properties['RandomRoute'] = RandomRoute
        if RouteStep is not None:
            properties['RouteStep'] = RouteStep
        if Ipv4RouteStep is not None:
            properties['Ipv4RouteStep'] = Ipv4RouteStep
        if LastRoute is not None:
            properties['LastRoute'] = LastRoute
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if EndPrefixLength is not None:
            properties['EndPrefixLength'] = EndPrefixLength
        if NextHop is not None:
            properties['NextHop'] = NextHop
        if NextHopStep is not None:
            properties['NextHopStep'] = NextHopStep

        # call base class function, and it will send message to renix server to create a class.
        super(BgpIpv4RoutepoolConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, FirstRoute=None, RandomRoute=None, RouteStep=None, Ipv4RouteStep=None, LastRoute=None, PrefixLength=None, EndPrefixLength=None, NextHop=None, NextHopStep=None, **kwargs):
        properties = kwargs.copy()
        if FirstRoute is not None:
            self._FirstRoute = FirstRoute
            properties['FirstRoute'] = FirstRoute
        if RandomRoute is not None:
            self._RandomRoute = RandomRoute
            properties['RandomRoute'] = RandomRoute
        if RouteStep is not None:
            self._RouteStep = RouteStep
            properties['RouteStep'] = RouteStep
        if Ipv4RouteStep is not None:
            self._Ipv4RouteStep = Ipv4RouteStep
            properties['Ipv4RouteStep'] = Ipv4RouteStep
        if LastRoute is not None:
            self._LastRoute = LastRoute
            properties['LastRoute'] = LastRoute
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

        super(BgpIpv4RoutepoolConfig, self).edit(**properties)

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
    def Ipv4RouteStep(self):
        """
        get the value of property _Ipv4RouteStep
        """
        if self.force_auto_sync:
            self.get('Ipv4RouteStep')
        return self._Ipv4RouteStep

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

    @Ipv4RouteStep.setter
    def Ipv4RouteStep(self, value):
        self._Ipv4RouteStep = value
        self.edit(Ipv4RouteStep=value)

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

    @NextHop.setter
    def NextHop(self, value):
        self._NextHop = value
        self.edit(NextHop=value)

    @NextHopStep.setter
    def NextHopStep(self, value):
        self._NextHopStep = value
        self.edit(NextHopStep=value)

    def _set_firstroute_with_str(self, value):
        self._FirstRoute = value

    def _set_randomroute_with_str(self, value):
        self._RandomRoute = (value == 'True')

    def _set_routestep_with_str(self, value):
        self._RouteStep = value

    def _set_ipv4routestep_with_str(self, value):
        try:
            self._Ipv4RouteStep = int(value)
        except ValueError:
            self._Ipv4RouteStep = hex(int(value, 16))

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

    def _set_nexthop_with_str(self, value):
        self._NextHop = value

    def _set_nexthopstep_with_str(self, value):
        self._NextHopStep = value

