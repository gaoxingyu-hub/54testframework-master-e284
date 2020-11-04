"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class PppoePortRateConfig(ROMObject):
    def __init__(self, ConnectRate=None, DisconnectRate=None, MaxSessionsOutstanding=None, **kwargs):
        self._ConnectRate = ConnectRate  # Connect Rate (sessions/sec)
        self._DisconnectRate = DisconnectRate  # Disconnect Rate (sessions/sec)
        self._MaxSessionsOutstanding = MaxSessionsOutstanding  # Maximum Outstanding Sessions

        properties = kwargs.copy()
        if ConnectRate is not None:
            properties['ConnectRate'] = ConnectRate
        if DisconnectRate is not None:
            properties['DisconnectRate'] = DisconnectRate
        if MaxSessionsOutstanding is not None:
            properties['MaxSessionsOutstanding'] = MaxSessionsOutstanding

        # call base class function, and it will send message to renix server to create a class.
        super(PppoePortRateConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, ConnectRate=None, DisconnectRate=None, MaxSessionsOutstanding=None, **kwargs):
        properties = kwargs.copy()
        if ConnectRate is not None:
            self._ConnectRate = ConnectRate
            properties['ConnectRate'] = ConnectRate
        if DisconnectRate is not None:
            self._DisconnectRate = DisconnectRate
            properties['DisconnectRate'] = DisconnectRate
        if MaxSessionsOutstanding is not None:
            self._MaxSessionsOutstanding = MaxSessionsOutstanding
            properties['MaxSessionsOutstanding'] = MaxSessionsOutstanding

        super(PppoePortRateConfig, self).edit(**properties)

    @property
    def ConnectRate(self):
        """
        get the value of property _ConnectRate
        """
        if self.force_auto_sync:
            self.get('ConnectRate')
        return self._ConnectRate

    @property
    def DisconnectRate(self):
        """
        get the value of property _DisconnectRate
        """
        if self.force_auto_sync:
            self.get('DisconnectRate')
        return self._DisconnectRate

    @property
    def MaxSessionsOutstanding(self):
        """
        get the value of property _MaxSessionsOutstanding
        """
        if self.force_auto_sync:
            self.get('MaxSessionsOutstanding')
        return self._MaxSessionsOutstanding

    @ConnectRate.setter
    def ConnectRate(self, value):
        self._ConnectRate = value
        self.edit(ConnectRate=value)

    @DisconnectRate.setter
    def DisconnectRate(self, value):
        self._DisconnectRate = value
        self.edit(DisconnectRate=value)

    @MaxSessionsOutstanding.setter
    def MaxSessionsOutstanding(self, value):
        self._MaxSessionsOutstanding = value
        self.edit(MaxSessionsOutstanding=value)

    def _set_connectrate_with_str(self, value):
        try:
            self._ConnectRate = int(value)
        except ValueError:
            self._ConnectRate = hex(int(value, 16))

    def _set_disconnectrate_with_str(self, value):
        try:
            self._DisconnectRate = int(value)
        except ValueError:
            self._DisconnectRate = hex(int(value, 16))

    def _set_maxsessionsoutstanding_with_str(self, value):
        try:
            self._MaxSessionsOutstanding = int(value)
        except ValueError:
            self._MaxSessionsOutstanding = hex(int(value, 16))

