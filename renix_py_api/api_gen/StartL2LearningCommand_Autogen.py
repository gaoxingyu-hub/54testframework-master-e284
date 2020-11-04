"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class StartL2LearningCommand(ROMCommand):
    def __init__(self, StreamHandles=None, WaitLearningDone=None, WaitTime=None, **kwargs):
        self._StreamHandles = StreamHandles  # Stream Handles
        self._WaitLearningDone = WaitLearningDone  # Wait Learning Done
        self._WaitTime = WaitTime  # Wait Time (sec)

        properties = kwargs.copy()
        if StreamHandles is not None:
            properties['StreamHandles'] = StreamHandles
        if WaitLearningDone is not None:
            properties['WaitLearningDone'] = WaitLearningDone
        if WaitTime is not None:
            properties['WaitTime'] = WaitTime

        # call base class function, and it will send message to renix server to create a class.
        super(StartL2LearningCommand, self).__init__(**properties)

    @property
    def StreamHandles(self):
        """
        get the value of property _StreamHandles
        """
        return self._StreamHandles

    @property
    def WaitLearningDone(self):
        """
        get the value of property _WaitLearningDone
        """
        return self._WaitLearningDone

    @property
    def WaitTime(self):
        """
        get the value of property _WaitTime
        """
        return self._WaitTime

    @StreamHandles.setter
    def StreamHandles(self, value):
        self._StreamHandles = value

    @WaitLearningDone.setter
    def WaitLearningDone(self, value):
        self._WaitLearningDone = value

    @WaitTime.setter
    def WaitTime(self, value):
        self._WaitTime = value

    def _set_streamhandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._StreamHandles = tmp_value.split()

    def _set_waitlearningdone_with_str(self, value):
        self._WaitLearningDone = (value == 'True')

    def _set_waittime_with_str(self, value):
        try:
            self._WaitTime = int(value)
        except ValueError:
            self._WaitTime = hex(int(value, 16))

