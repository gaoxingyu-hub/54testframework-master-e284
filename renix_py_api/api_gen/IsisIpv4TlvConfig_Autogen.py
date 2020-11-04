"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IsisIpAddrTlvConfig_Autogen import IsisIpAddrTlvConfig


@rom_manager.rom
class IsisIpv4TlvConfig(IsisIpAddrTlvConfig):
    def __init__(self, StartIpv4Prefix=None, PrefixLength=None, NarrowMetric=None, **kwargs):
        self._StartIpv4Prefix = StartIpv4Prefix  # Start IPv4 Prefix
        self._EndIpv4Prefix = '192.0.0.1'  # End IPv4 Prefix, not editable
        self._PrefixLength = PrefixLength  # Prefix Length
        self._NarrowMetric = NarrowMetric  # Narrow Metric

        properties = kwargs.copy()
        if StartIpv4Prefix is not None:
            properties['StartIpv4Prefix'] = StartIpv4Prefix
        if PrefixLength is not None:
            properties['PrefixLength'] = PrefixLength
        if NarrowMetric is not None:
            properties['NarrowMetric'] = NarrowMetric

        # call base class function, and it will send message to renix server to create a class.
        super(IsisIpv4TlvConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, StartIpv4Prefix=None, PrefixLength=None, NarrowMetric=None, **kwargs):
        properties = kwargs.copy()
        if StartIpv4Prefix is not None:
            self._StartIpv4Prefix = StartIpv4Prefix
            properties['StartIpv4Prefix'] = StartIpv4Prefix
        if PrefixLength is not None:
            self._PrefixLength = PrefixLength
            properties['PrefixLength'] = PrefixLength
        if NarrowMetric is not None:
            self._NarrowMetric = NarrowMetric
            properties['NarrowMetric'] = NarrowMetric

        super(IsisIpv4TlvConfig, self).edit(**properties)

    @property
    def StartIpv4Prefix(self):
        """
        get the value of property _StartIpv4Prefix
        """
        if self.force_auto_sync:
            self.get('StartIpv4Prefix')
        return self._StartIpv4Prefix

    @property
    def EndIpv4Prefix(self):
        """
        get the value of property _EndIpv4Prefix
        """
        if self.force_auto_sync:
            self.get('EndIpv4Prefix')
        return self._EndIpv4Prefix

    @property
    def PrefixLength(self):
        """
        get the value of property _PrefixLength
        """
        if self.force_auto_sync:
            self.get('PrefixLength')
        return self._PrefixLength

    @property
    def NarrowMetric(self):
        """
        get the value of property _NarrowMetric
        """
        if self.force_auto_sync:
            self.get('NarrowMetric')
        return self._NarrowMetric

    @StartIpv4Prefix.setter
    def StartIpv4Prefix(self, value):
        self._StartIpv4Prefix = value
        self.edit(StartIpv4Prefix=value)

    @PrefixLength.setter
    def PrefixLength(self, value):
        self._PrefixLength = value
        self.edit(PrefixLength=value)

    @NarrowMetric.setter
    def NarrowMetric(self, value):
        self._NarrowMetric = value
        self.edit(NarrowMetric=value)

    def _set_startipv4prefix_with_str(self, value):
        self._StartIpv4Prefix = value

    def _set_endipv4prefix_with_str(self, value):
        self._EndIpv4Prefix = value

    def _set_prefixlength_with_str(self, value):
        try:
            self._PrefixLength = int(value)
        except ValueError:
            self._PrefixLength = hex(int(value, 16))

    def _set_narrowmetric_with_str(self, value):
        try:
            self._NarrowMetric = int(value)
        except ValueError:
            self._NarrowMetric = hex(int(value, 16))

