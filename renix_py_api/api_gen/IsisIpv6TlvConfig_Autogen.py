"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IsisIpAddrTlvConfig_Autogen import IsisIpAddrTlvConfig


@rom_manager.rom
class IsisIpv6TlvConfig(IsisIpAddrTlvConfig):
    def __init__(self, StartIpv6Prefix=None, PrefixLength=None, **kwargs):
        self._StartIpv6Prefix = StartIpv6Prefix  # Start IPv6 Prefix
        self._EndIpv6Prefix = '2000::1'  # End IPv6 Prefix, not editable
        self._PrefixLength = PrefixLength  # Prefix Length

        properties = kwargs.copy()
        if StartIpv6Prefix is not None:
            properties['StartIpv6Prefix'] = StartIpv6Prefix
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength

        # call base class function, and it will send message to renix server to create a class.
        super(IsisIpv6TlvConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StartIpv6Prefix=None, PrefixLength=None, **kwargs):
        properties = kwargs.copy()
        if StartIpv6Prefix is not None:
            self._StartIpv6Prefix = StartIpv6Prefix
            properties['StartIpv6Prefix'] = StartIpv6Prefix
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength

        super(IsisIpv6TlvConfig, self).edit(**properties)

    @property
    def StartIpv6Prefix(self):
        """
        get the value of property _StartIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('StartIpv6Prefix')
        return self._StartIpv6Prefix

    @property
    def EndIpv6Prefix(self):
        """
        get the value of property _EndIpv6Prefix
        """
        if self.force_auto_sync:
            self.get('EndIpv6Prefix')
        return self._EndIpv6Prefix

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @StartIpv6Prefix.setter
    def StartIpv6Prefix(self, value):
        self._StartIpv6Prefix = value
        self.edit(StartIpv6Prefix=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    def _set_startipv6prefix_with_str(self, value):
        self._StartIpv6Prefix = value

    def _set_endipv6prefix_with_str(self, value):
        self._EndIpv6Prefix = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

