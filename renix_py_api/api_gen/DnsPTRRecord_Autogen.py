"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsPTRRecord(DnsRecord):
    def __init__(self, PTRDomain=None, **kwargs):
        self._PTRDomain = PTRDomain  # PTR Domain

        properties = kwargs.copy()
        if PTRDomain is not None:
            properties['PTRDomain'] = PTRDomain

        # call base class function, and it will send message to renix server to create a class.
        super(DnsPTRRecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, PTRDomain=None, **kwargs):
        properties = kwargs.copy()
        if PTRDomain is not None:
            self._PTRDomain = PTRDomain
            properties['PTRDomain'] = PTRDomain

        super(DnsPTRRecord, self).edit(**properties)

    @property
    def PTRDomain(self):
        """
        get the value of property _PTRDomain
        """
        if self.force_auto_sync:
            self.get('PTRDomain')
        return self._PTRDomain

    @PTRDomain.setter
    def PTRDomain(self, value):
        self._PTRDomain = value
        self.edit(PTRDomain=value)

    def _set_ptrdomain_with_str(self, value):
        self._PTRDomain = value

