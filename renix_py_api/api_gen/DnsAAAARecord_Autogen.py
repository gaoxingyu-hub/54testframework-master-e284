"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsAAAARecord(DnsRecord):
    def __init__(self, IpAddress=None, **kwargs):
        self._IpAddress = IpAddress  # IPv6 Address

        properties = kwargs.copy()
        if IpAddress is not None:
            properties['IpAddress'] = IpAddress

        # call base class function, and it will send message to renix server to create a class.
        super(DnsAAAARecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, IpAddress=None, **kwargs):
        properties = kwargs.copy()
        if IpAddress is not None:
            self._IpAddress = IpAddress
            properties['IpAddress'] = IpAddress

        super(DnsAAAARecord, self).edit(**properties)

    @property
    def IpAddress(self):
        """
        get the value of property _IpAddress
        """
        if self.force_auto_sync:
            self.get('IpAddress')
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, value):
        self._IpAddress = value
        self.edit(IpAddress=value)

    def _set_ipaddress_with_str(self, value):
        self._IpAddress = value

