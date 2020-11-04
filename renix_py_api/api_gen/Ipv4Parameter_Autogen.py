"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Ipv4Parameter(ROMObject):
    def __init__(self, Ipv4SourceAddress=None, Ipv4DestinationAddress=None, IsBound=None, **kwargs):
        self._Ipv4SourceAddress = Ipv4SourceAddress  # Source IPv4 Address
        self._Ipv4DestinationAddress = Ipv4DestinationAddress  # Destination IPv4 Address
        self._IsBound = IsBound  # Current field is bound for interface

        properties = kwargs.copy()
        if Ipv4SourceAddress is not None:
            properties['Ipv4SourceAddress'] = Ipv4SourceAddress
        if Ipv4DestinationAddress is not None:
            properties['Ipv4DestinationAddress'] = Ipv4DestinationAddress
        if IsBound is not None:
            properties['IsBound'] = IsBound

        # call base class function, and it will send message to renix server to create a class.
        super(Ipv4Parameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Ipv4SourceAddress=None, Ipv4DestinationAddress=None, IsBound=None, **kwargs):
        properties = kwargs.copy()
        if Ipv4SourceAddress is not None:
            self._Ipv4SourceAddress = Ipv4SourceAddress
            properties['Ipv4SourceAddress'] = Ipv4SourceAddress
        if Ipv4DestinationAddress is not None:
            self._Ipv4DestinationAddress = Ipv4DestinationAddress
            properties['Ipv4DestinationAddress'] = Ipv4DestinationAddress
        if IsBound is not None:
            self._IsBound = IsBound
            properties['IsBound'] = IsBound

        super(Ipv4Parameter, self).edit(**properties)

    @property
    def Ipv4SourceAddress(self):
        """
        get the value of property _Ipv4SourceAddress
        """
        if self.force_auto_sync:
            self.get('Ipv4SourceAddress')
        return self._Ipv4SourceAddress

    @property
    def Ipv4DestinationAddress(self):
        """
        get the value of property _Ipv4DestinationAddress
        """
        if self.force_auto_sync:
            self.get('Ipv4DestinationAddress')
        return self._Ipv4DestinationAddress

    @property
    def IsBound(self):
        """
        get the value of property _IsBound
        """
        if self.force_auto_sync:
            self.get('IsBound')
        return self._IsBound

    @Ipv4SourceAddress.setter
    def Ipv4SourceAddress(self, value):
        self._Ipv4SourceAddress = value
        self.edit(Ipv4SourceAddress=value)

    @Ipv4DestinationAddress.setter
    def Ipv4DestinationAddress(self, value):
        self._Ipv4DestinationAddress = value
        self.edit(Ipv4DestinationAddress=value)

    @IsBound.setter
    def IsBound(self, value):
        self._IsBound = value
        self.edit(IsBound=value)

    def _set_ipv4sourceaddress_with_str(self, value):
        self._Ipv4SourceAddress = value

    def _set_ipv4destinationaddress_with_str(self, value):
        self._Ipv4DestinationAddress = value

    def _set_isbound_with_str(self, value):
        self._IsBound = (value == 'True')

