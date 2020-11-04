"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class KeepAliveConfig(ROMObject):
    def __init__(self, **kwargs):
        self._KeepAliveInterval = 60  # Keep Alive Interval (sec), not editable
        self._KeepAliveThreshold = 5  # Keep Alive Threshold, not editable
        self._PlTimeoutCount = 0  # PL Timeout Count, not editable
        self._ClTimeoutCont = 0  # CL Timeout Count, not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(KeepAliveConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, **kwargs):
        properties = kwargs.copy()

        super(KeepAliveConfig, self).edit(**properties)

    @property
    def KeepAliveInterval(self):
        """
        get the value of property _KeepAliveInterval
        """
        if self.force_auto_sync:
            self.get('KeepAliveInterval')
        return self._KeepAliveInterval

    @property
    def KeepAliveThreshold(self):
        """
        get the value of property _KeepAliveThreshold
        """
        if self.force_auto_sync:
            self.get('KeepAliveThreshold')
        return self._KeepAliveThreshold

    @property
    def PlTimeoutCount(self):
        """
        get the value of property _PlTimeoutCount
        """
        if self.force_auto_sync:
            self.get('PlTimeoutCount')
        return self._PlTimeoutCount

    @property
    def ClTimeoutCont(self):
        """
        get the value of property _ClTimeoutCont
        """
        if self.force_auto_sync:
            self.get('ClTimeoutCont')
        return self._ClTimeoutCont

    def _set_keepaliveinterval_with_str(self, value):
        try:
            self._KeepAliveInterval = int(value)
        except ValueError:
            self._KeepAliveInterval = hex(int(value, 16))

    def _set_keepalivethreshold_with_str(self, value):
        try:
            self._KeepAliveThreshold = int(value)
        except ValueError:
            self._KeepAliveThreshold = hex(int(value, 16))

    def _set_pltimeoutcount_with_str(self, value):
        try:
            self._PlTimeoutCount = int(value)
        except ValueError:
            self._PlTimeoutCount = hex(int(value, 16))

    def _set_cltimeoutcont_with_str(self, value):
        try:
            self._ClTimeoutCont = int(value)
        except ValueError:
            self._ClTimeoutCont = hex(int(value, 16))

