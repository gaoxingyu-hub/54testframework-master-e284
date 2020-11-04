"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3InterAreaRouterLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, LinkStateId=None, AsbrId=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router ID
        self._LinkStateId = LinkStateId  # Link State ID
        self._AsbrId = AsbrId  # ASBR ID
        self._Metric = Metric  # Metric
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv3OptionBit)  # Options
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum

        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            properties['LinkStateId'] = LinkStateId
        if AsbrId is not None:
            properties['AsbrId'] = AsbrId
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
        super(Ospfv3InterAreaRouterLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, LinkStateId=None, AsbrId=None, Metric=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            self._AdvertisingRouterId = AdvertisingRouterId
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            self._LinkStateId = LinkStateId
            properties['LinkStateId'] = LinkStateId
        if AsbrId is not None:
            self._AsbrId = AsbrId
            properties['AsbrId'] = AsbrId
        if Metric is not None:
            self._Metric = Metric
            properties['Metric'] = Metric
        if Options is not None:
            self._Options = swap_int_to_enum_flag(Options, EnumOspfv3OptionBit)
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

        super(Ospfv3InterAreaRouterLsaConfig, self).edit(**properties)

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
    def AsbrId(self):
        """
        get the value of property _AsbrId
        """
        if self.force_auto_sync:
            self.get('AsbrId')
        return self._AsbrId

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

    @LinkStateId.setter
    def LinkStateId(self, value):
        self._LinkStateId = value
        self.edit(LinkStateId=value)

    @AsbrId.setter
    def AsbrId(self, value):
        self._AsbrId = value
        self.edit(AsbrId=value)

    @Metric.setter
    def Metric(self, value):
        self._Metric = value
        self.edit(Metric=value)

    @Options.setter
    def Options(self, value):
        self._Options = swap_int_to_enum_flag(value, EnumOspfv3OptionBit)
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

    def _set_linkstateid_with_str(self, value):
        try:
            self._LinkStateId = int(value)
        except ValueError:
            self._LinkStateId = hex(int(value, 16))

    def _set_asbrid_with_str(self, value):
        self._AsbrId = value

    def _set_metric_with_str(self, value):
        try:
            self._Metric = int(value)
        except ValueError:
            self._Metric = hex(int(value, 16))

    def _set_options_with_str(self, value):
        seperate = value.find(':')
        self._Options = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv3OptionBit)

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

