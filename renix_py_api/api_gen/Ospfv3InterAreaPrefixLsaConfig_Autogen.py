"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3InterAreaPrefixLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, LinkStateId=None, PrefixCount=None, StartPrefixAddress=None, PrefixLength=None, Increment=None, Metric=None, PrefixOptions=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router ID
        self._LinkStateId = LinkStateId  # Link State ID
        self._PrefixCount = PrefixCount  # Number Of Prefixes
        self._StartPrefixAddress = StartPrefixAddress  # Start Prefix Address
        self._PrefixLength = PrefixLength  # Prefix Length
        self._Increment = Increment  # Increment
        self._EndPrefixAddress = '2000::1'  # End Prefix Address, not editable
        self._Metric = Metric  # Metric
        self._PrefixOptions = swap_int_to_enum_flag(PrefixOptions, EnumOspfv3PrefixOptionBit)  # Prefix Options
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum

        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            properties['LinkStateId'] = LinkStateId
        if PrefixCount is not None:
            properties['PrefixCount'] = PrefixCount
        if StartPrefixAddress is not None:
            properties['StartPrefixAddress'] = StartPrefixAddress
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if Increment is not None:
            properties['Increment'] = Increment
        if Metric is not None:
            properties['Metric'] = Metric
        if PrefixOptions is not None:
            if isinstance(PrefixOptions, Flag):
                properties['PrefixOptions'] = PrefixOptions.value
            else:
                properties['PrefixOptions'] = PrefixOptions
        if Age is not None:
            properties['Age'] = Age
        if SequenceNumber is not None:
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            properties['Checksum'] = Checksum

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3InterAreaPrefixLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, LinkStateId=None, PrefixCount=None, StartPrefixAddress=None, PrefixLength=None, Increment=None, Metric=None, PrefixOptions=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            self._AdvertisingRouterId = AdvertisingRouterId
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            self._LinkStateId = LinkStateId
            properties['LinkStateId'] = LinkStateId
        if PrefixCount is not None:
            self._PrefixCount = PrefixCount
            properties['PrefixCount'] = PrefixCount
        if StartPrefixAddress is not None:
            self._StartPrefixAddress = StartPrefixAddress
            properties['StartPrefixAddress'] = StartPrefixAddress
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if Increment is not None:
            self._Increment = Increment
            properties['Increment'] = Increment
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric
        if PrefixOptions is not None:
            self._PrefixOptions = swap_int_to_enum_flag(PrefixOptions, EnumOspfv3PrefixOptionBit)
            if isinstance(PrefixOptions, Flag):
                properties['PrefixOptions'] = PrefixOptions.value
            else:
                properties['PrefixOptions'] = PrefixOptions
        if Age is not None:
            self._Age = Age
            properties['Age'] = Age
        if SequenceNumber is not None:
            self._SequenceNumber = SequenceNumber
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            self._Checksum = Checksum
            properties['Checksum'] = Checksum

        super(Ospfv3InterAreaPrefixLsaConfig, self).edit(**properties)

    @property
    def AdvertisingRouterId(self):
        """
        get the value of property _AdvertisingRouterId
        """
        if self.force_auto_sync:
            self.get('AdvertisingRouterId')
        return self._AdvertisingRouterId

    @property
    def LinkStateId(self):
        """
        get the value of property _LinkStateId
        """
        if self.force_auto_sync:
            self.get('LinkStateId')
        return self._LinkStateId

    @property
    def PrefixCount(self):
        """
        get the value of property _PrefixCount
        """
        if self.force_auto_sync:
            self.get('PrefixCount')
        return self._PrefixCount

    @property
    def StartPrefixAddress(self):
        """
        get the value of property _StartPrefixAddress
        """
        if self.force_auto_sync:
            self.get('StartPrefixAddress')
        return self._StartPrefixAddress

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
    def EndPrefixAddress(self):
        """
        get the value of property _EndPrefixAddress
        """
        if self.force_auto_sync:
            self.get('EndPrefixAddress')
        return self._EndPrefixAddress

    @property
    def Metric(self):
        """
        get the value of property _Metric
        """
        if self.force_auto_sync:
            self.get('Metric')
        return self._Metric

    @property
    def PrefixOptions(self):
        """
        get the value of property _PrefixOptions
        """
        if self.force_auto_sync:
            self.get('PrefixOptions')
        return self._PrefixOptions

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

    @LinkStateId.setter
    def LinkStateId(self, value):
        self._LinkStateId = value
        self.edit(LinkStateId=value)

    @PrefixCount.setter
    def PrefixCount(self, value):
        self._PrefixCount = value
        self.edit(PrefixCount=value)

    @StartPrefixAddress.setter
    def StartPrefixAddress(self, value):
        self._StartPrefixAddress = value
        self.edit(StartPrefixAddress=value)

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

    @PrefixOptions.setter
    def PrefixOptions(self, value):
        self._PrefixOptions = swap_int_to_enum_flag(value, EnumOspfv3PrefixOptionBit)
        if isinstance(value, Flag):
            self.edit(PrefixOptions=value.value)
        else:
            self.edit(PrefixOptions=value)

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

    def _set_linkstateid_with_str(self, value):
        try:
            self._LinkStateId = int(value)
        except ValueError:
            self._LinkStateId = hex(int(value, 16))

    def _set_prefixcount_with_str(self, value):
        try:
            self._PrefixCount = int(value)
        except ValueError:
            self._PrefixCount = hex(int(value, 16))

    def _set_startprefixaddress_with_str(self, value):
        self._StartPrefixAddress = value

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

    def _set_endprefixaddress_with_str(self, value):
        self._EndPrefixAddress = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

    def _set_prefixoptions_with_str(self, value):
        seperate = value.find(':')
        self._PrefixOptions = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv3PrefixOptionBit)

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

