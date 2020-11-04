"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsSOARecord(DnsRecord):
    def __init__(self, NameServer=None, EmailAddress=None, SN=None, Expire=None, **kwargs):
        self._NameServer = NameServer  # Name Server
        self._EmailAddress = EmailAddress  # Email
        self._SN = SN  # Serial Number
        self._Expire = Expire  # Expire

        properties = kwargs.copy()
        if NameServer is not None:
            properties['NameServer'] = NameServer
        if EmailAddress is not None:
            properties['EmailAddress'] = EmailAddress
        if SN is not None:
            properties['SN'] = SN
        if Expire is not None:
            properties['Expire'] = Expire

        # call base class function, and it will send message to renix server to create a class.
        super(DnsSOARecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, NameServer=None, EmailAddress=None, SN=None, Expire=None, **kwargs):
        properties = kwargs.copy()
        if NameServer is not None:
            self._NameServer = NameServer
            properties['NameServer'] = NameServer
        if EmailAddress is not None:
            self._EmailAddress = EmailAddress
            properties['EmailAddress'] = EmailAddress
        if SN is not None:
            self._SN = SN
            properties['SN'] = SN
        if Expire is not None:
            self._Expire = Expire
            properties['Expire'] = Expire

        super(DnsSOARecord, self).edit(**properties)

    @property
    def NameServer(self):
        """
        get the value of property _NameServer
        """
        if self.force_auto_sync:
            self.get('NameServer')
        return self._NameServer

    @property
    def EmailAddress(self):
        """
        get the value of property _EmailAddress
        """
        if self.force_auto_sync:
            self.get('EmailAddress')
        return self._EmailAddress

    @property
    def SN(self):
        """
        get the value of property _SN
        """
        if self.force_auto_sync:
            self.get('SN')
        return self._SN

    @property
    def Expire(self):
        """
        get the value of property _Expire
        """
        if self.force_auto_sync:
            self.get('Expire')
        return self._Expire

    @NameServer.setter
    def NameServer(self, value):
        self._NameServer = value
        self.edit(NameServer=value)

    @EmailAddress.setter
    def EmailAddress(self, value):
        self._EmailAddress = value
        self.edit(EmailAddress=value)

    @SN.setter
    def SN(self, value):
        self._SN = value
        self.edit(SN=value)

    @Expire.setter
    def Expire(self, value):
        self._Expire = value
        self.edit(Expire=value)

    def _set_nameserver_with_str(self, value):
        self._NameServer = value

    def _set_emailaddress_with_str(self, value):
        self._EmailAddress = value

    def _set_sn_with_str(self, value):
        try:
            self._SN = int(value)
        except ValueError:
            self._SN = hex(int(value, 16))

    def _set_expire_with_str(self, value):
        try:
            self._Expire = int(value)
        except ValueError:
            self._Expire = hex(int(value, 16))

