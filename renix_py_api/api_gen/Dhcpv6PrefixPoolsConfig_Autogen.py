"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv6PrefixPoolsConfig(ROMObject):
    def __init__(self, PrefixLength=None, PrefixPoolStart=None, PrefixPoolStep=None, PrefixAddressCount=None, PreferredLifetime=None, ValidLifetime=None, MinIaidValue=None, MaxIaidValue=None, **kwargs):
        self._PrefixLength = PrefixLength  # Prefix Pool Prefix Length
        self._PrefixPoolStart = PrefixPoolStart  # Prefix Pool Start
        self._PrefixPoolStep = PrefixPoolStep  # Prefix Pool Step
        self._PrefixAddressCount = PrefixAddressCount  # Prefix Address Count
        self._PreferredLifetime = PreferredLifetime  # Preferred Lifetime (secs)
        self._ValidLifetime = ValidLifetime  # Valid Lifetime (secs)
        self._MinIaidValue = MinIaidValue  # Minimum IAID Value
        self._MaxIaidValue = MaxIaidValue  # Maximum IAID Value

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if PrefixPoolStart is not None:
            properties['PrefixPoolStart'] = PrefixPoolStart
        if PrefixPoolStep is not None:
            properties['PrefixPoolStep'] = PrefixPoolStep
        if PrefixAddressCount is not None:
            properties['PrefixAddressCount'] = PrefixAddressCount
        if PreferredLifetime is not None:
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            properties['ValidLifetime'] = ValidLifetime
        if MinIaidValue is not None:
            properties['MinIaidValue'] = MinIaidValue
        if MaxIaidValue is not None:
            properties['MaxIaidValue'] = MaxIaidValue

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6PrefixPoolsConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, PrefixPoolStart=None, PrefixPoolStep=None, PrefixAddressCount=None, PreferredLifetime=None, ValidLifetime=None, MinIaidValue=None, MaxIaidValue=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if PrefixPoolStart is not None:
            self._PrefixPoolStart = PrefixPoolStart
            properties['PrefixPoolStart'] = PrefixPoolStart
        if PrefixPoolStep is not None:
            self._PrefixPoolStep = PrefixPoolStep
            properties['PrefixPoolStep'] = PrefixPoolStep
        if PrefixAddressCount is not None:
            self._PrefixAddressCount = PrefixAddressCount
            properties['PrefixAddressCount'] = PrefixAddressCount
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

        super(Dhcpv6PrefixPoolsConfig, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def PrefixPoolStart(self):
        """
        get the value of property _PrefixPoolStart
        """
        if self.force_auto_sync:
            self.get('PrefixPoolStart')
        return self._PrefixPoolStart

    @property
    def PrefixPoolStep(self):
        """
        get the value of property _PrefixPoolStep
        """
        if self.force_auto_sync:
            self.get('PrefixPoolStep')
        return self._PrefixPoolStep

    @property
    def PrefixAddressCount(self):
        """
        get the value of property _PrefixAddressCount
        """
        if self.force_auto_sync:
            self.get('PrefixAddressCount')
        return self._PrefixAddressCount

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

    @PrefixPoolStart.setter
    def PrefixPoolStart(self, value):
        self._PrefixPoolStart = value
        self.edit(PrefixPoolStart=value)

    @PrefixPoolStep.setter
    def PrefixPoolStep(self, value):
        self._PrefixPoolStep = value
        self.edit(PrefixPoolStep=value)

    @PrefixAddressCount.setter
    def PrefixAddressCount(self, value):
        self._PrefixAddressCount = value
        self.edit(PrefixAddressCount=value)

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

    def _set_prefixpoolstart_with_str(self, value):
        self._PrefixPoolStart = value

    def _set_prefixpoolstep_with_str(self, value):
        self._PrefixPoolStep = value

    def _set_prefixaddresscount_with_str(self, value):
        try:
            self._PrefixAddressCount = int(value)
        except ValueError:
            self._PrefixAddressCount = hex(int(value, 16))

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

