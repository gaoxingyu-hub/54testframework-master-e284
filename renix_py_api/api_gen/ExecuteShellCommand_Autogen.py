"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class ExecuteShellCommand(ROMCommand):
    def __init__(self, CommandString=None, CommandParameter=None, WorkingDir=None, Mode=None, WaitTime=None, **kwargs):
        self._CommandString = CommandString  # Command String
        self._CommandParameter = CommandParameter  # Command Parameter
        self._WorkingDir = WorkingDir  # Working Directory
        self._Mode = Mode  # Execute Mode
        self._WaitTime = WaitTime  # Wait Time (sec)

        properties = kwargs.copy()
        if CommandString is not None:
            properties['CommandString'] = CommandString
        if CommandParameter is not None:
            properties['CommandParameter'] = CommandParameter
        if WorkingDir is not None:
            properties['WorkingDir'] = WorkingDir
        if Mode is not None:
            properties['Mode'] = Mode
        if WaitTime is not None:
            properties['WaitTime'] = WaitTime

        # call base class function, and it will send message to renix server to create a class.
        super(ExecuteShellCommand, self).__init__(**properties)

    @property
    def CommandString(self):
        """
        get the value of property _CommandString
        """
        return self._CommandString

    @property
    def CommandParameter(self):
        """
        get the value of property _CommandParameter
        """
        return self._CommandParameter

    @property
    def WorkingDir(self):
        """
        get the value of property _WorkingDir
        """
        return self._WorkingDir

    @property
    def Mode(self):
        """
        get the value of property _Mode
        """
        return self._Mode

    @property
    def WaitTime(self):
        """
        get the value of property _WaitTime
        """
        return self._WaitTime

    @CommandString.setter
    def CommandString(self, value):
        self._CommandString = value

    @CommandParameter.setter
    def CommandParameter(self, value):
        self._CommandParameter = value

    @WorkingDir.setter
    def WorkingDir(self, value):
        self._WorkingDir = value

    @Mode.setter
    def Mode(self, value):
        self._Mode = value

    @WaitTime.setter
    def WaitTime(self, value):
        self._WaitTime = value

    def _set_commandstring_with_str(self, value):
        self._CommandString = value

    def _set_commandparameter_with_str(self, value):
        self._CommandParameter = value

    def _set_workingdir_with_str(self, value):
        self._WorkingDir = value

    def _set_mode_with_str(self, value):
        seperate = value.find(':')
        exec('self._Mode = EnumExecuteShellMode.%s' % value[:seperate])

    def _set_waittime_with_str(self, value):
        try:
            self._WaitTime = int(value)
        except ValueError:
            self._WaitTime = hex(int(value, 16))

