"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class SleepCommand(ROMCommand):
    def __init__(self, SleepTime=None, SleepTimeMode=None, **kwargs):
        self._SleepTime = SleepTime  # Sleep Time (sec)
        self._SleepTimeMode = SleepTimeMode  # Sleep Time Mode

        properties = kwargs.copy()
        if SleepTime is not None:
            properties['SleepTime'] = SleepTime
        if SleepTimeMode is not None:
            properties['SleepTimeMode'] = SleepTimeMode

        # call base class function, and it will send message to renix server to create a class.
        super(SleepCommand, self).__init__(**properties)

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

    @SleepTime.setter
    def SleepTime(self, value):
        self._SleepTime = value

    @SleepTimeMode.setter
    def SleepTimeMode(self, value):
        self._SleepTimeMode = value

    def _set_sleeptime_with_str(self, value):
        self._SleepTime = float(value)

    def _set_sleeptimemode_with_str(self, value):
        seperate = value.find(':')
        exec('self._SleepTimeMode = EnumSleepTimeMode.%s' % value[:seperate])

