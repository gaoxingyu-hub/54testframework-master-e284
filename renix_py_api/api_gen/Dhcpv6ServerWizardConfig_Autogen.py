"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class Dhcpv6ServerWizardConfig(ProtocolWizardConfig):
    def __init__(self, PreferredLifetime=None, ValidLifetime=None, RenewalTimer=None, RebindingTimer=None, PrefixLength=None, PrefixCount=None, StartPrefix=None, PrefixStep=None, AddressPrefixLength=None, AddressCount=None, StartAddress=None, AddressStep=None, **kwargs):
        self._PreferredLifetime = PreferredLifetime  # Preferred Lifetime (secs)
        self._ValidLifetime = ValidLifetime  # Valid Lifetime (secs)
        self._RenewalTimer = RenewalTimer  # Renewal Timer(%)
        self._RebindingTimer = RebindingTimer  # Rebinding Timer(%)
        self._PrefixLength = PrefixLength  # Prefix Length
        self._PrefixCount = PrefixCount  # Prefix per server
        self._StartPrefix = StartPrefix  # Start Prefix
        self._PrefixStep = PrefixStep  # Step
        self._AddressPrefixLength = AddressPrefixLength  # Prefix Length
        self._AddressCount = AddressCount  # Address per server
        self._StartAddress = StartAddress  # Start Address
        self._AddressStep = AddressStep  # Step

        properties = kwargs.copy()
        if PreferredLifetime is not None:
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            properties['ValidLifetime'] = ValidLifetime
        if RenewalTimer is not None:
            properties['RenewalTimer'] = RenewalTimer
        if RebindingTimer is not None:
            properties['RebindingTimer'] = RebindingTimer
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if PrefixCount is not None:
            properties['PrefixCount'] = PrefixCount
        if StartPrefix is not None:
            properties['StartPrefix'] = StartPrefix
        if PrefixStep is not None:
            properties['PrefixStep'] = PrefixStep
        if AddressPrefixLength is not None:
            properties['AddressPrefixLength'] = AddressPrefixLength
        if AddressCount is not None:
            properties['AddressCount'] = AddressCount
        if StartAddress is not None:
            properties['StartAddress'] = StartAddress
        if AddressStep is not None:
            properties['AddressStep'] = AddressStep

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ServerWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PreferredLifetime=None, ValidLifetime=None, RenewalTimer=None, RebindingTimer=None, PrefixLength=None, PrefixCount=None, StartPrefix=None, PrefixStep=None, AddressPrefixLength=None, AddressCount=None, StartAddress=None, AddressStep=None, **kwargs):
        properties = kwargs.copy()
        if PreferredLifetime is not None:
            self._PreferredLifetime = PreferredLifetime
            properties['PreferredLifetime'] = PreferredLifetime
        if ValidLifetime is not None:
            self._ValidLifetime = ValidLifetime
            properties['ValidLifetime'] = ValidLifetime
        if RenewalTimer is not None:
            self._RenewalTimer = RenewalTimer
            properties['RenewalTimer'] = RenewalTimer
        if RebindingTimer is not None:
            self._RebindingTimer = RebindingTimer
            properties['RebindingTimer'] = RebindingTimer
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if PrefixCount is not None:
            self._PrefixCount = PrefixCount
            properties['PrefixCount'] = PrefixCount
        if StartPrefix is not None:
            self._StartPrefix = StartPrefix
            properties['StartPrefix'] = StartPrefix
        if PrefixStep is not None:
            self._PrefixStep = PrefixStep
            properties['PrefixStep'] = PrefixStep
        if AddressPrefixLength is not None:
            self._AddressPrefixLength = AddressPrefixLength
            properties['AddressPrefixLength'] = AddressPrefixLength
        if AddressCount is not None:
            self._AddressCount = AddressCount
            properties['AddressCount'] = AddressCount
        if StartAddress is not None:
            self._StartAddress = StartAddress
            properties['StartAddress'] = StartAddress
        if AddressStep is not None:
            self._AddressStep = AddressStep
            properties['AddressStep'] = AddressStep

        super(Dhcpv6ServerWizardConfig, self).edit(**properties)

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
    def RenewalTimer(self):
        """
        get the value of property _RenewalTimer
        """
        if self.force_auto_sync:
            self.get('RenewalTimer')
        return self._RenewalTimer

    @property
    def RebindingTimer(self):
        """
        get the value of property _RebindingTimer
        """
        if self.force_auto_sync:
            self.get('RebindingTimer')
        return self._RebindingTimer

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def PrefixCount(self):
        """
        get the value of property _PrefixCount
        """
        if self.force_auto_sync:
            self.get('PrefixCount')
        return self._PrefixCount

    @property
    def StartPrefix(self):
        """
        get the value of property _StartPrefix
        """
        if self.force_auto_sync:
            self.get('StartPrefix')
        return self._StartPrefix

    @property
    def PrefixStep(self):
        """
        get the value of property _PrefixStep
        """
        if self.force_auto_sync:
            self.get('PrefixStep')
        return self._PrefixStep

    @property
    def AddressPrefixLength(self):
        """
        get the value of property _AddressPrefixLength
        """
        if self.force_auto_sync:
            self.get('AddressPrefixLength')
        return self._AddressPrefixLength

    @property
    def AddressCount(self):
        """
        get the value of property _AddressCount
        """
        if self.force_auto_sync:
            self.get('AddressCount')
        return self._AddressCount

    @property
    def StartAddress(self):
        """
        get the value of property _StartAddress
        """
        if self.force_auto_sync:
            self.get('StartAddress')
        return self._StartAddress

    @property
    def AddressStep(self):
        """
        get the value of property _AddressStep
        """
        if self.force_auto_sync:
            self.get('AddressStep')
        return self._AddressStep

    @PreferredLifetime.setter
    def PreferredLifetime(self, value):
        self._PreferredLifetime = value
        self.edit(PreferredLifetime=value)

    @ValidLifetime.setter
    def ValidLifetime(self, value):
        self._ValidLifetime = value
        self.edit(ValidLifetime=value)

    @RenewalTimer.setter
    def RenewalTimer(self, value):
        self._RenewalTimer = value
        self.edit(RenewalTimer=value)

    @RebindingTimer.setter
    def RebindingTimer(self, value):
        self._RebindingTimer = value
        self.edit(RebindingTimer=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @PrefixCount.setter
    def PrefixCount(self, value):
        self._PrefixCount = value
        self.edit(PrefixCount=value)

    @StartPrefix.setter
    def StartPrefix(self, value):
        self._StartPrefix = value
        self.edit(StartPrefix=value)

    @PrefixStep.setter
    def PrefixStep(self, value):
        self._PrefixStep = value
        self.edit(PrefixStep=value)

    @AddressPrefixLength.setter
    def AddressPrefixLength(self, value):
        self._AddressPrefixLength = value
        self.edit(AddressPrefixLength=value)

    @AddressCount.setter
    def AddressCount(self, value):
        self._AddressCount = value
        self.edit(AddressCount=value)

    @StartAddress.setter
    def StartAddress(self, value):
        self._StartAddress = value
        self.edit(StartAddress=value)

    @AddressStep.setter
    def AddressStep(self, value):
        self._AddressStep = value
        self.edit(AddressStep=value)

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

    def _set_renewaltimer_with_str(self, value):
        try:
            self._RenewalTimer = int(value)
        except ValueError:
            self._RenewalTimer = hex(int(value, 16))

    def _set_rebindingtimer_with_str(self, value):
        try:
            self._RebindingTimer = int(value)
        except ValueError:
            self._RebindingTimer = hex(int(value, 16))

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_prefixcount_with_str(self, value):
        try:
            self._PrefixCount = int(value)
        except ValueError:
            self._PrefixCount = hex(int(value, 16))

    def _set_startprefix_with_str(self, value):
        self._StartPrefix = value

    def _set_prefixstep_with_str(self, value):
        self._PrefixStep = value

    def _set_addressprefixlength_with_str(self, value):
        try:
            self._AddressPrefixLength = int(value)
        except ValueError:
            self._AddressPrefixLength = hex(int(value, 16))

    def _set_addresscount_with_str(self, value):
        try:
            self._AddressCount = int(value)
        except ValueError:
            self._AddressCount = hex(int(value, 16))

    def _set_startaddress_with_str(self, value):
        self._StartAddress = value

    def _set_addressstep_with_str(self, value):
        self._AddressStep = value

