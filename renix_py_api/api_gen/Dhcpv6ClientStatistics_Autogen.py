"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class Dhcpv6ClientStatistics(Result):
    def __init__(self, **kwargs):
        self._Dhcpv6ClientId = ''  # DHCPv6 Session Name, not editable
        self._IaidValue = 0  # IAID Value, not editable
        self._SessionIndex = 0  # Session Index, not editable
        self._MacAddr = '00:00:00:00:00:00'  # MAC Address, not editable
        self._VlanId = 0  # VLAN ID, not editable
        self._LeaseRx = 0  # Lease Received (sec), not editable
        self._AddressType = ''  # Address Type, not editable
        self._SessionState = ''  # Session State, not editable
        self._StateCode = ''  # State Code, not editable
        self._IpAddress = '::'  # IPv6 Address, not editable
        self._LeaseRemaining = 0  # Lease Remaining (secs), not editable
        self._PrefixLength = 0  # Prefix Length, not editable
        self._RequestResponseTime = 0  # Request Response Time (us), not editable
        self._SolicitResponseTime = 0  # Solicit Response Time (us), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv6ClientStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def Dhcpv6ClientId(self):
        """
        get the value of property _Dhcpv6ClientId
        """
        if self.force_auto_sync:
            self.get('Dhcpv6ClientId')
        return self._Dhcpv6ClientId

    @property
    def IaidValue(self):
        """
        get the value of property _IaidValue
        """
        if self.force_auto_sync:
            self.get('IaidValue')
        return self._IaidValue

    @property
    def SessionIndex(self):
        """
        get the value of property _SessionIndex
        """
        if self.force_auto_sync:
            self.get('SessionIndex')
        return self._SessionIndex

    @property
    def MacAddr(self):
        """
        get the value of property _MacAddr
        """
        if self.force_auto_sync:
            self.get('MacAddr')
        return self._MacAddr

    @property
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def LeaseRx(self):
        """
        get the value of property _LeaseRx
        """
        if self.force_auto_sync:
            self.get('LeaseRx')
        return self._LeaseRx

    @property
    def AddressType(self):
        """
        get the value of property _AddressType
        """
        if self.force_auto_sync:
            self.get('AddressType')
        return self._AddressType

    @property
    def SessionState(self):
        """
        get the value of property _SessionState
        """
        if self.force_auto_sync:
            self.get('SessionState')
        return self._SessionState

    @property
    def StateCode(self):
        """
        get the value of property _StateCode
        """
        if self.force_auto_sync:
            self.get('StateCode')
        return self._StateCode

    @property
    def IpAddress(self):
        """
        get the value of property _IpAddress
        """
        if self.force_auto_sync:
            self.get('IpAddress')
        return self._IpAddress

    @property
    def LeaseRemaining(self):
        """
        get the value of property _LeaseRemaining
        """
        if self.force_auto_sync:
            self.get('LeaseRemaining')
        return self._LeaseRemaining

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def RequestResponseTime(self):
        """
        get the value of property _RequestResponseTime
        """
        if self.force_auto_sync:
            self.get('RequestResponseTime')
        return self._RequestResponseTime

    @property
    def SolicitResponseTime(self):
        """
        get the value of property _SolicitResponseTime
        """
        if self.force_auto_sync:
            self.get('SolicitResponseTime')
        return self._SolicitResponseTime

    def _set_dhcpv6clientid_with_str(self, value):
        self._Dhcpv6ClientId = value

    def _set_iaidvalue_with_str(self, value):
        try:
            self._IaidValue = int(value)
        except ValueError:
            self._IaidValue = hex(int(value, 16))

    def _set_sessionindex_with_str(self, value):
        try:
            self._SessionIndex = int(value)
        except ValueError:
            self._SessionIndex = hex(int(value, 16))

    def _set_macaddr_with_str(self, value):
        self._MacAddr = value

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_leaserx_with_str(self, value):
        try:
            self._LeaseRx = int(value)
        except ValueError:
            self._LeaseRx = hex(int(value, 16))

    def _set_addresstype_with_str(self, value):
        self._AddressType = value

    def _set_sessionstate_with_str(self, value):
        self._SessionState = value

    def _set_statecode_with_str(self, value):
        self._StateCode = value

    def _set_ipaddress_with_str(self, value):
        self._IpAddress = value

    def _set_leaseremaining_with_str(self, value):
        try:
            self._LeaseRemaining = int(value)
        except ValueError:
            self._LeaseRemaining = hex(int(value, 16))

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_requestresponsetime_with_str(self, value):
        try:
            self._RequestResponseTime = int(value)
        except ValueError:
            self._RequestResponseTime = hex(int(value, 16))

    def _set_solicitresponsetime_with_str(self, value):
        try:
            self._SolicitResponseTime = int(value)
        except ValueError:
            self._SolicitResponseTime = hex(int(value, 16))

