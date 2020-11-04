"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DynamicNetworkLayer_Autogen import DynamicNetworkLayer


@rom_manager.rom
class Ipv4MulticastGroup(DynamicNetworkLayer):
    def __init__(self, StartIpAddress=None, NumberOfGroups=None, Increment=None, PrefixLength=None, **kwargs):
        self._StartIpAddress = StartIpAddress  # Start IP Address
        self._NumberOfGroups = NumberOfGroups  # Number of Groups
        self._Increment = Increment  # Increment
        self._PrefixLength = PrefixLength  # Prefix Length

        properties = kwargs.copy()
        if StartIpAddress is not None:
            properties['StartIpAddress'] = StartIpAddress
        if NumberOfGroups is not None:
            properties['NumberOfGroups'] = NumberOfGroups
        if Increment is not None:
            properties['Increment'] = Increment
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv4MulticastGroup, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StartIpAddress=None, NumberOfGroups=None, Increment=None, PrefixLength=None, **kwargs):
        properties = kwargs.copy()
        if StartIpAddress is not None:
            self._StartIpAddress = StartIpAddress
            properties['StartIpAddress'] = StartIpAddress
        if NumberOfGroups is not None:
            self._NumberOfGroups = NumberOfGroups
            properties['NumberOfGroups'] = NumberOfGroups
        if Increment is not None:
            self._Increment = Increment
            properties['Increment'] = Increment
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength

        super(Ipv4MulticastGroup, self).edit(**properties)

    @property
    def StartIpAddress(self):
        """
        get the value of property _StartIpAddress
        """
        if self.force_auto_sync:
            self.get('StartIpAddress')
        return self._StartIpAddress

    @property
    def NumberOfGroups(self):
        """
        get the value of property _NumberOfGroups
        """
        if self.force_auto_sync:
            self.get('NumberOfGroups')
        return self._NumberOfGroups

    @property
    def Increment(self):
        """
        get the value of property _Increment
        """
        if self.force_auto_sync:
            self.get('Increment')
        return self._Increment

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @StartIpAddress.setter
    def StartIpAddress(self, value):
        self._StartIpAddress = value
        self.edit(StartIpAddress=value)

    @NumberOfGroups.setter
    def NumberOfGroups(self, value):
        self._NumberOfGroups = value
        self.edit(NumberOfGroups=value)

    @Increment.setter
    def Increment(self, value):
        self._Increment = value
        self.edit(Increment=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    def _set_startipaddress_with_str(self, value):
        self._StartIpAddress = value

    def _set_numberofgroups_with_str(self, value):
        try:
            self._NumberOfGroups = int(value)
        except ValueError:
            self._NumberOfGroups = hex(int(value, 16))

    def _set_increment_with_str(self, value):
        try:
            self._Increment = int(value)
        except ValueError:
            self._Increment = hex(int(value, 16))

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

