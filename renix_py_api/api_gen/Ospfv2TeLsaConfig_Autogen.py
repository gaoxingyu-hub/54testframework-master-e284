"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv2TeLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, TlvType=None, RouterId=None, LinkId=None, LinkType=None, Instance=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router
        self._TlvType = TlvType  # TLV Type
        self._RouterId = RouterId  # Router ID
        self._LinkId = LinkId  # Link ID
        self._LinkType = LinkType  # Link Type
        self._Instance = Instance  # Instance
        self._Metric = Metric  # Metric
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv2OptionBit)  # Options
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum

        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if TlvType is not None:
            properties['TlvType'] = TlvType
        if RouterId is not None:
            properties['RouterId'] = RouterId
        if LinkId is not None:
            properties['LinkId'] = LinkId
        if LinkType is not None:
            properties['LinkType'] = LinkType
        if Instance is not None:
            properties['Instance'] = Instance
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
        super(Ospfv2TeLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, TlvType=None, RouterId=None, LinkId=None, LinkType=None, Instance=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            self._AdvertisingRouterId = AdvertisingRouterId
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if TlvType is not None:
            self._TlvType = TlvType
            properties['TlvType'] = TlvType
        if RouterId is not None:
            self._RouterId = RouterId
            properties['RouterId'] = RouterId
        if LinkId is not None:
            self._LinkId = LinkId
            properties['LinkId'] = LinkId
        if LinkType is not None:
            self._LinkType = LinkType
            properties['LinkType'] = LinkType
        if Instance is not None:
            self._Instance = Instance
            properties['Instance'] = Instance
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

        super(Ospfv2TeLsaConfig, self).edit(**properties)

    @property
    def AdvertisingRouterId(self):
        """
        get the value of property _AdvertisingRouterId
        """
        if self.force_auto_sync:
            self.get('AdvertisingRouterId')
        return self._AdvertisingRouterId

    @property
    def TlvType(self):
        """
        get the value of property _TlvType
        """
        if self.force_auto_sync:
            self.get('TlvType')
        return self._TlvType

    @property
    def RouterId(self):
        """
        get the value of property _RouterId
        """
        if self.force_auto_sync:
            self.get('RouterId')
        return self._RouterId

    @property
    def LinkId(self):
        """
        get the value of property _LinkId
        """
        if self.force_auto_sync:
            self.get('LinkId')
        return self._LinkId

    @property
    def LinkType(self):
        """
        get the value of property _LinkType
        """
        if self.force_auto_sync:
            self.get('LinkType')
        return self._LinkType

    @property
    def Instance(self):
        """
        get the value of property _Instance
        """
        if self.force_auto_sync:
            self.get('Instance')
        return self._Instance

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

    @TlvType.setter
    def TlvType(self, value):
        self._TlvType = value
        self.edit(TlvType=value)

    @RouterId.setter
    def RouterId(self, value):
        self._RouterId = value
        self.edit(RouterId=value)

    @LinkId.setter
    def LinkId(self, value):
        self._LinkId = value
        self.edit(LinkId=value)

    @LinkType.setter
    def LinkType(self, value):
        self._LinkType = value
        self.edit(LinkType=value)

    @Instance.setter
    def Instance(self, value):
        self._Instance = value
        self.edit(Instance=value)

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

    def _set_tlvtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._TlvType = EnumTeTlvType.%s' % value[:seperate])

    def _set_routerid_with_str(self, value):
        self._RouterId = value

    def _set_linkid_with_str(self, value):
        self._LinkId = value

    def _set_linktype_with_str(self, value):
        seperate = value.find(':')
        exec('self._LinkType = EnumTeLinkType.%s' % value[:seperate])

    def _set_instance_with_str(self, value):
        try:
            self._Instance = int(value)
        except ValueError:
            self._Instance = hex(int(value, 16))

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

