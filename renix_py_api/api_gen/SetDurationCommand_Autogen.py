"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class SetDurationCommand(TrafficTestCommand):
    def __init__(self, ConfigList=None, DurationMode=None, DurationSeconds=None, DurationBursts=None, DurationRepetitions=None, **kwargs):
        self._ConfigList = ConfigList  # Stream Port Handles
        self._DurationMode = DurationMode  # Duration mode
        self._DurationSeconds = DurationSeconds  # Duration seconds
        self._DurationBursts = DurationBursts  # Duration bursts
        self._DurationRepetitions = DurationRepetitions  # Duration Repetitions

        properties = kwargs.copy()
        if ConfigList is not None:
            properties['ConfigList'] = ConfigList
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if DurationSeconds is not None:
            properties['DurationSeconds'] = DurationSeconds
        if DurationBursts is not None:
            properties['DurationBursts'] = DurationBursts
        if DurationRepetitions is not None:
            properties['DurationRepetitions'] = DurationRepetitions

        # call base class function, and it will send message to renix server to create a class.
        super(SetDurationCommand, self).__init__(**properties)

    @property
    def ConfigList(self):
        """
        get the value of property _ConfigList
        """
        return self._ConfigList

    @property
    def DurationMode(self):
        """
        get the value of property _DurationMode
        """
        return self._DurationMode

    @property
    def DurationSeconds(self):
        """
        get the value of property _DurationSeconds
        """
        return self._DurationSeconds

    @property
    def DurationBursts(self):
        """
        get the value of property _DurationBursts
        """
        return self._DurationBursts

    @property
    def DurationRepetitions(self):
        """
        get the value of property _DurationRepetitions
        """
        return self._DurationRepetitions

    @ConfigList.setter
    def ConfigList(self, value):
        self._ConfigList = value

    @DurationMode.setter
    def DurationMode(self, value):
        self._DurationMode = value

    @DurationSeconds.setter
    def DurationSeconds(self, value):
        self._DurationSeconds = value

    @DurationBursts.setter
    def DurationBursts(self, value):
        self._DurationBursts = value

    @DurationRepetitions.setter
    def DurationRepetitions(self, value):
        self._DurationRepetitions = value

    def _set_configlist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._ConfigList = tmp_value.split()

    def _set_durationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DurationMode = EnumTransmitMode.%s' % value[:seperate])

    def _set_durationseconds_with_str(self, value):
        self._DurationSeconds = float(value)

    def _set_durationbursts_with_str(self, value):
        try:
            self._DurationBursts = int(value)
        except ValueError:
            self._DurationBursts = hex(int(value, 16))

    def _set_durationrepetitions_with_str(self, value):
        self._DurationRepetitions = float(value)

