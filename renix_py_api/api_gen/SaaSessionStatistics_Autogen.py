"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class SaaSessionStatistics(Result):
    def __init__(self, **kwargs):
        self._SaaSessionBlockId = ''  # SAA Session Block Name, not editable
        self._SessionIndex = 0  # Session Index, not editable
        self._SessionState = 'Disabled'  # Session State, not editable
        self._MacAddress = '00:00:00:00:00:00'  # MAC Address, not editable
        self._VlanId = 0  # VLAN, not editable
        self._InnerVlanId = 0  # Inner VLAN, not editable
        self._GlobalIpv6Address = '::0'  # Global IPv6 Address, not editable
        self._LinkLocalIpv6Address = '::0'  # Link Local IPv6 Address, not editable
        self._PrefixIpv6Address = '::0'  # Prefix IPv6 Address, not editable
        self._PrefixLength = 0  # Prefix Length, not editable
        self._ValidLifeTime = 0  # Valid Life Time (sec), not editable
        self._PreferredLifeTime = 0  # Preferred Life Time (sec), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(SaaSessionStatistics, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def SaaSessionBlockId(self):
        """
        get the value of property _SaaSessionBlockId
        """
        if self.force_auto_sync:
            self.get('SaaSessionBlockId')
        return self._SaaSessionBlockId

    @property
    def SessionIndex(self):
        """
        get the value of property _SessionIndex
        """
        if self.force_auto_sync:
            self.get('SessionIndex')
        return self._SessionIndex

    @property
    def SessionState(self):
        """
        get the value of property _SessionState
        """
        if self.force_auto_sync:
            self.get('SessionState')
        return self._SessionState

    @property
    def MacAddress(self):
        """
        get the value of property _MacAddress
        """
        if self.force_auto_sync:
            self.get('MacAddress')
        return self._MacAddress

    @property
    def VlanId(self):
        """
        get the value of property _VlanId
        """
        if self.force_auto_sync:
            self.get('VlanId')
        return self._VlanId

    @property
    def InnerVlanId(self):
        """
        get the value of property _InnerVlanId
        """
        if self.force_auto_sync:
            self.get('InnerVlanId')
        return self._InnerVlanId

    @property
    def GlobalIpv6Address(self):
        """
        get the value of property _GlobalIpv6Address
        """
        if self.force_auto_sync:
            self.get('GlobalIpv6Address')
        return self._GlobalIpv6Address

    @property
    def LinkLocalIpv6Address(self):
        """
        get the value of property _LinkLocalIpv6Address
        """
        if self.force_auto_sync:
            self.get('LinkLocalIpv6Address')
        return self._LinkLocalIpv6Address

    @property
    def PrefixIpv6Address(self):
        """
        get the value of property _PrefixIpv6Address
        """
        if self.force_auto_sync:
            self.get('PrefixIpv6Address')
        return self._PrefixIpv6Address

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def ValidLifeTime(self):
        """
        get the value of property _ValidLifeTime
        """
        if self.force_auto_sync:
            self.get('ValidLifeTime')
        return self._ValidLifeTime

    @property
    def PreferredLifeTime(self):
        """
        get the value of property _PreferredLifeTime
        """
        if self.force_auto_sync:
            self.get('PreferredLifeTime')
        return self._PreferredLifeTime

    def _set_saasessionblockid_with_str(self, value):
        self._SaaSessionBlockId = value

    def _set_sessionindex_with_str(self, value):
        try:
            self._SessionIndex = int(value)
        except ValueError:
            self._SessionIndex = hex(int(value, 16))

    def _set_sessionstate_with_str(self, value):
        self._SessionState = value

    def _set_macaddress_with_str(self, value):
        self._MacAddress = value

    def _set_vlanid_with_str(self, value):
        try:
            self._VlanId = int(value)
        except ValueError:
            self._VlanId = hex(int(value, 16))

    def _set_innervlanid_with_str(self, value):
        try:
            self._InnerVlanId = int(value)
        except ValueError:
            self._InnerVlanId = hex(int(value, 16))

    def _set_globalipv6address_with_str(self, value):
        self._GlobalIpv6Address = value

    def _set_linklocalipv6address_with_str(self, value):
        self._LinkLocalIpv6Address = value

    def _set_prefixipv6address_with_str(self, value):
        self._PrefixIpv6Address = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_validlifetime_with_str(self, value):
        try:
            self._ValidLifeTime = int(value)
        except ValueError:
            self._ValidLifeTime = hex(int(value, 16))

    def _set_preferredlifetime_with_str(self, value):
        try:
            self._PreferredLifeTime = int(value)
        except ValueError:
            self._PreferredLifeTime = hex(int(value, 16))

