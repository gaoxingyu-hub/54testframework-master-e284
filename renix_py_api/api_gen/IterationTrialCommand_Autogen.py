"""
Auto-generated File 
Create Time: 2019-12-27 02:33:27
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .IterationCommand_Autogen import IterationCommand


@rom_manager.rom
class IterationTrialCommand(IterationCommand):
    def __init__(self, NumTrials=None, **kwargs):
        self._NumTrials = NumTrials  # Trial Number

        properties = kwargs.copy()
        if NumTrials is not None:
            properties['NumTrials'] = NumTrials

        # call base class function, and it will send message to renix server to create a class.
        super(IterationTrialCommand, self).__init__(**properties)

    @property
    def NumTrials(self):
        """
        get the value of property _NumTrials
        """
        return self._NumTrials

    @NumTrials.setter
    def NumTrials(self, value):
        self._NumTrials = value

    def _set_numtrials_with_str(self, value):
        try:
            self._NumTrials = int(value)
        except ValueError:
            self._NumTrials = hex(int(value, 16))

