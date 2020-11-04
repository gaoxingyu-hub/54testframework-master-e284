"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .ROMCommand_Autogen import ROMCommand


@rom_manager.rom
class BenchmarkStopCommand(ROMCommand):
    def __init__(self, IsLastCommand=None, StopReason=None, **kwargs):
        self._IsLastCommand = IsLastCommand  # Is Last Command
        self._StopReason = StopReason  # Benchmark stop reason

        properties = kwargs.copy()
        if IsLastCommand is not None:
            properties['IsLastCommand'] = IsLastCommand
        if StopReason is not None:
            properties['StopReason'] = StopReason

        # call base class function, and it will send message to renix server to create a class.
        super(BenchmarkStopCommand, self).__init__(**properties)

    @property
    def IsLastCommand(self):
        """
        get the value of property _IsLastCommand
        """
        return self._IsLastCommand

    @property
    def StopReason(self):
        """
        get the value of property _StopReason
        """
        return self._StopReason

    @IsLastCommand.setter
    def IsLastCommand(self, value):
        self._IsLastCommand = value

    @StopReason.setter
    def StopReason(self, value):
        self._StopReason = value

    def _set_islastcommand_with_str(self, value):
        self._IsLastCommand = (value == 'True')

    def _set_stopreason_with_str(self, value):
        self._StopReason = value

