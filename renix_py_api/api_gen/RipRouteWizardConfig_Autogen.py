"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .WizardConfigBase_Autogen import WizardConfigBase


@rom_manager.rom
class RipRouteWizardConfig(WizardConfigBase):
    def __init__(self, Ipv4TotalNumberOfRoutes=None, Ipv4StartRoutesPrefix=None, Ipv4EndRoutesPrefix=None, Ipv4RoutesNoneSeq=None, Ipv4RoutesPrefixLenType=None, Ipv4RoutesPrefixLenStart=None, Ipv4RoutesPrefixLenEnd=None, Ipv4Metric=None, Ipv6TotalNumberOfRoutes=None, Ipv6StartRoutesPrefix=None, Ipv6EndRoutesPrefix=None, Ipv6RoutesNoneSeq=None, Ipv6RoutesPrefixLenType=None, Ipv6RoutesPrefixLenStart=None, Ipv6RoutesPrefixLenEnd=None, Ipv6Metric=None, **kwargs):
        self._Ipv4TotalNumberOfRoutes = Ipv4TotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv4StartRoutesPrefix = Ipv4StartRoutesPrefix  # Starting IP Prefix
        self._Ipv4EndRoutesPrefix = Ipv4EndRoutesPrefix  # Ending IP Prefix
        self._Ipv4RoutesNoneSeq = Ipv4RoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv4RoutesPrefixLenType = Ipv4RoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv4RoutesPrefixLenStart = Ipv4RoutesPrefixLenStart  # Start Prefix Length
        self._Ipv4RoutesPrefixLenEnd = Ipv4RoutesPrefixLenEnd  # End Prefix Length
        self._Ipv4Metric = Ipv4Metric  # Metric
        self._Ipv6TotalNumberOfRoutes = Ipv6TotalNumberOfRoutes  # Total Number of Routes to Create
        self._Ipv6StartRoutesPrefix = Ipv6StartRoutesPrefix  # Starting IP Prefix
        self._Ipv6EndRoutesPrefix = Ipv6EndRoutesPrefix  # Ending IP Prefix
        self._Ipv6RoutesNoneSeq = Ipv6RoutesNoneSeq  # Prevent Route Aggregation
        self._Ipv6RoutesPrefixLenType = Ipv6RoutesPrefixLenType  # Prefix Length Distribution Type
        self._Ipv6RoutesPrefixLenStart = Ipv6RoutesPrefixLenStart  # Start Prefix Length
        self._Ipv6RoutesPrefixLenEnd = Ipv6RoutesPrefixLenEnd  # End Prefix Length
        self._Ipv6Metric = Ipv6Metric  # Metric

        properties = kwargs.copy()
        if Ipv4TotalNumberOfRoutes is not None:
            properties['Ipv4TotalNumberOfRoutes'] = Ipv4TotalNumberOfRoutes
        if Ipv4StartRoutesPrefix is not None:
            properties['Ipv4StartRoutesPrefix'] = Ipv4StartRoutesPrefix
        if Ipv4EndRoutesPrefix is not None:
            properties['Ipv4EndRoutesPrefix'] = Ipv4EndRoutesPrefix
        if Ipv4RoutesNoneSeq is not None:
            properties['Ipv4RoutesNoneSeq'] = Ipv4RoutesNoneSeq
        if Ipv4RoutesPrefixLenType is not None:
            properties['Ipv4RoutesPrefixLenType'] = Ipv4RoutesPrefixLenType
        if Ipv4RoutesPrefixLenStart is not None:
            properties['Ipv4RoutesPrefixLenStart'] = Ipv4RoutesPrefixLenStart
        if Ipv4RoutesPrefixLenEnd is not None:
            properties['Ipv4RoutesPrefixLenEnd'] = Ipv4RoutesPrefixLenEnd
        if Ipv4Metric is not None:
            properties['Ipv4Metric'] = Ipv4Metric
        if Ipv6TotalNumberOfRoutes is not None:
            properties['Ipv6TotalNumberOfRoutes'] = Ipv6TotalNumberOfRoutes
        if Ipv6StartRoutesPrefix is not None:
            properties['Ipv6StartRoutesPrefix'] = Ipv6StartRoutesPrefix
        if Ipv6EndRoutesPrefix is not None:
            properties['Ipv6EndRoutesPrefix'] = Ipv6EndRoutesPrefix
        if Ipv6RoutesNoneSeq is not None:
            properties['Ipv6RoutesNoneSeq'] = Ipv6RoutesNoneSeq
        if Ipv6RoutesPrefixLenType is not None:
            properties['Ipv6RoutesPrefixLenType'] = Ipv6RoutesPrefixLenType
        if Ipv6RoutesPrefixLenStart is not None:
            properties['Ipv6RoutesPrefixLenStart'] = Ipv6RoutesPrefixLenStart
        if Ipv6RoutesPrefixLenEnd is not None:
            properties['Ipv6RoutesPrefixLenEnd'] = Ipv6RoutesPrefixLenEnd
        if Ipv6Metric is not None:
            properties['Ipv6Metric'] = Ipv6Metric

        # call base class function, and it will send message to renix server to create a class.
        super(RipRouteWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Ipv4TotalNumberOfRoutes=None, Ipv4StartRoutesPrefix=None, Ipv4EndRoutesPrefix=None, Ipv4RoutesNoneSeq=None, Ipv4RoutesPrefixLenType=None, Ipv4RoutesPrefixLenStart=None, Ipv4RoutesPrefixLenEnd=None, Ipv4Metric=None, Ipv6TotalNumberOfRoutes=None, Ipv6StartRoutesPrefix=None, Ipv6EndRoutesPrefix=None, Ipv6RoutesNoneSeq=None, Ipv6RoutesPrefixLenType=None, Ipv6RoutesPrefixLenStart=None, Ipv6RoutesPrefixLenEnd=None, Ipv6Metric=None, **kwargs):
        properties = kwargs.copy()
        if Ipv4TotalNumberOfRoutes is not None:
            self._Ipv4TotalNumberOfRoutes = Ipv4TotalNumberOfRoutes
            properties['Ipv4TotalNumberOfRoutes'] = Ipv4TotalNumberOfRoutes
        if Ipv4StartRoutesPrefix is not None:
            self._Ipv4StartRoutesPrefix = Ipv4StartRoutesPrefix
            properties['Ipv4StartRoutesPrefix'] = Ipv4StartRoutesPrefix
        if Ipv4EndRoutesPrefix is not None:
            self._Ipv4EndRoutesPrefix = Ipv4EndRoutesPrefix
            properties['Ipv4EndRoutesPrefix'] = Ipv4EndRoutesPrefix
        if Ipv4RoutesNoneSeq is not None:
            self._Ipv4RoutesNoneSeq = Ipv4RoutesNoneSeq
            properties['Ipv4RoutesNoneSeq'] = Ipv4RoutesNoneSeq
        if Ipv4RoutesPrefixLenType is not None:
            self._Ipv4RoutesPrefixLenType = Ipv4RoutesPrefixLenType
            properties['Ipv4RoutesPrefixLenType'] = Ipv4RoutesPrefixLenType
        if Ipv4RoutesPrefixLenStart is not None:
            self._Ipv4RoutesPrefixLenStart = Ipv4RoutesPrefixLenStart
            properties['Ipv4RoutesPrefixLenStart'] = Ipv4RoutesPrefixLenStart
        if Ipv4RoutesPrefixLenEnd is not None:
            self._Ipv4RoutesPrefixLenEnd = Ipv4RoutesPrefixLenEnd
            properties['Ipv4RoutesPrefixLenEnd'] = Ipv4RoutesPrefixLenEnd
        if Ipv4Metric is not None:
            self._Ipv4Metric = Ipv4Metric
            properties['Ipv4Metric'] = Ipv4Metric
        if Ipv6TotalNumberOfRoutes is not None:
            self._Ipv6TotalNumberOfRoutes = Ipv6TotalNumberOfRoutes
            properties['Ipv6TotalNumberOfRoutes'] = Ipv6TotalNumberOfRoutes
        if Ipv6StartRoutesPrefix is not None:
            self._Ipv6StartRoutesPrefix = Ipv6StartRoutesPrefix
            properties['Ipv6StartRoutesPrefix'] = Ipv6StartRoutesPrefix
        if Ipv6EndRoutesPrefix is not None:
            self._Ipv6EndRoutesPrefix = Ipv6EndRoutesPrefix
            properties['Ipv6EndRoutesPrefix'] = Ipv6EndRoutesPrefix
        if Ipv6RoutesNoneSeq is not None:
            self._Ipv6RoutesNoneSeq = Ipv6RoutesNoneSeq
            properties['Ipv6RoutesNoneSeq'] = Ipv6RoutesNoneSeq
        if Ipv6RoutesPrefixLenType is not None:
            self._Ipv6RoutesPrefixLenType = Ipv6RoutesPrefixLenType
            properties['Ipv6RoutesPrefixLenType'] = Ipv6RoutesPrefixLenType
        if Ipv6RoutesPrefixLenStart is not None:
            self._Ipv6RoutesPrefixLenStart = Ipv6RoutesPrefixLenStart
            properties['Ipv6RoutesPrefixLenStart'] = Ipv6RoutesPrefixLenStart
        if Ipv6RoutesPrefixLenEnd is not None:
            self._Ipv6RoutesPrefixLenEnd = Ipv6RoutesPrefixLenEnd
            properties['Ipv6RoutesPrefixLenEnd'] = Ipv6RoutesPrefixLenEnd
        if Ipv6Metric is not None:
            self._Ipv6Metric = Ipv6Metric
            properties['Ipv6Metric'] = Ipv6Metric

        super(RipRouteWizardConfig, self).edit(**properties)

    @property
    def Ipv4TotalNumberOfRoutes(self):
        """
        get the value of property _Ipv4TotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv4TotalNumberOfRoutes')
        return self._Ipv4TotalNumberOfRoutes

    @property
    def Ipv4StartRoutesPrefix(self):
        """
        get the value of property _Ipv4StartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4StartRoutesPrefix')
        return self._Ipv4StartRoutesPrefix

    @property
    def Ipv4EndRoutesPrefix(self):
        """
        get the value of property _Ipv4EndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv4EndRoutesPrefix')
        return self._Ipv4EndRoutesPrefix

    @property
    def Ipv4RoutesNoneSeq(self):
        """
        get the value of property _Ipv4RoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv4RoutesNoneSeq')
        return self._Ipv4RoutesNoneSeq

    @property
    def Ipv4RoutesPrefixLenType(self):
        """
        get the value of property _Ipv4RoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv4RoutesPrefixLenType')
        return self._Ipv4RoutesPrefixLenType

    @property
    def Ipv4RoutesPrefixLenStart(self):
        """
        get the value of property _Ipv4RoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv4RoutesPrefixLenStart')
        return self._Ipv4RoutesPrefixLenStart

    @property
    def Ipv4RoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv4RoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv4RoutesPrefixLenEnd')
        return self._Ipv4RoutesPrefixLenEnd

    @property
    def Ipv4Metric(self):
        """
        get the value of property _Ipv4Metric
        """
        if self.force_auto_sync:
            self.get('Ipv4Metric')
        return self._Ipv4Metric

    @property
    def Ipv6TotalNumberOfRoutes(self):
        """
        get the value of property _Ipv6TotalNumberOfRoutes
        """
        if self.force_auto_sync:
            self.get('Ipv6TotalNumberOfRoutes')
        return self._Ipv6TotalNumberOfRoutes

    @property
    def Ipv6StartRoutesPrefix(self):
        """
        get the value of property _Ipv6StartRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6StartRoutesPrefix')
        return self._Ipv6StartRoutesPrefix

    @property
    def Ipv6EndRoutesPrefix(self):
        """
        get the value of property _Ipv6EndRoutesPrefix
        """
        if self.force_auto_sync:
            self.get('Ipv6EndRoutesPrefix')
        return self._Ipv6EndRoutesPrefix

    @property
    def Ipv6RoutesNoneSeq(self):
        """
        get the value of property _Ipv6RoutesNoneSeq
        """
        if self.force_auto_sync:
            self.get('Ipv6RoutesNoneSeq')
        return self._Ipv6RoutesNoneSeq

    @property
    def Ipv6RoutesPrefixLenType(self):
        """
        get the value of property _Ipv6RoutesPrefixLenType
        """
        if self.force_auto_sync:
            self.get('Ipv6RoutesPrefixLenType')
        return self._Ipv6RoutesPrefixLenType

    @property
    def Ipv6RoutesPrefixLenStart(self):
        """
        get the value of property _Ipv6RoutesPrefixLenStart
        """
        if self.force_auto_sync:
            self.get('Ipv6RoutesPrefixLenStart')
        return self._Ipv6RoutesPrefixLenStart

    @property
    def Ipv6RoutesPrefixLenEnd(self):
        """
        get the value of property _Ipv6RoutesPrefixLenEnd
        """
        if self.force_auto_sync:
            self.get('Ipv6RoutesPrefixLenEnd')
        return self._Ipv6RoutesPrefixLenEnd

    @property
    def Ipv6Metric(self):
        """
        get the value of property _Ipv6Metric
        """
        if self.force_auto_sync:
            self.get('Ipv6Metric')
        return self._Ipv6Metric

    @Ipv4TotalNumberOfRoutes.setter
    def Ipv4TotalNumberOfRoutes(self, value):
        self._Ipv4TotalNumberOfRoutes = value
        self.edit(Ipv4TotalNumberOfRoutes=value)

    @Ipv4StartRoutesPrefix.setter
    def Ipv4StartRoutesPrefix(self, value):
        self._Ipv4StartRoutesPrefix = value
        self.edit(Ipv4StartRoutesPrefix=value)

    @Ipv4EndRoutesPrefix.setter
    def Ipv4EndRoutesPrefix(self, value):
        self._Ipv4EndRoutesPrefix = value
        self.edit(Ipv4EndRoutesPrefix=value)

    @Ipv4RoutesNoneSeq.setter
    def Ipv4RoutesNoneSeq(self, value):
        self._Ipv4RoutesNoneSeq = value
        self.edit(Ipv4RoutesNoneSeq=value)

    @Ipv4RoutesPrefixLenType.setter
    def Ipv4RoutesPrefixLenType(self, value):
        self._Ipv4RoutesPrefixLenType = value
        self.edit(Ipv4RoutesPrefixLenType=value)

    @Ipv4RoutesPrefixLenStart.setter
    def Ipv4RoutesPrefixLenStart(self, value):
        self._Ipv4RoutesPrefixLenStart = value
        self.edit(Ipv4RoutesPrefixLenStart=value)

    @Ipv4RoutesPrefixLenEnd.setter
    def Ipv4RoutesPrefixLenEnd(self, value):
        self._Ipv4RoutesPrefixLenEnd = value
        self.edit(Ipv4RoutesPrefixLenEnd=value)

    @Ipv4Metric.setter
    def Ipv4Metric(self, value):
        self._Ipv4Metric = value
        self.edit(Ipv4Metric=value)

    @Ipv6TotalNumberOfRoutes.setter
    def Ipv6TotalNumberOfRoutes(self, value):
        self._Ipv6TotalNumberOfRoutes = value
        self.edit(Ipv6TotalNumberOfRoutes=value)

    @Ipv6StartRoutesPrefix.setter
    def Ipv6StartRoutesPrefix(self, value):
        self._Ipv6StartRoutesPrefix = value
        self.edit(Ipv6StartRoutesPrefix=value)

    @Ipv6EndRoutesPrefix.setter
    def Ipv6EndRoutesPrefix(self, value):
        self._Ipv6EndRoutesPrefix = value
        self.edit(Ipv6EndRoutesPrefix=value)

    @Ipv6RoutesNoneSeq.setter
    def Ipv6RoutesNoneSeq(self, value):
        self._Ipv6RoutesNoneSeq = value
        self.edit(Ipv6RoutesNoneSeq=value)

    @Ipv6RoutesPrefixLenType.setter
    def Ipv6RoutesPrefixLenType(self, value):
        self._Ipv6RoutesPrefixLenType = value
        self.edit(Ipv6RoutesPrefixLenType=value)

    @Ipv6RoutesPrefixLenStart.setter
    def Ipv6RoutesPrefixLenStart(self, value):
        self._Ipv6RoutesPrefixLenStart = value
        self.edit(Ipv6RoutesPrefixLenStart=value)

    @Ipv6RoutesPrefixLenEnd.setter
    def Ipv6RoutesPrefixLenEnd(self, value):
        self._Ipv6RoutesPrefixLenEnd = value
        self.edit(Ipv6RoutesPrefixLenEnd=value)

    @Ipv6Metric.setter
    def Ipv6Metric(self, value):
        self._Ipv6Metric = value
        self.edit(Ipv6Metric=value)

    def _set_ipv4totalnumberofroutes_with_str(self, value):
        try:
            self._Ipv4TotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv4TotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv4startroutesprefix_with_str(self, value):
        self._Ipv4StartRoutesPrefix = value

    def _set_ipv4endroutesprefix_with_str(self, value):
        self._Ipv4EndRoutesPrefix = value

    def _set_ipv4routesnoneseq_with_str(self, value):
        self._Ipv4RoutesNoneSeq = (value == 'True')

    def _set_ipv4routesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv4RoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv4routesprefixlenstart_with_str(self, value):
        try:
            self._Ipv4RoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv4RoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv4routesprefixlenend_with_str(self, value):
        try:
            self._Ipv4RoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv4RoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv4metric_with_str(self, value):
        try:
            self._Ipv4Metric = int(value)
        except ValueError:
            self._Ipv4Metric = hex(int(value, 16))

    def _set_ipv6totalnumberofroutes_with_str(self, value):
        try:
            self._Ipv6TotalNumberOfRoutes = int(value)
        except ValueError:
            self._Ipv6TotalNumberOfRoutes = hex(int(value, 16))

    def _set_ipv6startroutesprefix_with_str(self, value):
        self._Ipv6StartRoutesPrefix = value

    def _set_ipv6endroutesprefix_with_str(self, value):
        self._Ipv6EndRoutesPrefix = value

    def _set_ipv6routesnoneseq_with_str(self, value):
        self._Ipv6RoutesNoneSeq = (value == 'True')

    def _set_ipv6routesprefixlentype_with_str(self, value):
        seperate = value.find(':')
        exec('self._Ipv6RoutesPrefixLenType = EnumPrefixLenDistributionType.%s' % value[:seperate])

    def _set_ipv6routesprefixlenstart_with_str(self, value):
        try:
            self._Ipv6RoutesPrefixLenStart = int(value)
        except ValueError:
            self._Ipv6RoutesPrefixLenStart = hex(int(value, 16))

    def _set_ipv6routesprefixlenend_with_str(self, value):
        try:
            self._Ipv6RoutesPrefixLenEnd = int(value)
        except ValueError:
            self._Ipv6RoutesPrefixLenEnd = hex(int(value, 16))

    def _set_ipv6metric_with_str(self, value):
        try:
            self._Ipv6Metric = int(value)
        except ValueError:
            self._Ipv6Metric = hex(int(value, 16))

