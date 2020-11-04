"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv2SummaryLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, RouteCount=None, StartNetworkPrefix=None, PrefixLength=None, Increment=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router ID
        self._RouteCount = RouteCount  # Number Of Routes
        self._StartNetworkPrefix = StartNetworkPrefix  # Start Network Prefix
        self._PrefixLength = PrefixLength  # Prefix Length
        self._Increment = Increment  # Increment
        self._EndNetworkPrefix = '192.0.1.0'  # End Network Prefix, not editable
        self._Metric = Metric  # Metric
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)  # Options
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum

        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if RouteCount is not None:
            properties['RouteCount'] = RouteCount
        if StartNetworkPrefix is not None:
            properties['StartNetworkPrefix'] = StartNetworkPrefix
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if Increment is not None:
            properties['Increment'] = Increment
        if Metric is not None:
            properties['Metric'] = Metric
        if Options is not None:
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if Age is not None:
            properties['Age'] = Age
        if SequenceNumber is not None:
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            properties['Checksum'] = Checksum

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv2SummaryLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, RouteCount=None, StartNetworkPrefix=None, PrefixLength=None, Increment=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            self._AdvertisingRouterId = AdvertisingRouterId
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if RouteCount is not None:
            self._RouteCount = RouteCount
            properties['RouteCount'] = RouteCount
        if StartNetworkPrefix is not None:
            self._StartNetworkPrefix = StartNetworkPrefix
            properties['StartNetworkPrefix'] = StartNetworkPrefix
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if Increment is not None:
            self._Increment = Increment
            properties['Increment'] = Increment
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric
        if Options is not None:
            self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)
            if isinstance(Options, Flag):
                properties['Options'] = Options.value
            else:
                properties['Options'] = Options
        if Age is not None:
            self._Age = Age
            properties['Age'] = Age
        if SequenceNumber is not None:
            self._SequenceNumber = SequenceNumber
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            self._Checksum = Checksum
            properties['Checksum'] = Checksum

        super(Ospfv2SummaryLsaConfig, self).edit(**properties)

    @property
    def AdvertisingRouterId(self):
        """
        get the value of property _AdvertisingRouterId
        """
        if self.force_auto_sync:
            self.get('AdvertisingRouterId')
        return self._AdvertisingRouterId

    @property
    def RouteCount(self):
        """
        get the value of property _RouteCount
        """
        if self.force_auto_sync:
            self.get('RouteCount')
        return self._RouteCount

    @property
    def StartNetworkPrefix(self):
        """
        get the value of property _StartNetworkPrefix
        """
        if self.force_auto_sync:
            self.get('StartNetworkPrefix')
        return self._StartNetworkPrefix

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def Increment(self):
        """
        get the value of property _Increment
        """
        if self.force_auto_sync:
            self.get('Increment')
        return self._Increment

    @property
    def EndNetworkPrefix(self):
        """
        get the value of property _EndNetworkPrefix
        """
        if self.force_auto_sync:
            self.get('EndNetworkPrefix')
        return self._EndNetworkPrefix

    @property
    def Metric(self):
        """
        get the value of property _Metric
        """
        if self.force_auto_sync:
            self.get('Metric')
        return self._Metric

    @property
    def Options(self):
        """
        get the value of property _Options
        """
        if self.force_auto_sync:
            self.get('Options')
        return self._Options

    @property
    def Age(self):
        """
        get the value of property _Age
        """
        if self.force_auto_sync:
            self.get('Age')
        return self._Age

    @property
    def SequenceNumber(self):
        """
        get the value of property _SequenceNumber
        """
        if self.force_auto_sync:
            self.get('SequenceNumber')
        return self._SequenceNumber

    @property
    def Checksum(self):
        """
        get the value of property _Checksum
        """
        if self.force_auto_sync:
            self.get('Checksum')
        return self._Checksum

    @AdvertisingRouterId.setter
    def AdvertisingRouterId(self, value):
        self._AdvertisingRouterId = value
        self.edit(AdvertisingRouterId=value)

    @RouteCount.setter
    def RouteCount(self, value):
        self._RouteCount = value
        self.edit(RouteCount=value)

    @StartNetworkPrefix.setter
    def StartNetworkPrefix(self, value):
        self._StartNetworkPrefix = value
        self.edit(StartNetworkPrefix=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @Increment.setter
    def Increment(self, value):
        self._Increment = value
        self.edit(Increment=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    @Options.setter
    def Options(self, value):
        self._Options = swap_int_to_enum_flag(value, EnumOspfv2OptionBit)
        if isinstance(value, Flag):
            self.edit(Options=value.value)
        else:
            self.edit(Options=value)

    @Age.setter
    def Age(self, value):
        self._Age = value
        self.edit(Age=value)

    @SequenceNumber.setter
    def SequenceNumber(self, value):
        self._SequenceNumber = value
        self.edit(SequenceNumber=value)

    @Checksum.setter
    def Checksum(self, value):
        self._Checksum = value
        self.edit(Checksum=value)

    def _set_advertisingrouterid_with_str(self, value):
        self._AdvertisingRouterId = value

    def _set_routecount_with_str(self, value):
        try:
            self._RouteCount = int(value)
        except ValueError:
            self._RouteCount = hex(int(value, 16))

    def _set_startnetworkprefix_with_str(self, value):
        self._StartNetworkPrefix = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_increment_with_str(self, value):
        try:
            self._Increment = int(value)
        except ValueError:
            self._Increment = hex(int(value, 16))

    def _set_endnetworkprefix_with_str(self, value):
        self._EndNetworkPrefix = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

    def _set_options_with_str(self, value):
        seperate = value.find(':')
        self._Options = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv2OptionBit)

    def _set_age_with_str(self, value):
        try:
            self._Age = int(value)
        except ValueError:
            self._Age = hex(int(value, 16))

    def _set_sequencenumber_with_str(self, value):
        try:
            self._SequenceNumber = int(value)
        except ValueError:
            self._SequenceNumber = hex(int(value, 16))

    def _set_checksum_with_str(self, value):
        self._Checksum = (value == 'True')

