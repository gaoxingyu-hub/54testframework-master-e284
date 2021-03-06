"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3AsExternalLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, LinkStateId=None, PrefixCount=None, StartPrefixAddress=None, PrefixLength=None, Increment=None, PrefixOptions=None, IsExternalMetric=None, Metric=None, EnableForwardingAddress=None, ForwardingAddress=None, AdminTag=None, ReferencedLsType=None, ReferencedLinkStateId=None, Age=None, SequenceNumber=None, Checksum=None, LsaAutomaticConversion=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router ID
        self._LinkStateId = LinkStateId  # Link State ID
        self._PrefixCount = PrefixCount  # Number Of Prefixes
        self._StartPrefixAddress = StartPrefixAddress  # Start Prefix Address
        self._PrefixLength = PrefixLength  # Prefix Length
        self._Increment = Increment  # Increment
        self._EndPrefixAddress = '2000::1'  # End Prefix Address, not editable
        self._PrefixOptions = swap_int_to_enum_flag(PrefixOptions, EnumOspfv3PrefixOptionBit)  # Prefix Options
        self._IsExternalMetric = IsExternalMetric  # Is External Metric
        self._Metric = Metric  # Metric
        self._EnableForwardingAddress = EnableForwardingAddress  # Enable Forwarding Address
        self._ForwardingAddress = ForwardingAddress  # Forwarding Address
        self._AdminTag = AdminTag  # Admin Tag
        self._ReferencedLsType = ReferencedLsType  # Referenced LS Type
        self._ReferencedLinkStateId = ReferencedLinkStateId  # Referenced Link State ID
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum
        self._LsaAutomaticConversion = LsaAutomaticConversion  # LSA Automatic Conversion

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
        if PrefixOptions is not None:
            if isinstance(PrefixOptions, Flag):
                properties['PrefixOptions'] = PrefixOptions.value
            else:
                properties['PrefixOptions'] = PrefixOptions
        if IsExternalMetric is not None:
            properties['IsExternalMetric'] = IsExternalMetric
        if Metric is not None:
            properties['Metric'] = Metric
        if EnableForwardingAddress is not None:
            properties['EnableForwardingAddress'] = EnableForwardingAddress
        if ForwardingAddress is not None:
            properties['ForwardingAddress'] = ForwardingAddress
        if AdminTag is not None:
            properties['AdminTag'] = AdminTag
        if ReferencedLsType is not None:
            properties['ReferencedLsType'] = ReferencedLsType
        if ReferencedLinkStateId is not None:
            properties['ReferencedLinkStateId'] = ReferencedLinkStateId
        if Age is not None:
            properties['Age'] = Age
        if SequenceNumber is not None:
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            properties['Checksum'] = Checksum
        if LsaAutomaticConversion is not None:
            properties['LsaAutomaticConversion'] = LsaAutomaticConversion

        # call base class function, and it will send message to renix server to create a class.
        super(Ospfv3AsExternalLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, LinkStateId=None, PrefixCount=None, StartPrefixAddress=None, PrefixLength=None, Increment=None, PrefixOptions=None, IsExternalMetric=None, Metric=None, EnableForwardingAddress=None, ForwardingAddress=None, AdminTag=None, ReferencedLsType=None, ReferencedLinkStateId=None, Age=None, SequenceNumber=None, Checksum=None, LsaAutomaticConversion=None, **kwargs):
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
        if PrefixOptions is not None:
            self._PrefixOptions = swap_int_to_enum_flag(PrefixOptions, EnumOspfv3PrefixOptionBit)
            if isinstance(PrefixOptions, Flag):
                properties['PrefixOptions'] = PrefixOptions.value
            else:
                properties['PrefixOptions'] = PrefixOptions
        if IsExternalMetric is not None:
            self._IsExternalMetric = IsExternalMetric
            properties['IsExternalMetric'] = IsExternalMetric
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric
        if EnableForwardingAddress is not None:
            self._EnableForwardingAddress = EnableForwardingAddress
            properties['EnableForwardingAddress'] = EnableForwardingAddress
        if ForwardingAddress is not None:
            self._ForwardingAddress = ForwardingAddress
            properties['ForwardingAddress'] = ForwardingAddress
        if AdminTag is not None:
            self._AdminTag = AdminTag
            properties['AdminTag'] = AdminTag
        if ReferencedLsType is not None:
            self._ReferencedLsType = ReferencedLsType
            properties['ReferencedLsType'] = ReferencedLsType
        if ReferencedLinkStateId is not None:
            self._ReferencedLinkStateId = ReferencedLinkStateId
            properties['ReferencedLinkStateId'] = ReferencedLinkStateId
        if Age is not None:
            self._Age = Age
            properties['Age'] = Age
        if SequenceNumber is not None:
            self._SequenceNumber = SequenceNumber
            properties['SequenceNumber'] = SequenceNumber
        if Checksum is not None:
            self._Checksum = Checksum
            properties['Checksum'] = Checksum
        if LsaAutomaticConversion is not None:
            self._LsaAutomaticConversion = LsaAutomaticConversion
            properties['LsaAutomaticConversion'] = LsaAutomaticConversion

        super(Ospfv3AsExternalLsaConfig, self).edit(**properties)

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
    def PrefixOptions(self):
        """
        get the value of property _PrefixOptions
        """
        if self.force_auto_sync:
            self.get('PrefixOptions')
        return self._PrefixOptions

    @property
    def IsExternalMetric(self):
        """
        get the value of property _IsExternalMetric
        """
        if self.force_auto_sync:
            self.get('IsExternalMetric')
        return self._IsExternalMetric

    @property
    def Metric(self):
        """
        get the value of property _Metric
        """
        if self.force_auto_sync:
            self.get('Metric')
        return self._Metric

    @property
    def EnableForwardingAddress(self):
        """
        get the value of property _EnableForwardingAddress
        """
        if self.force_auto_sync:
            self.get('EnableForwardingAddress')
        return self._EnableForwardingAddress

    @property
    def ForwardingAddress(self):
        """
        get the value of property _ForwardingAddress
        """
        if self.force_auto_sync:
            self.get('ForwardingAddress')
        return self._ForwardingAddress

    @property
    def AdminTag(self):
        """
        get the value of property _AdminTag
        """
        if self.force_auto_sync:
            self.get('AdminTag')
        return self._AdminTag

    @property
    def ReferencedLsType(self):
        """
        get the value of property _ReferencedLsType
        """
        if self.force_auto_sync:
            self.get('ReferencedLsType')
        return self._ReferencedLsType

    @property
    def ReferencedLinkStateId(self):
        """
        get the value of property _ReferencedLinkStateId
        """
        if self.force_auto_sync:
            self.get('ReferencedLinkStateId')
        return self._ReferencedLinkStateId

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

    @property
    def LsaAutomaticConversion(self):
        """
        get the value of property _LsaAutomaticConversion
        """
        if self.force_auto_sync:
            self.get('LsaAutomaticConversion')
        return self._LsaAutomaticConversion

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

    @PrefixOptions.setter
    def PrefixOptions(self, value):
        self._PrefixOptions = swap_int_to_enum_flag(value, EnumOspfv3PrefixOptionBit)
        if isinstance(value, Flag):
            self.edit(PrefixOptions=value.value)
        else:
            self.edit(PrefixOptions=value)

    @IsExternalMetric.setter
    def IsExternalMetric(self, value):
        self._IsExternalMetric = value
        self.edit(IsExternalMetric=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    @EnableForwardingAddress.setter
    def EnableForwardingAddress(self, value):
        self._EnableForwardingAddress = value
        self.edit(EnableForwardingAddress=value)

    @ForwardingAddress.setter
    def ForwardingAddress(self, value):
        self._ForwardingAddress = value
        self.edit(ForwardingAddress=value)

    @AdminTag.setter
    def AdminTag(self, value):
        self._AdminTag = value
        self.edit(AdminTag=value)

    @ReferencedLsType.setter
    def ReferencedLsType(self, value):
        self._ReferencedLsType = value
        self.edit(ReferencedLsType=value)

    @ReferencedLinkStateId.setter
    def ReferencedLinkStateId(self, value):
        self._ReferencedLinkStateId = value
        self.edit(ReferencedLinkStateId=value)

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

    @LsaAutomaticConversion.setter
    def LsaAutomaticConversion(self, value):
        self._LsaAutomaticConversion = value
        self.edit(LsaAutomaticConversion=value)

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

    def _set_prefixoptions_with_str(self, value):
        seperate = value.find(':')
        self._PrefixOptions = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv3PrefixOptionBit)

    def _set_isexternalmetric_with_str(self, value):
        self._IsExternalMetric = (value == 'True')

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

    def _set_enableforwardingaddress_with_str(self, value):
        self._EnableForwardingAddress = (value == 'True')

    def _set_forwardingaddress_with_str(self, value):
        self._ForwardingAddress = value

    def _set_admintag_with_str(self, value):
        try:
            self._AdminTag = int(value)
        except ValueError:
            self._AdminTag = hex(int(value, 16))

    def _set_referencedlstype_with_str(self, value):
        try:
            self._ReferencedLsType = int(value)
        except ValueError:
            self._ReferencedLsType = hex(int(value, 16))

    def _set_referencedlinkstateid_with_str(self, value):
        try:
            self._ReferencedLinkStateId = int(value)
        except ValueError:
            self._ReferencedLinkStateId = hex(int(value, 16))

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

    def _set_lsaautomaticconversion_with_str(self, value):
        self._LsaAutomaticConversion = (value == 'True')

