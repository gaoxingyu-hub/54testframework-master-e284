"""
Auto-generated File 
Create Time: 2019-12-27 02:33:28
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .TrafficTestCommand_Autogen import TrafficTestCommand


@rom_manager.rom
class Y1564SetDurationCommand(TrafficTestCommand):
    def __init__(self, StreamTemplateHandles=None, DurationMode=None, DurationSeconds=None, DurationBursts=None, **kwargs):
        self._StreamTemplateHandles = StreamTemplateHandles  # Stream Handles
        self._DurationMode = DurationMode  # Duration Mode
        self._DurationSeconds = DurationSeconds  # Duration seconds
        self._DurationBursts = DurationBursts  # Duration bursts

        properties = kwargs.copy()
        if StreamTemplateHandles is not None:
            properties['StreamTemplateHandles'] = StreamTemplateHandles
        if DurationMode is not None:
            properties['DurationMode'] = DurationMode
        if DurationSeconds is not None:
            properties['DurationSeconds'] = DurationSeconds
        if DurationBursts is not None:
            properties['DurationBursts'] = DurationBursts

        # call base class function, and it will send message to renix server to create a class.
        super(Y1564SetDurationCommand, self).__init__(**properties)

    @property
    def StreamTemplateHandles(self):
        """
        get the value of property _StreamTemplateHandles
        """
        return self._StreamTemplateHandles

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

    @StreamTemplateHandles.setter
    def StreamTemplateHandles(self, value):
        self._StreamTemplateHandles = value

    @DurationMode.setter
    def DurationMode(self, value):
        self._DurationMode = value

    @DurationSeconds.setter
    def DurationSeconds(self, value):
        self._DurationSeconds = value

    @DurationBursts.setter
    def DurationBursts(self, value):
        self._DurationBursts = value

    def _set_streamtemplatehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamTemplateHandles = tmp_value.split()

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

