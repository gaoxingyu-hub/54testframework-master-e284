"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .DnsRecord_Autogen import DnsRecord


@rom_manager.rom
class DnsMXRecord(DnsRecord):
    def __init__(self, Preference=None, MailServer=None, **kwargs):
        self._Preference = Preference  # Preference
        self._MailServer = MailServer  # Mail Server

        properties = kwargs.copy()
        if Preference is not None:
            properties['Preference'] = Preference
        if MailServer is not None:
            properties['MailServer'] = MailServer

        # call base class function, and it will send message to renix server to create a class.
        super(DnsMXRecord, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Preference=None, MailServer=None, **kwargs):
        properties = kwargs.copy()
        if Preference is not None:
            self._Preference = Preference
            properties['Preference'] = Preference
        if MailServer is not None:
            self._MailServer = MailServer
            properties['MailServer'] = MailServer

        super(DnsMXRecord, self).edit(**properties)

    @property
    def Preference(self):
        """
        get the value of property _Preference
        """
        if self.force_auto_sync:
            self.get('Preference')
        return self._Preference

    @property
    def MailServer(self):
        """
        get the value of property _MailServer
        """
        if self.force_auto_sync:
            self.get('MailServer')
        return self._MailServer

    @Preference.setter
    def Preference(self, value):
        self._Preference = value
        self.edit(Preference=value)

    @MailServer.setter
    def MailServer(self, value):
        self._MailServer = value
        self.edit(MailServer=value)

    def _set_preference_with_str(self, value):
        try:
            self._Preference = int(value)
        except ValueError:
            self._Preference = hex(int(value, 16))

    def _set_mailserver_with_str(self, value):
        self._MailServer = value

