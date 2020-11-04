"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .Result_Autogen import Result


@rom_manager.rom
class PortAvgLatencyStats(Result):
    def __init__(self, **kwargs):
        self._PortID = ''  # Port Name, not editable
        self._MinLatency = 0  # Min Latency (us), not editable
        self._AvaLatency = 0  # Avg Latency (us), not editable
        self._MaxLatency = 0  # Max Latency (us), not editable

        properties = kwargs.copy()

        # call base class function, and it will send message to renix server to create a class.
        super(PortAvgLatencyStats, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    @property
    def PortID(self):
        """
        get the value of property _PortID
        """
        if self.force_auto_sync:
            self.get('PortID')
        return self._PortID

    @property
    def MinLatency(self):
        """
        get the value of property _MinLatency
        """
        if self.force_auto_sync:
            self.get('MinLatency')
        return self._MinLatency

    @property
    def AvaLatency(self):
        """
        get the value of property _AvaLatency
        """
        if self.force_auto_sync:
            self.get('AvaLatency')
        return self._AvaLatency

    @property
    def MaxLatency(self):
        """
        get the value of property _MaxLatency
        """
        if self.force_auto_sync:
            self.get('MaxLatency')
        return self._MaxLatency

    def _set_portid_with_str(self, value):
        self._PortID = value

    def _set_minlatency_with_str(self, value):
        self._MinLatency = float(value)

    def _set_avalatency_with_str(self, value):
        self._AvaLatency = float(value)

    def _set_maxlatency_with_str(self, value):
        self._MaxLatency = float(value)

