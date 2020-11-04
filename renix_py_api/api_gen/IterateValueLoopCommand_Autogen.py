"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .LoopCommand_Autogen import LoopCommand


@rom_manager.rom
class IterateValueLoopCommand(LoopCommand):
    def __init__(self, IterateValues=None, IterateHandles=None, **kwargs):
        self._IterateValues = IterateValues  # Iterate Value
        self._IterateHandles = IterateHandles  # Iterate Handles

        properties = kwargs.copy()
        if IterateValues is not None:
            properties['IterateValues'] = IterateValues
        if IterateHandles is not None:
            properties['IterateHandles'] = IterateHandles

        # call base class function, and it will send message to renix server to create a class.
        super(IterateValueLoopCommand, self).__init__(**properties)

    @property
    def IterateValues(self):
        """
        get the value of property _IterateValues
        """
        return self._IterateValues

    @property
    def IterateHandles(self):
        """
        get the value of property _IterateHandles
        """
        return self._IterateHandles

    @IterateValues.setter
    def IterateValues(self, value):
        self._IterateValues = value

    @IterateHandles.setter
    def IterateHandles(self, value):
        self._IterateHandles = value

    def _set_iteratevalues_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IterateValues = tmp_value.split()

    def _set_iteratehandles_with_str(self, value):
        tmp_value = value.strip()
        if tmp_value.startswith('{'):
            tmp_value = tmp_value[1:-1]
        self._IterateHandles = tmp_value.split()

