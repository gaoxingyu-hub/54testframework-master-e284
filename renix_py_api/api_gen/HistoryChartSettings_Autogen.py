"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class HistoryChartSettings(ROMObject):
    def __init__(self, SamplingInterval=None, AutoLoad=None, **kwargs):
        self._SamplingInterval = SamplingInterval  # Sampling Interval
        self._AutoLoad = AutoLoad  # Auto Load

        properties = kwargs.copy()
        if SamplingInterval is not None:
            properties['SamplingInterval'] = SamplingInterval
        if AutoLoad is not None:
            properties['AutoLoad'] = AutoLoad

        # call base class function, and it will send message to renix server to create a class.
        super(HistoryChartSettings, self).__init__(**properties)

    def delete(self):
        """
        call to delete itself
        """
        return self._finalize()

    def edit(self, SamplingInterval=None, AutoLoad=None, **kwargs):
        properties = kwargs.copy()
        if SamplingInterval is not None:
            self._SamplingInterval = SamplingInterval
            properties['SamplingInterval'] = SamplingInterval
        if AutoLoad is not None:
            self._AutoLoad = AutoLoad
            properties['AutoLoad'] = AutoLoad

        super(HistoryChartSettings, self).edit(**properties)

    @property
    def SamplingInterval(self):
        """
        get the value of property _SamplingInterval
        """
        if self.force_auto_sync:
            self.get('SamplingInterval')
        return self._SamplingInterval

    @property
    def AutoLoad(self):
        """
        get the value of property _AutoLoad
        """
        if self.force_auto_sync:
            self.get('AutoLoad')
        return self._AutoLoad

    @SamplingInterval.setter
    def SamplingInterval(self, value):
        self._SamplingInterval = value
        self.edit(SamplingInterval=value)

    @AutoLoad.setter
    def AutoLoad(self, value):
        self._AutoLoad = value
        self.edit(AutoLoad=value)

    def _set_samplinginterval_with_str(self, value):
        try:
            self._SamplingInterval = int(value)
        except ValueError:
            self._SamplingInterval = hex(int(value, 16))

    def _set_autoload_with_str(self, value):
        self._AutoLoad = (value == 'True')

