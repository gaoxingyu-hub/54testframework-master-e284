"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsCNAMERecord(DnsRecord):
    def __init__(self, CName=None, **kwargs):
        self._CName = CName  # CNAME

        properties = kwargs.copy()
        if CName is not None:
            properties['CName'] = CName

        # call base class function, and it will send message to renix server to create a class.
        super(DnsCNAMERecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, CName=None, **kwargs):
        properties = kwargs.copy()
        if CName is not None:
            self._CName = CName
            properties['CName'] = CName

        super(DnsCNAMERecord, self).edit(**properties)

    @property
    def CName(self):
        """
        get the value of property _CName
        """
        if self.force_auto_sync:
            self.get('CName')
        return self._CName

    @CName.setter
    def CName(self, value):
        self._CName = value
        self.edit(CName=value)

    def _set_cname_with_str(self, value):
        self._CName = value

