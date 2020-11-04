"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class SetRespectiveDurationCommand(TrafficTestCommand):
    def __init__(self, StreamHandleList=None, DurationMode=None, DurationCounts=None, **kwargs):
        self._StreamHandleList = StreamHandleList  # Stream Handles
        self._DurationMode = DurationMode  # Duration mode
        self._DurationCounts = DurationCounts  # Duration Count

        properties = kwargs.copy()
        if StreamHandleList is not None:
            properties['StreamHandleList'] = StreamHandleList
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if DurationCounts is not None:
            properties['DurationCounts'] = DurationCounts

        # call base class function, and it will send message to renix server to create a class.
        super(SetRespectiveDurationCommand, self).__init__(**properties)

    @property
    def StreamHandleList(self):
        """
        get the value of property _StreamHandleList
        """
        return self._StreamHandleList

    @property
    def DurationMode(self):
        """
        get the value of property _DurationMode
        """
        return self._DurationMode

    @property
    def DurationCounts(self):
        """
        get the value of property _DurationCounts
        """
        return self._DurationCounts

    @StreamHandleList.setter
    def StreamHandleList(self, value):
        self._StreamHandleList = value

    @DurationMode.setter
    def DurationMode(self, value):
        self._DurationMode = value

    @DurationCounts.setter
    def DurationCounts(self, value):
        self._DurationCounts = value

    def _set_streamhandlelist_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamHandleList = tmp_value.split()

    def _set_durationmode_with_str(self, value):
        seperate = value.find(':')
        exec('self._DurationMode = EnumTransmitMode.%s' % value[:seperate])

    def _set_durationcounts_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._DurationCounts = []
        values = tmp_value.split()
        for str_value in values:
            try:
                self._DurationCounts.append(int(str_value))
            except ValueError:
                self._DurationCounts.append(hex(int(str_value, 16)))

