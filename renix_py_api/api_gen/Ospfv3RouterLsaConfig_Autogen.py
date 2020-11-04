"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ospfv3RouterLsaConfig(ROMObject):
    def __init__(self, AdvertisingRouterId=None, LinkStateId=None, RouterType=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        self._AdvertisingRouterId = AdvertisingRouterId  # Advertising Router ID
        self._LinkStateId = LinkStateId  # Link State ID
        self._RouterType = swap_int_to_enum_flag(RouterType, EnumOspfv3RouterType)  # Router Type
        self._Options = swap_int_to_enum_flag(Options, EnumOspfv3OptionBit)  # Options
        self._Age = Age  # Age (sec)
        self._SequenceNumber = SequenceNumber  # Sequence Number
        self._Checksum = Checksum  # Checksum

        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            properties['LinkStateId'] = LinkStateId
        if RouterType is not None:
            if isinstance(RouterType, Flag):
                properties['RouterType'] = RouterType.value
            else:
                properties['RouterType'] = RouterType
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
        super(Ospfv3RouterLsaConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, AdvertisingRouterId=None, LinkStateId=None, RouterType=None, Options=None, Age=None, SequenceNumber=None, Checksum=None, **kwargs):
        properties = kwargs.copy()
        if AdvertisingRouterId is not None:
            self._AdvertisingRouterId = AdvertisingRouterId
            properties['AdvertisingRouterId'] = AdvertisingRouterId
        if LinkStateId is not None:
            self._LinkStateId = LinkStateId
            properties['LinkStateId'] = LinkStateId
        if RouterType is not None:
            self._RouterType = swap_int_to_enum_flag(RouterType, EnumOspfv3RouterType)
            if isinstance(RouterType, Flag):
                properties['RouterType'] = RouterType.value
            else:
                properties['RouterType'] = RouterType
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

        super(Ospfv3RouterLsaConfig, self).edit(**properties)

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
    def RouterType(self):
        """
        get the value of property _RouterType
        """
        if self.force_auto_sync:
            self.get('RouterType')
        return self._RouterType

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

    @RouterType.setter
    def RouterType(self, value):
        self._RouterType = swap_int_to_enum_flag(value, EnumOspfv3RouterType)
        if isinstance(value, Flag):
            self.edit(RouterType=value.value)
        else:
            self.edit(RouterType=value)

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

    def _set_routertype_with_str(self, value):
        seperate = value.find(':')
        self._RouterType = swap_int_to_enum_flag(int(value[seperate+1:]), EnumOspfv3RouterType)

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

