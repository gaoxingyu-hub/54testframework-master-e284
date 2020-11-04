"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class Dhcpv4ServerPortConfig(ROMObject):
    def __init__(self, RenewRate=None, MaxOutstanding=None, **kwargs):
        self._RenewRate = RenewRate  # Force Renew Rate
        self._MaxOutstanding = MaxOutstanding  # Max Outstanding

        properties = kwargs.copy()
        if RenewRate is not None:
            properties['RenewRate'] = RenewRate
        if MaxOutstanding is not None:
            properties['MaxOutstanding'] = MaxOutstanding

        # call base class function, and it will send message to renix server to create a class.
        super(Dhcpv4ServerPortConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RenewRate=None, MaxOutstanding=None, **kwargs):
        properties = kwargs.copy()
        if RenewRate is not None:
            self._RenewRate = RenewRate
            properties['RenewRate'] = RenewRate
        if MaxOutstanding is not None:
            self._MaxOutstanding = MaxOutstanding
            properties['MaxOutstanding'] = MaxOutstanding

        super(Dhcpv4ServerPortConfig, self).edit(**properties)

    @property
    def RenewRate(self):
        """
        get the value of property _RenewRate
        """
        if self.force_auto_sync:
            self.get('RenewRate')
        return self._RenewRate

    @property
    def MaxOutstanding(self):
        """
        get the value of property _MaxOutstanding
        """
        if self.force_auto_sync:
            self.get('MaxOutstanding')
        return self._MaxOutstanding

    @RenewRate.setter
    def RenewRate(self, value):
        self._RenewRate = value
        self.edit(RenewRate=value)

    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._MaxOutstanding = value
        self.edit(MaxOutstanding=value)

    def _set_renewrate_with_str(self, value):
        try:
            self._RenewRate = int(value)
        except ValueError:
            self._RenewRate = hex(int(value, 16))

    def _set_maxoutstanding_with_str(self, value):
        try:
            self._MaxOutstanding = int(value)
        except ValueError:
            self._MaxOutstanding = hex(int(value, 16))

