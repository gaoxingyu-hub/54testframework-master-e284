"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class RipIpv6RouteConfig(ROMObject):
    def __init__(self, RouteCount=None, StartIpv6Prefix=None, RouteStep=None, PrefixLength=None, NextHop=None, Metric=None, RouteTag=None, **kwargs):
        self._RouteCount = RouteCount  # Number of Routes
        self._StartIpv6Prefix = StartIpv6Prefix  # Start IPv6 Prefix
        self._RouteStep = RouteStep  # IPv6 Route Step
        self._EndIpv6Prefix = '2000::'  # End IPv6 Prefix, not editable
        self._PrefixLength = PrefixLength  # Prefix Length
        self._NextHop = NextHop  # Next Hop
        self._Metric = Metric  # Metric
        self._RouteTag = RouteTag  # Route Tag

        properties = kwargs.copy()
        if RouteCount is not None:
            properties['RouteCount'] = RouteCount
        if StartIpv6Prefix is not None:
            properties['StartIpv6Prefix'] = StartIpv6Prefix
        if RouteStep is not None:
            properties['RouteStep'] = RouteStep
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if NextHop is not None:
            properties['NextHop'] = NextHop
        if Metric is not None:
            properties['Metric'] = Metric
        if RouteTag is not None:
            properties['RouteTag'] = RouteTag

        # call base class function, and it will send message to renix server to create a class.
        super(RipIpv6RouteConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RouteCount=None, StartIpv6Prefix=None, RouteStep=None, PrefixLength=None, NextHop=None, Metric=None, RouteTag=None, **kwargs):
        properties = kwargs.copy()
        if RouteCount is not None:
            self._RouteCount = RouteCount
            properties['RouteCount'] = RouteCount
        if StartIpv6Prefix is not None:
            self._StartIpv6Prefix = StartIpv6Prefix
            properties['StartIpv6Prefix'] = StartIpv6Prefix
        if RouteStep is not None:
            self._RouteStep = RouteStep
            properties['RouteStep'] = RouteStep
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if NextHop is not None:
            self._NextHop = NextHop
            properties['NextHop'] = NextHop
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric
        if RouteTag is not None:
            self._RouteTag = RouteTag
            properties['RouteTag'] = RouteTag

        super(RipIpv6RouteConfig, self).edit(**properties)

    @property
    def RouteCount(self):
        """
        get the value of property _RouteCount
        """
        if self.force_auto_sync:
            self.get('RouteCount')
        return self._RouteCount

    @property
    def StartIpv6Prefix(self):
        """
        get the value of property _StartIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('StartIpv6Prefix')
        return self._StartIpv6Prefix

    @property
    def RouteStep(self):
        """
        get the value of property _RouteStep
        """
        if self.force_auto_sync:
            self.get('RouteStep')
        return self._RouteStep

    @property
    def EndIpv6Prefix(self):
        """
        get the value of property _EndIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('EndIpv6Prefix')
        return self._EndIpv6Prefix

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def NextHop(self):
        """
        get the value of property _NextHop
        """
        if self.force_auto_sync:
            self.get('NextHop')
        return self._NextHop

    @property
    def Metric(self):
        """
        get the value of property _Metric
        """
        if self.force_auto_sync:
            self.get('Metric')
        return self._Metric

    @property
    def RouteTag(self):
        """
        get the value of property _RouteTag
        """
        if self.force_auto_sync:
            self.get('RouteTag')
        return self._RouteTag

    @RouteCount.setter
    def RouteCount(self, value):
        self._RouteCount = value
        self.edit(RouteCount=value)

    @StartIpv6Prefix.setter
    def StartIpv6Prefix(self, value):
        self._StartIpv6Prefix = value
        self.edit(StartIpv6Prefix=value)

    @RouteStep.setter
    def RouteStep(self, value):
        self._RouteStep = value
        self.edit(RouteStep=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @NextHop.setter
    def NextHop(self, value):
        self._NextHop = value
        self.edit(NextHop=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    @RouteTag.setter
    def RouteTag(self, value):
        self._RouteTag = value
        self.edit(RouteTag=value)

    def _set_routecount_with_str(self, value):
        try:
            self._RouteCount = int(value)
        except ValueError:
            self._RouteCount = hex(int(value, 16))

    def _set_startipv6prefix_with_str(self, value):
        self._StartIpv6Prefix = value

    def _set_routestep_with_str(self, value):
        self._RouteStep = value

    def _set_endipv6prefix_with_str(self, value):
        self._EndIpv6Prefix = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_nexthop_with_str(self, value):
        self._NextHop = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

    def _set_routetag_with_str(self, value):
        try:
            self._RouteTag = int(value)
        except ValueError:
            self._RouteTag = hex(int(value, 16))

