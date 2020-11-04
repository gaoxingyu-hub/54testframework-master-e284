"""
Auto-generated File 
Create Time: 2019-12-27 02:33:25
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from renix_py_api.core import Command
from .ROMObject_Autogen import ROMObject


@rom_manager.rom
class ROMCommand(Command, ROMObject):
    def __init__(self, AutoDelete=None, **kwargs):
        self._CommandState = ROMCommandStateEnum.INIT  # Command State, not editable
        self._AutoDelete = AutoDelete  # Auto Delete Command
        self._StartTime = ''  # Start Time, not editable
        self._ElapsedTime = ''  # Elapsed Time, not editable

        properties = kwargs.copy()
        if AutoDelete is not None:
            properties['AutoDelete'] = AutoDelete

        # call base class function, and it will send message to renix server to create a class.
        ROMObject.__init__(self, **properties)

        Command.__init__(self, **properties)

    @property
    def CommandState(self):
        """
        get the value of property _CommandState
        """
        return self._CommandState

    @property
    def AutoDelete(self):
        """
        get the value of property _AutoDelete
        """
        return self._AutoDelete

    @property
    def StartTime(self):
        """
        get the value of property _StartTime
        """
        return self._StartTime

    @property
    def ElapsedTime(self):
        """
        get the value of property _ElapsedTime
        """
        return self._ElapsedTime

    @AutoDelete.setter
    def AutoDelete(self, value):
        self._AutoDelete = value

    def _set_commandstate_with_str(self, value):
        seperate = value.find(':')
        exec('self._CommandState = ROMCommandStateEnum.%s' % value[:seperate])

    def _set_autodelete_with_str(self, value):
        self._AutoDelete = (value == 'True')

    def _set_starttime_with_str(self, value):
        self._StartTime = value

    def _set_elapsedtime_with_str(self, value):
        self._ElapsedTime = value

