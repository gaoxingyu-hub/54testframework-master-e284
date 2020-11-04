"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv6LeaseStatistics(Result):
    def __init__(self, **kwargs):
        self._Dhcpv6ServerId = ''  # DHCPv6 Server Session Name, not editable
        self._Dhcpv6LeaseId = ''  # DHCPv6 Lease ID, not editable
        self._Iaid = 0  # IAID, not editable
        self._ClientDuid = ''  # Client DUID, not editable
        self._ClientIpv6Address = '::'  # Client IPv6 Address, not editable
        self._LeaseRemaining = 0  # Lease Remaining (sec), not editable
        self._LeaseTime = 0  # Lease Time (sec), not editable
        self._PrefixLength = 0  # Prefix Length, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6LeaseStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dhcpv6ServerId(self):
        """
        get the value of property _Dhcpv6ServerId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6ServerId')
        return self._Dhcpv6ServerId

    @property
    def Dhcpv6LeaseId(self):
        """
        get the value of property _Dhcpv6LeaseId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6LeaseId')
        return self._Dhcpv6LeaseId

    @property
    def Iaid(self):
        """
        get the value of property _Iaid
        """
        if self.force_auto_sync:
            self.get('Iaid')
        return self._Iaid

    @property
    def ClientDuid(self):
        """
        get the value of property _ClientDuid
        """
        if self.force_auto_sync:
            self.get('ClientDuid')
        return self._ClientDuid

    @property
    def ClientIpv6Address(self):
        """
        get the value of property _ClientIpv6Address
        """
        if self.force_auto_sync:
            self.get('ClientIpv6Address')
        return self._ClientIpv6Address

    @property
    def LeaseRemaining(self):
        """
        get the value of property _LeaseRemaining
        """
        if self.force_auto_sync:
            self.get('LeaseRemaining')
        return self._LeaseRemaining

    @property
    def LeaseTime(self):
        """
        get the value of property _LeaseTime
        """
        if self.force_auto_sync:
            self.get('LeaseTime')
        return self._LeaseTime

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    def _set_dhcpv6serverid_with_str(self, value):
        self._Dhcpv6ServerId = value

    def _set_dhcpv6leaseid_with_str(self, value):
        self._Dhcpv6LeaseId = value

    def _set_iaid_with_str(self, value):
        try:
            self._Iaid = int(value)
        except ValueError:
            self._Iaid = hex(int(value, 16))

    def _set_clientduid_with_str(self, value):
        self._ClientDuid = value

    def _set_clientipv6address_with_str(self, value):
        self._ClientIpv6Address = value

    def _set_leaseremaining_with_str(self, value):
        try:
            self._LeaseRemaining = int(value)
        except ValueError:
            self._LeaseRemaining = hex(int(value, 16))

    def _set_leasetime_with_str(self, value):
        try:
            self._LeaseTime = int(value)
        except ValueError:
            self._LeaseTime = hex(int(value, 16))

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

