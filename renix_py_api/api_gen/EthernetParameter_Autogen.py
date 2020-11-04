"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class EthernetParameter(ROMObject):
    def __init__(self, MacSourceAddress=None, MacDestinationAddress=None, IsBound=None, **kwargs):
        self._MacSourceAddress = MacSourceAddress  # Source MAC Address
        self._MacDestinationAddress = MacDestinationAddress  # Destination MAC Address
        self._IsBound = IsBound  # Current field is bound for interface

        properties = kwargs.copy()
        if MacSourceAddress is not None:
            properties['MacSourceAddress'] = MacSourceAddress
        if MacDestinationAddress is not None:
            properties['MacDestinationAddress'] = MacDestinationAddress
        if IsBound is not None:
            properties['IsBound'] = IsBound

        # call base class function, and it will send message to renix server to create a class.
        super(EthernetParameter, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, MacSourceAddress=None, MacDestinationAddress=None, IsBound=None, **kwargs):
        properties = kwargs.copy()
        if MacSourceAddress is not None:
            self._MacSourceAddress = MacSourceAddress
            properties['MacSourceAddress'] = MacSourceAddress
        if MacDestinationAddress is not None:
            self._MacDestinationAddress = MacDestinationAddress
            properties['MacDestinationAddress'] = MacDestinationAddress
        if IsBound is not None:
            self._IsBound = IsBound
            properties['IsBound'] = IsBound

        super(EthernetParameter, self).edit(**properties)

    @property
    def MacSourceAddress(self):
        """
        get the value of property _MacSourceAddress
        """
        if self.force_auto_sync:
            self.get('MacSourceAddress')
        return self._MacSourceAddress

    @property
    def MacDestinationAddress(self):
        """
        get the value of property _MacDestinationAddress
        """
        if self.force_auto_sync:
            self.get('MacDestinationAddress')
        return self._MacDestinationAddress

    @property
    def IsBound(self):
        """
        get the value of property _IsBound
        """
        if self.force_auto_sync:
            self.get('IsBound')
        return self._IsBound

    @MacSourceAddress.setter
    def MacSourceAddress(self, value):
        self._MacSourceAddress = value
        self.edit(MacSourceAddress=value)

    @MacDestinationAddress.setter
    def MacDestinationAddress(self, value):
        self._MacDestinationAddress = value
        self.edit(MacDestinationAddress=value)

    @IsBound.setter
    def IsBound(self, value):
        self._IsBound = value
        self.edit(IsBound=value)

    def _set_macsourceaddress_with_str(self, value):
        self._MacSourceAddress = value

    def _set_macdestinationaddress_with_str(self, value):
        self._MacDestinationAddress = value

    def _set_isbound_with_str(self, value):
        self._IsBound = (value == 'True')

