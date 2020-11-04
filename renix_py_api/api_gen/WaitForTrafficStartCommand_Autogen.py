"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class WaitForTrafficStartCommand(TrafficTestCommand):
    def __init__(self, ConfigList=None, SleepTime=None, SleepTimeMode=None, **kwargs):
        self._ConfigList = ConfigList  # Stream Handles
        self._SleepTime = SleepTime  # Sleep Time (sec)
        self._SleepTimeMode = SleepTimeMode  # Sleep Time Mode

        properties = kwargs.copy()
        if ConfigList is not None:
            properties['ConfigList'] = ConfigList
        if SleepTime is not None:
            properties['SleepTime'] = SleepTime
        if SleepTimeMode is not None:
            properties['SleepTimeMode'] = SleepTimeMode

        # call base class function, and it will send message to renix server to create a class.
        super(WaitForTrafficStartCommand, self).__init__(**properties)

    @property
    def ConfigList(self):
        """
        get the value of property _ConfigList
        """
        return self._ConfigList

    @property
    def SleepTime(self):
        """
        get the value of property _SleepTime
        """
        return self._SleepTime

    @property
    def SleepTimeMode(self):
        """
        get the value of property _SleepTimeMode
        """
        return self._SleepTimeMode

    @ConfigList.setter
    def ConfigList(self, value):
        self._ConfigList = value

    @SleepTime.setter
    def SleepTime(self, value):
        self._SleepTime = value

    @SleepTimeMode.setter
    def SleepTimeMode(self, value):
        self._SleepTimeMode = value

    def _set_configlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ConfigList = tmp_value.split()

    def _set_sleeptime_with_str(self, value):
        self._SleepTime = float(value)

    def _set_sleeptimemode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SleepTimeMode = EnumSleepTimeMode.%s' % value[:seperate])

