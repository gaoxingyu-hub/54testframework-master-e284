"""
Auto-generated File 
Create Time: 2019-12-27 02:33:26
"""
from .ROMEnum_Autogen import *
from renix_py_api.renix_common_api import *
from renix_py_api import rom_manager
from .GroupCommand_Autogen import GroupCommand


@rom_manager.rom
class LoopCommand(GroupCommand):
    def __init__(self, LoopCount=None, **kwargs):
        self._LoopCount = LoopCount  # Loop Count
        self._CurrentLoop = 0  # Current Loop, not editable

        properties = kwargs.copy()
        if LoopCount is not None:
            properties['LoopCount'] = LoopCount

        # call base class function, and it will send message to renix server to create a class.
        super(LoopCommand, self).__init__(**properties)

    @property
    def LoopCount(self):
        """
        get the value of property _LoopCount
        """
        return self._LoopCount

    @property
    def CurrentLoop(self):
        """
        get the value of property _CurrentLoop
        """
        return self._CurrentLoop

    @LoopCount.setter
    def LoopCount(self, value):
        self._LoopCount = value

    def _set_loopcount_with_str(self, value):
        try:
            self._LoopCount = int(value)
        except ValueError:
            self._LoopCount = hex(int(value, 16))

    def _set_currentloop_with_str(self, value):
        try:
            self._CurrentLoop = int(value)
        except ValueError:
            self._CurrentLoop = hex(int(value, 16))

