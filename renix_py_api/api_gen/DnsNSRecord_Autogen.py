"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsNSRecord(DnsRecord):
    def __init__(self, NS=None, **kwargs):
        self._NS = NS  # Name Server

        properties = kwargs.copy()
        if NS is not None:
            properties['NS'] = NS

        # call base class function, and it will send message to renix server to create a class.
        super(DnsNSRecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NS=None, **kwargs):
        properties = kwargs.copy()
        if NS is not None:
            self._NS = NS
            properties['NS'] = NS

        super(DnsNSRecord, self).edit(**properties)

    @property
    def NS(self):
        """
        get the value of property _NS
        """
        if self.force_auto_sync:
            self.get('NS')
        return self._NS

    @NS.setter
    def NS(self, value):
        self._NS = value
        self.edit(NS=value)

    def _set_ns_with_str(self, value):
        self._NS = value

