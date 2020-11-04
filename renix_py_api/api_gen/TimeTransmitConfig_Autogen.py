"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .PortTransmitConfig_Autogen import PortTransmitConfig


@rom_manager.rom
class TimeTransmitConfig(PortTransmitConfig):
    def __init__(self, Seconds=None, **kwargs):
        self._Seconds = Seconds  # Seconds

        properties = kwargs.copy()
        if Seconds is not None:
            properties['Seconds'] = Seconds

        # call base class function, and it will send message to renix server to create a class.
        super(TimeTransmitConfig, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, Seconds=None, **kwargs):
        properties = kwargs.copy()
        if Seconds is not None:
            self._Seconds = Seconds
            properties['Seconds'] = Seconds

        super(TimeTransmitConfig, self).edit(**properties)

    @property
    def Seconds(self):
        """
        get the value of property _Seconds
        """
        if self.force_auto_sync:
            self.get('Seconds')
        return self._Seconds

    @Seconds.setter
    def Seconds(self, value):
        self._Seconds = value
        self.edit(Seconds=value)

    def _set_seconds_with_str(self, value):
        self._Seconds = float(value)

