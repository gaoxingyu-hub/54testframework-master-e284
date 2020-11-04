"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Y1564SetPortsLoadCommand(TrafficTestCommand):
    def __init__(self, PortHandles=None, LoadRates=None, **kwargs):
        self._PortHandles = PortHandles  # Port Handle List
        self._LoadRates = LoadRates  # Ports Load (bps)

        properties = kwargs.copy()
        if PortHandles is not None:
            properties['PortHandles'] = PortHandles
        if LoadRates is not None:
            properties['LoadRates'] = LoadRates

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564SetPortsLoadCommand, self).__init__(**properties)

    @property
    def PortHandles(self):
        """
        get the value of property _PortHandles
        """
        return self._PortHandles

    @property
    def LoadRates(self):
        """
        get the value of property _LoadRates
        """
        return self._LoadRates

    @PortHandles.setter
    def PortHandles(self, value):
        self._PortHandles = value

    @LoadRates.setter
    def LoadRates(self, value):
        self._LoadRates = value

    def _set_porthandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._PortHandles = tmp_value.split()

    def _set_loadrates_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._LoadRates = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._LoadRates.append(int(str_value))
            except ValueError:
                self._LoadRates.append(hex(int(str_value, 16)))

