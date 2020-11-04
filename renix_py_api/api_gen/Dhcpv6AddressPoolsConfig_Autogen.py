"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv6AddressPoolsConfig(ROMObject):
    def __init__(self, PrefixLength=None, StartAddress=None, HostStep=None, AddressCount=None, PreferredLifetime=None, ValidLifetime=None, MinIaidValue=None, MaxIaidValue=None, **kwargs):
        self._PrefixLength = PrefixLength  # Address Pool Prefix Length
        self._StartAddress = StartAddress  # Address Pool Start Address
        self._HostStep = HostStep  # Address Pool Host Step
        self._AddressCount = AddressCount  # Address Count
        self._PreferredLifetime = PreferredLifetime  # Preferred Lifetime (secs)
        self._ValidLifetime = ValidLifetime  # Valid Lifetime (secs)
        self._MinIaidValue = MinIaidValue  # Minimum IAID Value
        self._MaxIaidValue = MaxIaidValue  # Maximum IAID Value

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if StartAddress is not None:
            properties['StartAddress'] = StartAddress
        if HostStep is not None:
            properties['HostStep'] = HostStep
        if AddressCount is not None:
            properties['AddressCount'] = AddressCount
        if PreferredLifetime is not None:
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            properties['ValidLifetime'] = ValidLifetime
        if MinIaidValue is not None:
            properties['MinIaidValue'] = MinIaidValue
        if MaxIaidValue is not None:
            properties['MaxIaidValue'] = MaxIaidValue

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6AddressPoolsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, StartAddress=None, HostStep=None, AddressCount=None, PreferredLifetime=None, ValidLifetime=None, MinIaidValue=None, MaxIaidValue=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if StartAddress is not None:
            self._StartAddress = StartAddress
            properties['StartAddress'] = StartAddress
        if HostStep is not None:
            self._HostStep = HostStep
            properties['HostStep'] = HostStep
        if AddressCount is not None:
            self._AddressCount = AddressCount
            properties['AddressCount'] = AddressCount
        if PreferredLifetime is not None:
            self._PreferredLifetime = PreferredLifetime
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            self._ValidLifetime = ValidLifetime
            properties['ValidLifetime'] = ValidLifetime
        if MinIaidValue is not None:
            self._MinIaidValue = MinIaidValue
            properties['MinIaidValue'] = MinIaidValue
        if MaxIaidValue is not None:
            self._MaxIaidValue = MaxIaidValue
            properties['MaxIaidValue'] = MaxIaidValue

        super(Dhcpv6AddressPoolsConfig, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def StartAddress(self):
        """
        get the value of property _StartAddress
        """
        if self.force_auto_sync:
            self.get('StartAddress')
        return self._StartAddress

    @property
    def HostStep(self):
        """
        get the value of property _HostStep
        """
        if self.force_auto_sync:
            self.get('HostStep')
        return self._HostStep

    @property
    def AddressCount(self):
        """
        get the value of property _AddressCount
        """
        if self.force_auto_sync:
            self.get('AddressCount')
        return self._AddressCount

    @property
    def PreferredLifetime(self):
        """
        get the value of property _PreferredLifetime
        """
        if self.force_auto_sync:
            self.get('PreferredLifetime')
        return self._PreferredLifetime

    @property
    def ValidLifetime(self):
        """
        get the value of property _ValidLifetime
        """
        if self.force_auto_sync:
            self.get('ValidLifetime')
        return self._ValidLifetime

    @property
    def MinIaidValue(self):
        """
        get the value of property _MinIaidValue
        """
        if self.force_auto_sync:
            self.get('MinIaidValue')
        return self._MinIaidValue

    @property
    def MaxIaidValue(self):
        """
        get the value of property _MaxIaidValue
        """
        if self.force_auto_sync:
            self.get('MaxIaidValue')
        return self._MaxIaidValue

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @StartAddress.setter
    def StartAddress(self, value):
        self._StartAddress = value
        self.edit(StartAddress=value)

    @HostStep.setter
    def HostStep(self, value):
        self._HostStep = value
        self.edit(HostStep=value)

    @AddressCount.setter
    def AddressCount(self, value):
        self._AddressCount = value
        self.edit(AddressCount=value)

    @PreferredLifetime.setter
    def PreferredLifetime(self, value):
        self._PreferredLifetime = value
        self.edit(PreferredLifetime=value)

    @ValidLifetime.setter
    def ValidLifetime(self, value):
        self._ValidLifetime = value
        self.edit(ValidLifetime=value)

    @MinIaidValue.setter
    def MinIaidValue(self, value):
        self._MinIaidValue = value
        self.edit(MinIaidValue=value)

    @MaxIaidValue.setter
    def MaxIaidValue(self, value):
        self._MaxIaidValue = value
        self.edit(MaxIaidValue=value)

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_startaddress_with_str(self, value):
        self._StartAddress = value

    def _set_hoststep_with_str(self, value):
        self._HostStep = value

    def _set_addresscount_with_str(self, value):
        try:
            self._AddressCount = int(value)
        except ValueError:
            self._AddressCount = hex(int(value, 16))

    def _set_preferredlifetime_with_str(self, value):
        try:
            self._PreferredLifetime = int(value)
        except ValueError:
            self._PreferredLifetime = hex(int(value, 16))

    def _set_validlifetime_with_str(self, value):
        try:
            self._ValidLifetime = int(value)
        except ValueError:
            self._ValidLifetime = hex(int(value, 16))

    def _set_miniaidvalue_with_str(self, value):
        try:
            self._MinIaidValue = int(value)
        except ValueError:
            self._MinIaidValue = hex(int(value, 16))

    def _set_maxiaidvalue_with_str(self, value):
        try:
            self._MaxIaidValue = int(value)
        except ValueError:
            self._MaxIaidValue = hex(int(value, 16))

