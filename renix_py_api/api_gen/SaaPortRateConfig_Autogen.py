"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class SaaPortRateConfig(ROMObject):
    def __init__(self, RequestRate=None, MaxOutstanding=None, **kwargs):
        self._RequestRate = RequestRate  # Request Rate (sessions/sec)
        self._MaxOutstanding = MaxOutstanding  # Max Outstanding Session

        properties = kwargs.copy()
        if RequestRate is not None:
            properties['RequestRate'] = RequestRate
        if MaxOutstanding is not None:
            properties['MaxOutstanding'] = MaxOutstanding

        # call base class function, and it will send message to renix server to create a class.
        super(SaaPortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, RequestRate=None, MaxOutstanding=None, **kwargs):
        properties = kwargs.copy()
        if RequestRate is not None:
            self._RequestRate = RequestRate
            properties['RequestRate'] = RequestRate
        if MaxOutstanding is not None:
            self._MaxOutstanding = MaxOutstanding
            properties['MaxOutstanding'] = MaxOutstanding

        super(SaaPortRateConfig, self).edit(**properties)

    @property
    def RequestRate(self):
        """
        get the value of property _RequestRate
        """
        if self.force_auto_sync:
            self.get('RequestRate')
        return self._RequestRate

    @property
    def MaxOutstanding(self):
        """
        get the value of property _MaxOutstanding
        """
        if self.force_auto_sync:
            self.get('MaxOutstanding')
        return self._MaxOutstanding

    @RequestRate.setter
    def RequestRate(self, value):
        self._RequestRate = value
        self.edit(RequestRate=value)

    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._MaxOutstanding = value
        self.edit(MaxOutstanding=value)

    def _set_requestrate_with_str(self, value):
        try:
            self._RequestRate = int(value)
        except ValueError:
            self._RequestRate = hex(int(value, 16))

    def _set_maxoutstanding_with_str(self, value):
        try:
            self._MaxOutstanding = int(value)
        except ValueError:
            self._MaxOutstanding = hex(int(value, 16))

