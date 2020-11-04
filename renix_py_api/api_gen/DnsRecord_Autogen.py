"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class DnsRecord(ROMObject):
    def __init__(self, DomainName=None, RecordType=None, TTL=None, **kwargs):
        self._DomainName = DomainName  # Record Name
        self._RecordType = RecordType  # Record Type
        self._TTL = TTL  # TTL

        properties = kwargs.copy()
        if DomainName is not None:
            properties['DomainName'] = DomainName
        if RecordType is not None:
            properties['RecordType'] = RecordType
        if TTL is not None:
            properties['TTL'] = TTL

        # call base class function, and it will send message to renix server to create a class.
        super(DnsRecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, DomainName=None, RecordType=None, TTL=None, **kwargs):
        properties = kwargs.copy()
        if DomainName is not None:
            self._DomainName = DomainName
            properties['DomainName'] = DomainName
        if RecordType is not None:
            self._RecordType = RecordType
            properties['RecordType'] = RecordType
        if TTL is not None:
            self._TTL = TTL
            properties['TTL'] = TTL

        super(DnsRecord, self).edit(**properties)

    @property
    def DomainName(self):
        """
        get the value of property _DomainName
        """
        if self.force_auto_sync:
            self.get('DomainName')
        return self._DomainName

    @property
    def RecordType(self):
        """
        get the value of property _RecordType
        """
        if self.force_auto_sync:
            self.get('RecordType')
        return self._RecordType

    @property
    def TTL(self):
        """
        get the value of property _TTL
        """
        if self.force_auto_sync:
            self.get('TTL')
        return self._TTL

    @DomainName.setter
    def DomainName(self, value):
        self._DomainName = value
        self.edit(DomainName=value)

    @RecordType.setter
    def RecordType(self, value):
        self._RecordType = value
        self.edit(RecordType=value)

    @TTL.setter
    def TTL(self, value):
        self._TTL = value
        self.edit(TTL=value)

    def _set_domainname_with_str(self, value):
        self._DomainName = value

    def _set_recordtype_with_str(self, value):
        seperate = value.find(':')
        exec('self._RecordType = DnsRecordType.%s' % value[:seperate])

    def _set_ttl_with_str(self, value):
        try:
            self._TTL = int(value)
        except ValueError:
            self._TTL = hex(int(value, 16))

