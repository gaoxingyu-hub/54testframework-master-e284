"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv4LeaseStats(Result):
    def __init__(self, **kwargs):
        self._ServerHandle = ''  # Server Name, not editable
        self._ClientId = '00:00:00:00:00:00'  # Client ID, not editable
        self._ClientIp = '0.0.0.0'  # Client IP Address, not editable
        self._LeaseTime = 0  # Lease Time (sec), not editable
        self._LeaseLeft = 0  # Lease Left (secs), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4LeaseStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def ServerHandle(self):
        """
        get the value of property _ServerHandle
        """
        if self.force_auto_sync:
            self.get('ServerHandle')
        return self._ServerHandle

    @property
    def ClientId(self):
        """
        get the value of property _ClientId
        """
        if self.force_auto_sync:
            self.get('ClientId')
        return self._ClientId

    @property
    def ClientIp(self):
        """
        get the value of property _ClientIp
        """
        if self.force_auto_sync:
            self.get('ClientIp')
        return self._ClientIp

    @property
    def LeaseTime(self):
        """
        get the value of property _LeaseTime
        """
        if self.force_auto_sync:
            self.get('LeaseTime')
        return self._LeaseTime

    @property
    def LeaseLeft(self):
        """
        get the value of property _LeaseLeft
        """
        if self.force_auto_sync:
            self.get('LeaseLeft')
        return self._LeaseLeft

    def _set_serverhandle_with_str(self, value):
        self._ServerHandle = value

    def _set_clientid_with_str(self, value):
        self._ClientId = value

    def _set_clientip_with_str(self, value):
        self._ClientIp = value

    def _set_leasetime_with_str(self, value):
        try:
            self._LeaseTime = int(value)
        except ValueError:
            self._LeaseTime = hex(int(value, 16))

    def _set_leaseleft_with_str(self, value):
        try:
            self._LeaseLeft = int(value)
        except ValueError:
            self._LeaseLeft = hex(int(value, 16))

