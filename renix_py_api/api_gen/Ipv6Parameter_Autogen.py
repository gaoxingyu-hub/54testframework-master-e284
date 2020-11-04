"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ipv6Parameter(ROMObject):
    def __init__(self, Ipv6SourceAddress=None, Ipv6DestinationAddress=None, IsBound=None, **kwargs):
        self._Ipv6SourceAddress = Ipv6SourceAddress  # Source IPv6 Address
        self._Ipv6DestinationAddress = Ipv6DestinationAddress  # Destination IPv6 Address
        self._IsBound = IsBound  # Current field is bound for interface

        properties = kwargs.copy()
        if Ipv6SourceAddress is not None:
            properties['Ipv6SourceAddress'] = Ipv6SourceAddress
        if Ipv6DestinationAddress is not None:
            properties['Ipv6DestinationAddress'] = Ipv6DestinationAddress
        if IsBound is not None:
            properties['IsBound'] = IsBound

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv6Parameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Ipv6SourceAddress=None, Ipv6DestinationAddress=None, IsBound=None, **kwargs):
        properties = kwargs.copy()
        if Ipv6SourceAddress is not None:
            self._Ipv6SourceAddress = Ipv6SourceAddress
            properties['Ipv6SourceAddress'] = Ipv6SourceAddress
        if Ipv6DestinationAddress is not None:
            self._Ipv6DestinationAddress = Ipv6DestinationAddress
            properties['Ipv6DestinationAddress'] = Ipv6DestinationAddress
        if IsBound is not None:
            self._IsBound = IsBound
            properties['IsBound'] = IsBound

        super(Ipv6Parameter, self).edit(**properties)

    @property
    def Ipv6SourceAddress(self):
        """
        get the value of property _Ipv6SourceAddress
        """
        if self.force_auto_sync:
            self.get('Ipv6SourceAddress')
        return self._Ipv6SourceAddress

    @property
    def Ipv6DestinationAddress(self):
        """
        get the value of property _Ipv6DestinationAddress
        """
        if self.force_auto_sync:
            self.get('Ipv6DestinationAddress')
        return self._Ipv6DestinationAddress

    @property
    def IsBound(self):
        """
        get the value of property _IsBound
        """
        if self.force_auto_sync:
            self.get('IsBound')
        return self._IsBound

    @Ipv6SourceAddress.setter
    def Ipv6SourceAddress(self, value):
        self._Ipv6SourceAddress = value
        self.edit(Ipv6SourceAddress=value)

    @Ipv6DestinationAddress.setter
    def Ipv6DestinationAddress(self, value):
        self._Ipv6DestinationAddress = value
        self.edit(Ipv6DestinationAddress=value)

    @IsBound.setter
    def IsBound(self, value):
        self._IsBound = value
        self.edit(IsBound=value)

    def _set_ipv6sourceaddress_with_str(self, value):
        self._Ipv6SourceAddress = value

    def _set_ipv6destinationaddress_with_str(self, value):
        self._Ipv6DestinationAddress = value

    def _set_isbound_with_str(self, value):
        self._IsBound = (value == 'True')

