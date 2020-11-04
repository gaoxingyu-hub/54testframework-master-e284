"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ProtocolWizardConfig_Autogen import ProtocolWizardConfig


@rom_manager.rom
class Dhcpv4ServerWizardConfig(ProtocolWizardConfig):
    def __init__(self, PrefixLength=None, LimitPoolCount=None, AddressCount=None, StartAddress=None, AddressStep=None, **kwargs):
        self._PrefixLength = PrefixLength  # Prefix Length
        self._LimitPoolCount = LimitPoolCount  # Limit Pool Address Count
        self._AddressCount = AddressCount  # Address per server
        self._StartAddress = StartAddress  # Start Address
        self._AddressStep = AddressStep  # Step

        properties = kwargs.copy()
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if LimitPoolCount is not None:
            properties['LimitPoolCount'] = LimitPoolCount
        if AddressCount is not None:
            properties['AddressCount'] = AddressCount
        if StartAddress is not None:
            properties['StartAddress'] = StartAddress
        if AddressStep is not None:
            properties['AddressStep'] = AddressStep

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerWizardConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PrefixLength=None, LimitPoolCount=None, AddressCount=None, StartAddress=None, AddressStep=None, **kwargs):
        properties = kwargs.copy()
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if LimitPoolCount is not None:
            self._LimitPoolCount = LimitPoolCount
            properties['LimitPoolCount'] = LimitPoolCount
        if AddressCount is not None:
            self._AddressCount = AddressCount
            properties['AddressCount'] = AddressCount
        if StartAddress is not None:
            self._StartAddress = StartAddress
            properties['StartAddress'] = StartAddress
        if AddressStep is not None:
            self._AddressStep = AddressStep
            properties['AddressStep'] = AddressStep

        super(Dhcpv4ServerWizardConfig, self).edit(**properties)

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def LimitPoolCount(self):
        """
        get the value of property _LimitPoolCount
        """
        if self.force_auto_sync:
            self.get('LimitPoolCount')
        return self._LimitPoolCount

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

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @LimitPoolCount.setter
    def LimitPoolCount(self, value):
        self._LimitPoolCount = value
        self.edit(LimitPoolCount=value)

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

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_limitpoolcount_with_str(self, value):
        self._LimitPoolCount = (value == 'True')

    def _set_addresscount_with_str(self, value):
        try:
            self._AddressCount = int(value)
        except ValueError:
            self._AddressCount = hex(int(value, 16))

    def _set_startaddress_with_str(self, value):
        self._StartAddress = value

    def _set_addressstep_with_str(self, value):
        self._AddressStep = value

